"""
Program: string_methods.py
Author: Dylan Thomas
Last date modified: 09/14/2020
"""

character_movie = 'tony stark in Iron Man'

#Capitalize and Find

capitalized = character_movie.capitalize()
print (capitalized)
result = capitalized.find('tar')
print(result)


#index and isalnum (False and true)

result_2 = character_movie.index('tar')
print(result_2)
print(character_movie.isalnum())
character_movie2 = 'tonystarkinIronMan'
print(character_movie2.isalnum())


#isalpha and isdigit

print(character_movie.isalpha())
print(character_movie2.isalpha())
print(character_movie.isdigit())


#islower and isupper true examples

character_movie3 = 'tonystarkinironman'
character_movie4 = 'TONYSTARKINIRONMAN'
print(character_movie3.islower())
print(character_movie4.isupper())


#isspace and startswith

print(character_movie.isspace())
result = character_movie.startswith('tony')
print (result)
