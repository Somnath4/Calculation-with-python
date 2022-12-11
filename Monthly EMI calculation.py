#Monthly EMI calculation
try:
    total_amount = int(input('Enter total amount: '))           # Total amount of the loan
    downpayment = int(input('Enter downpayment: '))             # Down payment
    rate_y = float(input('Enter rate: '))                       # yearly interest rate
    duration_y =int(input('Enter duration: '))                  # tenure of the loan in year
    loan_amount = total_amount-downpayment                      # loan amount after subtracting total amount by down payment
    rate_m = rate_y / 12                                        # dividing interest rate into months
    duration_m = duration_y * 12                                # dividing tenure into months
    def loan_emi(loan_amount, duration_m, rate_m):
        try:
            emi = loan_amount * rate_m * ((1 + rate_m) ** duration_m) / ((( 1 +rate_m) ** duration_m) - 1) # Formula for calculating EMI
        except ZeroDivisionError:                               # Returns error it's dividing by zero
            emi = loan_amount/duration_m
        emi = round(emi, ndigits = 2)                           
        print(emi)
    loan_emi(loan_amount, duration_m, rate_m)
except:
    print('You can only enter numbers.')                        # Error message when enter wrong
    exit()                                                      # This will terminate the program when you enter wrong
