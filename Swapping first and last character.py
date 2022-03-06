def character_exchange(str1):
      str2=(str1[-1:] + str1[1:-1] + str1[:1])
      return str2
str = input("Enter the string: ")
print("The original string:",str)
print("The string after swapping first and last characters", character_exchange(str))