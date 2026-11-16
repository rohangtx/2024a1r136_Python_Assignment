"""main.py - Household Energy Consumption and Conservation Tracker (final version)."""
import time
from energy_utils import (CATALOGUE, calculate_kwh, calculate_cost, classify_usage,
                          household_total, save_record, read_records)

FILE = "energy_records.txt"
lookup = {k.lower(): k for k in CATALOGUE}


def add_appliance(records):
    """Option 1: read one appliance, validate it, and add it to this month's list."""
    print("Available:", ", ".join(CATALOGUE))
    name = input("Appliance name: ").strip()
    if name.lower() not in lookup:
        print("  Rejected: unknown appliance.")
        return
    try:
        units = int(input("  Number of units: "))
        hours = float(input("  Hours per day: "))
    except ValueError:
        print("  ValueError: please enter numbers only. Entry skipped.")
        return
    if units <= 0 or hours <= 0 or hours > 24:
        print("  Rejected: impossible usage (units > 0, hours > 0 and <= 24).")
        return
    key = lookup[name.lower()]
    records.append((key, units, hours))
    print(f"  Added {key}: {calculate_kwh(CATALOGUE[key], hours, units):.2f} kWh/month")


def monthly_summary(records):
    """Option 2: show the monthly summary table, then save the record to the file."""
    if not records:
        print("No appliances added yet. Use option 1 first.")
        return
    try:
        tariff = float(input("Tariff per kWh in Rs. (e.g. 6.50): "))
        if tariff <= 0:
            raise ValueError
    except ValueError:
        print("  ValueError: invalid tariff, using default 6.50.")
        tariff = 6.50

    total = household_total(records)
    top = max(records, key=lambda r: calculate_kwh(CATALOGUE[r[0]], r[2], r[1]))[0]
    level = classify_usage(total)

    print("\n" + "=" * 62)
    print("                MONTHLY ENERGY SUMMARY (30 days)")
    print("=" * 62)
    print(f"{'Appliance':<14}{'Units':>6}{'Hrs/day':>9}{'kWh':>10}{'Cost (Rs.)':>14}")
    print("-" * 62)
    for n, u, h in records:
        k = calculate_kwh(CATALOGUE[n], h, u)
        print(f"{n:<14}{u:>6}{h:>9.1f}{k:>10.2f}{calculate_cost(k, tariff):>14.2f}")
    print("-" * 62)
    print(f"{'TOTAL':<29}{total:>10.2f}{calculate_cost(total, tariff):>14.2f}")
    print("=" * 62)
    print(f"Tariff used       : Rs. {tariff:.2f} per kWh")
    print(f"Highest appliance : {top}")
    print(f"Usage level       : {level}")
    print("Report generated  :", time.strftime("%d-%m-%Y %H:%M:%S"))

    items = ", ".join(f"{n} x{u} @ {h}h" for n, u, h in records)
    line = (f"{time.strftime('%d-%m-%Y %H:%M')} | {items} | Total: {total:.2f} kWh | "
            f"Cost: Rs. {calculate_cost(total, tariff):.2f} | Highest: {top} | Level: {level}")
    save_record(FILE, line)
    print(f"\nMonthly record saved to {FILE}.")
    records.clear()                                  # ready for the next month


def view_records():
    """Option 3: read the saved file and show every record clearly, one field per line."""
    try:
        lines = read_records(FILE)
    except FileNotFoundError:
        print(f"FileNotFoundError: '{FILE}' does not exist yet. "
              "Add appliances and run the monthly summary first.")
        return
    if not lines:
        print("No records saved yet.")
        return
    print("\n" + "=" * 62)
    print(f"                SAVED RECORDS ({len(lines)} found)")
    print("=" * 62)
    for i, ln in enumerate(lines, 1):
        parts = ln.split(" | ")
        if len(parts) != 6:                          # unexpected format: show as it is
            print(f"Record {i}: {ln}")
            continue
        date, items, total, cost, highest, level = parts
        print(f"Record {i}  (saved on {date})")
        print("  Appliances used:")
        for item in items.split(", "):
            print(f"    - {item}")
        print(f"  {total}")
        print(f"  {cost}")
        print(f"  {highest}")
        print(f"  {level}")
        print("-" * 62)


def main():
    records = []                                     # appliances for the current month
    while True:
        choice = input("\n1.Add appliance 2.Monthly summary 3.View saved records 4.Exit : ").strip()
        if choice == "1":
            add_appliance(records)
        elif choice == "2":
            monthly_summary(records)
        elif choice == "3":
            view_records()
        elif choice == "4":
            print("Report generated on:", time.strftime("%d-%m-%Y %H:%M:%S"))
            break
        else:
            print("Invalid choice. Enter 1, 2, 3 or 4.")


if __name__ == "__main__":
    main()
