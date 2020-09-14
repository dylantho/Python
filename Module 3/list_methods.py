"""
Program: list_methods.py
Author: Dylan Thomas
Last date modified: 09/14/2020
"""

#Base
listOne = ['not','enough', 'mana']
print(listOne)

#append
listOne.append('song')
print(listOne)

#clear
listOne.clear()
print(listOne)

#copy
listOne = ['not','enough', 'mana']
newList  = listOne.copy()
print (newList)

#count
listOne.count('mana')

#extend
listTwo = ['follow','your', 'ghost']
listOne.extend(listTwo)
print(listOne)

#index
print(listOne.index('follow'))

#insert
listOne.insert(1, 'quite')
print(listOne)

#remove
listOne.remove('quite')
print(listOne)

#reverse
listOne.reverse()
print(listOne)

#sort (alpha)
listOne.sort()
print(listOne)
