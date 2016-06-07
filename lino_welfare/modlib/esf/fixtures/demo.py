from lino.api import rt

from lino_welfare.modlib.esf.choicelists import StatisticalFields
from lino.utils.cycler import Cycler

FIELDS = Cycler(StatisticalFields.objects())


def objects():
    EventType = rt.modules.cal.EventType
    for et in EventType.objects.all():
        et.esf_field = FIELDS.pop()
        yield et