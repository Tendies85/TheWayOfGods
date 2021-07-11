from random import randint, choice
from time import sleep
from dataclasses import dataclass

from .gen import Avatar, Question, Choice
from .events import Event

prophet_allfather = {"follower": 10}
prophet_presidalil = {"food": 5, "follower": 5}
prophet_wenom = {"follower": 5, "money": 5}
prophet_alkor = {"follower": 5, "health": -5}
prophet_haltarna = {"follower": 5, "money": 5}

DIFFICULTY = 1


def reward(fl, fo, mo, hp):
    return {
        "food": fo*DIFFICULTY,
        "follower": fl*DIFFICULTY,
        "money": mo*DIFFICULTY,
        "health": hp*DIFFICULTY
    }

story = [
    Event(
        "Which god will you serve?",
        {},
        [
            Choice("Allvater, god of the skies and stars", prophet_allfather),
            Choice("Presidalil, god of life and growth", prophet_presidalil),
            Choice("Wenom, god of death", prophet_wenom),
            Choice("Alkor, god of love and insanity", prophet_alkor),
            Choice("Hal'tarna, god of materia", prophet_haltarna),
        ],
    ),
    Event(
        "Would be a force of Evil or of Good?",
        {},
        [
            Choice("I dont like either", reward(0, 0, 5, 10)),
            Choice("I like good", reward(10, 0, 0, 0)),
            Choice("I like Evil!", reward(0, 0, 0, 10)),
        ],
    ),
    Event(
        "Why do you serve?",
        {},
        [
            Choice("i want to be rich!", reward(0, 5, 15, 0)),
            Choice("I live to serve my god", reward(15, 0, 0, 5)),
            Choice("wanderlust", reward(0, 10, 5, 5)),
            Choice("for might and glory", reward(10, 0, 4, 4)),
        ],
    ),
]



@dataclass
class Game:
    player: Avatar
    events: list
    values: dict


def create(stats):
    g = Avatar(**stats)
    return g


def update_values(game, values):
    for k, v in values.items():
        if k in game.values:
            game.values[k] += values[k]
        else:
            game.values[k] = values[k]


def run():
    name = input("Enter your name, prophet: ")
    player = create(
            {
                "name": name,
                "_food": 25,
                "_money": 0,
                "_health": 100,
                "_follower": 0,
            }
        )
    game = Game(player, story, {})

    while True:
        try:
            q = choice(story)
        except IndexError:
            break
        story.pop(story.index(q))

        chosen = int(input(f"{q}\n\nYour choice, {name}? "))
        update_values(game, q.choices[chosen].values)

        # print("#", end="", flush=True)

    print(game.player, game.values)
