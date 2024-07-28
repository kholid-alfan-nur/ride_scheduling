import pandas as pd

# Constants
DRIVER_CAC = 500  # Average cost to acquire a new driver
RIDER_CAC = 15    # Average cost to acquire a new rider
INITIAL_RIDERS = 1000
INITIAL_DRIVERS = 100
RIDES_PER_MONTH_PER_DRIVER = 100

# Churn rates
RIDER_CHURN_RATE_NO_FAIL = 0.10
RIDER_CHURN_RATE_FAIL = 0.33
DRIVER_CHURN_RATES = {
    'Scenario 1': 0.05,
    'Scenario 2': 0.03,
    'Scenario 3': 0.04,
}

# Match rates
MATCH_RATES = {
    'Scenario 1': 0.60,
    'Scenario 2': 0.93,
    'Scenario 3': 0.85,
}

# Function to calculate net revenue
def calculate_net_revenue(rider_payment, driver_earnings):
    results = []

    for scenario in DRIVER_CHURN_RATES.keys():
        # Churn rates and match rates
        driver_churn_rate = DRIVER_CHURN_RATES[scenario]
        match_rate = MATCH_RATES[scenario]
        
        # Calculate total rides and fulfilled rides
        total_rides = INITIAL_RIDERS
        fulfilled_rides = total_rides * match_rate
        
        # Calculate Lyft's take per ride
        lyft_take = rider_payment - driver_earnings
        
        # Calculate revenue from rides
        total_lyft_revenue = fulfilled_rides * lyft_take
        
        # Calculate driver churn costs
        driver_churn_cost = INITIAL_DRIVERS * driver_churn_rate * DRIVER_CAC
        
        # Calculate rider churn costs
        failed_matches = total_rides - fulfilled_rides
        rider_churn_cost = (failed_matches * RIDER_CHURN_RATE_FAIL + fulfilled_rides * RIDER_CHURN_RATE_NO_FAIL) * RIDER_CAC
        
        # Calculate net revenue
        net_revenue = total_lyft_revenue - driver_churn_cost - rider_churn_cost
        results.append((scenario, net_revenue))

    return results

# Input values
rider_payment = float(input("Enter how much riders pay per trip: "))
driver_earnings = float(input("Enter how much drivers earn per trip: "))

# Calculate net revenue
net_revenue_results = calculate_net_revenue(rider_payment, driver_earnings)

# Display results
for scenario, net_revenue in net_revenue_results:
    print(f"{scenario}: Net Revenue = ${net_revenue:.2f}")