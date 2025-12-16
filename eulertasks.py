# def fizzbuzz(n):
#     for i in range(1, n + 1):
#         if i % 3 == 0 and i % 5 == 0:
#             print("FizzBuzz")
#         elif i % 3 == 0:
#             print("Fizz")
#         elif i % 5 == 0:
#             print("Buzz")
#         else:
#             print(i)

# user = int(input("Enter a number: "))
# fizzbuzz(user)


# def fizzbuzzA(n):
#     if n %15 ==0:
#         return "FizzBuzz"
#     elif n %3 ==0:
#         return "fizz"
#     elif n %5 ==0:
#         return "Buzz"
#     else:
#         return str(n)
# user = int(input("Enter a number: "))
# print(fizzbuzzA(user))


# def make_fizzbuzz_list(n):
#     return [fizzbuzzA(n) for i in range(1, n + 1)]


# def fizzbuzzB(n):
#     fizzbuzz = ""
#     if n % 3 == 0:
#         fizzbuzz += "Fizz"
#     if n % 5 == 0:
#         fizzbuzz += "Buzz"
#     return fizzbuzz or str(n)


# user = int(input("Enter a number: "))

# for i in range(1, user + 1):
#     print(fizzbuzzB(i))


# def kaprekar(num):
#     count = 0
#     while num != 6174:
#         s = f"{num:04d}" 
#         asc = int("".join(sorted(s)))
#         desc = int("".join(sorted(s, reverse=True)))
#         num = desc - asc
#         count += 1
#         print(f"Step {count}: {desc} - {asc} = {num}")
# user = int(input("Enter a 4-digit number (not all digits the same): "))
# kaprekar(user)



# def arms_number(a,b):
#   for i in range(a, b+1):
#     num =str(i)
#     digits = len(num)
#     sum=0

#     for n in num:
#       sum += int(n)**digits

#     if sum == i:
#       print(sum)
# a=int(input("Enter first number: "))
# b=int(input("Enter second number: "))

# arms_number(a,b)

# def armstrong_numbers(a, b):
#     return [
#         n for n in range(a, b + 1)
#         if n == sum(int(d) ** len(str(n)) for d in str(n))
#     ]


# print(armstrong_numbers(1, 1000))
