# -*- coding: UTF-8 -*-
# Copyright 2014-2015 Luc Saffre
# License: BSD (see file COPYING for details)

from __future__ import unicode_literals


from lino.utils.instantiator import Instantiator

from lino.api import dd, rt, _


def excerpt_types():  # also used for migration to 1.1.11

    ContentType = rt.modules.contenttypes.ContentType
    ExcerptType = rt.modules.excerpts.ExcerptType

    attType = Instantiator(ExcerptType,
                           # build_method='appypdf',
                           email_template='Default.eml.html').build
    
    Shortcuts = rt.modules.excerpts.Shortcuts

    yield attType(
        body_template='presence_certificate.body.html',
        template='Default.odt',
        primary=True,
        content_type=ContentType.objects.get_for_model(
            dd.resolve_model('cal.Guest')),
        **dd.babelkw('name',
                     de="Anwesenheitsbescheinigung",
                     fr="Attestation de présence",
                     en="Presence certificate"))

    yield attType(
        build_method='appyrtf',
        template='cv.odt',
        shortcut=Shortcuts.cvs_emitted,
        content_type=ContentType.objects.get_for_model(
            dd.resolve_model('pcsw.Client')),
        **dd.str2kw('name', "Curriculum vitae"))

    yield attType(
        template='file_sheet.odt',
        primary=True,
        content_type=ContentType.objects.get_for_model(
            dd.resolve_model('pcsw.Client')),
        **dd.str2kw('name', _("File sheet")))

    yield attType(
        template='eid-content.odt',
        content_type=ContentType.objects.get_for_model(
            dd.resolve_model('pcsw.Client')),
        **dd.str2kw('name', _("eID sheet")))
        # **dd.babelkw('name',
        #              de="eID-Inhalt",
        #              fr="Contenu carte eID",
        #              en="eID sheet"))

    yield attType(
        body_template='pac.body.html',
        template='Default.odt',
        content_type=ContentType.objects.get_for_model(
            dd.resolve_model('pcsw.Client')),
        **dd.str2kw('name', _("Action plan")))
        # **dd.babelkw('name',
        #              de="Aktionsplan",
        #              fr="Plan d'action",
        #              en="to-do list"))

    yield ExcerptType.update_for_model(
        'jobs.Contract', certifying=True, backward_compat=True)

    yield ExcerptType.update_for_model(
        'isip.Contract', certifying=True, backward_compat=True)

    yield ExcerptType.update_for_model(
        'art61.Contract', certifying=True,
        print_recipient=False, body_template='contract.body.html')


def objects():
    yield excerpt_types()
