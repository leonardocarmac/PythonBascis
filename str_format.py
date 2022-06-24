# *** string formatting ***

name = "Joe"
age = 5
cost = 1200.5563

#using str format method
print("Hi I'm {}, I'm {} years old".format(name, age) )

#using format string f
print(f"Hi I'm {name}, I'm {age} years old" )

#using % formatting - considered old way of doing it (Python 2)
print("Hi I'm %s, I'm %d years old" % (name,age) )

#formatting to x decimal places
print("The Python course costs %.2f" %cost) 

#will take up at least 10 spaces. 
print("The Python course costs %10f" %cost) 

#will take up at least 10 spaces, 2 after decimal point 
print("The Python course costs %10.2f" %cost) 

# will print a string reading excape characters
print("We \tlove \nPython")

# will print a "raw" string not interpreting escape characters
print(r"We \tlove \nPython")

# triple quotes can make a multi line string. New lines formatted as written
# the backslash escapes the new line symbol
s = '''\
Multi 
line 
string'''
print(s)