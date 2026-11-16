import time
from energy_utils import CATALOGUE, calculate_kwh, calculate_cost, classify_usage, household_total

lookup = {k.lower(): k for k in CATALOGUE}
records = []
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
        print("  Rejected: invalid units/hours.")
        continue
    records.append((lookup[name.lower()], units, hours))

total = household_total(records)                 # default days=30
print("\n===== MONTHLY ENERGY REPORT =====")
for n, u, h in records:
    k = calculate_kwh(CATALOGUE[n], h, u)
    print(f"{n:<14} x{u} {h:>5} h/day {k:>8.2f} kWh  Rs. {calculate_cost(k):>8.2f}")
print(f"Total      : {total:.2f} kWh | Cost (default tariff 6.50): Rs. {calculate_cost(total):.2f}")
print(f"Cost @ 7.25: Rs. {calculate_cost(total, tariff=7.25):.2f}   (keyword argument)")
print(f"Usage level: {classify_usage(total)}")
print("Report generated on:", time.strftime("%d-%m-%Y %H:%M:%S"))
