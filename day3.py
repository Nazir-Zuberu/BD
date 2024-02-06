# print("hello world")



# def addition(a,b):
#     return(a+b)

# print(addition(2,4))


# print("""Exception handling is used to gracefully handle and recover from unexpected errors or exceptional 

# conditions that may occur during program execution. It prevents the 
# program from crashing and 

# provides error-handling mechanisms. """)

# print('Exception handling is used to gracefully handle and \n' 
#       'recover romunexpected errors or exceptional conditions \n'
#       'that may occur uring program execution. It prevents the program from crashing \n'
#       'nd provides error-handling mechanisms.')

# basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']

# for f in sorted(set(basket)):
#     print(f)


# for i in range(2,2):
#     print(i)



# for n in range(2, 10):
#     for x in range(2, n):
#         if n % x == 0:
#             print(n, 'equals', x, '*', n//x)
#             break
#     else:
#         # loop fell through without finding a factor
#         print(n, 'is a prime number')


# for n in range(2, 10):
#     print(n)


# a = [2,45,66,7,8,9]


# b = [0,0]

# print(a+b)



# def fibonacci(n):
#     if n<=0:
#         return 0
#     elif n==1:
#         return 1
#     else:
#         return fibonacci(n-2) + fibonacci(n-1)

# print(fibonacci(5))


matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]

new1 = [ [row[i] for row in matrix] for i in range(4)]

print(new1)