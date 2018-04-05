import operator
f = open("D:\Python_Program\\new file.txt", "w+")
n = int(input("Enter number of cities"))
for i in range(n):
    city= input("enter name of city")
    f.write(""+city)
    pop = (input("enter population"))
    f.write(" \t"+pop)
    area = (input("enter area"))
    f.write(" \t"+area)
    f.write("\n")

f.close()

with open('D:\Python_Program\\new file.txt') as f:
    lines = [line.split(' ') for line in f]
output = open("D:\Python_Program\\new file(sorted).txt", 'w')

for line in sorted(lines, key=operator.itemgetter(0)):
    output.write(' '.join(line))