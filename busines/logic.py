from business_actions import *
from flow_control import *
from game_settings import *

def start_game():
    intro().welcome()
    difficulty = intro().business_set_up()
    
    if difficulty.lower() == 'easy':
        cash = Easy_Game().cash
        debt = Easy_Game().debt
        inventory = Easy_Game().inventory
        in_debt = Easy_Game().in_debt
        return Easy_Game(), Business_Logic(cash,debt,inventory,0,in_debt,0)
    else:
        cash = Hard_Game().cash
        debt = Hard_Game().debt
        inventory = Hard_Game().inventory
        in_debt = Hard_Game().in_debt
        return Hard_Game(), Business_Logic(cash,debt,inventory,1,in_debt,0)
    
def pay_bill(setting,logic):
    """
    Pays the bills. Returns True for bankrupt and False for game continue.
    """
    day_num = logic.days
    
    if (day_num % 7) == 0:
        electric, rent = setting.bills()
        print('Time to pay the bills!')
        print("We'll substracted ${} for electricity and ${} for rent.".format(electric,rent))
        
        if logic.cash < (electric + rent):
            print('You Lost :( ')
            return True
        
        else:
            logic.cash -= (electric+rent)
            return False
    else:
        return False

def beggining_day(logic):
    actions = ""
    
    while actions == "":
        print("Type debt to get a loan.")
        print("Type inv to buy inventory.")
        print("Type repay to pay debt.")
        print("Type done to simulate the day.")
        print('\n')
        action = input()
        print(intro.split)
        
        if action == 'done':
            break
        
        elif action == 'debt':
            logic.ask_for_debt()
            
        elif action == 'inv':
            logic.buy_inventory()
        
        elif action == 'repay':
            logic.loan_repayment(pay=True)
        
        print(intro.split)

def simulate_day(settings,logic):
    bankrupt = False
    day = logic.days
    cash = logic.cash
    inventory = logic.inventory
    weather = settings.rand_weather()
    lawsuit = settings.get_sued(cash)
    flood = settings.store_flooded(cash)    
    sales = round(settings.sales_for_the_day(weather,inventory))
    
    Day_To_Day().beggining_of_day(day,weather)
    
    if (lawsuit > 0) and (flood > 0):
        print('Unexpected things!')
        print('Your store flood and you got sued.')
        print("We'll deduct the claim amount")
        if (lawsuit + flood) > logic.cash:
            print('You lost.')
            bankrupt = True
        
        else:
            logic.cash -= (lawsuit + flood)
            bankrupt = False
            
    elif lawsuit > 0:
        print('Unexpected things!')
        print('You got sued.')
        print("We'll deduct the claim amount")
        if lawsuit > logic.cash:
            print('You lost.')
            bankrupt = True
        else:
            logic.cash -= (lawsuit + flood)
            bankrupt = False
    
    elif flood > 0:
        print('Unexpected things!')
        print('Your store flood.')
        print("We'll deduct the claim amount")
        if flood > logic.cash:
            print('You lost.')
            bankrupt = True
        else:
            logic.cash -= (lawsuit + flood)
            bankrupt = False
    
    logic.cash += sales
    logic.inventory -= sales
    
    logic.loan_repayment()
    
    debt = logic.debt
    cash = logic.cash
    inventory = logic.inventory
    
    Day_To_Day().end_of_day_report(sales,inventory, debt, cash)
    
    logic.days += 1
    
    return bankrupt
    