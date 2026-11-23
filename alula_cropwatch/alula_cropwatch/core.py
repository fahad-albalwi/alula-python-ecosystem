"""Sentinel-2 convention: B04=red, B08=NIR, B11=SWIR1 (resample grids first)."""
from math import isfinite
from statistics import mean

def _num(v):
    if isinstance(v, bool) or not isinstance(v, (int, float)) or not isfinite(v):
        raise ValueError('Band values must be finite numeric reflectance')
    return float(v)

def _ratio(a,b):
    a,b=_num(a),_num(b)
    return None if a+b == 0 else (a-b)/(a+b)

def ndvi(nir, red):
    """Normalized Difference Vegetation Index; None if denominator is zero."""
    return _ratio(nir, red)

def ndmi(nir, swir1):
    """Normalized Difference Moisture Index (vegetation moisture proxy, not direct soil water)."""
    return _ratio(nir, swir1)

def summarize_field(pixels):
    """Pixels: iterable of {'B04': red, 'B08': nir, 'B11': swir1}."""
    rows=list(pixels)
    if not rows:
        raise ValueError('At least one pixel required')
    stats=analyze_pixels(rows)
    valid_ndvi=[r['ndvi'] for r in stats if r['ndvi'] is not None]
    valid_ndmi=[r['ndmi'] for r in stats if r['ndmi'] is not None]
    return {'pixel_count':len(rows), 'valid_ndvi_count':len(valid_ndvi),
            'mean_ndvi':round(mean(valid_ndvi),4) if valid_ndvi else None,
            'mean_ndmi':round(mean(valid_ndmi),4) if valid_ndmi else None,
            'note':'Indices are descriptive; field calibration and cloud masking required.'}

def analyze_pixels(pixels):
    return [{'ndvi':ndvi(p['B08'],p['B04']), 'ndmi':ndmi(p['B08'],p['B11'])} for p in pixels]
