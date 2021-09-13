# https://www.reddit.com/r/dailyprogrammer/comments/44qzj5/20160208_challenge_253_easy_unconditional_loan/

annual_loan_amount = 15000
clawback_trigger = 100000
royalty_rate_under65 = 0.2
royalty_rate_over65 = 0.4
interest_rate = 0.02


def loan(income_list):
    age = 18
    loans_taken = 0
    repayments_from_income = 0
    repayments_from_clawbacks = 0
    total_loan_balance = 0
    for income in income_list:
        income *= 1000
        clawback = 0
        loans_taken += annual_loan_amount
        total_loan_balance = total_loan_balance * (1 + interest_rate) + annual_loan_amount
        royalty = 0


        #Checks royalty and clawback
        if age < 65:
            royalty = royalty_rate_under65 * income
            if total_loan_balance >= clawback_trigger:
                clawback = royalty_rate_under65 * annual_loan_amount
        else:
            royalty = royalty_rate_over65 * income
            if total_loan_balance >= clawback_trigger:
                clawback = royalty_rate_over65 * annual_loan_amount


        #Adds to the balance (or subtracts from the loan)
        repayments_from_income += royalty
        repayments_from_clawbacks += clawback
        total_loan_balance -= (royalty + clawback)
        age += 1
        print("New Loan: %d, Income: %d, Clawback: %d, Royalty: %d, Current Balance: %d" % (
        annual_loan_amount, income, clawback, royalty, total_loan_balance))
    print("Overall loan taken: %d" % loans_taken)
    print("Repayments from income: %d" % repayments_from_income)
    print("Repayments from benefit clawbacks: %d" % repayments_from_clawbacks)
    print("Ending balance with interest: %d" % total_loan_balance)
    print('-' * 20)


# Long string
input1 = ''' 0 0 20 20 20 20 20 20 20 20 20 20 30 30 30 30 30 30 30 30 30 30 40 40 40 40 40 40 40 40 40 40 50 50 50 50 50 50 50 50 50 50 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0'''

# Map makes a list, but each split item into an int
loan(map(int, input1.split()))