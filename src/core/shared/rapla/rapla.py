import requests
from bs4 import BeautifulSoup
from .week_and_days_handling import WeekAndDaysHandling as wdh
import json
from ..PreferencesFetcher.PreferencesFetcher import PreferencesFetcher as pf

rapla_url = pf.fetch("rapla-url")

class Rapla:
    def __init__(self, rapla_url=rapla_url):
        self.rapla_url = rapla_url

    def get_week_data(self, calendar_week, year):
        # Make a request to the website
        r = requests.get(self.rapla_url)
        vorlesungsdaten = {
            "monday": [],
            "tuesday": [],
            "wednesday": [],
            "thursday": [],
            "friday": [],
            "saturday": [],
            "sunday": []
        }

        # Parse the HTML content
        soup = BeautifulSoup(r.text, 'html.parser')

        # Finden Sie die Tabelle mit <th class="week_number">KW XX</th>
        tables = soup.find_all('table')

        for table in tables:
            th = table.find('th', {'class': 'week_number'})
            kw_str = "KW " + str(calendar_week)
            
            if th and kw_str in th.text:
                # --------------------------------------------------------------------------------

                for row in table.find_all('tr'):  # Geht durch jede Zeile in der Tabelle
                    day_counter = 0

                    for td in row.find_all('td'):  # 'week_separatorcell' nur am Ende der Spalten -> definiert neuen Tag

                        if(td.get('class') and ('week_separatorcell' in td.get('class'))):
                            day_counter += 1

                        elif(td.get('class') and ('week_block' in td.get('class'))):
                            
                            # vorlesungseigenschaften scrapen
                            prof = td.find('span', {'class': 'person'})
                            room = td.find_all('span', {'class': 'resource'})
                            name = td.find('a')
                            time, subject = name.get_text(separator='<br>').split('<br>')
                            time_start, time_end = time.split('-')
                            time_start = time_start.replace('\u00a0', '')
                            date = wdh.get_date_from_week(year, calendar_week, day_counter)
                            
                            # Vorlesung in json object hauen
                            if(prof and ...):
                                neue_vorlesung = {
                                    "date": f"{date}",
                                    "time_start": f"{time_start}",
                                    "time_end": f"{time_end}",
                                    "subject": f"{subject}",
                                    "prof": f"{prof}",
                                    "room": f"{room[1]}"
                                }
                                
                                week_day = wdh.get_week_day(day_counter)
                                vorlesungsdaten[week_day].append({"vorlesung": neue_vorlesung})

                break  # Beenden nach gefundener Tabelle
                # --------------------------------------------------------------------------------

        # Konvertieren Sie das Python-Objekt in eine JSON-Zeichenkette
        json_string = json.dumps(vorlesungsdaten)

        return json_string