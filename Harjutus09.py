from dateutil.relativedelta import relativedelta
import datetime
import locale
now = datetime.datetime.now()
print ("Current date and time : ")
print (now.strftime("%d %B %Y"))
'''##################################'''
locale.setlocale(locale.LC_TIME, 'et_ET') 
today = datetime.datetime.now()
print(today.strftime("%d %B %Y"))

kood = "50508120000"
aasta = int(kood[1]+kood[2])+2000
kuu = int(kood[4])
paev = int(kood[5]+kood[6])

import datetime

fe = datetime.datetime(aasta, kuu, paev)
se = datetime.datetime(int(today.strftime(" %Y")), int(today.strftime(" %m")), int(today.strftime(" %d")))

difference_in_years = relativedelta(se, fe).years
print(difference_in_years)
