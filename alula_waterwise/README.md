# alula-waterwise

Author: **FAHAD SAAD ALBALWI**  
License: MIT  
Status: **experimental v0.1.0**

Reference evapotranspiration and irrigation estimates for AlUla.

## Installation

Once publicly released to PyPI:

```bash
python -m pip install alula-waterwise
```

Before release, install locally from this folder with `python -m pip install .`.

## Public functions

`fao56_et0, irrigation_budget, groundwater_trend, rain_summary` (import from `alula_waterwise`).

## Limitations

This first release does **not** download live satellite imagery, live weather, actual booking availability or validate agricultural decisions. Examples are educational and estimates require site calibration. This project is independent and is **not affiliated with or endorsed by** the Royal Commission for AlUla.

See the parent repository for a demonstration, tests, and full documentation.
