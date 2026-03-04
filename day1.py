
#Ques no1
rent=2000
petrol=500
groceries=1000
total=rent+petrol+groceries
print("Total expenses for the month:", total)

#Ques no2
birth_month=2003
current_year=2026
age=current_year-birth_month
print("Age of the person:", age)

#Ques no3
first_name="Uswa"
middle_name="Tul Hussna"
Last_name="Amjad"
print("full_name:", first_name, middle_name, Last_name)

#Ques no4
_nation="Pakistan"
# 1record=500
record1=500
record_one=600
# record-one=900
#record^one=1000

 #Ques no5
tile_square=5.5
cost=500
area=tile_square**2
print(area)
total_cost=area*cost
print("Total cost of replacing tiling of the floor:", total_cost)

#Ques no6
football_field_length=92
football_field_width=48.8
area=football_field_length*football_field_width 
print("Area of the football field:", area)

#Ques no7
chips_packet=9
cost_per_packet=1.49
gave_money=20
gave_back=gave_money-(chips_packet*cost_per_packet)
print("Money given back to the customer:", gave_back)

#Ques no8
print(format(17, 'b'))

#Ques no9
food='pizza'
print(food[0:5])
print(food[-5:])

#Ques no10
myfood='jalebi','samosa','burger'
print('jalebi' in myfood)
print('pizza' in myfood)
print('pizza' not in myfood)

#Ques no11
myfood='jalebi','samosa','burger'
myfood=myfood[0].replace('jalebi','fries'),myfood[1],myfood[2]
print(myfood)

#Ques no12
first='uswa'
last='amjad'
full_name=first+' '+last
print("Full name of person is:", full_name)

#Ques no13
sentence="Earth revolve around the sun"
print(sentence[6:13])
print(sentence[-3:])

#Ques no14
street = "117 street"
city = "lahore"
country = "Pakistan"
address = street + '\n' + city + '\n' + country
print("Address using + operator:"+ address)
address = f'\n{street}\n{city}\n{country}'
print("Address using f-string:",address)

#Ques no15
n1=int(input("enter first number:"))
n2=int(input("enter second number:"))
print(n1+n2)

#Ques no16
base=int(input("enter base of triangle:"))
height=int(input("enter height of triangle:"))
area=0.5*base*height
print("Area of triangle:", area)