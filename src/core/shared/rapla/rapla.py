import requests
from bs4 import BeautifulSoup
from .DateParser import DateParser as dp
import json
import datetime

class Rapla:
    def __init__(self, rapla_url):
        self.rapla_url = rapla_url

    def fetchLecturesOfWeek(self, calendar_week, year):
        # Make a request to the website
        r = requests.get(self.rapla_url)

        # Create a dictionary to store the lecture data for each day of the week
        lecture_data = {
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

        # Find the table with <th class="week_number">KW XX</th>
        tables = soup.find_all('table')

        for table in tables:
            th = table.find('th', {'class': 'week_number'})
            kw_str = "KW " + str(calendar_week)

            if th and kw_str in th.text:
                for row in table.find_all('tr'):  # Iterate through each row in the table
                    day_counter = 0
                    for td in row.find_all('td'):  # 'week_separatorcell' only at the end of columns -> defines new day
                        if td.get('class') and ('week_separatorcell' in td.get('class')):
                            day_counter += 1
                        elif td.get('class') and ('week_block' in td.get('class')):
                            # Scrape lecture properties
                            prof = td.find('span', {'class': 'person'})
                            room = td.find_all('span', {'class': 'resource'})
                            name = td.find('a')
                            time, subject = name.get_text(separator='<br>', strip=True).split('<br>')
                            time_start, time_end = time.split('-')
                            time_start = time_start.replace('\u00a0', '')
                            current_date = dp.get_date_from_week(year, calendar_week, day_counter)
                            
                            # Add lecture to the JSON object
                            if prof and ...:
                                new_lecture = {
                                    "date": f"{current_date}",
                                    "time_start": f"{time_start}",
                                    "time_end": f"{time_end}",
                                    "subject": f"{subject}",
                                    "prof": f"{prof.get_text(strip=True)}",
                                    "room": f"{room[1].get_text(strip=True)}"
                                }
                                
                                week_day = dp.get_week_day(day_counter)
                                lecture_data[week_day].append({"lecture": new_lecture})
                break  # Stop after finding the table

        # Convert the Python object to a JSON string
        json_string = json.dumps(lecture_data)
        return json_string

    def compareTimetablesAndRespondWithLecturesThatChanged(self, timetable1, timetable2):
        changed_lectures = []

        # Iterate through the days of the week
        days_of_week = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
        for day in days_of_week:
            lectures1 = timetable1.get(day, [])
            lectures2 = timetable2.get(day, [])

            # Check if there are any lectures for this day
            if lectures1 and lectures2:
                # Compare the lectures for this day
                for lecture1 in lectures1:
                    for lecture2 in lectures2:
                        # Check if the lectures are for the same date and time
                        if lecture1['lecture']['date'] == lecture2['lecture']['date'] and \
                        lecture1['lecture']['time_start'] == lecture2['lecture']['time_start'] and \
                        lecture1['lecture']['time_end'] == lecture2['lecture']['time_end']:
                            # Check if the other details have changed
                            if lecture1['lecture'] != lecture2['lecture']:
                                changed_lectures.append({
                                    'old_lecture': lecture1['lecture'],
                                    'new_lecture': lecture2['lecture']
                                })

        return changed_lectures
