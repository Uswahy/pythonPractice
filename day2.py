
#Ques no1

india=['Delhi','Mumbai','Bangalore','Hyderabad','Chennai']
pakistan=['Lahore','Karachi','Islamabad','Peshawar','Faisalabad']
bangladeshi=['Dhaka','Chittagong','Khulna','Rajshahi','Sylhet']
city=input("Enter the name of the city: ")
if city in india:
    print(f"The city {city} is in India.", india)
elif city in pakistan:
    print(f"The city {city} is in Pakistan.", pakistan)
elif city in bangladeshi:
    print(f"The city {city} is in Bangladesh.", bangladeshi)
else:
    print("The city is not in the list according to my knowledge.")


#Ques no2

india=['Delhi','Mumbai','Bangalore','Hyderabad','Chennai']
pakistan=['Lahore','Karachi','Islamabad','Peshawar','Faisalabad']
bangladeshi=['Dhaka','Chittagong','Khulna','Rajshahi','Sylhet']
city1=input("Enter the name of the city: ")
city2=input("Enter the name of the city: ")
if city1 in india and city2 in india:
    print(f"Both cities {city1} and {city2} are in India.", india)
elif city1 in pakistan and city2 in pakistan:
    print(f"Both cities {city1} and {city2} are in Pakistan.", pakistan)
elif city1 in bangladeshi and city2 in bangladeshi:
    print(f"Both cities {city1} and {city2} are in Bangladesh.", bangladeshi)
else:
    print("The cities are not in the same country.")

#Ques no3
sugar=input("Please enter your fasting sugar level:")
sugar=float(sugar)
if sugar<80:
    print("Your sugar is low, go eat some jalebi :)")
elif sugar>100:
    print("Your sugar is high, stop eating all mithais..!")
else:
    print("Your sugar is normal, relax and enjoy your life!")

    #Ques no4

user=int(input("Enter a number between 1 and 10: "))
for i in range(1,11):
    if i==user:
        print("Number is in range.")
        break
else:
    print("Number is not in range.")
 
#Ques no5

result = ["heads","tails","tails","heads","tails","heads","heads","tails","tails","tails"]
count=0
for res in result:
    if res=="heads":
        count+=1
print("Number of heads:", count)
if res=="tails":
    count+=2
    print("number of tails",count)

month_list = ["January", "February", "March", "April", "May"]
expense_list = [2340, 2500, 2100, 3100, 2980]
e = input("Enter expense amount: ")
e = int(e)

month = 1
for i in range(len(expense_list)):
    if e == expense_list[i]:
        month = i
        break
if month != 1:
    print(f'You spent {e} in {month_list[month]}')
else:
    print(f'You didn\'t spend {e} in any month')

#Ques no6
poem= """\n
 Twinkle, twinkle, little star,
    How I wonder what you are! 
        Up above the world so high,   		
        Like a diamond in the sky. 
Twinkle, twinkle, little star, 
    How I wonder what you are"""
print(poem)
