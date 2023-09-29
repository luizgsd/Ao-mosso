from time import strftime

def checkLunchtime():
    timeNow = int(strftime('%H'))
    
    if timeNow >= 11 and timeNow <= 13:
        return True
    else:
        return False
    