import json
from datetime import date
from datetime import datetime
from datetime import timedelta

NUMBER_OF_DAYS = 7

class Model(object):

    def __init__(self, requester):
        self.__requester = requester
        self.__viewsList = []
        self.__viewsDict = {}
        self.__openPrsCallback = None
        self.__infoPrDays = []
        self.__infoOpenPrDays = []
        self.__infoMergedPrDays = []
        self.__info = json.loads(self.__requester.getAllOpenReviews())

        today = date.today()

        for x in range(0, NUMBER_OF_DAYS):
            infoOpenPrDays = []
            infoMergedPrDays = []
            dateToCheck = today - timedelta(days=x)
            dayChange = json.loads(self.__requester.getAllReviewsByDate(dateToCheck))

            self.__infoPrDays.insert(0, dayChange)

            for change in dayChange:
                created = datetime.strptime(change['created'].split(' ')[0], '%Y-%m-%d')
                if (created.date() == dateToCheck and (change['status'] != 'ABANDONED')):
                    infoOpenPrDays.append(change)
                if (change['status'] == 'MERGED'):
                    infoMergedPrDays.append(change)

            print 'infoOpenPrDays' + str(infoOpenPrDays)
            print 'infoMergedPrDays' + str(infoMergedPrDays)

            self.__infoOpenPrDays.insert(0, infoOpenPrDays)
            self.__infoMergedPrDays.insert(0, infoMergedPrDays)

    def getInfo(self):
        self.__requester.getAllOpenReviews()

    def getSideMenuOption(self):
        return self.__viewsList

    def registerView(self, id, view):
        self.__viewsList.append(id)
        self.__viewsDict[id] = view

    def getViews(self):
        return self.__viewsDict

    def getTotalOpenPrs(self, callback):
        if (callback):
            callback(str(len(self.__info)))

    def getLast7DaysPrs(self, callback):
        if (callback):
            result = {}
            created = []
            merged = []
            for x in range(0, NUMBER_OF_DAYS):
                created.append(len(self.__infoOpenPrDays[x]))
                merged.append(len(self.__infoMergedPrDays[x]))

            result['created'] = created
            result['merged'] = merged

            print 'created' + str(created)
            print 'merged' + str(merged)

            callback(result)
