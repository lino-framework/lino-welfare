.. _welfare.specs.pcsw:
.. _welfare.tested.pcsw:

============
General PCSW
============

..
  To test only this document, run::

    $ python setup.py test -s tests.SpecsTests.test_pcsw

  doctest init:

    >>> from lino import startup
    >>> startup('lino_welfare.projects.std.settings.doctests')
    >>> from lino.api.doctest import *

A technical tour into the :mod:`lino_welfare.modlib.pcsw` module.

.. contents:: Contents
   :local:
   :depth: 2




Choicelists
===========

CivilStates
===========

>>> rt.show(beid.CivilStates)
======= ==================== ====================
 value   name                 text
------- -------------------- --------------------
 10      single               Single
 20      married              Married
 30      widowed              Widowed
 40      divorced             Divorced
 50      separated            Separated
 51      separated_de_facto   De facto separated
 60      cohabitating         Cohabitating
======= ==================== ====================
<BLANKLINE>

ResidenceType
=============

>>> rt.show(beid.ResidenceTypes)
======= ====== ========================
 value   name   text
------- ------ ------------------------
 1              Registry of citizens
 2              Registry of foreigners
 3              Waiting for registry
======= ====== ========================
<BLANKLINE>


ClientEvents
============

>>> rt.show(pcsw.ClientEvents)
=========== =========== ========================
 value       name        text
----------- ----------- ------------------------
 active      active      Coaching
 created     created     Created
 modified    modified    Modified
 note        note        Note
 learning    learning    Learning
 dispense    dispense    Dispense
 penalty     penalty     Penalty
 isip        isip        ISIP
 jobs        jobs        Art60§7 job supplyment
 available   available   Available
 art61       art61       Art61 job supplyment
 immersion   immersion   Immersion training
=========== =========== ========================
<BLANKLINE>

RefusalReasons
==============

>>> rt.show(pcsw.RefusalReasons)
======= ====== ==========================================
 value   name   text
------- ------ ------------------------------------------
 10             Information request (No coaching needed)
 20             PCSW is not competent
 30             Client did not return
======= ====== ==========================================
<BLANKLINE>




eID card summary
----------------

Here a test case (fixed :blogref:`20130827`) 
to test the new `eid_info` field:

>>> soup = get_json_soup('rolf', 'pcsw/Clients/177', 'overview')
>>> print(soup.get_text("\n"))
... #doctest: +ELLIPSIS +NORMALIZE_WHITESPACE +REPORT_UDIFF
Ansicht als Partner ,  Person , Klient
Herr
Bernd 
Brecht
Deutschland
Adressen verwalten
Karte Nr. 591413288107 (Belgischer Staatsbürger), ausgestellt durch Eupen, gültig von 19.08.11 bis 19.08.16

>>> soup = get_json_soup('rolf', 'pcsw/Clients/116', 'overview')
>>> print(soup.get_text("\n"))
... #doctest: +ELLIPSIS +NORMALIZE_WHITESPACE +REPORT_UDIFF
Ansicht als Partner , Person , Klient
Herr
Alfons 
Ausdemwald
Am Bahndamm
4700 Eupen
Adressen verwalten
Karte Nr. 123456789012 (C (Personalausweis für Ausländer)), ausgestellt durch Eupen
, gültig von 19.08.12 bis 18.08.13
Muss eID-Karte einlesen!
Do not offer coffee


Coaching types
--------------

>>> ses = rt.login('robin')
>>> with translation.override('de'):
...    ses.show('coachings.CoachingTypes')
... #doctest: +ELLIPSIS +NORMALIZE_WHITESPACE -REPORT_UDIFF
================= ===================== =================== ====== ====== =====================
 Bezeichnung       Bezeichnung (fr)      Bezeichnung (de)    DSBE   ASD    Role in evaluations
----------------- --------------------- ------------------- ------ ------ ---------------------
 General           SSG                   ASD                 Nein   Ja     Kollege
 Integ             SI                    DSBE                Ja     Nein   Kollege
 Debts mediation   Médiation de dettes   Schuldnerberatung   Nein   Nein
================= ===================== =================== ====== ====== =====================
<BLANKLINE>



Creating a new client
=====================


>>> url = '/api/pcsw/CoachedClients/-99999?an=insert&fmt=json'
>>> res = test_client.get(url, REMOTE_USER='rolf')
>>> res.status_code
200
>>> d = AttrDict(json.loads(res.content))
>>> d.keys()
[u'phantom', u'data', u'title']
>>> d.phantom
True
>>> print(d.title)
Einfügen in Klienten (Begleitet)

There are a lot of data fields:

>>> len(d.data.keys())
70

>>> print(' '.join(sorted(d.data.keys())))
... #doctest: +NORMALIZE_WHITESPACE +REPORT_UDIFF
AgentsByClient MovementsByProject activity activityHidden age
birth_country birth_countryHidden birth_date birth_place broker
brokerHidden cbss_relations civil_state civil_stateHidden client_state
client_stateHidden created cv_LanguageKnowledgesByPerson declared_name
disable_editing disabled_actions disabled_fields
dupable_clients_SimilarClients email excerpts_ExcerptsByProject
faculty facultyHidden fax first_name gender genderHidden group
groupHidden gsm households_MembersByPerson humanlinks_LinksByHuman id
id_document image in_belgium_since is_obsolete language languageHidden
last_name middle_name modified national_id nationality
nationalityHidden needs_residence_permit needs_work_permit
noble_condition obstacles overview phone refusal_reason
refusal_reasonHidden remarks residence_type residence_typeHidden
residence_until row_class seeking_since skills unavailable_until
unavailable_why unemployed_since uploads_UploadsByClient
work_permit_suspended_until workflow_buttons





The detail action
=================

The following would have detected a bug which caused the MTI navigator
to not work (bug has been fixed :blogref:`20150227`) :

>>> from lino.utils.xmlgen.html import E
>>> p = contacts.Person.objects.get(pk=178)
>>> cli = pcsw.Client.objects.get(pk=178)

>>> ses = rt.login('robin')
>>> ar = contacts.Partners.request_from(ses)
>>> print(cli.get_detail_action(ses))
<BoundAction(pcsw.Clients, <lino.core.actions.ShowDetail detail ('Detail')>)>
>>> print(cli.get_detail_action(ar))
<BoundAction(pcsw.Clients, <lino.core.actions.ShowDetail detail ('Detail')>)>

And this tests a potential source of problems in `E.tostring` which I
removed at the same time:

>>> ses = rt.login('robin', renderer=settings.SITE.kernel.extjs_renderer)
>>> ar = contacts.Partners.request_from(ses)
>>> ar.renderer = settings.SITE.kernel.extjs_renderer
>>> print(E.tostring(ar.obj2html(p)))
<a href="javascript:Lino.contacts.Persons.detail.run(null,{ &quot;record_id&quot;: 178 })">Herr Karl KELLER</a>

>>> print(E.tostring(ar.obj2html(cli)))
<a href="javascript:Lino.pcsw.Clients.detail.run(null,{ &quot;record_id&quot;: 178 })">KELLER Karl (178)</a>
>>> print(settings.SITE.kernel.extjs_renderer.instance_handler(ar, cli, None))
Lino.pcsw.Clients.detail.run(null,{ "record_id": 178 })
>>> print(E.tostring(p.get_mti_buttons(ar)))
... #doctest: +ELLIPSIS +NORMALIZE_WHITESPACE -REPORT_UDIFF
<a href="javascript:Lino.contacts.Partners.detail.run(null,{
&quot;record_id&quot;: 178 })">Partner</a>, <b>Person</b>, <a
href="javascript:Lino.pcsw.Clients.detail.run(null,{
&quot;record_id&quot;: 178 })">Klient</a> [<a
href="javascript:Lino.contacts.Partners.del_client(null,178,{
})...">&#10060;</a>]


Virtual fields on client
========================

The following snippet just tests some virtual fields on Client for
runtime errors.

>>> vfields = ('primary_coach', 'coaches', 'active_contract', 'contract_company',
...     'find_appointment', 'cbss_relations', 'applies_from', 'applies_until')
>>> counters = { k: set() for k in vfields }
>>> for cli in pcsw.Client.objects.all():
...     for k in vfields:
...         counters[k].add(getattr(cli, k))
>>> [len(counters[k]) for k in vfields]
[1, 21, 18, 4, 1, 1, 18, 18]

