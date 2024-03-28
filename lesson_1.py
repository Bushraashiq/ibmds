# checking the length of a variable
var1, var2, var3, var4 = 3455, 3.14, True, "aline et charlotte"
var_len = len(var4)
# print(var_len)

list_info = ["bushra", "ashiq", "shahid", 33, 81.8, True]
print(list_info)
print(type(list_info))
print(len(list_info))
# index/indices of list
print(list_info[-4])

# y = list(range(0,1541,2))
# print(y)
# print(y[-10])

list_cuisine=["air","fryer","fridge","table","chaise","Machine","stove"]
print(list_cuisine)
print(type(list_cuisine))
print(len(list_cuisine))
print(list_cuisine[-1])
list_cuisine.append("oven")
print(list_cuisine)

############################################
# 4 basic datatypes
# String datatype
var_str = "my name is busra"

# int datatype
var_int = 12546

# float datatype
var_flt = 1605.1990

# boolean datatype
var1_bool = True
var2_bool = False

# comment savoir c'est quel type?
# grâce a type()
typ_var_int = type(var_int)
print(typ_var_int)

typ_var_float=type(var_flt)
print(typ_var_float)

typ_var1_bool=type(var1_bool)
print(typ_var1_bool)

typ_var_str=type(var_str)
print(typ_var_str)



######################
# Store each of the following informations in variables 
# and display the value and type of these informations
# hint : print(first_name, typ_first_name)

# informations to work on;
# first name, last name, date of birth, age, 
# is_female, is_male, bank balance, number of children
# str
var_last_name="ashiq"
typ_var=type(var_last_name)
print(var_last_name,typ_var)
#
var_age="16-05-1990"
typ_var=type(var_age)
print(var_age,typ_var)

var_age=33.20
typ_var=type(var_age)
print(var_age,typ_var)

var_is_female=True
typ_var=type(var_is_female)
print(var_is_female,typ_var)

var_first_name="bushra"
typ_var=type(var_first_name)
print(var_first_name,typ_var)

var_is_male=False
typ_var=type(var_is_male)
print(var_is_male,typ_var)

var_bank_balance=10.66
typ_var=type(var_bank_balance)
print(var_bank_balance,typ_var)

var_children=2
typ_var=type(var_children)
print(var_children,typ_var)

vr_cd=3.69
print(vr_cd)
typ_var=type(vr_cd)
print(typ_var)

var_t="aline,charlotte"
print(var_t)
typ_var=type(var_t)
print(typ_var)

var_age_23=True
print(var_age_23)
typ_var=type(var_age_23)
print(typ_var)






