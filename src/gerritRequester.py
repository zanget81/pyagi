
from datetime import timedelta
import requests
from requests.auth import HTTPDigestAuth

AUTHENTICATION_PREFIX = 'a/'
OPEN_REVIEWS = 'changes/?q=status:open+p:onemw-js'
MERGED_REVIEWS = 'changes/?q=status:merged+p:onemw-js'
BY_DAY = 'changes/?q=p:onemw-js+after:{$START_TIME}+before:{$END_TIME}'

RESPONSE_DELIMITER = ")]}'"



class GerritRequester(object):
    def __init__(self, config):
        self.__config = config
        self.__authentication = HTTPDigestAuth(self.__config.config['user'], self.__config.config['password'])

    def getAllOpenReviews(self):
        r = requests.get(self.__config.config['backend'] + AUTHENTICATION_PREFIX + OPEN_REVIEWS, auth=self.__authentication, verify=False)
        #print '##############################'
        #print 'response text: ' + r.text
        return r.text.replace(RESPONSE_DELIMITER, '')

    def getAllReviewsByDate(self, date):
        dayBefore = date
        dayAfter = date + timedelta(days=1)

        byDay = BY_DAY.replace('{$START_TIME}', str(dayBefore)).replace('{$END_TIME}', str(dayAfter))

        r = requests.get(self.__config.config['backend'] + AUTHENTICATION_PREFIX + byDay, auth=self.__authentication, verify=False)
        #print '##############################'
        #print 'byDay: ' + byDay
        #print 'open response text: ' + r.text
        return r.text.replace(RESPONSE_DELIMITER, '')