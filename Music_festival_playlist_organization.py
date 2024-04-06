'''
3. Music Festival Playlist Organization
Objective:
The aim of this assignment is to develop your skills in using Python loops with sets, 
particularly for organizing and managing playlists for a music festival. 
You will work with sets to handle various artists and genres, ensuring no duplicates and maintaining a well-organized collection.

Task 1: Artist Lineup Compilation
You are provided with a list of artist names scheduled to perform at different stages of the music festival. 
Using a loop, compile these artist names into a set to create a unique lineup without duplicates.

Example Code:

artist_names = ["The Lumineers", "Tame Impala", "Billie Eilish", "The Lumineers", "Arctic Monkeys", "Tame Impala"]
unique_artists = set()
Expected Outcome:
A set containing unique artist names, such as {'The Lumineers', 'Tame Impala', 'Billie Eilish', 'Arctic Monkeys'}.

Task 2: Genre Sorting
You have a list of genres associated with each artist. Using a loop with sets, categorize artists by their genres, 
creating a set for each genre.

Example Code:

artists_genres = {
    "The Lumineers": "Folk",
    "Tame Impala": "Psychedelic Rock",
    "Billie Eilish": "Pop",
    "Arctic Monkeys": "Indie Rock"
}
Expected Outcome:
A categorization of artists by genres, such as Genre: Folk, Artists: The Lumineers.

Task 3: Playlist Duplication Check
Create a Python script that takes multiple playlist sets and checks if any playlist is a duplicate of another 
(i.e., contains the same set of songs).

Example Code:

playlist1 = {"Song A", "Song B", "Song C"}
playlist2 = {"Song D", "Song E", "Song F"}
playlist3 = {"Song A", "Song B", "Song C"}

playlists = [playlist1, playlist2, playlist3]
Expected Outcome:
A confirmation of whether there are duplicate playlists, such as Duplicate playlists found: True.
'''

# Task one

artist_names = ["The Lumineers", "Tame Impala", "Billie Eilish", "The Lumineers", "Arctic Monkeys", "Tame Impala"]
unique_artists = set(artist_names)
print("Artist Line up for the Festival:")
for count, artist in enumerate(unique_artists):
  print(f"{count + 1}. {artist}")


# Task Two


artists_genres = {
    "The Lumineers": "Folk",
    "Tame Impala": "Psychedelic Rock",
    "Billie Eilish": "Pop",
    "Arctic Monkeys": "Indie Rock"
}

new_artist_genres = {}

for artists, genres in artists_genres.items():
    if genres not in new_artist_genres:
        new_artist_genres[genres] = set()
    new_artist_genres[genres].add(artists)

for genre, artists in new_artist_genres.items():
    print(f"Genre: {genre}, Artists: {', '.join(artists)}")


# Task Three

# Need to make a set to store the playlists 
# need to make a variable = to False so when i find a match it will = True 

def duplicate_playlists(playlists):
  new_playlist = set()
  duplicate_found = False
  
  for playlist in playlists:
    unchangeable_playlist = frozenset(playlist)
    if unchangeable_playlist in new_playlist:
      duplicate_found = True
      break
    new_playlist.add(unchangeable_playlist)

  print(f"Duplicate playlists found: {duplicate_found}")
  
  

playlist1 = {"Song A", "Song B", "Song C"}
playlist2 = {"Song D", "Song E", "Song F"}
playlist3 = {"Song A", "Song B", "Song C"}

playlists = [playlist1, playlist2, playlist3]


def main():
  print("Welcome to the Playlist Comparison Application")
  while True:
    print("\nMain Menu:\n1. Duplicate look-up\n2. Exit")
    user_input = input("Enter your choice: ")
    if user_input == "1":
      duplicate_playlists(playlists)
    elif user_input == "2":
      print("Thank you! Good bye")
      break
    else:
      print("Invalid Input") 

main()   