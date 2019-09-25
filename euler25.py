a = 0
b = 1
count = 1
while len(str(b)) < 1000:
    count += 1
    c = a + b
    a = b
    b = c
print(count)
print(b)

def fibonacci(n):
    a = 0
    b = 1
    if n < 0:
        print("Incorrect input")
    elif n == 0:
        return a
    elif n == 1:
        return b
    else:
        for i in range(2,n):
            c = a + b
            a = b
            b = c
        return b

print(len(str(fibonacci(count+1))))