import requests

# Get Disney Dogs Questions using the api
questions = requests.get('http://jservice.io/api/clues?category=4469').json()

# Disney Song Lyrics
# requests.get('http://jservice.io/api/clues?category=8031').json()
# Disney Villians
# requests.get('http://jservice.io/api/clues?category=4778').json()
# Disney Movie Taglines
# requests.get('http://jservice.io/api/clues?category=10927').json()
# Disney 7 Dwarfs
# requests.get('http://jservice.io/api/clues?category=18399').json()
# Disney Anagramed Characters
# requests.get('http://jservice.io/api/clues?category=4888').json()

# Find your favorite categories here: http://jservice.io/

print(questions)
print(len(questions))