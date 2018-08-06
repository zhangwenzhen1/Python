#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  namecase.py
#  
#  Copyright 2018 zhanngwenzhen <zhanngwenzhen@DESKTOP-OG03N0J>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  
######################################################

name="zhang wen zhen"
string="would you like to learn some Python today?"
#print("Hello,"+" "+name.title()+"!"+string)
message="A person who never made a mistake never tried anything new."
famous_person="Albert Einstein"
#print(famous_person+"once said,"+'"'+message+'"')
famous_person="\tAlbert\n"
#print(famous_person)
#print(famous_person.lstrip())
#print(famous_person.rstrip())
#print(famous_person.strip())
#print(famous_person)
numbers= [value*3 for value in range(1,11)]
print(numbers)
for number in numbers:
	print(number)

favorite_languages = {
	'jen  ab': 'python',
	'sarah': 'c',
	'edward': 'ruby',
	'phil': 'python',
	}
for name in favorite_languages.keys():
	print(name.title())
	
#复制列表[:]
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]
print("My favorite foods are:")
print(my_foods)
print("\nMy friend's favorite foods are:")
print(friend_foods)

#遍历字典所有键值对
user_0 = {
	'username': 'efermi',
	'first': 'enrico',
	'last': 'fermi',
	}
for key, value in user_0.items():
	print("\nKey: " + key)
	print("Value: " + value)
	
#遍历字典所有键
favorite_languages = {
	'jen': 'python',
	'sarah': 'c',
	'edward': 'ruby',
	'phil': 'python',
}
for name in favorite_languages.keys():
	print(name.title())
	
#遍历字典所有值
for value in favorite_languages.values():
	print(value.title())
#set()删除重复项
for language in set(favorite_languages.values()):
	print("\n"+language.title())
#按顺序遍历字典中的所有键
for name in sorted(favorite_languages.keys()):
	print(name.title() + ", thank you for taking the poll.")
######################################
friends = ['phil', 'sarah']
for name in favorite_languages.keys():
	print(name.title())
	if name in friends:
		print(" Hi " + name.title() +
				", I see your favorite language is " +
				favorite_languages[name].title() + "!")
###########################				

# 创建一个用于存储外星人的空列表
aliens = []
# 创建30个绿色的外星人
for alien_number in range (0,30):
	new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
	aliens.append(new_alien)
for alien in aliens[0:3]:
	if alien['color'] == 'green':
		alien['color'] = 'yellow'
		alien['speed'] = 'medium'
		alien['points'] = 10
	elif alien['color'] == 'yellow':
		alien['color'] = 'red'
		alien['speed'] = 'fast'
		alien['points'] = 15
# 显示前五个外星人
"""
for alien in aliens[0:3]:
	if alien['color'] == 'green':
		alien['color'] = 'yellow'
		alien['speed'] = 'medium'
		alien['points'] = 10
	elif alien['color'] == 'yellow':
		alien['color'] = 'red'
		alien['speed'] = 'fast'
		alien['points'] = 15
"""		
for alien in aliens[0:5]:
	print(alien)
#	print("...")
# 存储所点比萨的信息
pizza = {
	'crust': 'thick',
	'toppings': ['mushrooms', 'extra cheese'],
	}
# 概述所点的比萨
print("You ordered a " + pizza['crust'] + "-crust pizza " +
	"with the following toppings:")
for topping in pizza['toppings']:
	print("\t" + topping)
#
#from collections import OrderedDict
#favorite_languages = OrderedDict()
favorite_languages = {
	'jen': ['python', 'ruby'],
	'sarah': ['c'],
	'edward': ['ruby', 'go'],
	'phil': ['python', 'haskell'],
	}
#print(favorite_languages['sarah'])
for name, languages in favorite_languages.items():
	if  len(languages)>1:
		print("\n" + name.title() + "'s favorite languages are:")
		for language in languages:
			print("\t" + language.title())
			#print(len(languages))
	else:
		for language in languages:
			print("\n" + name.title() + "'s favorite languages are:"+
			"\n  \t"+language.title())
#message=input("Tell me something, and I will repeat it back to you: ")
#print(message)

# 首先，创建一个待验证用户列表
# 和一个用于存储已验证用户的空列表
unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []
# 验证每个用户，直到没有未验证用户为止
# 将每个经过验证的列表都移到已验证用户列表中
while unconfirmed_users:
	current_user = unconfirmed_users.pop()
	print("Verifying user: " + current_user.title())
	confirmed_users.append(current_user)
# 显示所有已验证的用户
print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
	print(confirmed_user.title())
	
##使用任意数量的关键字实参
def build_profile(first,last,**user_info):
#	"""创建一个字典，其中包含我们知道的有关用户的一切"""
	profile = {}
	profile['first_name'] = first
	profile['last_name'] = last
	#print(profile)
	for key,value in user_info.items():
		profile[key]= value
		#profile[vlaue]=value
	return profile
user_profile = build_profile('albert', 'einstein',
							location='princeton',
							field='physics',
							home='123')
print(user_profile)
##
"""
	def make_pizza(*toppings):
		
		print("\nMaking a pizza with the following toppings:")
		for topping in toppings:
			print("- " + topping)
	make_pizza('pepperoni')
	make_pizza('mushrooms', 'green peppers', 'extra cheese')
		##
	def make_pizza(size, *toppings):
	
		print("\nMaking a " + str(size) +
				"-inch pizza with the following toppings:")
		for topping in toppings:
			print("- " + topping)
	make_pizza(16, 'pepperoni')
	make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
"""
#def (manufacturer,model,**exterior)
def make_car(manufacturer,model,**exterior):
	car_info={}
	car_info['manufacturer']=manufacturer
	car_info['model']=model
	for key,value in exterior.items():
		car_info[key]=value
	return car_info
car= make_car('subaru','outback',color='blue',tow_package=True)
print(car)


