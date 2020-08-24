a = 1
b = 1
fibonacci = [1,2]

for i in range(10):
    a,b = b,a+b
    fibonacci.append(b)
print(fibonacci)