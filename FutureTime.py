#FutureTime.py
#Name:
#Date:
#Assignment:

# datetime will allow us to access the system date and time.
import datetime

def main():

  now = datetime.datetime.now()

  currentHour = (now.hour + 6)

  currentMinute = now.minute
  #Ask user for hours

  askhours = int(input("Enter the number of hours to add"))
  
  #Ask user for minutes
  askmins = int(input("Enter the number of minutes to add"))
  #Calculate the time after the user-supplied time has passed.
  futuremins = (currentMinute + askmins) % 60
  timefix = (currentMinute + askmins) // 60
  #Do not use any if statements in calculating the time.

  #Output the future time in standard format "HH:MM"


if __name__ == '__main__':
  main()
