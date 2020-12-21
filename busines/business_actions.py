class Business_Logic:
    days = 0
    
    def __init__(self, cash, debt, inventory, difficulty, in_debt, pay_debt_day):
        "difficulty: 0 = easy and 1 = hard"
        self.cash = cash
        self.debt = debt
        self.inventory = inventory
        self.difficulty = difficulty
        self.in_debt = in_debt
        self.pay_debt_day = pay_debt_day
        
    def buy_inventory(self):
        amount = int(input('How much you want to buy? Use only whole numbers. Type 0 to quit.\n'))
        
        if  amount > self.cash:
            print("You dont have enough money.")
            self.buy_inventory()
        
        elif amount == 0:
            print('You did not buy anything.')

        else:
            self.inventory = amount
            self.cash -= amount
            print("purchase of {} is complete.".format(amount))
    
    def ask_for_debt(self):
        print('Welcome to the bank!')
        print('The following are your debt options.')
        
        if self.in_debt == False:
            if self.difficulty == 0:
                if self.cash < 500:
                    print('RISKY!')
                    print('We can loan you $500 to be paid within 7 days.')
                    print('We will charge you $100 in interest. So you repay us $600 within 7 days.')
                    print('\n')
                    accept = input('Type "A" to accept.\n')
                    
                    if accept == 'A':
                        self.debt = 600
                        self.cash += 500
                        self.in_debt = True
                        self.pay_debt_day = self.days + 7
                        print('Great!')
                    else:
                        print("No problem!")
                else:
                    loan_amount = self.cash 
                    interest = loan_amount * .15
                    payment_amount = loan_amount + interest
                    
                    print('We can loan you ${}.'.format(loan_amount))
                    print('We will charge you ${}, so you have to pay ${} within 7 days.'.format(interest,payment_amount))
                    accept = input('Type "A" to accept.\n')
                    
                    if accept == 'A':
                        self.debt = payment_amount
                        self.cash += loan_amount
                        self.in_debt = True
                        self.pay_debt_day = self.days + 7
                        print('Great!')
                    else:
                        print("No problem!")
            else:
                if self.cash < 500:
                    print('RISKY!')
                    print('We can loan you $250 to be paid within 7 days.')
                    print('We will charge you $50 in interest. So you repay us $300 within 7 days.')
                    print('\n')
                    accept = input('Type "A" to accept.\n')
                    
                    if accept == 'A':
                        self.debt = 300
                        self.cash += 250
                        self.in_debt = True
                        self.pay_debt_day = self.days + 7
                        print('Great!')
                    else:
                        print("No problem!")
                else:
                    loan_amount = self.cash * .85
                    interest = loan_amount * .2
                    payment_amount = loan_amount + interest
                    
                    print('We can loan you ${}.'.format(loan_amount))
                    print('We will charge you ${}, so you have to pay ${} within 7 days.'.format(interest,payment_amount))
                    print('\n')
                    accept = input('Type "A" to accept.\n')
                    
                    if accept == 'A':
                        self.debt = payment_amount
                        self.cash += loan_amount
                        self.in_debt = True
                        self.pay_debt_day = self.days + 7
                        print('Great!')
                    else:
                        print("No problem!")
                    
        else:
            print("Sorry, you're in debt already.")
            
    def loan_repayment(self,pay=False):
        if self.in_debt:
            if self.pay_debt_day == self.days:
                print('Time to pay your loan!')
                
                if self.cash < self.debt:
                    print('You lost!')
                    return True
                else:
                    print('Amount deducted.')
                    self.cash -= self.debt
                    self.in_debt = False
                    self.pay_debt_day = 0
                    self.debt = 0
                    return False
            elif pay:
                print('Thanks for paying us!')
                if self.cash < self.debt:
                    print('You lost!')
                    return True
                else:
                    print('Amount deducted.')
                    self.cash -= self.debt
                    self.in_debt = False
                    self.pay_debt_day = 0
                    self.debt = 0
                    return False
        elif pay:
            print("You're not in debt.")
            
