#Program to check if a number is the power of two
def power2(num):
    if(num == 0):
        return 0
    if((num & (~(num - 1))) == num):
        return 1
    return 0
num = int(input("Enter the number: "))
if(power2(num)):
    print("\n The number is power of two.")
else:
    print("The number is not power of two.")