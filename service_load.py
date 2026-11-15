#!/usr/bin/env python3
"""Preliminary electrical service size estimator for a small commercial unit."""
import argparse, json, os
D = json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "service-load-data.json")))

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--lighting-kw", type=float, default=0)
    p.add_argument("--kitchen-kw", type=float, default=0)
    p.add_argument("--hvac-kw", type=float, default=0)
    p.add_argument("--receptacles-kw", type=float, default=0)
    p.add_argument("--other-kw", type=float, default=0)
    p.add_argument("--system", default="3ph208", choices=["3ph208", "1ph240"])
    a = p.parse_args()
    f = D["default_demand_factors_for_planning"]
    loads = {"lighting": a.lighting_kw, "kitchen_equipment": a.kitchen_kw, "hvac": a.hvac_kw,
             "receptacles": a.receptacles_kw, "other": a.other_kw}
    conn = sum(loads.values())
    dem = sum(loads[k] * f[k] for k in loads)
    amps = dem * 1000 / (1.732 * 208) if a.system == "3ph208" else dem * 1000 / 240
    size = next((s for s in D["standard_service_sizes_a"] if s >= amps), None)
    print(f"Connected load: {conn:.1f} kW | Demand load (planning factors): {dem:.1f} kVA")
    print(f"At {'120/208 V 3-phase' if a.system == '3ph208' else '120/240 V single-phase'}: {amps:.0f} A -> standard service size: {size} A" if size else "Exceeds 800 A standard sizes in this estimator")
    print("Preliminary planning estimate only - the permit design uses the CEC Section 8 demand calculation.")

if __name__ == "__main__":
    main()
