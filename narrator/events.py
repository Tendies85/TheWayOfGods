import typing as t
from dataclasses import dataclass, asdict
from .gen import Choice


@dataclass
class Event:
    event_str: str
    data: dict
    choices: t.List[Choice]

    def __str__(self):
        desc = self.event_str.format(**self.data)
        choices = ""
        for i, c in enumerate(self.choices):
            choices += f"\n{i}: {c}"

        return f"{desc}\n{choices}"

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
