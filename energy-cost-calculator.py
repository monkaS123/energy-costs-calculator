# Sample Code for Foo Electric's Energy Costs Calculator

class EnergyUsage:
    def __init__(self, kWh, rate_per_kWh):
        self.kWh = kWh
        self.rate_per_kWh = rate_per_kWh

    def calculate_cost(self):
        return self.kWh * self.rate_per_kWh


def main():
    # Example usage data (in kilowatt-hours)
    monthly_usage_kWh = 350

    # Energy rate (cost per kilowatt-hour in dollars)
    energy_rate = 0.12

    # Create an instance of EnergyUsage
    energy_usage = EnergyUsage(monthly_usage_kWh, energy_rate)

    # Calculate and print the cost
    cost = energy_usage.calculate_cost()
    print(f"The total energy cost for the month is: ${cost:.2f}")


if __name__ == "__main__":
    main()
