class intro:
    split = '_____________________________________________________________'
    
    def welcome(self):
        print('Welcome to Business!')
        print('This is a game that will put you in the position')
        print('of a retail business person. You will be able to plan')
        print('the activities of the following day, purchase inventory,')
        print('and even take out debt. This is easier said than done')
        print('because you will have random events happening.')
        print('Good luck!')
        print(intro.split)
    
    def business_set_up(self):
        print('Before you begin in your adventure, we need to pick your difficulty.')
        print('type: Easy or Hard. There is no medium. \n')
        print('\n')
        difficulty = input()
        print(intro.split)
        return difficulty
    
class Day_To_Day(intro):
    def end_of_day_report(self,sales,inventory,debt,cash):
        print('End of day report:')
        print('Sales: {}'.format(sales))
        print('Inventory: {}'.format(inventory))
        print('Debt: ${}'.format(debt))
        print('Cash: ${}'.format(cash))
        print(super().split)
    
    def beggining_of_day(self,day_num,weather):
        print('You been in business for: {} days.'.format(day_num))
        print('Today the weather will be {}'.format(weather))
        print(super().split)