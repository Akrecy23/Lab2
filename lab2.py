print ("ET0735 (DevOps for AIot) - Lab 2 - Introduction to Python")
def display_main_menu():
    print("Enter some numbers separated by commas (e.g. 5, 67, 32)")
def get_user_input():
    numbers = input()
    user_list = numbers.split(",")
    print(user_list)
    new_list = [float(i) for i in user_list]
    print(new_list)
    return new_list
def calc_average():
    y = get_user_input()
    print ("value returned")
    print (y)
def main():
    display_main_menu()
    get_user_input()
    calc_average()
if __name__=='__main__':
    main()