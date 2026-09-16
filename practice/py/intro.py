x = 'bonsoir'
print(x)
#strings and string methods:
message="""triple double quotes
are used for multi line strings"""
print(message)
print(len(message))
print(message[1])
print(message[0:5])
print(message[:5])
print(message[48:])
print("string methods: .lower(), .upper(), .count(<args>), count is used to find occurence, .find(<args>), .replace(what to replace, what to replace with), .format() is used for complex strings")
print(message.count('multi'))
print(message.count('hello'))
print(message.count('l'))
print(message.find('for'))
sellMethod='fast'
sellMethod2='slow'
newMessage='how to sell drugs online {}'.format(sellMethod)
print(newMessage.replace('sell', 'buy'))
print(newMessage)
print('fstrings can be used in place of format method, these were introduced in python 3.6')
newNew=f'how to sell drugs online {sellMethod2}'
print(newNew)
print('dir() function is a special function which exposes everything available to be done to something, methods, operations, etc')
print(dir(newNew))
#et viola
print('similarly theres help() functions, but it accept datatypes, you cant pass a var to it')
print(help(int))
print(help(str.__class__))
print('similarly teh type() function shows the datatype of a variable')


#ints and floats:
print('// is used for floor division & ** for exponent')
print('abs() function provides the absolute value for a num,  round() for round off')
num=-3
num1=3.5678
print(abs(num))
print(round(num1))
print(round(num1, 2))
#casting:
num2='300'
num2=int(num2)
print(type(num2))
print('the id() function shows the object id')
print(id(num2))

# conditionals(if, else, elif) are easy af in py