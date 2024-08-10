'''Escape Sequences in Python;
The escape sequence is used to escape some of the characters present inside a string.
Suppose we need to include both a double quote and a single quote inside a string,

example = "He said, "What's there?"" '''



# escape double quotes
example = "He said, \"What's there?\"

# escape single quotes
example = " He said, What\'s there?"

print(example)

# Output: He said, "What's there?"


#Escape Sequence	Description
#\\	Backslash
#\'	Single quote
#\"	Double quote
#\a	ASCII Bell
#\b	ASCII Backspace
#\f	ASCII Formfeed
#\n	ASCII Linefeed
#\r	ASCII Carriage Return
#\t	ASCII Horizontal Tab
#\v	ASCII Vertical Tab
#\ooo Character with octal value ooo
#\xHH Character with hexadecimal value HH 