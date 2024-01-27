
# Assign String to a Variable
mystring= "Hello! World"


# Lengh of the string
print("lenght of mystring: %d" % len(mystring))


# First occurrence of "a" should be at index 9
print("The first occurrence of the letter o = %d" % mystring.index('o') )

# Number of a's should be 2
print("l occurs %d times" % mystring.count("l"))

# Convert everything to uppercase and lower case
print("String in uppercase: %s" % mystring.upper())
print("String in lowercase: %s" % mystring.lower())


# Check how a string starts and end
print("Is my String Start with Hello: %s" % mystring.startswith("Hello"))
print("Is my String End with Hello: %s" %mystring.endswith("afgh"))


# Split the string into strings
print("Split the words of the string: %s" % mystring.split(" "))

mystring.strip

# Slicing the string into bits -- arr[start:stop:step]
print("The first five characters are '%s'" % mystring[:5]) # Start to 5
print("The next five characters are '%s'" % mystring[5:10]) # 5 to 10
print("The 7th character is '%s'" % mystring[6]) 
print("The characters with odd index are '%s'" % mystring[1::2]) #(0-based indexing)
print("The last five characters are '%s'" % mystring[-5:]) # 5th-from-last to end


# Using a slice() method - 
    # slice(stop)
    # slice(start, stop, step)
print("slice() first five characters are '%s'" % mystring[slice(5)]) 
print("slice() alternative characters '%s'" % mystring[slice(1,10,2)]) 



# Reverse string
print("Reverse mystring: '%s'" % mystring[::-1])

reversed_string = ''.join(reversed(mystring))
print(f"Reversed String using join: {reversed_string}")

print(mystring.replace('W','L')) #replcae matched substring
print(mystring.strip()) # trim the string




