
import datetime
DT_FORMAT = "%Y-%m-%d %H:%M:%S"

def getFormatedDateTime(datetime_obj, format = None):
    if( datetime_obj is None):
        return None
    if format is None:
        format = DT_FORMAT
    return datetime_obj.strftime(format)

def getDateTimeObjectFromString(dt_string, format = None):
    if format is None:
        format = DT_FORMAT
    return datetime.datetime.strptime(dt_string, format)

def getCurrentDateTime():
    pass
