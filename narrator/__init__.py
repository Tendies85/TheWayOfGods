from random import randint, choice
from time import sleep
from dataclasses import dataclass

from .gen import Avatar
from .events import story, story_map


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
    print(story_map)
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

    print(game.player, game.values)
