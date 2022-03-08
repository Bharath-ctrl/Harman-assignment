#Handling missing keys in Python dictionaries
#problem
example = { 'a' : 1 , 'b' : 2 }
#print(example['d'])


#error
    # Traceback (most recent call last):
#   File "d:\python practice\#Handling missing keys in Python diction.py", line 4, in <module>
#     print(example['d'])
     # KeyError: 'd'



#solution
#Method 1 : Using get()
#print(example.get('e','Not found'))#prints not found if e is not present in the dictionary

#Method 2 : Using setdefault()
PoliceContacts={ 'Karnataka': 890754678,"Kerala": 980789098}
PoliceContacts.setdefault('Maharashtra','112')
print(PoliceContacts['Karnataka'])
print(PoliceContacts['Maharashtra'])

#Method 3: Using defaultdict
import collections
PoliceContacts=collections.defaultdict(lambda: 'Contact not found')
print(PoliceContacts['Delhi'])
