# Ontario Electrical Service Load Estimator

A planning estimator for the electrical service of a small commercial unit: enter connected loads by category, apply stated demand factors, and get the demand kVA, the current at 120/208 V three-phase or 120/240 V single-phase, and the next standard service size.

**Live web tool:** https://dust2engineering.github.io/ontario-electrical-service-load-estimator/web/

## How it works

- Demand factors are printed in the open (lighting 1.0, kitchen equipment 0.8, HVAC 1.0, receptacles 0.5, other 1.0) so the estimate is auditable.
- This is not the CEC Rule 8-200/8-202 demand calculation used for permit; it is the feasibility answer before that design starts.

## Data in this repository

- service-load-data.json — method, standard sizes and default factors, machine-readable.

## Command line

```bash
python3 service_load.py --lighting-kw 6 --kitchen-kw 45 --hvac-kw 18 --receptacles-kw 8 --other-kw 5
```

## Worked examples

- [restaurant-200a-service.md](examples/restaurant-200a-service.md)
- [retail-100a-service.md](examples/retail-100a-service.md)

## Scope and limits

Preliminary design aid only. It does not replace the current Ontario Building Code or the judgement of the designer of record. Verify all values against the Code in force for your project before submitting drawings for permit.

## About

Maintained by **Dust 2 Engineering Inc.** (Mississauga, Ontario) — building permit drawings
(architectural, HVAC, plumbing, sprinkler, electrical) for restaurants and small commercial
projects across the Greater Toronto Area, stamped by an Ontario P.Eng. Flat rate $3,500–$5,000.

Category: Electrical. More free Ontario code tools: see the full index at
https://github.com/dust2engineering
