h = float(input("enter the height in miter =  "))
w = int(input("enter the weight in kg =  "))
bmi = w / (h * h)
print("the bmi value is kg/m*m: ",bmi)

if bmi < 18:
    print("thin")

elif (bmi >= 18 and bmi <= 24):
    print("healthy")

elif (bmi >=25 and bmi <= 30) :
    print("overweight")     

else:
    print("wrong input")        

