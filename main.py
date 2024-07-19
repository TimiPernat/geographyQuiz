import json
import random


def reading_data():
    with open("countries_cities.json", "r") as countries_file:
        countries_capitals = json.load(countries_file)
        return countries_capitals


def play_quiz():

    guessed_countries = []
    streak = 0
    random_country = random.choice(list(reading_data().items()))

    while True:

        if random_country in guessed_countries:
            random_country = random.choice(list(reading_data().items()))

        answer = input(f"Glavno mesto {random_country[0]} (napiši Hint, za namig): ").capitalize()

        if answer == "Hint":
            print(f"Prvi dve črki: {random_country[1][:2]}")
        elif answer == random_country[1]:
            print("Odgovor je pravilen!")
            streak += 1
            guessed_countries.append(random_country)
            random_country = random.choice(list(reading_data().items()))
        else:
            print(f"Več sreče prihodnjič. Pravilen odgovor je {random_country[1]}")
            print(f"Ugotovil si {streak} glavnih mest.")
            break


print("Dobrodošel v quizu glavnih mest. Začnimo!")
game_on = True

while game_on:

    play_quiz()
    play_on = input("Želiš poskusiti ponovno? (yes/no): ")
    if play_on == "yes":
        play_quiz()
    elif play_on == "no":
        game_on = False
