import datetime
import locale
now = datetime.datetime.now()
print ("Current date and time : ")
print (now.strftime("%d %B %Y"))
'''##################################'''
locale.setlocale(locale.LC_TIME, 'et_ET') 
today = datetime.datetime.now()
print(today.strftime("%d %B %Y"))

kood = int(input(((((('siset aisiku kood:')))))))
