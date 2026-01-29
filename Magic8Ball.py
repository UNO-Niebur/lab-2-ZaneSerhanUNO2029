#Magic8Ball.py
#Name:Zane Serhan
#Date: 1/28/2026
#Assignment: Lab2 Magic 8 Ball

#We will need random for this program, import to use this package.
import random

def main():

  print("Magic 8 Ball")
#Create a list of your responses.
answers = ["It is certain.",
    "It is decidedly so.",
    "Without a doubt.",
    "Yes, most definitely.",
    "You may rely on it.",
    "As I see it, yes.",
    "Most likely.",
    "Outlook good.",
    "Yes.",
    "Signs point to yes.",
    "Reply hazy, try again.",
    "Ask again later.",
    "Better not tell you now.",
    "Cannot predict now.",
    "Concentrate and ask again.",
    "Don't count on it.",
    "My reply is no.",
    "My sources say no.",
    "Outlook not so good.",
    "Very doubtful."]

#Prompt the user for their question.
question = input("Ask the Magic 8 Ball a question    ")
#Answer question randomly with one of the options from your earlier list.
response = random.choice(answers)
print("Response is:", response)

if __name__ == '__main__':
  main()
