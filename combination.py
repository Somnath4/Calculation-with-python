import itertools as it                                          # importing 'itertools' library

# combination
try:
    j = input('Enter words or numbers: ')                       # Enter words or number or anything for combination 
    f = int(input('Enter the length of the combination: '))     # Enter the length of the combination
    combination = it.combinations(j,f)
    def combinations():
        count_combin = 0
        for i in combination:
            count_combin += 1                                   # It will count each permutation 
            print(i)                                            # Returns the each combination
        print('There is total {} combinations'.format(count_combin)) # Returns the total number of possible combination
    combinations()
except:
    print('Length should be number only(e.g.2)')                # Error message when enter wrong
    exit()                                                      # This will terminate the program when you enter wrong

