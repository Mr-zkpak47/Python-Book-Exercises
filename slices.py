slices:list[str] = ["apple", "orange","grapes","melon","guava","lime","cherry","strawberry","watermelon"]
print("First three items : ")
for i in slices[:3]:
    print(i)
print("\nMiddle three items : ")
for i in slices[3:6]:
    print(i)
print("\nLast three items : ")
for i in slices[-3:]:
    print(i)