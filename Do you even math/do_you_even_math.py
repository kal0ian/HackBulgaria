from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
import random

Base = declarative_base()


class Player(Base):
    __tablename__ = "players"
    id = Column(Integer, primary_key=True)
    username = Column(String)
    maxScore = Column(Integer)

engine = create_engine("sqlite:///do_you_even_math.db")
Base.metadata.create_all(engine)

session = Session(bind=engine)
session.commit()


def start():
    name = input("Enter your playername> ")
    player = session.query(Player).filter(Player.username == name).all()

    if player:
        pass
    else:
        player = Player(username=name, maxScore=0)
        session.add(player)
        session.commit()

    print("Welcome ", name, "! Let the game begin!")
    correct = True
    countQuestions = 0
    operations = ["*", "-", "+", "^"]
    while correct:
        countQuestions += 1
        random1 = random.randint(1, 10)
        random2 = random.randint(1, 10)
        op = random.randint(0, 3)
        expectAnswer = 0
        print("Question #", countQuestions, ":")
        print("What is the answer to", random1, operations[op], random2, "?")
        answer = input("?>")
        answer = int(answer)
        if op == 0:
            expectAnswer = random1 * random2
        if op == 1:
            expectAnswer = random1 - random2
        if op == 2:
            expectAnswer = random1 + random2
        if op == 3:
            expectAnswer = random1 ** random2
        if expectAnswer == answer:
            print("Correct!")
        else:
            print(
                "Incorrect! Ending game. You score is: ", (countQuestions - 1) ** 2)
            correct = False
    addScore(name, countQuestions)


def addScore(name, countQuestions):
    score = (countQuestions - 1) ** 2
    players = session.query(Player).filter(Player.username == name).all()
    for player in players:
        if player.maxScore < score:
            session.query(Player).filter(
                Player.username == name).update({'maxScore': score})
            session.commit()


def highscores():
    print("This is the current top10:")
    all_players = session.query(Player).order_by(Player.maxScore.desc())
    count = 0
    for player in all_players:
        count += 1
        print(count, ".", " ", player.username, " with ", player.maxScore)
        if count == 10:
            break


def main():
    print(
        "Welcome to the \"Do you even math?\" game!")
    choise = ""
    while choise != "exit":
        print("Here are your options:\n- start\n- highscores\n- exit")
        choise = input("?> ")
        if choise == "start":
            start()
        if choise == "highscores":
            highscores()


if __name__ == '__main__':
    main()
