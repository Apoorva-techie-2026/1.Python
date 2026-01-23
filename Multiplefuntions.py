class practice():
    def SubfieldsInAI():
        print("Sub-fields in AI are:")
        Lists=["Machine Learning","Neural Networks","Vision","Robotics","Speech Processing","Natural Language Processing"]
        for subfield in Lists:
           print(subfield)
        return subfield

    def OddEven():
        num=int(input("Enter a number: "))
        if (num%2==0):
            print(num,"is an Even number.")
            cal="Entered number is an Even number."
        else:
            print(num,"is an Odd number.")
            cal="Entered number is an Odd Number."
        return cal

    def Elegiblity():
        Gender=input("Your Gender:")
        Age=float(input("Your Age: "))
        if (Gender=="Male" and Age>=21):
            print("Eligible")
        elif(Gender=="Female" and Age>=18):
            print("Eligible")
        else:
            print("Not Eligible")
        
    def addition():
        Subject1= 98
        Subject2= 87
        Subject3= 95
        Subject4= 95
        Subject5= 93
        Total=Subject1+Subject2+Subject3+Subject4+Subject5
        print("Total: ",Total)
        percent=Total/5
        print("Percentage: ",percent)
        
    def triangle():
            Height=float(input("Height: "))
            Breadth=float(input("Breadth: "))
            Area=(Height*Breadth)/2
            print("Area of triangle: ",Area)
            Height1=float(input("Height1: "))
            Height2=float(input("Height2: "))
            Breadth1=float(input("Breadth1: "))
            Perimeter=Height1+Height2+Breadth1
            print("Perimeter of a triangle: ",Perimeter)