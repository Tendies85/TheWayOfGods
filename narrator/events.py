import typing as t
from dataclasses import dataclass, asdict


@dataclass
class Choice:
    text: str
    values: dict

    def __str__(self):
        value = ""
        if 'health' in self.values:
            value += f"{self.values['health']}♥ "
        if 'follower' in self.values:
            value += f"{self.values['follower']}🙏 "
        if 'food' in self.values:
            value += f"{self.values['food']}🍎 "
        if 'money' in self.values:
            value += f"{self.values['money']}💰 "

        return f"{self.text} \n\t{value}"


@dataclass
class Event:
    id: str
    event_str: str
    data: dict
    choices: t.List[Choice]

    def __str__(self):
        desc = self.event_str.format(**self.data)
        choices = ""
        for i, c in enumerate(self.choices):
            choices += f"\n{i}: {c}"

        return f"{desc}\n{choices}"


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


    """
Du schreitest durch die Tore des Tempelhofes. Keine Erinnerungen an die Zeit
vor dem Tempel, nur eine wage Vermutung auf das was hinter diesen Toren kommen
mag. So jung warst du als die Mönche dich vor den Toren des Tempels fand und
aufnahmen.

Im Tempel erfuhr man nichts von außerhalb der Mauern.  Um deinen Geist rein
zuhalten.  Um dich auf die Aufgabe vorzubereiten zu der du erwählt wurdest.

Einzig und allein vernahm man Laute wenn Markttag war. Aber nicht genug um sich
ausmalen zu können was dort vorsich ging.  Zum Abschied versammelten sich deine
Brüder und Schwestern im Hof. Segnungen und letzte Worte sollten das letzte
sein was du von deinen Freunden, von deiner Familie hören solltest. Ein Alter
Mann kommt auf dich zu. Die Kapuze, so wie es Brauch war, tief ins Gesicht
gefallen, bewegte sich auf dich zu. An seiner wackeligen Gangart und an seinen
zittrigen Händen die fest umschlossen einen Stab hielten, fiel dir auf das es
sich um den Meister Setius handeln müsste. Oder vielleicht daran daß er der
einzige ist dem es gestattet war eine weißes Robe mit goldenen Verziehrungen zu
tragen.

Vater Setius sieht dich an und sagt:

Mein Sohn {player_name}, der Weg wird schwer sein. Er wird Schmerzen. Er wird
Verzweiflung und Versuchung mit sich bringen. Aber auch die Hoffnung. Wir haben
etwas gesammelt was dir auf den Weg mitgeben möchten, siehe es als unser
letztes Geschenk an dich.

Der Alte reicht dir einen Lederbeutel hin. Er sieht reich gefüllt aus. Du.....

"""

story = [
    Event(
        "1",
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
        "2",
        "Would be a force of Evil or of Good?",
        {},
        [
            Choice("I dont like either", reward(0, 0, 5, 10)),
            Choice("I like good", reward(10, 0, 0, 0)),
            Choice("I like Evil!", reward(0, 0, 0, 10)),
        ],
    ),
    Event(
        "3",
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

story_map = {s.id: s for s in story}


