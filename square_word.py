name = 'World'
line = '+' + name + '+'
spaces = ''
for _ in name: 
    spaces +=' '
    
print(line)
for char in name:
    print(char+spaces+char)
print(line)