def calculate_bmi(height,weight):
    print("Height = " + str(height))
    print("Weight = " + str(weight))

    bmi = weight/(height ** 2) #x ** y is like x to the power of y
    print("BMI = " + str(bmi))

    if bmi < 18.5:
        ret_val = "Under Weight"
    elif bmi >= 18.5 and bmi <= 25.0:
        ret_val = "Normal Weight"
    else:
        ret_val = "Over Weight"

    return ret_val
def main():
    bmi_val = calculate_bmi(1.73,57)

    print(bmi_val)

if __name__=='__main__':
    main()