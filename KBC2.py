import random

print("Kaun Banega Crorepati mein aap ka swagat hai!")

questions = [
    ["The International Literacy Day is observed on", "Sep 8", "Nov 28", "Jan 6", "Feb 14"],
    ["The language of Lakshadweep, a Union Territory of India, is", "Malayalam", "Hindi", "Tamil", "Telugu"],
    ["Which of the following is observed as Sports Day every year?", "22nd April", "26th July", "29th August", "2nd October"],
    ["Bahubali festival is related to", "Jainism", "Hinduism", "Buddhism", "Islam"],
    ["Which day is observed as the World Standards Day?", "June 26", "Oct 14", "Nov 15", "Dec 2"],
    ["Which of the following was the theme of the World Red Cross and Red Crescent Day?", "Dignity for all - focus on women", "Dignity for all - focus on Children", "Focus on health for all", "Nourishment for all - focus on children"],
    ["September 27 is celebrated every year as", "Teachers' Day", "National Integration Day", "World Tourism Day", "International Literacy Day"]
]

def kbc():
    sum = 0
    p = 1
    life = 3
    asked_questions = []

    while life > 0 and len(questions) > 0:
        question = random.choice(questions)
        if question in asked_questions:
            continue

        asked_questions.append(question)

        print(question[0])
        for i in range(1, 5):
            print(f"{i}. {question[i]}")

        answer = input("Write your answer: ")

        if answer == question[1]:
            print("Sahi Jawab!")
            sum = sum + p
            print("Aap jeet chuke hain", sum, "Crore")
        else:
            print("Ghalat Jawab!")
            life = life - 1
            print("Your remaining lives are:", life)
    
    if life == 0:
        print("Aapka khel samapt hua. Aap jeet chuke hain", sum, "Crore")
    elif len(questions) == 0:
        print("Aapka khel samapt hua. Aap jeet chuke hain", sum, "Crore")

kbc()
# question = random.choice(questions)
# asked_questions =[]
# print(asked_questions.append(question))