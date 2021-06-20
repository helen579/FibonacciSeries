a = 0
b = 1
c = 0
count = 1

n = int(input("Enter the value of n: "))
if(n==0 or n==1):
 print("Please enter value above 1!")
else:
    print("Fibonacci Series: ")
    while(count <= n):
      print(c, end = " ")
      count += 1
      a = b
      b = c
      c = a + b
