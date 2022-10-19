# 2

# nume = input("Cum te numesti?")
# varsta = int(input("Ce varsta ai "))
# x = 2022 - varsta
# print("Ceau", nume, "Deci te-ai nascut in ", x)

# 3

# x = input("Introduceti un sir: ")
# y = len(x)
# print("Lungimea sirului este" ,y)
# print(f"lungimea sirului este {y}")
# print("lungimea sirului este {0}".format(y))
# print("lungimea sirului este " + str(y))

# 4a

# print('*'.center(7))
# print('***'.center(7))
# print('*****'.center(7))
# print('*******'.center(7))

# 4b
# result = ' /-\ '.center(7)
# print(result)
# result = '//_\\\\'.center(7)
# print(result)
# result = '-------'.center(7)
# print(result)
# result = '\\\\_//'.center(7)
# print(result)
# result = '\_/'.center(7)
# print(result)

# 4c
# print('----'.center(8))
# print('/    \\'.center(8))
# print('/______\\'.center(8))


# #6
# a = 'Hello Python'
# b = 'Ana are mere'
# c = 'Pizza Party'
# print(a.replace(' ','_'), b.replace(' ','_'), c.replace(' ','_'),sep='_')
#
# print(a.replace(' ','_'),'.',b.replace(' ','_'),'.',c.replace(' ','_'),'.',)
# #
# print(a.split()[0]*4,a.split()[1], b.split()[0]*4,b.split()[1],b.split()[2], c.split()[0]*4,c.split()[1])

# a = 'hello python'
# x, y = a.split()
# print(x,y)

#7
a = 5.
b = 5
c = "ana"
print(id(a), id(b), id(c))
print(hex(id(a)), hex(id(b)), hex(id(c)))
print('Type of a is: ', type(a),
      'Type of b is: ', type(b),
      'Type of c is: ', type(c))