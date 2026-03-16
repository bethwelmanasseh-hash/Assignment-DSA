#Reverse a string

string=input("Enter any string:")
reversed_string=""

for character in string:
    reversed_string= character+reversed_string

print("Reversed String: "+str(reversed_string))


#Character frequency

d={}
for x in string:
    if x not in d:
        d[x]=1
    else:
        d[x]+=1

print(d)

