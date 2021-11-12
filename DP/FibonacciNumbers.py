'''
Write a function to calculate the nth Fibonacci number.
'''
def calculateFibonacci(n):
    if n < 2:
        return n

    fib = [0,1]
    for i in range(2, n+1):
        fib.append(fib[i-1]+fib[i-2])

    return fib[n]

def main():
    print("5th Fibonacci is ---> " + str(calculateFibonacci(5)))
    print("6th Fibonacci is ---> " + str(calculateFibonacci(6)))
    print("7th Fibonacci is ---> " + str(calculateFibonacci(7)))

main()