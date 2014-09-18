# -*- coding: UTF-8 -*-
# Copyright 2014 Luc Saffre
# License: BSD (see file COPYING for details)

from __future__ import unicode_literals
from __future__ import print_function

import logging
logger = logging.getLogger(__name__)

from django.utils.translation import ugettext_lazy as _

from lino import dd


def objects():
    CourseAreas = dd.modules.courses.CourseAreas
    Line = dd.modules.courses.Line
    Course = dd.modules.courses.Course

    def line(course_area, name, **kw):
        kw.update(course_area=course_area)
        kw.update(dd.str2kw('name', name))
        return Line(**kw)

    obj = line(CourseAreas.integ, _("Kitchen"))
    yield obj
    yield Course(line=obj, start_date=dd.demo_date(-10))

    obj = line(CourseAreas.integ, _("Creativity"))
    yield obj
    yield Course(line=obj, start_date=dd.demo_date(-10))

    obj = line(CourseAreas.integ, _("Our first baby"))
    yield obj
    yield Course(line=obj, start_date=dd.demo_date(-10))

    obj = line(CourseAreas.basic, _("Mathematics"))
    yield obj
    yield Course(line=obj, start_date=dd.demo_date(-10))

    obj = line(CourseAreas.basic, _("French"))
    yield obj
    yield Course(line=obj, start_date=dd.demo_date(-10))

    obj = line(CourseAreas.job, _("Get active!"))
    yield obj
    yield Course(line=obj, start_date=dd.demo_date(-10))
