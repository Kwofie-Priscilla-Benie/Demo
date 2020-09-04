# -*- coding: utf-8 -*-
"""
Created on Sun Oct 27 19:48:21 2019

@author: RITA
"""

#customer ={
 #       "name": "Kwofie Priscilla Benie",
  #      "age": 22,
   #     "is_verified":True
#}
#customer["name"] = "Millicent Kwofie"
#print(customer["name"])
#print(customer["is_verified"])
#print(customer.get("birthday" , "10 May 1997"))
#phone = input("Enter your phone number: ")
#number =  {
#       "1": "One",
#       "2": "Two",
#       "3": "Three",
#       "4": "Four"
#}
#output = ""
#for item in phone:
    #output += number.get(item, "!") +" "
#print(output)
#def greet_user(first_name, last_name):
 #   print(f'Hi {first_name} {last_name}!')
  #  print("Welcome here")
    
    
#print("Start")
#greet_user(last_name="Kwofie", first_name="Priscilla")
#print("Finish")
#def to_c(total, shipping, discount):
 #   total_cost = float(total) * float(shipping) *float(discount)
  #  print(f'total cost : {total_cost}')
    
#to_c(10,23,0.2)
#def square(number):
 #   return number * number
#result = square(3)
#print(result)
#
from ecommerce.shipping import calc_shipping
calc_shipping()

import random
for i in range(3):
    print(random.random())
    print(random.randint(10,20))
    
members = ["John", "liz","bee","priscy"]
leader = random.choice(members)
print(leader)