
import operator
f = open("bmi.txt", "w+")
n = int(input("Enter number of students"))
for i in range(n):
    city= input("enter name")
    f.write(""+city)
    age = (input("enter age"))
    f.write(" \t"+age)
    sex = (input("enter sex"))
    f.write("\t"+sex)
    height = (input("enter height"))
    f.write(" \t"+height)
    weight = (input("enter weight"))
    f.write(" \t"+weight)
    f.write("\n")



with open('bmi.txt') as f:
    content = f.read().splitlines()
    


bmi1= (int(content[0][4])//int(content[0][3]))
bmi2= (int(content[1][4])//int(content[1][3]))
bmi3= (int(content[2][4])//int(content[2][3]))
bmi4= (int(content[3][4])//int(content[3][3]))
bmi5= (int(content[4][4])//int(content[4][3]))
    
bmi =[bmi1,bmi2,bmi3,bmi4,bmi5]   
f.write(" \t"+bmi1)
f.write(" \t"+bmi2)
f.write(" \t"+bmi3)
f.write(" \t"+bmi4)
f.write(" \t"+bmi5)

for i in range(0,4):
    if bmi[i] > 40:
        print(content[i],"over weight")
    elif bmi[i]>=20 and bmi[0]<40:
        print(content[i],"obese") 
    else:
        print(content[i],"healthy")    
    