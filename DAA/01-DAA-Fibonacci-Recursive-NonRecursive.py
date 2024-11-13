def recur(n):
    if n <= 1:
        return n
    else:
        return recur(n - 1) + recur(n - 2)

def iterative(n):
    a = 0
    b = 1
    fibonacci_series = []
    
    if n > 0:
        fibonacci_series.append(a)
    if n > 1:
        fibonacci_series.append(b)

    for i in range(2, n):
        fibonacci_series.append(a + b)
        a, b = b, a + b

    return fibonacci_series

if __name__ == "__main__":
    num = int(input("Enter the nth number for series: "))
    
    if num <= 0:
        print("Please enter a positive integer")
    else:
        print("\nFibonacci sequence with Recursion:")
        for i in range(num):
            print(recur(i), end=" ")

        print("\nFibonacci sequence with Iteration:")
        print(*iterative(num))
