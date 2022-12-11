import scipy.stats as sp

# Geometric distribution calculation
try:
    trials = int(input('Enter number of trials: '))     # number of trials
    probability = float(input('Enter probability: '))    # probability of success
    def geom_distribution():                            # Defines the function
        geom_exact = sp.geom.pmf(trials,probability)      # Calculation of the geometric normal distribution
        geom_cumulative = sp.geom.cdf(trials,probability) # Calculation of the geometric cumulative distribution
        print('Geometric distribution for exact value {}'.format(geom_exact)) # Returns the geometric distribution of the exact value
        print('Geometric cumulative distribution for the value {}'.format(geom_cumulative))  # Returns the geometric distribution of the value
    geom_distribution()
except:                                                 
    print('You can only enter numbers')                 # Returns an error message when enter wrong
    exit()                                              # This will terminate the program when you enter wrong