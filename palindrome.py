num = int(input("Enter a number: "))
temp = num
reverse = 0
while temp != 0:
    digit = temp % 10
    reverse = reverse * 10 + digit
    temp //= 10
if num == reverse:
    print(num, "is a palindrome")
else:
    print(num, "is not a palindrome")
