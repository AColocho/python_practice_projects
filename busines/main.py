from logic import *

setting, logic = start_game()
bankrupt = False

while (logic.cash > 0) and (bankrupt == False):
    beggining_day(logic)
    
    bankrupt = simulate_day(setting,logic)
    bankrupt = pay_bill(setting,logic)