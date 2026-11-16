# Milestone 2 - Multiple appliances using collections, decisions and loops
DAYS = 30
catalogue = {"LED Bulb": 12, "Ceiling Fan": 75, "Television": 120,
             "Refrigerator": 180, "AC": 1500}          # dictionary: name -> watts
lookup = {k.lower(): k for k in catalogue}             # case-insensitive matching

records = []                                           # list of (name, units, hours, kwh)
while True:
    name = input("Appliance name (or DONE): ").strip()
    if name.upper() == "DONE":
        break
    if name.lower() not in lookup:
        print("  Rejected: unknown appliance.")
        continue
    units = int(input("  Number of units: "))
    hours = float(input("  Hours per day: "))
    if units <= 0 or hours <= 0 or hours > 24:
        print("  Rejected: invalid units/hours (hours must be >0 and <=24).")
        continue
    key = lookup[name.lower()]
    kwh = catalogue[key] / 1000 * hours * units * DAYS
    records.append((key, units, hours, kwh))
    print(f"  Added {key}: {kwh:.2f} kWh")

if records:
    total = sum(r[3] for r in records)
    top = max(records, key=lambda r: r[3])
    print("\n----- MONTHLY SUMMARY (30 days) -----")
    for n, u, h, k in records:
        print(f"{n:<14} x{u}  {h:>4} h/day  {k:>8.2f} kWh")
    print(f"Total consumption : {total:.2f} kWh")
    print(f"Highest appliance : {top[0]} ({top[3]:.2f} kWh)")
    level = "Low" if total < 150 else "Moderate" if total <= 300 else "High"
    print(f"Usage level       : {level}")
else:
    print("No valid records entered.")
