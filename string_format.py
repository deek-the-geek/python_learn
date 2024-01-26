#Python uses C-style string formatting to create new, formatted strings.
# The "%" operator is used to format a set of variables enclosed in a "tuple" (a fixed size list), 
# together with a format string, which contains normal text together with "argument specifiers", special symbols like "%s" and "%d".

# This prints out "Hello, John!"
name = "John"
print("Hello, %s!" % name)

#To use two or more argument specifiers, use a tuple (parentheses):

# This prints out "John is 23 years old."
age = 23
print("%s is %d years old." % (name, age))

# This prints out: A list: [1, 2, 3]
mylist = [1,2,3]
print("A list: %s" % mylist)


num=1.2222
print("number is %.1f" % num)

intnum=15
print("hex num %x" % intnum)

