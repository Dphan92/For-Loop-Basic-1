#1 - Basic
for count in range(0,151):
    print(count)

#2 - Multiples of 5
for count in range(5,1001,5):
    print(count)

#3 - Counting, the Dojo Way
for i in range(1,101):
    if i % 10 == 0:
        print("Coding Dojo")
    elif i % 5 == 0:
        print("Coding")
    else:
        print(i)

#4 - Whoa. That Sucker's Huge
sum = 0
for i in range(0,500001):
    if i % 2 == 1:
        sum += i
print(sum)

#5 - Countdown by 4
for count in range(2019,0,-4):
    print(count)

#6 Flexible Counter
lowNum = 1
highNum = 100
mult = 2
for i in range (lowNum, highNum):
    if i % mult == 0:
        print(i)

