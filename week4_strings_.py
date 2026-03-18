#Reverse a string

string=input("Enter a string:")
reversed_string=string[ ::-1]
print("Reversed string: "+str(reversed_string))   #Using slicing to reverse the string

#Reversing a string using for loop

reversed_loop=""
for character in string:
    reversed_loop= character+reversed_loop

print("Reversed String: "+str(reversed_loop))


#Character frequency

string=string.lower() #Converting the string to lower case to avoid case sensitivity
d={} #Empty dictionary to store character frequency
for x in string:
    if x not in d:
        d[x]=1
    else:
        d[x]+=1

print(f"\n{'character':<15}{'frequency':<10}")
for character, frequency in d.items():
    print(f"{character:<15}{frequency:<10}")