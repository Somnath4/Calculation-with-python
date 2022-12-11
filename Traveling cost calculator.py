# Traveling cost calculator
try:
    return_flight = int(input('Enter flight cost($): '))        # Enter you return flight amount
    hotel = int(input('Enter per day hotel cost($): '))         # Enter hotel cost per day
    food = int(input('Enter daily food cost: '))                # Daily food cost including breakfast to dinner. 
    car_rent = int(input('Enter weekly car rent cost($): '))    # Enter weekly car rent amount
    duration = int(input('Enter duration(days): '))             # Enter how many days you're gonna stay
    car_rent_day = car_rent / duration                          # Weekly car cost divided by total duration day 
    city = input('Enter the city name: ')                       # Enter the city name you want to visit
    def cost_of_trip():
        cost = return_flight + (hotel + car_rent_day + food) * duration    # Calculation of traveling cost
        return(cost)
    total_cost = cost_of_trip()
    print('{} days trip to {} will cost ${}'.format(duration, city, total_cost))  # Returns the total cost including days and the city

except:
    print('You can only enter numbers except in city')      # Error message when enter wrong
    exit()                                                  # This will terminate the program when you enter wrong
    
