#QUes1
def calculate_area(base,height,length,width):
    
    triangle_area=(1/2)*float(base)*float(height)
    rectangle_area=float(length)*float(width)
    return triangle_area, rectangle_area

base=input("Enter base of traingle:")
height=input("Enter height of triangle:")
length=input("Enter length of rectangle:")
width=input("Enter width of rectangle:")
print("Area of triangle:", calculate_area(base,height,0,0))
print("Area of rectangle:", calculate_area(0,0,length,width))

#Ques2

def print_pattern(n=5):
    for i in range(n):
        for j in range(i+1):
            print("*", end="")
        print()  # New line after each row

n=int(input("Enter the number of rows for the pattern: "))
print_pattern(n)