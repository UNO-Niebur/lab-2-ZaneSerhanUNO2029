#FutureTime.py
#Name: Zane Serhan
#Date: 1/28/2026
#Assignment: Lab2 Future Time

# datetime will allow us to access the system date and time.
import datetime

def main():

  now = datetime.datetime.now()
  currentHour = (now.hour + 6)
  currentMinute = now.minute
  #Ask user for hours
  askhours = int(input("Enter the number of hours to add   "))
  #Ask user for minutes
  askmins = int(input("Enter the number of minutes to add   "))
  #Calculate the time after the user-supplied time has passed.
  futuremins = (currentMinute + askmins) % 60
  timefixhour = (currentMinute + askmins) // 60
  futurehour = (currentHour + askhours + timefixhour) % 24
  futurehour12 = futurehour % 12
  futurehourdisplay = (futurehour12 + 11) % 12 + 1
  print("The future time is {:02d}:{:02d}".format(futurehourdisplay, futuremins))
  #Do not use any if statements in calculating the time.

  #Output the future time in standard format "HH:MM"


if __name__ == '__main__':
  main()
