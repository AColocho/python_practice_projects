from numpy import random
from numpy.random import choice
    
class Easy_Game:
    cash = 1000
    debt = 0
    inventory = 1000
    in_debt = False
    
    def rand_weather(self):
        weather = ['sunny','snowy','rainy','cloudy']
        probability = [.5, .05, .15, .3]
        
        return choice(weather,p=probability)
    
    def get_sued(self,cash):
        sued = ['y','n']
        probability = [.05,.95]
        chosen = choice(sued,p=probability)
        
        if chosen == 'y':
            amount_percentage = random.randint(25,100)/100
            claim = cash * amount_percentage
            
        else:
            claim = 0
            
        return claim
            
    
    def store_flooded(self,cash):
        flood = ['y','n']
        probability = [.05,.95]
        chosen = choice(flood,p=probability)
        
        if chosen == 'y':
            amount_percentage = random.randint(10,20)/100
            claim = cash * amount_percentage
            
        else:
            claim = 0
            
        return claim
    
    def bills(self):
        electric = 250
        rent = 500
        return electric, rent
    
    def sales_for_the_day(self,weather,inventory):
        if weather == 'sunny':
            low = inventory * .5
            high = inventory 
            sales = random.randint(low=low,high=high)
            total_inv_sold = sales
            sales = (sales * .5) + sales
        
        elif weather == 'cloudy':
            low = inventory * .5
            high = inventory * .85
            sales = random.randint(low=low,high=high)
            total_inv_sold = sales
            sales = (sales * .5) + sales
            
        elif weather == 'rain':
            low = inventory * .3
            high = inventory * .6
            sales = random.randint(low=low,high=high)
            total_inv_sold = sales
            sales = (sales * .5) + sales
            
        else:
            low = 0
            high = inventory * .35
            sales = random.randint(low=low,high=high)
            total_inv_sold = sales
            sales = (sales * .5) + sales
            
        return sales, total_inv_sold

class Hard_Game:
    cash = 2000
    debt = 2500
    inventory = 2000
    in_debt = True
    
    def rand_weather(self):
        weather = ['sunny','snowy','rainy','cloudy']
        probability = [.35, .1, .2, .35]
        
        return choice(weather,p=probability)
    
    def get_sued(self,cash):
        sued = ['y','n']
        probability = [.1,.9]
        chosen = choice(sued,p=probability)
        
        if chosen == 'y':
            amount_percentage = random.randint(40,100)/100
            claim = cash * amount_percentage
            
        else:
            claim = 0
            
        return claim
            
    
    def store_flooded(self,cash):
        flood = ['y','n']
        probability = [.15,.85]
        chosen = choice(flood,p=probability)
        
        if chosen == 'y':
            amount_percentage = random.randint(10,20)/100
            claim = cash * amount_percentage
            
        else:
            claim = 0
            
        return claim
    
    def bills(self):
        electric = 500
        rent = 750
        
        return electric, rent
    
    def sales_for_the_day(self,weather,inventory):
        if weather == 'sunny':
            low = inventory * .3
            high = inventory * .85
            sales = random.randint(low=low,high=high)
            total_inv_sold = sales
            sales = (sales * .25) + sales
        
        elif weather == 'cloudy':
            low = inventory * .35
            high = inventory * .7
            sales = random.randint(low=low,high=high)
            total_inv_sold = sales
            sales = (sales * .25) + sales
            
        elif weather == 'rain':
            low = inventory * .25
            high = inventory * .6
            sales = random.randint(low=low,high=high)
            total_inv_sold = sales
            sales = (sales * .25) + sales
            
        else:
            low = 0
            high = inventory * .2
            sales = random.randint(low=low,high=high)
            total_inv_sold = sales
            sales = (sales * .25) + sales
            
        return sales, total_inv_sold