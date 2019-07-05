import random
a=int(input("Enter a number"))
if a>random.randint(1,10):
    print("You are choosen batting")
else:
    print("You are choosen bowling")
print("Start your bowling")
wickets=0
sum1=0
c=int(input("Enter a number"))
for i in range(c,random.randint(1,10),1):
    if random.randint(1,10)>i:
        sum1=sum1+i
    elif random.randint(1,10)==i:
        wickets=wickets+i
    
print(sum1)
print(wickets)
print("Start your batting")
sum=0
wickets1=0
b=int(input("Enter a number"))
for i in range(b,random.randint(1,10),1):
    if i>random.randint(1,10):
          sum=sum+i
    elif i==random.randint(1,10):
        wickets1=wickets1+i
        print("you loose")
print(sum)
print(wickets1)
if sum1>sum:
    print("cp won the match")
else:
    print("you won")
        
