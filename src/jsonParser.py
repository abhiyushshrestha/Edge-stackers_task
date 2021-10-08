from dataLoader import DataLoader
import datetime

class JSONParser:
    def __init__(self):
        self.dl = DataLoader()
        self.structured_data = {
            "meeting_id": [],
            "meeting_name": [],
            "race_number": [],
            "race_link": [],
            "event_id": [],
            "distance": [],
            "start_time": []
        }

    def loadJSON(self):
        raw_data = self.dl.loadData()
        return raw_data

    def dataParser(self, raw_data):
        meetings_data = raw_data['dates'][0]['sections'][0]['meetings']
        for meeting_data in meetings_data:
            events_data = meeting_data['events']
            for event_data in events_data:
                try:
                    self.structured_data['meeting_id'].append(meeting_data['id'])
                    self.structured_data['meeting_name'].append(meeting_data['name'])
                    self.structured_data['race_number'].append(event_data['raceNumber'])
                    self.structured_data['race_link'].append(event_data['httpLink'])
                    self.structured_data['event_id'].append(event_data['id'])
                    self.structured_data['distance'].append(event_data['distance'])
                    self.structured_data['start_time'].append(datetime.datetime.utcfromtimestamp(event_data['startTime']))
                except:
                    self.structured_data['meeting_id'].append("NA")
                    self.structured_data['meeting_name'].append("NA")
                    self.structured_data['race_number'].append("NA")
                    self.structured_data['race_link'].append("NA")
                    self.structured_data['event_id'].append("NA")
                    self.structured_data['distance'].append("NA")
                    self.structured_data['start_time'].append("NA")


        return self.structured_data

