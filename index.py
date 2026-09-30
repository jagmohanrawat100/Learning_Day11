print("Day11")

# str = "helloworld"

# #uppercase
# res = str.upper()

# print(res)



# str = "helloworld"
# #use split to convert string to list

# res = " ".join(reversed(str))
# print(res)



# str1 = "helloworld"

# res = list(str1)
# res.reverse()

# print(res)



# str1 = "helloworld"

# res = list(str1)
# res.reverse()

# result = ''.join(res) #to convert back list to string as we can use join() in both list and string
# print(result)



list4 = [1,3,5,7,9]

even = []
odd = []

for i in list4:
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)

print(odd)
print(even)




list5 = [1,3,5,7,9,2,18,22]


for i in list5:
    if i % 2 == 0:  #for Odd i %2 !=0
        print(i)
    else:
        print("odd")
        



str6 = "hey hello hii"

res = list(str6)
res1 =res.count("h")

print(res1)
        
res5 =str6.count("h")
print(res5)       


#Q2 Count Heads of Assignment3

S = "hey hello hii"

freq = {}

for ch in S:
    if ch in freq:
        freq[ch] += 1
    else:
        freq[ch] = 1

print(freq)
