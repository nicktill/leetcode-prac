#compund interest formula => 
#this would mean initial investment of 20k, at 10% growth, over 10y
#i.e 20,000(1.1)^10 = 51874.80
#code for the formula would look something like this


def compound_interest(principal, rate, time, sufficientAmount):
    #compund interest formula as shown => amount = principal * (1 + rate/100) ** time 
    amount = principal * (pow((1 + rate / 100), time))
    if amount > sufficientAmount:
        print("You have enough money to retire\n, you have:$",amount, "\nand you needed: \n$",sufficientAmount, "to retire")
    else:
        print("You don't have enough money to retire, you have", "$", amount, "\nyou still need to save an extra: $", sufficientAmount-amount, "\nto meet your goal of retirement", "$", sufficientAmount)

def calculate_can_retire(age, retirement_age, principal, income, rate): 
    sufficientAmount = income*25 #creates the sufficient goal needed to retire
    if retirement_age > 59.5: 
        #this technically isnt 100% correct, since a tax of 30% is different than applying 130% but will assume its 'good enough' for testing purposes as of now
        sufficientAmount*= 1.3 #if age is less than 59.5, then the goal is increased by 30%
    if age < retirement_age:
        time_to_retirement = retirement_age - age
        compound_interest(principal, rate, time_to_retirement, sufficientAmount)
    else:
        print("You are already retired")

#call function as follows: 
#AGE = INITIAL AGE
#RETIREMENT AGE = FINAL AGE
#PRINCIPAL = INITIAL INVESTMENT 
#INCOME = ANNUAL INCOME
#RATE = ANNUAL GROWTH RATE
#caclaulte_can_retire(age, retirement_age, principal, income, rate)

calculate_can_retire(25, 59.5, 10000, 25000, 10)



