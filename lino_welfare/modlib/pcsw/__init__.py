# Copyright 2014 Luc Saffre
# License: BSD (see file COPYING for details)


"""

The :mod:`lino_welfare.modlib.pcsw` package provides data definitions
for PCSW specific objects.

Most important models are :class:`Client` and :class:`Coaching`.

.. autosummary::
   :toctree:

   models
   coaching
   fixtures

See also :mod:`welfare.pcsw`.

"""


from lino import ad

from django.utils.translation import ugettext_lazy as _


class Plugin(ad.Plugin):
    "Ceci n'est pas une documentation."
    verbose_name = _("PCSW")

    def setup_main_menu(self, site, profile, m):
        m = m.add_menu(self.app_label, self.verbose_name)
        m.add_action('pcsw.MyCoachings')

    def setup_config_menu(config, site, profile, m):
        m = m.add_menu(config.app_label, config.verbose_name)
        m.add_action('pcsw.PersonGroups')
        m.add_action('pcsw.Activities')
        m.add_action('pcsw.ExclusionTypes')
        m.add_action('pcsw.CoachingTypes')
        m.add_action('pcsw.CoachingEndings')
        m.add_action('pcsw.DispenseReasons')
        m.add_action('pcsw.ClientContactTypes')

    def setup_explorer_menu(config, site, profile, m):
        m = m.add_menu(config.app_label, config.verbose_name)
        m.add_action('pcsw.Coachings')
        m.add_action('pcsw.ClientContacts')
        m.add_action('pcsw.Exclusions')
        m.add_action('pcsw.Convictions')
        m.add_action('pcsw.AllClients')
        #~ m.add_action(PersonSearches)
        m.add_action('pcsw.CivilState')
        m.add_action('pcsw.ClientStates')
        m.add_action('beid.BeIdCardTypes')

    def setup_reports_menu(config, site, profile, m):
        m = m.add_menu(config.app_label, config.verbose_name)
        #~ m.add_action(site.modules.jobs.OldJobsOverview)
        #~ m.add_action(site.modules.integ.UsersWithClients)
        m.add_action('pcsw.ClientsTest')
        #~ m  = m.add_menu("pcsw",pcsw.MODULE_LABEL)
        # ~ m.add_action(ActivityReport1) # old version

