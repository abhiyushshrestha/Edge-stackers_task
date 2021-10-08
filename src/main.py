from jsonParser import JSONParser

class Main:
    def __init__(self):
        self.jp = JSONParser()

    def run(self):
        raw_data = self.jp.loadJSON()
        structured_data = self.jp.dataParser(raw_data)
        return structured_data

if __name__ == "__main__":
    m = Main()
    structured_data = m.run()
    print(structured_data)