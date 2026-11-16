"""energy_utils.py - helper functions for the Household Energy Tracker (Milestone 4)."""

CATALOGUE = {"LED Bulb": 12, "Ceiling Fan": 75, "Television": 120,
             "Refrigerator": 180, "AC": 1500}


def calculate_kwh(power_watts, hours_per_day, units=1, days=30):
    """Monthly energy in kWh; days defaults to 30."""
    return power_watts / 1000 * hours_per_day * units * days


def calculate_cost(kwh, tariff=6.50):
    """Cost in Rs.; tariff defaults to Rs. 6.50/kWh."""
    return kwh * tariff


def classify_usage(total_kwh):
    if total_kwh < 150:
        return "Low"
    if total_kwh <= 300:
        return "Moderate"
    return "High"


def household_total(records, days=30):
    """records: list of (name, units, hours_per_day) -> total kWh."""
    return sum(calculate_kwh(CATALOGUE[n], h, u, days) for n, u, h in records)
