#ASSIGN MULTIPLE VALUES TO MULTIPLE VARIABLE

# x=10
# y=20
# z=30
# EK SATH LIKHNA

# x,y,z=10,20,30
# print(x)
# print(y)
# print(z)

#assign same values to multiple variable
# x=y=z=10
# print(x,y,z)

#OUTPUT THE VARIABLES
# x='my name is rjs'
# print(x)

# x='my'
# y='name'
# z='john'
# print(x,y,z)    have space
# print(x+y+z)    no space

# x=10
# y='john'
# # print(x+y)   invailed
# print(x,y)   vailed


#GLOBAL VARIABLE
#variables that are created outside of funcn
#they can be used inside/outside of funcn

#Example like clg garden and public garden

#1  x='john'  #public garden - global variable

# def myfunc():     #campus
#     print('my name is'+x)

# print(x)    
# myfunc()
    
#2 x='john'  #public garden - global variable

# def myfunc():     #campus
#      x='peter' #local garden
#      print('my name is '+x)
     

# print(x)    
# myfunc( )

#3 y='john'  #public garden - global variable

# def myfunc():     #campus
#      x='peter' #local garden
#      print('my name is '+y,x)
     

# print(y)    
# myfunc( )

#hence global variable use in inside and outside of funcn but inside the function not use by out side print funcn like example3
    
    
    
