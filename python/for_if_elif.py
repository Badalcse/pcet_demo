#if statement
#x = int(input("Please enter an integer: "))

#if x < 0:
    #print("Nagetive change to zoro")
#elif x == 0:
   # print("Zero")

#elif x == 1:
   # print("single")

#else:
  #  print("more") 

#for statement

#words = ['cat','window','defenestrate']

#for x in words:
 #   print(x, len(x))

# Create a sample collection
'''users = {'Hans': 'active', 'Éléonore': 'inactive', '景太郎': 'active'}'''

# Strategy:  Iterate over a copy
'''for user, status in users.copy().items():
    if status == 'inactive':
        del users[user]'''

# Strategy:  Create a new collection
#active_users = {}
"""for user, status in users.items():
    if status == 'active':
        active_users[user] = status  """

 

"""a = ['Mary', 'had', 'a', 'little', 'lamb']
for i in range(len(a)):
    print(i, a[i])"""


# def http_error(status):
#     match status:
#         case 400:
#             return "Bad request"
#         case 418:
#             return "I'm a teapot"
#         case 421:
#             return "something is wrong with the internet"

bike = 'yamaha'

if bike == 'hero':
    print("bike is hero")

elif bike == "Suzuki":
    print("bike is suzuki")

elif bike == "Suzuki":
    print("bike is suzuki")    

     
        