# AlUla Python Ecosystem

**Independent project by FAHAD SAAD ALBALWI.**

This repository contains three experimental Python packages for crop monitoring (`alula-cropwatch`), water and irrigation estimates (`alula-waterwise`), and heritage information (`alula-heritage`). The repository is independent of the Royal Commission for AlUla and is not endorsed by it. The packages use deterministic demonstration calculations and curated illustrative tourism metadata; they are NOT connected to live satellites/weather, certified irrigation advice, or live booking systems.

## Start locally (Python 3.10+)

```powershell
py -m pip install -e ./alula_cropwatch -e ./alula_waterwise -e ./alula_heritage
py -m unittest discover -s tests -v
py examples/demo.py
```

You may also use `تشغيل_المشروع.bat` on Windows.

## Project structure

- `alula_cropwatch/`, `alula_waterwise/`, `alula_heritage/`: independent package sources and packaging metadata
- `tests/`: basic regression tests; scientific validation is pending
- `.github/workflows/`: test workflow and independent manual publication workflows
- `PUBLISH_AR.md`: novice-friendly publication instructions
- `SUNWISE_PLAN_AR.md`: original solar sensing concept and staged low-cost prototype

## Publishing

Package names are requested, not reserved until PyPI accepts a release. Set up three *pending trusted publishers* with the repository and corresponding workflow filenames documented in `PUBLISH_AR.md`. Run `tests.yml` first and publish each package manually with GitHub Actions only after reviewing its contents. All three publish workflows use GitHub's PyPI environment, OIDC and the official pypa/gh-action-pypi-publish action.

## License and attribution

MIT, copyright 2026 FAHAD SAAD ALBALWI, with third-party software licensed separately where later dependencies are used. Do not claim official RCU affiliation.
