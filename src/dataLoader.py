import json
import config
class DataLoader:
    def __init__(self):
        pass

    def loadData(self):
        jsonData = open(config.jsonDataPath)

        # returns JSON object as
        # a dictionary
        rawData = json.load(jsonData)
        return rawData
