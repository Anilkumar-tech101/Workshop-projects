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





def check_string_order_and_pv(s):
    if len(s) < 2:
        return "Not enough characters"

    asc = True
    strict_asc = True
    desc = True
    strict_desc = True

    peak = False
    valley = False

    for i in range(len(s) - 1):
        if s[i] > s[i + 1]:
            asc = False
            strict_asc = False
        elif s[i] < s[i + 1]:
            desc = False
            strict_desc = False
        else: 
            strict_asc = False
            strict_desc = False

    for i in range(1, len(s) - 1):
        if s[i] > s[i - 1] and s[i] > s[i + 1]:
            peak = True
        elif s[i] < s[i - 1] and s[i] < s[i + 1]:
            valley = True


    if strict_asc:
        return "Strict Ascending"
    if asc:
        return "Ascending"
    if strict_desc:
        return "Strict Descending"
    if desc:
        return "Descending"
    if peak and valley:
        return "Peaks & Valleys"
    if peak:
        return "Peak pattern"
    if valley:
        return "Valley pattern"

    return "Unordered"
print(check_string_order_and_pv("abvbb"))