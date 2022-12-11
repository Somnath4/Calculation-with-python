import itertools as it                                  # importing 'itertools' library

#combination with replacement
try:
    j = input('Enter words or numbers: ')               # Enter words or number or anything for combination 
    f = int(input('Enter the length of the combination: '))     
    combin_replacement = it.combinations_with_replacement('somnath',4)
    def combination_replacement():
        count_combin_replace = 0
        for i in combin_replacement:
            count_combin_replace += 1               # It will count each permutation 
            print(i)                                # Returns each combination with replacement
        print('Total combinations with replacement {}'.format(count_combin_replace)) # Returns the total number of possible combination
    combination_replacement()
except:
    print('Length should be number only(e.g.2)')        # Error message when enter wrong
    exit()                                              # This will terminate the program when you enter wrong