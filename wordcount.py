"""Count words in file."""


# put your code here.
file = open('test.txt')
#print(file.read())
word_count = {}

for line in file:
  line = line.rstrip()
  words = line.split()

  for word in words:
    word_count[word] = word_count.get(word, 0) + 1

for word, count in word_count.items():
    print(word, count)
















#Notes
#animals = {'duck': 2, 'chicken': 3, 'horse': 1} 
""" for key, value in animals.items():
  print(key, value) """
#for animal in animals:
  #get the key print(animal)
 #get the value print(animals[animal])

#Update in dictionary and if the key doesn't exist, the value is added
""" animals['pony'] = 2 """
#-------------------------------------------------------------------------
#Dictionary Notes 

#1.All keys has to have a value otherwise it will throw an error.
#2.Use del key word to delete
#3.You can use variable as key to update the value
#4.When iterate over, you get each key in the dictionary
#5.Dictionary are not order
#6.Keys must be unique
#7.Keys must be immutable
#8.Immutable types are - numbers, strings, tuples
#9.Check if key is in dictionary -> if 'frog' in animals:
#10.If you look for a nonexist key in the dictionary, it will throw an error
#11.A way to prevent key error --> animal.get('frog', 0) + 1
#12.Animals.values()--> for animal in animals.values(): --> gives you all the values in your dictionary
#13.Animals.items() --> act like a list of tuples
#14.Cannot use .sort() cause its unordered
#15.Could use .sorted() --> .sorted(animals.items()) --> print sorted tuple list.

#-------------------------------------------------------------------
#With Tuples as value

# animals = {('pony': 1, True), ('frog': 2, True), ('duck': 3, False)}

#1.animals['pony'][2] --> animals 'pony' at index 2
#2.Before creating a dictionary think about how you would access your data
#3.

""" count = {}
phrase = 'delicious knishes'
for letter in phrase:
  count[letter] = count.get(letter, 0) + 1
return count """

#---------------------------------------------------------------------
""" test_scores = {
  'Alice': [100,80,75],
  'Jon': [90,85,80]
}
for student in test_scores:
  print(test_scores[student][0]) """

