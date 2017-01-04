import datetime
from lino_welfare.projects.chatelet.settings import *


class Site(Site):
    # title = "Welfare Chatelet Demo"
    the_demo_date = datetime.date(2014, 5, 22)
    # ignore_dates_after = datetime.date(2019, 05, 22)
    use_java = False
    # use_silk_icons = True  # temporarily


SITE = Site(globals())

DEBUG = True
