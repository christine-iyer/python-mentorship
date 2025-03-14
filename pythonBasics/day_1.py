#Day one is a little practice with variables. Variables are little packages. Each variable represents a single thing which can be mutated. Variables can be strung together using f strings. Make sure the types are all consistent in order to concatonate. 
import string


name="Crystal Crystal"
age=58
height=5.0
is_student=False

print("My name is: ", name)
print("I am ", age, "years")
print("I am ", height, "feet tall")
print("is a student: ", is_student)

tv_show="I can't think of any"
release_year="2002"
rating=5000000

print(f"My favorite movie is, {tv_show.upper()}, released in {release_year}, gets {rating} stars.")
favorite_shows= [
    "Breaking Bad", "The Sopranos", "The Wire", "Game of Thrones", 
    "Stranger Things", "Mad Men", "Fargo", "The Crown", 
    "Westworld", "Sherlock", "Better Call Saul", "Parks and Recreation", 
    "The Office", "Arrested Development", "Seinfeld", "Friends", 
    "Black Mirror", "Weeds", "The Mandalorian", "The Boys", 
    "True Detective", "Big Little Lies", "Homeland", "House of Cards", 
    "Billions", "Happy Valley"
]
print(f"My third favorite show is {favorite_shows[2]}")

#List the top 3 in a single sentence
print(f"{name} is {str(age)} years old! She loves to watch TV...her favorite shows are 1. {favorite_shows[0]} 2. {favorite_shows[1]} 3. {favorite_shows[2]}")

#Tidy up the above using a for loop
#Step 1 
for i in favorite_shows:
     print(i)
     
letter=["a","b","c"]
for i,rate in enumerate(favorite_shows, start=1):
     print(f"{i}. {rate}")
     
for i in favorite_shows:
     # print(len(i)) 
     print(f"The length of {i} is {len(i)} and if you add 9 it is {len(i)+9}")
      
     
#Reflections: I know this stuff is basic, but I'm trying to make it automatic. Rather that getting bogged down ahead of time with trying to make sunse of next steps, I need to just concentrate on this step. So let's take the above code and have it incorporate the letters...giving the favorite shows more properties. 
#     favorite_shows = ["Weeds", "Billions", "Happy Valley"]
alphabet = list(string.ascii_lowercase)
vowel_sounds = ["a", "e", "i", "o", "u", "h"]

# print("Favorite shows and their corresponding alphabets:")
# for i, (show, letter) in enumerate(zip(favorite_shows, alphabet), start=1):
#     print(f"{i}. {show} - {letter}")

print(f"Favorite shows with numerical and alphabetical grades.  ")
for i, (show, letter) in enumerate(zip(favorite_shows, alphabet), 1):
     # if letter =="a":
     if letter in vowel_sounds:
          print(f"{i}. {show} gets an '{letter}'")
     else:
          print    (f"{i}. {show} gets a '{letter}'") 
     


     
