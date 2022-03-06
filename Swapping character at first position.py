a=input("Enter the first string: ")
b=input("Enter the second string: ")
new_a = b[:1]+a[1:]
new_b = a[:1]+b[1:]
print("The string after character swappping:",str(new_a +''+ new_b))