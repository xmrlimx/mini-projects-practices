from playsound import playsound
from datetime import datetime
import pause

def alarm_():
    now = datetime.now()
    this_year = int(now.strftime('%Y'))
    this_month = int(now.strftime('%m'))
    this_date = int(now.strftime('%d'))

    hour = int(input('Nhập giờ vào đi em: '))
    mins = int(input('Nhập phút vào đi em: '))
    secs = 00

    pause.until(datetime(this_year, this_month, this_date, hour, mins, secs))
    playsound(r'M:\\Muzik\Stronger.mp3')

alarm_()