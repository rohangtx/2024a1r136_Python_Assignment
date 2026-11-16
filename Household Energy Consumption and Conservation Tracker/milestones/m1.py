# Milestone 1 - Estimate electricity use for ONE appliance
name = input("Appliance name: ")
power = float(input("Power (W): "))          # numeric input -> float
hours = float(input("Hours used per day: ")) # numeric input -> float
days = int(input("Number of days: "))        # whole number -> int
tariff = float(input("Tariff per kWh (Rs): "))

print("\nData type of power :", type(power))
print("Data type of hours :", type(hours))

kwh = (power / 1000) * hours * days
cost = kwh * tariff

print("\n===== MONTHLY ESTIMATE =====")
print("Appliance :", name.strip().title())   # string operation: strip() + title()
print(f"Energy    : {kwh:.2f} kWh")
print(f"Cost      : Rs. {cost:.2f}")
