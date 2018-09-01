.. doctest docs/specs/main.rst
.. _welfare.specs.main:

===================
The admin main page
===================

..  doctest init:
    
    >>> from lino import startup
    >>> startup('lino_welfare.projects.eupen.settings.doctests')
    >>> from lino.api.doctest import *


A technical tour into the main page of :ref:`welfare`.

.. contents::
   :depth: 2

Test the content of the admin main page.

>>> test_client.force_login(rt.login('rolf').user)
>>> res = test_client.get('/api/main_html', REMOTE_USER='rolf')
>>> print(res.status_code)
200
>>> result = json.loads(res.content)
>>> result['success']
True
>>> # print(html2text(result['html']))
>>> soup = BeautifulSoup(result['html'], 'lxml')

We might test the complete content here, but currently we skip this as
it is much work to maintain.

>>> print(soup.get_text(' ', strip=True))
... #doctest: +NORMALIZE_WHITESPACE +REPORT_CDIFF +SKIP

>>> links = soup.find_all('a')
>>> len(links)
115

>>> print(links[0].text)
Suchen

>>> tables = soup.find_all('table')
>>> len(tables)
4

>>> for h in soup.find_all('h2'):
...     print(h.text.strip())
Benutzer und ihre Klienten ⏏
Wartende Besucher ⏏
Meine Termine ⏏
Meine überfälligen Termine ⏏
Meine Benachrichtigungen ⏏


>>> test_client.force_login(rt.login('robin').user)
>>> res = test_client.get('/api/main_html', REMOTE_USER='robin')
>>> print(res.status_code)
200
>>> result = json.loads(res.content)
>>> soup = BeautifulSoup(result['html'], 'lxml')
>>> for h in soup.find_all('h2'):
...     print(h.text.strip())
Users with their Clients ⏏
Waiting visitors ⏏
My appointments ⏏
My overdue appointments ⏏
My Notification messages ⏏
