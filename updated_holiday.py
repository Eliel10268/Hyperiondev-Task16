
def hotel_cost(num_nights):
    price_per_night = 100  # Assuming a fixed price per night
    return num_nights * price_per_night

def plane_cost(city_flight):
    # Set default cost in case the city is not recognized
    default_cost = 500

    if city_flight == "New York":
        return 500
    elif city_flight == "Paris":
        return 800
    elif city_flight == "Tokyo":
        return 1000
    else:
        print("City not recognized. Using default cost.")
        return default_cost

def car_rental(rental_days):
    daily_rental_cost = 50  # Assuming a fixed daily rental cost
    return rental_days * daily_rental_cost


# this function calculates the total cost of the holiday by
# adding the costs of the hotel stay,
# the flight, and the car rental
def holiday_cost(num_nights, city_flight, rental_days):
    total_cost = hotel_cost(num_nights) + plane_cost(city_flight) + car_rental(rental_days)
    return total_cost

# Get user inputs
valid_cities = ["New York", "Paris", "Tokyo"]
city_flight = input("Enter the city you will be flying to (New York, Paris, Tokyo): ")

# Prompt the user until a valid city is entered
while city_flight not in valid_cities:
    print("Invalid city. Please enter a valid city.")
    city_flight = input("Enter the city you will be flying to (New York, Paris, Tokyo): ")

num_nights = int(input("Enter the number of nights you will be staying at a hotel: "))
rental_days = int(input("Enter the number of days you will be hiring a car for: "))

# Calculate holiday cost
total_cost = holiday_cost(num_nights, city_flight, rental_days)

# Print holiday details
print("\nHoliday Details")
print("--------------")
print("City of Flight: ", city_flight)
print("Hotel Cost: $", hotel_cost(num_nights))
print("Plane Cost: $", plane_cost(city_flight))
print("Car Rental Cost: $", car_rental(rental_days))
print("Total Holiday Cost: $", total_cost)
