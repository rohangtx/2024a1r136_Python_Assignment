# Milestone 3 - Object-Oriented version
class ApplianceUsage:
    days_in_month = 30                                   # class variable

    def __init__(self, appliance_name, power_watts, hours_per_day, units):
        self.appliance_name = appliance_name
        self.power_watts = power_watts
        self.hours_per_day = hours_per_day
        self.units = units

    def calculate_kwh(self):
        return self.power_watts / 1000 * self.hours_per_day * self.units * self.days_in_month

    def calculate_cost(self, tariff):
        return self.calculate_kwh() * tariff

    def display_summary(self, tariff=6.50):
        print(f"{self}\n  Monthly energy: {self.calculate_kwh():.2f} kWh"
              f" | Estimated cost: Rs. {self.calculate_cost(tariff):.2f}")

    def __str__(self):
        return (f"{self.appliance_name} ({self.units} unit(s), {self.power_watts} W, "
                f"{self.hours_per_day} h/day)")


catalogue = {"LED Bulb": 12, "Ceiling Fan": 75, "Television": 120,
             "Refrigerator": 180, "AC": 1500}
lookup = {k.lower(): k for k in catalogue}

objects = []
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
    key = lookup[name.lower()]
    objects.append(ApplianceUsage(key, catalogue[key], hours, units))

print("\n----- MONTHLY SUMMARY -----")
for obj in objects:
    obj.display_summary(6.50)
total = sum(o.calculate_kwh() for o in objects)
top = max(objects, key=lambda o: o.calculate_kwh())
print(f"Total: {total:.2f} kWh | Highest: {top.appliance_name} | "
      f"Level: {'Low' if total < 150 else 'Moderate' if total <= 300 else 'High'}")
