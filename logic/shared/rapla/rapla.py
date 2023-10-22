'''
Beispielformat zum übergeben der Rapla Daten einer Woche in JSON:
[
    {
        'name': 'Grundlagen der Künstlichen Intelligenz',
        'von': '2023-09-09-10-15-00',
        'bis': '2023-09-09-12-00-00'
    },
    {
        'name': 'Grundlagen Maschinellem Lernens',
        'von': '2023-09-10-08-30-00',
        'bis': '2023-09-10-11-45-00'
    },
    ...
]

Mehr informationen brauchen wir ja nicht (glaube ich)

'''

class Rapla:
    def __init__(self):
        return
    
    def getRaplaTimeTableOfGivenWeek(self, week):
        return "Keine Vorlesungen!"