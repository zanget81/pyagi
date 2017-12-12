import json

class Config(object):

    def __init__(self):
        filePath = 'config.json'
        self.config = {}

        with open(filePath) as f:
            self.config = json.loads(f.read())
