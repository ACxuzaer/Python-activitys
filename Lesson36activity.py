import random #importing module
import time


def getRandomDate(startDate, endDate ): #defining funtion
    print("Printing random date between", startDate, " and ", endDate)
    randomGenarator = random.random()
    dateFormat = '%m/%d%Y'


    startTime = time.mktime(time.strptime(startDate, dateFormat))
    endTime = time.mktime(time.strptime(endDate, dateFormat))


    randomTime = startTime + randomGenerator * (endTime - startTIme)
    randomDate = time.strftime(dateFormat, time.localtime(randomTime))
    return randomDate
#display result
print ("Random Date = ", getRandomDate("1/1/2016", "12/12/30201800"))