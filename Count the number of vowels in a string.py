s=input("Enter the string: ")
count=0
for i in s:
    if i in 'aeiouAEIOU':
        count=count+1
print("the number of vowels",s,"is: ",count)
