import itertools as it

#permutation calculation
try:
    j = input('Enter words or numbers: ')                        # Enter words or number or anything you want to ber permuted 
    f = int(input('Enter the length of the permutation: '))      # Enter the length of the permutation
    permute = it.permutations(j,f)                               
    def permutations():                                          
        count_permute = 0                               
        for i in permute:
            count_permute += 1                          # It will count each permutation 
            print(i)                                    # Returns each permutation
        print('There is total {} permutations'.format(count_permute))   # Returns the total number of possible permutation   
    permutations()
except:
    print('You can only enter number in permutation section.')          # Error message when enter wrong
    exit()                                                              # This will terminate the program when you enter wrong