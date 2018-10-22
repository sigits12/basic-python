print("Hello World")
for num in [1, 2, 3, 4]:
    print(num)

count = 1
while count < 11:
    print(count)
    count = count + 1

if count == 11:
    print('Counting Complete')

##########################################################################
## Modify the variables so that all of the statements evaluate to True. ##
##########################################################################

var1 = 3
var6 = var1
var2 = "python Alhamdulillah"
var3 = [1, 2, 3, 4, 5]
var4 = (1, 2, "Hello, Python!", 4, 5)
var5 = {"happy": "Alhamdulillah", "sum": 7, "egg": "salad"}

############################################
## Don't edit anything below this comment ##
############################################

# integers
print(type(var1) is int)
print(type(var6) is float)
print(var1 < 35)
print(var1 <= var6)

# strings
print(type(var2) is str)
print(var2[5] == 'n' and var2[0] == "p")

# lists
print(type(var3) is list)
print(len(var3) == 5)

# tuples
print(type(var4) is tuple)
print(var4[2] == "Hello, Python!")

# dictionaries
print("var5")
print(type(var5) is dict)
print("happy" in var5)
print(7 in var5.values())
print(var5.get("egg") == "salad")
print(len(var5) == 3)
var5["tuna"] = var5.pop("egg")
var5["tuna"] = "fish"
print(len(var5) == 3)

bilangan = 90


def local_var(bilangan):
    print(bilangan)
    bilangan = 34
    print(f'local variables {bilangan}')


local_var(bilangan)
print(bilangan)

try:
    print(pos)
except Exception as e:
    print(e)
