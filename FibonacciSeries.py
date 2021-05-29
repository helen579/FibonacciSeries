n = int(input("Enter the value of n: "))
a = 0
b = 1
c = 0
count = 1
print("Fibonacci Series: ")
while(count <= n):
  print(c, end = " ")
  count += 1
  a = b
  b = c
  c = a + b
