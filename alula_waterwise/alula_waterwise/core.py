"""Engineering demonstration, not certified agronomic advice."""
from math import exp, isfinite
from statistics import mean

def _check(**values):
    for key,value in values.items():
        if isinstance(value,bool) or not isinstance(value,(int,float)) or not isfinite(value):
            raise ValueError(f'{key} must be finite numeric')

def _svp(temp_c):
    return 0.6108 * exp(17.27 * temp_c / (temp_c + 237.3))

def fao56_et0(tmin_c, tmax_c, relative_humidity_pct, wind_2m_ms, net_radiation_mj_m2_day,
              elevation_m=700.0, soil_heat_flux_mj_m2_day=0.0):
    """Daily FAO-56 Penman-Monteith reference ET0 (mm/day), approximate actual vapour pressure from mean RH.

    Requires measured/estimated *net* radiation, not sunshine duration. Inputs must
    reflect local site; do not treat as a validated field irrigation prescription.
    """
    _check(tmin_c=tmin_c,tmax_c=tmax_c,relative_humidity_pct=relative_humidity_pct,
           wind_2m_ms=wind_2m_ms,net_radiation_mj_m2_day=net_radiation_mj_m2_day,
           elevation_m=elevation_m,soil_heat_flux_mj_m2_day=soil_heat_flux_mj_m2_day)
    if not (-50 < tmin_c <= tmax_c < 65) or not 0 <= relative_humidity_pct <= 100 or wind_2m_ms < 0:
        raise ValueError('Invalid weather input range')
    t=(tmin_c+tmax_c)/2
    es=(_svp(tmin_c)+_svp(tmax_c))/2
    ea=es*relative_humidity_pct/100
    delta=4098*_svp(t)/((t+237.3)**2)
    pressure=101.3*((293-0.0065*elevation_m)/293)**5.26
    gamma=0.000665*pressure
    numerator=0.408*delta*(net_radiation_mj_m2_day-soil_heat_flux_mj_m2_day)+gamma*(900/(t+273))*wind_2m_ms*(es-ea)
    denominator=delta+gamma*(1+0.34*wind_2m_ms)
    return round(max(0.0,numerator/denominator),3)

def irrigation_budget(et0_mm_day, crop_coefficient, area_m2, effective_rain_mm=0.0,
                      irrigation_efficiency=0.85):
    """Simplified single-day gross irrigation estimate; excludes storage, salinity and leaching."""
    _check(et0_mm_day=et0_mm_day,crop_coefficient=crop_coefficient,area_m2=area_m2,
           effective_rain_mm=effective_rain_mm,irrigation_efficiency=irrigation_efficiency)
    if min(et0_mm_day,crop_coefficient,area_m2,effective_rain_mm)<0 or not 0<irrigation_efficiency<=1:
        raise ValueError('Invalid water-budget parameters')
    etc=et0_mm_day*crop_coefficient
    net=max(0,etc-effective_rain_mm)
    gross=net/irrigation_efficiency
    return {'etc_mm_day':round(etc,3),'net_irrigation_mm':round(net,3),
            'gross_irrigation_mm':round(gross,3),'gross_irrigation_m3':round(gross*area_m2/1000,3)}

def groundwater_trend(records):
    """Records: sorted (ISO date, depth_to_water_m) pairs; increasing depth = falling water table.

    Needs consistent survey datum and measurement method.
    """
    records=list(records)
    if len(records)<2: raise ValueError('At least 2 readings required')
    if records!=sorted(records,key=lambda x:x[0]): raise ValueError('Sort records by date')
    for _,depth in records: _check(depth=depth)
    change=records[-1][1]-records[0][1]
    return {'first_date':records[0][0],'last_date':records[-1][0],
            'depth_change_m':round(change,3),
            'interpretation':'water_table_lower' if change>0 else ('water_table_higher' if change<0 else 'stable_depth')}

def rain_summary(daily_mm):
    daily=list(daily_mm)
    if not daily: raise ValueError('At least one day required')
    for val in daily:
        _check(rainfall=val)
        if val<0: raise ValueError('Rain cannot be negative')
    return {'days':len(daily),'total_mm':round(sum(daily),3),'mean_mm_day':round(mean(daily),3),'rainy_days':sum(x>0 for x in daily)}
