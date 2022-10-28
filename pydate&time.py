import datetime
x=datetime.datetime.now()    #first datetym import cheytha module aanu second datetym function aanu now enn paryunnath innathe date and tym aanu
print(x)
print(x.year)
print(x.strftime('%B'))
print(x.strftime('%y'))
print(x.strftime('%I'))
print(x.strftime('%p'))
print(x.strftime('%M'))
print(x.strftime('%H'))
print(x.strftime('%f'))  #microsecond
print(x.strftime('%C'))  #centuray
print(x.strftime('%X')) #local version of date
print(x.strftime('%x'))  #local version of time
print(x.strftime('%j')) #day number of year
print(x.strftime('%f'))
print(x.strftime('%c'))
print(x.strftime('%%'))
print(x.strftime('%G'))  #ISO 8601 year
print(x.strftime('%z'))
print(x.strftime('%Z'))


c=datetime.datetime(2024,4,12)
print(c)