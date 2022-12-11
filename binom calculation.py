import scipy.stats as sp

# Binomial distribution calculation
try:
    trials = int(input('Enter number of trials: '))     # the 'trials' is the total number of trials
    success = int(input('Enter number of success: '))   # 'success' is the total number of success
    probability = float(input('Enter probability: '))    # 'probability' is the probability of success not failure
    def binom_distribution():                           # Defines a function
        binom_exact = sp.binom.pmf(success,trials,probability)        # calculate for the exact value
        binom_cumulative = sp.binom.cdf(success,trials,probability) # calculate for the cumulative value
        print('Binomial distribution for exact value {}'.format(binom_exact)) # Returns distribution of the exact value
        print('Binomial distribution for cumulative value binom_cumulative {}'.format(binom_cumulative)) # Returns distribution of the cumulative value
    binom_distribution()
except:
    print('You can only enter numbers.') # Returns an error message when enter wrong
    exit()                               # This will terminate the program when you enter wrong
