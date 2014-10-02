# -*- coding: UTF-8 -*-
# Copyright 2014 Luc Saffre
# This file is part of the Lino-Welfare project.
# Lino-Welfare is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
# Lino-Welfare is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# You should have received a copy of the GNU General Public License
# along with Lino-Welfare; if not, see <http://www.gnu.org/licenses/>.

"""
"""

from django.utils.translation import ugettext_lazy as _
from lino.dd import resolve_model
from lino.utils import Cycler, ONE_DAY
from lino import dd, rt


def objects():
    Granting = rt.modules.aids.Granting
    AidType = rt.modules.aids.AidType
    Person = rt.modules.contacts.Person
    ClientStates = rt.modules.pcsw.ClientStates
    ClientContactType = rt.modules.pcsw.ClientContactType
    Board = rt.modules.boards.Board

    Project = resolve_model('pcsw.Client')
    qs = Project.objects.filter(client_state=ClientStates.coached)
    # if qs.count() > 10:
    #     qs = qs[:10]
    PROJECTS = Cycler(qs)

    l = []
    qs = ClientContactType.objects.filter(can_refund=True)
    for cct in qs:
        qs2 = Person.objects.filter(client_contact_type=cct)
        if qs2.count():
            i = (cct, Cycler(qs2))
            l.append(i)
    PARTNERS = Cycler(l)

    BOARDS = Cycler(Board.objects.all())

    fkw = dd.str2kw('name', _("Pharmacy"))  # Apotheke
    pharmacy_type = rt.modules.pcsw.ClientContactType.objects.get(**fkw)
    PHARMACIES = Cycler(rt.modules.contacts.Company.objects.filter(
        client_contact_type=pharmacy_type))

    for i, at in enumerate(AidType.objects.all()):
        kw = dict(start_date=dd.demo_date(days=i),
                  board=BOARDS.pop(),
                  decision_date=dd.demo_date(days=i-1),
                  aid_type=at)
        kw.update(client=PROJECTS.pop())
        g = Granting(**kw)
        g.after_ui_create(None)
        yield g

    # ConfirmationTypes = rt.modules.aids.ConfirmationTypes
    RefundConfirmation = rt.modules.aids.RefundConfirmation
    IncomeConfirmation = rt.modules.aids.IncomeConfirmation

    AMOUNTS = Cycler(123, 234, 345, 456, 678)
    CATEGORIES = Cycler(rt.modules.aids.Category.objects.all())

    for i in range(2):
        for g in Granting.objects.filter(aid_type__isnull=False):
            ct = g.aid_type.confirmation_type
            kw = dict(granting=g, client=g.client)
            kw.update(start_date=g.start_date + ONE_DAY)
            kw.update(end_date=g.start_date + ONE_DAY + ONE_DAY)
            if ct.model == IncomeConfirmation:
                kw.update(category=CATEGORIES.pop())
                kw.update(amount=AMOUNTS.pop())
            if ct.model == RefundConfirmation:
                type, cycler = PARTNERS.pop()
                kw.update(doctor_type=type)
                kw.update(doctor=cycler.pop())
                if g.aid_type.pharmacy_type == pharmacy_type:
                    kw.update(pharmacy=PHARMACIES.pop())
            yield ct.model(**kw)
