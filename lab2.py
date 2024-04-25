print ("ET0735 (DevOps for AIot) - Lab 2 - Introduction to Python")
def display_main_menu():
    print("Enter some numbers separated by commas (e.g. 5, 67, 32)")
def get_user_input():
    numbers = input()
    x = numbers.split(", ")
    for i in x:
        i = float(i)
        #print("Data Type of \"i\" = " + str(type(i)))
        return i
#def calc_average():
    #y = get_user_input()
    #print ("value returned")
    #print (y)