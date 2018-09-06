#Comments are text that will not be executed in your code. Rather comments are for other programmers to read. 

# All of the exercises below are commented out. Write your Javascript code after each exercise.

#Variables and Data Types 
#Print each variable and test your code in the terminal using the Python interpreter

#example
greeting = 'Hello Prepster'
print(greeting) #this should print 'Hello Prepster'

#1 Variables with a String value
#Declare variables named first_name, last_name, birth_place, hobby, role_model, famous_quote, fav_president, fav_food, fav_color, fav_song

#Assign your own string values to each variable and print each variable.
first_name = 'Chaz'
last_name = 'Leong'
birth_place = 'Honolulu, HI'
hobby = 'Coding and working out'
role_model = 'You!'
famous_quote = 'souuuuuwooooop'
fav_president = 'not trump'
fav_food = 'french fries'
fav_color = 'black'
fav_song = 'milk and cereal'

print(first_name)

#2 String Concatenation
#Declare a variable named full_name and concatenate first_name and last_name. Print the full_name variable.
full_name = first_name + ' ' + last_name
print(full_name)

#Declare a variable named intro that creates the following sentence:
#'Hello, my name is x and I was born in y.' Where x is full_name and y is birth_place. Print the intro variable.


#Declare a variable named about_me that creates the following sentence:
#'My hobby is x, my favorite song is y, and I like to eat z.' Where x is hobby, y is fav_song and z is fav_food. Print the about_me variable.


#3 Spacing with tabs and newlines
#Declare a variable named my_hero that the following sentence using a tab:
#'My hero is x and his famous quote is y.' Where x is role_model and y is famous_quote. Print the my_hero variable.
my_hero = 'My hero is me and \nmy famous quote is souuu\twoop'
print(my_hero)

#Declare a variable named my_favs that creates the following sentence and returns a new line after each numbered item. 
#'This is what I like: 1. hobby 2. fav_color 3. fav_song
#Print the my_favs variable.
my_favs = 'This is what I like: \n1. hobby \n2. fav_color \n3. fav_song'
print(my_favs)

#4 Variables with a Number value
#Declare variables named age, weight, shoe_size, fav_number, yen_rate, bitcoin_value, todays_temperature, hawaii_popuation, countries_traveled, number_of_siblings

#Assign your own number values to each variable and print each variable.
age = 29
print(age)

#5 Number as Strings Concatenation
#Declare a variable named self_intro that creates the following sentence:
#'Aloha, my name is x and I am y years old and my shoe size is z.' Where x is full_name, y is age and z is shoe_size. Print the self_intro variable.


#Declare a variable named market_update that creates the following sentence:
#"Today's bitcoin value is x and the yen exchange rate is y." Where x is bitcoin_value and y is yen_rate. Print the market_update variable.


#Declare a variable named about_hawaii that creates the following sentence:
#"Did you know that Hawaii's population is x and the average temperatue is y?" Where x is hawaii_population and y is todays_temperature. Print the about_hawaii variable.


#6 Variables with a List value
#Declare a variable named fab_five and assign it a list containing five of your all time favorite snacks. Print the fab_five variable.
fab_five = ['french fries', 'chips', 'pizza', 'ramen', 'pho']
print(fab_five)

#Declare a variable named plate_lunch and assign it a list containing five of your favorite lunch items. Print the plate_lunch variable.


#Declare a variable named ice_cream and assign it a list containing three of your favorite ice cream flavors. Print the ice_cream variable.


#Declare a variable named west_siiiiide and assign it a list containing states found on the west coast of the US. Print the west_siiiiide variable.


#Declare a variable named mega_millions and assign it a list containing the Mega Millions Lottery results for May, 4, 2018
#https://www.lotteryusa.com/mega-millions/. Print the mega_millions variable


#Declare a variable named hamajang and assign it a list containing six different data types. Print the hamajang variable.

#Declare a variable named dynamic_duos and assign it a list containing 3 lists, with each list containing items that pairs well with each other. Print the dynamic_duos variable.

#Print the following:
#Gin

#peanut butter

#cheeseburger


#7 Accessing values in List
vics_list = ['Hendricks gin', 'Fever Tree tonic', 'Costco pub mix', 'cool ranch doritos', 'oreos', 'Safeway fried chicken', 'Morning Glass coffee']

#Print the entire list.
print(vics_list)

#Print the length of the list.
print(len(vics_list))

#Print only the first element in the list.
print(vics_list[0])
#Print only the last element in the list.
print(vics_list[len(vics_list) - 1])

#Print 'Safeway fried chicken'
for item in vics_list:
  if(item == 'Safeway fried chicken'):
    print(item)

#Replace 'cool ranch doritos' with 'carrot cake' and print the list.
for i, item in enumerate(vics_list):
  if(item == 'cool ranch doritos'):
    vics_list[i] = 'carrot cake'
print(vics_list)

#Print the last element in the list using -1
print(vics_list[len(vics_list) - 1])

#8 Variables with a Dictionary value
#Declare a variable named car and create the following key-value pairs:
# - key: brand string value: Tesla,
# - key: model string value: Model 3,
# - key: price number value: 35000,
# - key: color string value: red,
# - key: production boolean value: False,
# - key: features list value: moon roof, leather seats, iphone docker

#Print the car variable.
car = {
  'brand': 'Subaru',
  'model': 'STI',
  'color': 'White',
  'features': 'Fast'
}
print(car)

#Declare a variable named footwear and create the following key-value pairs:
# - key: brand string value: Vivo Barefoot,
# - key: url string value: https://www.vivobarefoot.com/us,
# - key: gender string value: Mens,
# - key: type string value: Ababa Canvas,
# - key: price number value: 80,
# - key: color list value: tan, black stripes, gum
# - key: ordered boolean value: True

#Print the footwear variable.


#Declare a variable named bank and create the following key-value pairs:
# - key: name  string value: First Hawaiian Bank,
# - key: employees number value: 2200,
# - key: headquarters string value: Honolulu,
# - key: revenue number value: 700000000,
# - key: nasdaq string value: FHB,
# - key: products list value: savings, loans, trust, wealth management,
# - key: executive dictionary value: name: Robert Harrison, title CEO, salary: 2000000

#Print the bank variable.


#Declare a variable pandas and assign it an EMPTY dictionary.
#You will add the following key-value pairs:
# - key: name string value: Panda Express
# - key: restaurants number value: 2000
# - key: cuisine string value: Gourmet Chinese Food
# - key: menu list value: Orange Chicken, Walnut Shrimp, Sweet and Sour pork
# - key: highest_revenue string value: Ala Moana Center Food Court

#Print the pandas variable.
pandas = {}
pandas['name'] = 'pandas express'
pandas.update({'restaurant number': 2000})
pandas.update(cuisine = 'chinese')
pandas.update({
  'menu': ['orange chicken', 'walnut shrimp']
})

print(pandas)

#Declare a variable named bucket_list and assign it to an EMPTY dictionary.
#You will add the following key-value pairs:
# - key: travel string value of your choice
# - key: learn string value of your choice
# - key: weight number value of your choice
# - key: to_dos list value of your choice
# - key: meet_person string value of your choice  

#Print the bucket_list variable.


#9 Variable with a Tuple value
#Declare a variable named bruce_bio and assign a tuple containing the following values: Bruce Lee, male, 32, San Francisco, [Kung-Fu Master, actor, philosopher]

#Print the bruce_bio variable.
bruce_bio = ('bruce lee', 'male', 32, ['kung-fu master', 'actor'])
print(bruce_bio)

#Declare a variable named movies and assign a tuple containing the following values: [The Big Boss, 1971],[Fist of Fury, 1972], [The Way of the Dragon, 1972], [The Game of Death, 1972]

#Print the movies variable.
movies = (['the big boss', 1971], ['fist of fury', 1972])
print(movies)

#Declare a variable named updated_bio and add the bruce_bio and movies tuples together. Print the updated_bio variable.
updated_bio = bruce_bio + movies
print(updated_bio)

#Print the following values:
#The length of the updated_bio tuple
print(len(updated_bio))

#Bruce Lee
print(updated_bio[0])

#Index position 1
for i, item in enumerate(updated_bio):
  if(i == 1):
    print('I',updated_bio[i])

#['Game of Death', 1972]
for i, item in enumerate(updated_bio):
  if(item == ['kung-fu master', 'actor']):
    print('ITEM', item)

#philosopher
print('UPDATED BIO', updated_bio)
print('UPDATED BIO LENGTH', len(updated_bio))
for item in updated_bio:
  # print('EACH ITEM', item)
  if(type(item) is list):
    for list_item in item:
      # print('LIST ITEM', list_item)
      if(list_item == 'actor'):
        print(list_item)

#1971

#The Way of the Dragon

#Fist of Fury

#The last value using -1

#Game of Death using -1


#10 Variables with a Boolean value
#Declare the following variables and assign either a True or false value for each.
#female, american, likes_coding, is_hungry, has_a_dog

#Print each variable that you declare.

