"""Static curated sites, not authoritative live booking, access, or hours information."""
from copy import deepcopy

_SITES=(
    {'id':'hegra','name_ar':'الحِجر (مدائن صالح)','name_en':'Hegra','category':'heritage','suggested_minutes':120,'booking_check':True},
    {'id':'dadan','name_ar':'دادان','name_en':'Dadan','category':'heritage','suggested_minutes':90,'booking_check':True},
    {'id':'jabal_ikmah','name_ar':'جبل عِكمة','name_en':'Jabal Ikmah','category':'heritage','suggested_minutes':90,'booking_check':True},
    {'id':'old_town','name_ar':'بلدة العلا القديمة','name_en':'AlUla Old Town','category':'heritage','suggested_minutes':90,'booking_check':True},
    {'id':'oasis','name_ar':'واحة العلا','name_en':'AlUla Oasis','category':'nature','suggested_minutes':90,'booking_check':True},
)
SOURCE_URL='https://www.experiencealula.com/en'

def attractions(category=None):
    return deepcopy([site for site in _SITES if category is None or site['category']==category])

def search(query):
    q=query.strip().casefold()
    if not q: return []
    return deepcopy([s for s in _SITES if q in s['name_ar'].casefold() or q in s['name_en'].casefold()])

def plan_day(minutes_available=360,category=None):
    """Time-budget selection ONLY: no travel time, opening hours or tour availability."""
    if not isinstance(minutes_available,int) or isinstance(minutes_available,bool) or minutes_available<=0:
        raise ValueError('minutes_available must be a positive integer')
    remaining=minutes_available
    selected=[]
    for site in attractions(category):
        if site['suggested_minutes']<=remaining:
            selected.append(site)
            remaining-=site['suggested_minutes']
    return {'sites':selected,'visit_minutes':minutes_available-remaining,'unallocated_minutes':remaining,
            'notice':'Illustrative only. Add transport and breaks; check official bookings, opening times and access.',
            'official_source':SOURCE_URL}
