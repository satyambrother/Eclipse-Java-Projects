def factorial(n):
    if n==0:
        result=1
    else:
        result=n*factorial(n-1)
    return result
f=factorial(0)
print("factorial of given number",f)
print(factorial(5))

