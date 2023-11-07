import random

class RoundcubeMock():
    def __init__(self):
        pass

    def checkForNewEmail(self):
        if random.randint(0, 6) == 3:
            return random.choice(example_emails)
        
    def getLastReceivedEmail(self):
        return example_emails[0]
        
example_emails = [
    "Hallo liebe Studierende, ich hoffe ihr habt alle die Aufgabe 1.1 erfolgreich abgegeben. Falls nicht, dann wird es höchste Zeit. Ich wünsche euch noch einen schönen Tag. Viele Grüße, euer Professor Karsten",
    "Sehr geehrte Studenten und Studentinnen, die morgige Vorlesung zum Thema KI entfällt. Viele Grüße",
    "Liebe Studierende, zum Thema KI findet morgen eine Vorlesung statt. Viele Grüße",
    "Liebe Studierende, zum Thema Nachhaltigkeit findet morgen eine Konferenz am Standort 2 statt. Viele Grüße",
    "Hallo Studierende, Stress im Studium ist ganz normal. Braucht ihr Hilfe? Dann meldet euch doch einfach bei der Hochschul-Seelsorge an. Liebe Grüße",
    "Sehr geehrte Studierende, die Prüfungsergebnisse für den letzten Test sind jetzt verfügbar. Ihr könnt sie in eurem Online-Portal einsehen. Bei Fragen oder Unklarheiten, zögert nicht, euch bei uns zu melden. Viele Grüße, Prüfungsamt",
    "Liebe Kommilitonen, die nächste Sitzung des Mathematik-Clubs findet am Freitag um 15:00 Uhr in Raum 302 statt. Wir werden über komplexe Zahlen sprechen. Alle sind herzlich eingeladen! Beste Grüße",
    "Hallo zusammen, die Anmeldefrist für das Sommersemester endet in einer Woche. Vergesst nicht, euch für eure Kurse anzumelden, um euren Stundenplan rechtzeitig zu planen. Bei Fragen steht das Studierendensekretariat gerne zur Verfügung. Mit freundlichen Grüßen",
    "Liebe Studierende, wir suchen noch Freiwillige für das bevorstehende Campus-Fest. Wenn ihr Lust habt, bei der Organisation zu helfen oder einen Stand zu betreuen, meldet euch bitte bis Ende der Woche bei uns. Es wird eine großartige Gelegenheit sein, eure Kommilitonen zu treffen und Spaß zu haben. Viele Grüße",
    "Sehr geehrte Studierende, aufgrund von Wartungsarbeiten wird das Bibliotheksgebäude am Samstag geschlossen sein. Bitte plant eure Recherche und Studienzeiten entsprechend. Wir entschuldigen uns für etwaige Unannehmlichkeiten. Mit freundlichen Grüßen, Bibliotheksleitung"
]
