from datetime import datetime
from datetime import date

time_now = datetime.now()
time = time_now.strftime("%H %M %S")
date = date.today()

print time
print date
