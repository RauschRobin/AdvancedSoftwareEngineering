import requests
from bs4 import BeautifulSoup
import datetime
import dateutil.relativedelta as rd
import json

class Rapla:
    def __init__(self, rapla_url="https://rapla.dhbw.de/rapla/internal_calendar?key=YFQc7NlGleuSdybxizoa8NHjLLNjd9D6tjBdAvDwwzXobLEfUIsCXHwYu-Ma7QfggMDkLLj1CsQ-kB7hFJSGjcrCTGDFdUXDv_NNHoHvSJP_dG36z7u1r9aZLrggiD92Gryjvwt1kpad5g93Dkdn0A&salt=1046252309&day=3&month=10&year=2023&goto=Datum+anzeigen&pages=12#6"):
        self.rapla_url = rapla_url

    def get_current_calendar_week(self):
        calendar_week = datetime.datetime.now().isocalendar()[1]
        return calendar_week

    def get_calendar_week(self, year, month, day):
        calendar_week = datetime.date(year, month, day).isocalendar()[1]
        return calendar_week
    
    def get_week_day(self, day_counter):
        week_day = ""
        if(day_counter == 0):
            week_day = "monday"
        elif(day_counter == 1):
            week_day = "tuesday"
        elif(day_counter == 2):
            week_day = "wednesday"
        elif(day_counter == 3):
            week_day = "thursday"
        elif(day_counter == 4):
            week_day = "friday"
        elif(day_counter == 5):
            week_day = "saturday"
        elif(day_counter == 6):
            week_day = "sunday"
        
        return week_day
    
    def get_date_from_week(self, year, calendar_week, day_counter):
        # Berechnen Sie das Datum des ersten Tages des Jahres
        first_day_of_year = datetime.datetime(year, 1, 1)

        # Berechnen Sie das Datum des ersten Montags des Jahres
        if first_day_of_year.weekday() > 3:
            first_monday_of_year = first_day_of_year + rd.relativedelta(days=(7 - first_day_of_year.weekday() + 1))
        else:
            first_monday_of_year = first_day_of_year - rd.relativedelta(days=(first_day_of_year.weekday() - 1))

        # Berechnen Sie das Datum basierend auf der Kalenderwoche und dem Wochentag
        date = first_monday_of_year + rd.relativedelta(days=((calendar_week - 1) * 7 + day_counter))

        return date.date()
    
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
                            date = self.get_date_from_week(year, calendar_week, day_counter)
                            
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
                                
                                week_day = self.get_week_day(day_counter)
                                vorlesungsdaten[week_day].append({"vorlesung": neue_vorlesung})

                break  # Beenden nach gefundener Tabelle
                # --------------------------------------------------------------------------------

        # Konvertieren Sie das Python-Objekt in eine JSON-Zeichenkette
        json_string = json.dumps(vorlesungsdaten)

        return json_string