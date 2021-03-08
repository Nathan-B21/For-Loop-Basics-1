# Basic
for i in range(0,151,1):
    print(i)


# Multiples of 5
for i in range(5,1001,5):
    print(i)


# Couting, the dojo way
for i in range(1,1001,1):
    if i % 10 == 0:
        print("Coding Dojo")
    elif i % 5 == 0:
        print("Coding")
    else:
        print(i)


#4. woah that sucker's huge
sum = 0
for i in range(0,500001,1):
    if i % 2 == 1:
        sum = sum + i
print(sum)


# 5. countdown by fours
for i in range(2018,0,-4):
    print(i)


# 6. Flexible counter
lowNum = 2
highNum = 9
mult = 3
for i in range(lowNum, highNum+1,1):
    if i % mult == 0:
        print(i)
