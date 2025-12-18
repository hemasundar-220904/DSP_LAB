def fibonacci(n, memory={}):

    if n in memory:
        return memory[n]
    
    if n <= 1:
        return n
    
    memory[n] = fibonacci(n - 1, memory) + fibonacci(n - 2, memory)
    return memory[n]

n = 7
print("Fibonacci Series:")
for i in range(n):
    print(fibonacci(i), end=" ")