num = int(input("Enter the number : "))
num = str(num)
sum = 0
for i in range(len(num)):
    if(i + 1 )% 2 == 0:
       sum +=int(num[i])
print(f"Result : {sum}")
