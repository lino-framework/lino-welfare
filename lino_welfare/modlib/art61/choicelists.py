# -*- coding: UTF-8 -*-
# Copyright 2012-2015 Luc Saffre
# License: BSD (see file COPYING for details)

"""
Choicelists for `lino_welfare.modlib.art61`.

Original request:

- Gestion des subsides d'un projet art 61 : 3 nouveaux champs à cocher
  "Activa", "Tutorat" et "Région wallonne". + paramètres pour pouvoir
  filtrer.  Précision: il serait bien d'avoir une ChoiceList
  "Subsidiations" (`art61.Subsidizations`) configurable. Et puis un
  champ à cocher par subsidiation et par contrat. Ce sera l'occasion
  d'implémenter :class:`lino.core.choicelists.MultiChoiceListField`.


.. autosummary::

"""

from __future__ import unicode_literals
from __future__ import print_function

from django.db import models

from lino.api import dd, rt, _


class Subsidizations(dd.ChoiceList):
    verbose_name = _("Subsidization")
    verbose_name_plural = _("Subsidizations")

add = Subsidizations.add_item
add('10', _("Activa"), 'activa')
add('20', _("Tutorate"), 'tutorat')  # Tutorat: unique en communauté
                                     # francaise. par Ahmed Medhoune
add('30', _("Walloon Region"), 'region')

