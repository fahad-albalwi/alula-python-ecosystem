"""Run after installing all three packages: python examples/demo.py"""
from pprint import pprint
from alula_cropwatch import summarize_field
from alula_waterwise import fao56_et0, irrigation_budget, groundwater_trend
from alula_heritage import plan_day

print('CROP (synthetic satellite reflectance):')
pprint(summarize_field([{'B04':0.12,'B08':0.51,'B11':0.24},{'B04':0.19,'B08':0.43,'B11':0.31}]))
print('\nWATER (synthetic weather/field):')
et0=fao56_et0(21,36,35,2,13)
print('ET0:',et0,'mm/day')
pprint(irrigation_budget(et0,0.9,10000,effective_rain_mm=0))
pprint(groundwater_trend([('2026-01-01',30.2),('2026-02-01',30.8)]))
print('\nTOURISM (illustrative only):')
pprint(plan_day(240))
