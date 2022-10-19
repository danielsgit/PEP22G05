# # Output functions
# print('Hello World')
#
# # Input functions
#
# #input('Say Hi to: ')
#
# # Variables
# my_name = 'Daniel'
#
# print(my_name)
# my_number = 1000_000
# print(my_number)
#
# #type function
# result = type(10)
# print(result)
#
# #return of print
# result = print('exemple')
# print(result)
#
# # return of input
# result = input('Say Hi to: ')
# print(result)
#
# # print multiple args
#
# print('Emanuel', 'Ion', 'Illia')

# casting
# result = 'abdc'
# result = int(result)
# print(result)

# operations
# https://docs.python.org/3/library/operator.html
# comparation

# a=100
# b=100
# print(a == b)
# print('ID of a is:' , id(a))
# print('ID of b is:' , id(b))
# print(a is b)
#
# a='sad'
# b='sad'
# print(a == b)
# print('ID of a is:' , id(a))
# print('ID of b is:' , id(b))
# print(a is b)

# slice
#  #  0123456
# a ='my_text'
# print(a[1])  # - > extrage doar y-ul// care se afla pe pozitia 1, pt ca incepe numerotarea de la 0
#
# # print(a[1:4])
# print(a[1:]) # ->  printeaza pana la final
#
# print(a[1:6:2]) #-> # 2 = step.ul, o sa mearga din 2 in 2
#
# #   -7-6-5-4-3-2-1
# #a =' m y _ t e x t'
# a ='my_text'
# print(a[-1])
# print(a[-6:-1])
# print(a[-1:-6:-1])


# b = 'This is may reversed text'
# print(b[-1::-1]) #sau
# print(b[::-1])

# String and string methods
# my_var = 'dani'
# my_srt= u"asgas \n"# -> unicod string
# print(my_srt)
#
# my_str = f"My name is {my_var}" # -> format string
# print(my_str)
#
# my_str = r"dgdsgf{}\n   \n {}\ \,." # -> raw string, nu tine cont de \n sau \
# print(my_str)
#
# result = my_str.capitalize()
# print(result)
#
# result = my_str.split('\\')
# print(type(result))
# print(result)
#
# result = my_str.format('x', 'y')
# print(result)


#result = 'abys'.center(7, ' ')
#print(result)

my_str = 'sfafFASfsa'
result = my_str.lower()
print(result)

my_str = 'sfafFASfsa'
result = my_str.upper()
print(result)


