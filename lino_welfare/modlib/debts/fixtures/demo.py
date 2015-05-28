# -*- coding: UTF-8 -*-
# Copyright 2012-2015 Luc Saffre
# License: BSD (see file COPYING for details)

import decimal
from dateutil.relativedelta import relativedelta
ONE_DAY = relativedelta(days=1)

from django.conf import settings
from django.utils.translation import ugettext as _

from lino.utils import Cycler
from lino.api import rt

from lino.modlib.accounts.choicelists import AccountTypes


def n2dec(v):
    return decimal.Decimal("%.2d" % v)


def objects():

    User = rt.modules.users.User
    Household = rt.modules.households.Household
    Budget = rt.modules.debts.Budget
    # Chart = rt.modules.accounts.Chart
    Entry = rt.modules.debts.Entry
    Account = rt.modules.accounts.Account
    Company = rt.modules.contacts.Company

    kerstin = User(username="kerstin",
                   first_name="Kerstin", last_name=u"Kerres",
                   profile='300')
        #~ level=UserLevel.user,
        #~ debts_level=UserLevel.user)
    yield kerstin

    for hh in Household.objects.all():
        b = Budget(partner_id=hh.id, user=kerstin)
        b.fill_defaults(None)
        yield b

    INCOME_AMOUNTS = Cycler([i * 200 for i in range(8)])
    EXPENSE_AMOUNTS = Cycler([i * 5.24 for i in range(10)])
    DEBT_AMOUNTS = Cycler([(i + 1) * 300 for i in range(5)])
    DEBT_ENTRIES = Cycler([4, 8, 5, 3, 12, 5])
    PARTNERS = Cycler(Company.objects.all())
    
    LIABILITIES = Cycler(Account.objects.filter(
        type=AccountTypes.liabilities,
        chart=rt.modules.accounts.AccountCharts.debts))
    EXPENSE_REMARKS = Cycler(_("Shopping"), _("Cinema"), _("Seminar"))
    # qs = rt.modules.contacts.Companies.request().data_iterator
    # qs = qs.filter(client_contact_type__is_bailiff=True)
    BAILIFFS = Cycler(
        Company.objects.filter(client_contact_type__is_bailiff=True))

    for b in Budget.objects.all():
        seqno = 0
        for e in b.entry_set.all():
            seqno += 1
            if e.account.type == AccountTypes.incomes:
                amount = INCOME_AMOUNTS.pop()
            elif e.account.type == AccountTypes.expenses:
                amount = EXPENSE_AMOUNTS.pop()
                if e.account.ref in ('3030', '3071'):
                    e.remark = EXPENSE_REMARKS.pop()
            if e.account.required_for_household:
                e.amount = n2dec(amount)
            if e.account.required_for_person:
                for a in b.actor_set.all():
                    e.amount = n2dec(amount)
                    e.actor = a
            e.save()
        ACTORS = Cycler(None, *[a for a in b.actor_set.all()])
        for i in range(DEBT_ENTRIES.pop()):
            seqno += 1
            amount = int(DEBT_AMOUNTS.pop())
            account = LIABILITIES.pop()
            kw = dict(budget=b,
                      account=account,
                      partner=PARTNERS.pop(),
                      amount=amount,
                      actor=ACTORS.pop(),
                      seqno=seqno)
            if account.ref.startswith('71'):
                kw.update(bailiff=BAILIFFS.pop())
            if amount > 600:
                kw.update(distribute=True)
            else:
                kw.update(monthly_rate=n2dec(amount / 20))
            e = Entry(**kw)
            e.account_changed(None)  # set description
            yield e

    ses = settings.SITE.login("kerstin")
    for e in Entry.objects.filter(account__ref='3030'):
        new = e.duplicate.run_from_code(ses)
        new.remark = EXPENSE_REMARKS.pop()
        yield new

    settings.SITE.site_config.master_budget = Budget.objects.get(id=1)
    yield settings.SITE.site_config
