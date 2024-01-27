# Python Learning

## 1. Install and Environment setup
- Installing Python and setting up a development environment.
- Creating virtual environment

## 2. Variables and Types
### Data Types

In programming, a data type is a classification or categorization that specifies which type of value a variable can hold. Data types are essential because they determine how data is stored in memory and what operations can be performed on that data. Python, like many programming languages, supports several built-in data types. Here are some of the common data types in Python:

1. **Numeric Data Types:**
   - **int**: Represents integers (whole numbers). Example: `x = 5`
   - **float**: Represents floating-point numbers (numbers with decimal points). Example: `y = 3.14`
   - **complex**: Represents complex numbers. Example: `z = 2 + 3j`

2. **Sequence Types:**
   - **str**: Represents strings (sequences of characters). Example: `text = "Hello, World"`
   - **list**: Represents lists (ordered, mutable sequences). Example: `my_list = [1, 2, 3]`
   - **tuple**: Represents tuples (ordered, immutable sequences). Example: `my_tuple = (1, 2, 3)`

3. **Mapping Type:**
   - **dict**: Represents dictionaries (key-value pairs). Example: `my_dict = {'name': 'John', 'age': 30}`

4. **Set Types:**
   - **set**: Represents sets (unordered collections of unique elements). Example: `my_set = {1, 2, 3}`
   - **frozenset**: Represents immutable sets. Example: `my_frozenset = frozenset([1, 2, 3])`

5. **Boolean Type:**
   - **bool**: Represents Boolean values (`True` or `False`). Example: `is_valid = True`

6. **Binary Types:**
   - **bytes**: Represents immutable sequences of bytes. Example: `data = b'Hello'`
   - **bytearray**: Represents mutable sequences of bytes. Example: `data = bytearray(b'Hello')`

7. **None Type:**
   - **NoneType**: Represents the `None` object, which is used to indicate the absence of a value or a null value.

8. **Custom Data Types:**
   - You can also define your custom data types using classes and objects.

## 3. Strings
### String Formatting
- Multiline Strings assign by using 3 quotes ( """ or ''' )
- Python uses C-style string formatting to create new, formatted strings.The "%" operator is used to format a set of variables enclosed in a "tuple" (a fixed size list), together with a format string, which contains normal text together with "argument specifiers", special symbols like "%s" and "%d"
  - %s - String (or any object with a string representation, like numbers)
  - %d - Integers
  - %f - Floating point numbers
  - %.<number of digits>f - Floating point numbers with a fixed amount of digits to the right of the dot.
  - %x/%X - Integers in hex representation (lowercase/uppercase)
- String interpolation: Python supports various ways to format strings, including f-strings (f"...{variable}..."), %-formatting ("%s %d" % ("string", 42)), and `str.format()`.

### String Operations
- String methods: Python has a set of built-in methods that you can use on strings.such as `len()`, `index()`, `upper()`, `lower()`, `strip()`, `replace()`,`split()`, `join()`,`startswith()` and `endswith()` and more
- Concatenation: You can combine strings using the `+` operator.
- Escape sequences: Special characters like newline (\n), tab (\t), and others are represented using escape sequences.
- Substrings: Use slicing to extract portions of a string
  - arr[start:stop:step]
  - slice(start,stop,step)

