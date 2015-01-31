# -*- coding: UTF-8 -*-
# Copyright 2008-2015 Luc Saffre
# License: BSD (see file COPYING for details)

"""Database models for :mod:`lino_welfare.modlib.pcsw`.

"""

from lino.api import dd, rt

from lino.modlib.contacts.mixins import ContactRelated


class ClientContactBase(ContactRelated):
    """Also used by :class:`aids.RefundPartner
<lino_welfare.modlib.aids.models.RefundPartner>`."""

    class Meta:
        abstract = True
    type = dd.ForeignKey('pcsw.ClientContactType', blank=True, null=True)

    @dd.chooser()
    def company_choices(self, type):
        qs = rt.modules.contacts.Companies.request().data_iterator
        if type is not None:
            qs = qs.filter(client_contact_type=type)
        return qs

    @dd.chooser()
    def contact_person_choices(self, type):
        qs = rt.modules.contacts.Persons.request().data_iterator
        if type is not None:
            qs = qs.filter(client_contact_type=type)
        return qs

    def __unicode__(self):
        return unicode(self.contact_person or self.company or self.type)

