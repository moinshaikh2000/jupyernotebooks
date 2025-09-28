#!/usr/bin/env python
# coding: utf-8

# # Basic of Python
# 
# | Topic | Description |
# |----|-------|
# |Data Types | Int,Float,String|
# |Data Structure| List, Tuple, Dictionary, Set|
# |Loops | For, While |
# |Functions| Named Functions, Lamda Func, Kw, non-kw|
# | Classes | Basics of OOPs|
# 
# https://www.markdownguide.org/cheat-sheet/

# ### Data Types
# 

# In[1]:


type(1)


# In[2]:


type(1.0)


# In[3]:


type("1")


# In[4]:


type("data science")


# In[5]:


## Defining variables
## can start with a character or _
## cannot contains special character like $,@ etc
## cannot start with a number


# In[11]:


var1 = 12
var2 = 13.0


# In[12]:


type(var1),type(var2)


# In[13]:


var1 + var2  ## Adition


# In[14]:


var1 - var2


# In[15]:


var1 * var2


# In[16]:


var1 / var2


# In[18]:


var1 % var2


# In[27]:


144 %    12


# In[21]:


145 % 12


# In[23]:


12 ** 2


# In[25]:


16 ** 0.5


# In[26]:


16 ** (1/2)


# ### Strings

# In[2]:


s1 = "Hello World"
s2 = " Generative AI is the next Revolution "


# In[3]:


s1.lower()


# In[4]:


s1.upper()


# In[5]:


s1.capitalize()


# In[6]:


s1.split(" ")


# In[7]:


s1.find("world")


# In[8]:


s1.find("World")


# In[9]:


s1.lower().find('world')


# In[10]:


len(s1)


# In[11]:


s3  = s1 + s2
s3


# In[12]:


s2.strip()


# In[13]:


s2.lstrip()


# In[14]:


s2.rstrip()


# In[15]:


## index strings


# In[16]:


s3[:]


# In[17]:


s3[0:10] # left


# In[18]:


s3[:10] # left


# In[19]:


s3[10:]


# In[20]:


s3[10:15]


# In[21]:


s3[-10:]


# In[22]:


s3[-10:-2]


# In[23]:


s3[::-1]


# In[24]:


word = "generative"
s3[s3.lower().find(word):s3.lower().find(word)+len(word)]


# In[25]:


s3.lower().find(word)


# In[26]:


len(word)


# ### I/O operations

# In[27]:


# input function

ip1 = input("What is your Name : ")
ip1


# In[63]:


ip1 = input("Enter any number : ")
ip1


# In[2]:


## add 2 numbers

num1 = input("Enter the 1st Number : ")
num2 = input("Enter the 2nd Number : ")

num1 = float(num1)
num2 = float(num2)

num1 + num2


# In[66]:


print("Hello world")


# In[67]:


print(s1)


# In[68]:


print(s2)


# In[69]:


print(s1+s2)


# In[71]:


print(s1+num1)


# In[72]:


print(s1+str(num1))


# In[73]:


print(f"Hello World, My number is {num1}")


# In[74]:


print("Hello World, My number is " + str(num1) )


# In[77]:


print("Hello World, My number is {}, the next number is {}".format(num1,num2))


# ### Error catching

# In[29]:


num1 = input("Enter the 1st Number : ")
num2 = input("Enter the 2nd Number : ")

try:
    num1 = float(num1)
except:
    print(f"You have entered {num1}. Please enter a number")

try:
    num2 = float(num2)
except:
    print(f"You have entered {num2}. Please enter a number")
    
try:
    print(f"The addition is : {num1 + num2}")
    
except:
    print("Cannot Calculate because of above issues")


# ## Conditional Statements

# In[96]:


(1 == 1) & (2 != 3)


# In[97]:


(1 == 1) & (2 == 3)


# In[98]:


(1 == 1) & (2 == 2)


# In[99]:


(1 == 1) | (2 != 3)


# In[30]:


## IF ELSE
## Finding odd and even

var = 1235

if var % 2 == 0:
    print(f'{var} is an even no')
else:
    print(f'{var} is an odd no')



# In[31]:


## String start with vowel or consonnents

vowels = ('a','e','i','o','u')
string = "Moin"

if string[0].lower() in vowels:
    print(f'{string} starts with a vowel')
else:
    print(f'{string} starts with a consonents')


# In[32]:


## User Authentication Logic

user_db = {}
user_db['moin'] = 'pass431'
user_db['chandra'] = 'temp123'
user_db['swapnil'] = 'abc123'

user_name = input('Enter the username : ')
pass_word = input('Enter the password : ')

if user_name in user_db.keys():
    if user_db[user_name] == pass_word:
        print('Authentication Sucessfull !!!')
    else:
        print('Wrong Password')
else:
    print('Wrong Username')
    


# In[40]:


## ELSEIF

age = int(input('Enter yor age: '))
23
if age <= 15:
    age_group = '0 - 15'
elif (age > 15) & (age <=22):
    age_group = '16- 22'
elif (age > 22) & (age <= 30):
    age_group = '23 - 30'
else:
    age_group = '> 30'

print(age_group)


# In[41]:


age = 25

if age <= 15:
    age_group = '0 - 15'
elif (age > 15) & (age <=22):
    age_group = '16- 22'
elif (age > 22) & (age <= 30):
    age_group = '23 - 30'
else:
    age_group = '> 30'

print(age_group)


# In[119]:


## Loops 

## For Loop

for i in range(10):
    print(i)


# In[120]:


vowels = ('a','e','i','o','u')
for i in vowels:
    print(i)
    print('--'*10)


# In[43]:


numbers = [1,5,19,12,139,182,421,2931]
for i in numbers:
    if i % 2 == 0:
        print(f'{i} is even')
    else:
        print(f'{i} is odd')


# In[124]:


numbers = [1,5,19,12,139,182,421,2931]
even_numbers = []

for i in numbers:
    if i % 2 == 0:
        even_numbers.append(i)
even_numbers


# In[129]:


get_ipython().run_cell_magic('time', '', 'even_numbers = []\n\nfor i in range(100000):\n    if i % 2 == 0:\n        even_numbers.append(i)\n')


# In[130]:


get_ipython().run_cell_magic('time', '', 'even_numnbers = [i for i in range(100000) if i % 2 ==0 ]\n')


# In[44]:


names = ['chandra','swati','moin','roshan','swapnil','pooja','shanawaz','nikhil','arshiyan']
output = [i for i in names if i[0] not in ('a','e','i','o','u')]
output


# In[ ]:


## While 

i = 10
while i > 0:
    print(i)
    i -= 1


# In[ ]:


sensor_status = True
start_num = 101
while sensor_status == True:
    if start_num % 100 == 0:
        sensor_status = False
        print(start_num)
        print("Too High Temp")
    start_num += 0.5
        


# ## Functions

# In[46]:


def add_num(x1,x2):
    return x1 + x2

add_num(1,2)


# In[47]:


add_num(2,4)


# In[143]:


def check_age_group(age):
    if age <= 15:
        age_group = '0 - 15'
    elif (age > 15) & (age <=22):
        age_group = '16- 22'
    elif (age > 22) & (age <= 30):
        age_group = '23 - 30'
    else:
        age_group = '> 30'
    return age_group


# In[144]:


check_age_group(15)


# In[145]:


check_age_group(120)


# In[146]:


check_age_group(23)


# In[149]:


def login(user_name,password,user_db = user_db):
    login_status = False
    if user_name in user_db.keys():
        if user_db[user_name]  == password:
            login_status = True
        else:
            login_status = 1
    else:
        login_status = 2
    return login_status


# In[150]:


login('arshiyan','123')


# In[152]:


login('roshan','pass431')


# In[18]:


fn  = lambda x : True if x%2 == 0 else False
fn(4)


# In[162]:


filter(lambda x : True if x%2 == 0 else False,[1,2,3,4,5,6,7,8,9])


# In[163]:


list(filter(lambda x : True if x%2 == 0 else False,[1,2,3,4,5,6,7,8,9]))


# In[169]:


sorted([8,7,2,5,2,1,3,5,2,1])


# In[170]:


set([8,7,2,5,2,1,3,5,2,1])


# In[171]:


def add_num(x1,x2):
    return x1 + x2
add_num(1,2)


# In[172]:


add_num(1,2,3)


# In[177]:


def add_num(*args):
    i = 0
    for j in args:
        i+=j
    return i


# In[178]:


add_num(1,2,3,4,4,5,6,7)


# In[180]:


def difference(x1,x2):
    return x1-x2


# In[181]:


difference(x1=10,x2=20)


# In[182]:


difference(5,3)


# In[183]:


difference(1,2,3)


# In[202]:


def add_nums(*args):
    _sum = 0
    for i in args:
        if isinstance(i,int) or isinstance(i,float):
            _sum += i
    return _sum
    


# In[204]:


add_nums(1,2,3,3,4,54,56,6,3,2,1)


# In[200]:


add_nums(1,2,3,3,4,54,56,6,3,2,1,'a')


# In[203]:


add_nums(1,2,3,3,4,54,56,6,3,2,1,'a',1.0)


# In[205]:


def create_login(**kwargs):
    return kwargs


# In[206]:


create_login(user1='roshan',pass1='123',user2='swati',pass2='431')


# In[ ]:





# In[2]:


def decrese_num(n):
    print(n)
    if n > 0:
        return decrese_num(n-1)
    else:
        return 0


# In[3]:


decrese_num(10)


# In[8]:


def fib_series(n):
    if n <=1:
        return 1
    
    else:
        return fib_series(n-1) + fib_series(n-2)


# In[15]:


fib_series(10)/fib_series(9)


# In[16]:


isinstance('a',int)


# In[17]:


type('a') == int


# In[ ]:




