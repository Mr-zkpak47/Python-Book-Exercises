# Tests for equality and inequality with strings
word = 'python'
print(f"Is word == 'python'? I predict True.")
print(word == 'python')

print(f"\nIs word != 'java'? I predict True.")
print(word != 'java')

print(f"\nIs word == 'Python'? I predict False.")
print(word == 'Python')

# Tests using the lower() method
word = 'Python'
print(f"\nIs word.lower() == 'python'? I predict True.")
print(word.lower() == 'python')

# Numerical tests
number = 42
print(f"\nIs number == 42? I predict True.")
print(number == 42)

print(f"\nIs number != 7? I predict True.")
print(number != 7)

print(f"\nIs number > 50? I predict False.")
print(number > 50)

print(f"\nIs number < 30? I predict False.")
print(number < 30)

print(f"\nIs number >= 42? I predict True.")
print(number >= 42)

print(f"\nIs number <= 42? I predict True.")
print(number <= 42)

# Tests using the and keyword and the or keyword
value1 = True
value2 = False
print(f"\nIs value1 and value2? I predict False.")
print(value1 and value2)

print(f"\nIs value1 or value2? I predict True.")
print(value1 or value2)

# Test whether an item is in a list
fruits = ['apple', 'banana', 'cherry', 'date']
print(f"\nIs 'cherry' in fruits? I predict True.")
print('cherry' in fruits)

# Test whether an item is not in a list
print(f"\nIs 'grape' not in fruits? I predict True.")
print('grape' not in fruits)
