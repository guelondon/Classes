import datetime
import time
import pytz

class stamping(object):
    
    """
    Takes sDate and size 
    sDate: has to be datetime.datetime Object
    size: has to be int
    
    optional Parameters:
    
    interval: 15 as default
    zone: Europe/Berlin as default (from pytz class timezone function)
    Creates a List with time stamp
    """
    
    def __init__(self, sDate, size, interval=15, zone='Europe/Berlin'):
       
        if type(sDate)==datetime.datetime:
            self.sDate = sDate
            self.startDate_logged = sDate
        else:
            print('ValueError: Type of sDate is ' + str(type(sDate)) + '. This Class requires datetime.datetime Object.' )
            raise ValueError
            
        
        if type(size)==int:
            self.size= size
        else:
            print('ValueError: Type of size is ' + str(type(size)) + '. This Class requires int Object.' )
            raise ValueError
        
        self.interval=interval
        self.zone=zone   
        self.stamp_list=[]
        
        for i in range(self.size):
            self.sDate=self.sDate.astimezone(pytz.timezone(zone))
            self.sDate=self.sDate+datetime.timedelta(minutes=interval)
            self.stamp_list.append(self.sDate.strftime('%d.%m.%Y %H:%M:%S'))
    
    def get_size(self):
        return self.size
    
    def get_sDate(self):
        return self.startDate_logged
    
    def get_stamping(self):
        return self.stamp_list
    
    def __str__(self):
        return str(self.stamp_list)
    
