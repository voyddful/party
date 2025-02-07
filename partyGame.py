import random
import math
games = ['number guesser', "rock paper scissors", "silksong", 'quizzard']

def partyGame():
    print("Welcome to the party game!")
    print("Here are the games you can play!")
    for game in games:
        print(game)
    choice = input("What game would you like to play?")
    if choice == "number guesser":
        NumberGuesser()
    elif choice == "rock paper scissors":
        RockPaperScissors()
    elif choice == "silksong":
        print("This game is currently in development it wil release early 20025!")
    elif choice == "quizzard":
        quizzard()
    else:
        print("That is not a valid game! please choose a game from the list!")
        partyGame()

def quizzard():
    print("Welcome to Quizzard!")
    print("This is a quiz game where you will be asked a series of questions and you will have to answer them!")
    difficulty = input("What Subject would you like? Math, Science, or History?")
    multiplayer = input("Would you like to play 2p multiplayer? yes or no?")
    match multiplayer:
        case "yes" | "Yes" | "Y" | "y":
            multiplayer = True
        case "no" | "No" | "N" | "n":
            multiplayer = False
    match difficulty:
        case "math" | "Math" | "M" | "m":
            subject = "math"
        case "science" | "Science" | "S" | "s":
            subject = "science"
        case "history" | "History" | "H" | "h":
            subject = "history"
        case "random" | "Random" | "R" | "r":
            subject = random.choice(["math", "science", "history"])
    questions = {
        "math": {
            "subjects": ["Algebra", "Geometry"],
            "Algebra": ["What is x if 5x = 120?", "what is x if 3x + 5 = 20?", "what is x if 2x + 3 = 7?", "what is x if x^2 = 25?", "what is x if x^4 + 5 = 21?"],
            "AlgebraAnswers": [24, 5, 2, 5, 2],
            "Geometry": ["What is the area of a square with side length 5?", "What is the area of a triangle with base 4 and height 3?", "What is the volume of a cube with side length 4?", "What is the perimeter of a rectangle with length 10 and width 5?", "What is the volume of a cube with side length 3?"],
            "GeometryAnswers": [25, 6, 64, 30, 27],
        },
        "science": {
            "subjects": ["Biology", "Chemistry"],
            "Biology": ["What is the powerhouse of the cell?", "What is the process of plants making food called?", "What is the process of animals breaking down food called?", "What is the process of plants making oxygen called?", "What is the process of animals making carbon dioxide called?"],
            "BiologyAnswers": ["Mitochondria", "Photosynthesis", "Digestion", "Respiration", "Exhalation"],
            "Chemistry": ["What is the process of a solid turning into a liquid called?", "What is the process of a liquid turning into a gas called?", "What is the process of a gas turning into a liquid called?", "What is the process of a liquid turning into a solid called?", "What is the process of a solid turning into a gas called?"],
            "ChemistryAnswers": ["Melting", "Evaporation", "Condensation", "Freezing", "Sublimation"],
        
    },
        "history": {
            "subjects": ["US History", "World History"],
            "US History": ["What year was the Declaration of Independence signed?", "What year did the Civil War end?", "What year did the Revolutionary War end?", "What year did the US enter WW2?", "What year did the US enter WW1?"],
            "US HistoryAnswers": [1776, 1865, 1783, 1941, 1917],
            "World History": ["What year did the Berlin Wall fall?", "What year did the Soviet Union collapse?", "What year did the Cold War end?", "What year did the Korean War end?", "What year did the Vietnam War end?"],
            "World HistoryAnswers": [1989, 1991, 1991, 1953, 1975],

        },
        
    }
    points = 0
    p1points = 0
    p2points = 0
    while points < 5:
        if multiplayer == False:
            if subject == "math":
                quest1 = random.choice(questions["math"]["subjects"])
                question = random.choice(questions["math"][quest1])
                answer = questions["math"][f"{quest1}Answers"][questions["math"][quest1].index(question)]
                useranswer = int(input(f"{question}"))
                if useranswer == answer:
                    print("Correct!")
                    points = points + 1
                else:
                    print(f"Incorrect! the answer was {answer}")
            elif subject == "science":
                quest1 = random.choice(questions["science"]["subjects"])
                question = random.choice(questions["science"][quest1])
                answer = questions["science"][f"{quest1}Answers"][questions["science"][quest1].index(question)]
                useranswer = (input(f"{question}"))
                if useranswer == answer:
                    print("Correct!")
                    points = points + 1
                else:
                    print(f"Incorrect! the answer was {answer}")
            elif subject == "history":
                quest1 = random.choice(questions["history"]["subjects"])
                question = random.choice(questions["history"][quest1])
                answer = questions["history"][f"{quest1}Answers"][questions["history"][quest1].index(question)]
                useranswer = int(input(f"{question}"))
                if useranswer == answer:
                    print("Correct!")
                    points = points + 1
                else:
                    print(f"Incorrect! the answer was {answer}")
            if points == 5:
                print("You win! you beat the single player quiz!")   

        elif multiplayer == True:
            if subject == "math":
                quest1 = random.choice(questions["math"]["subjects"])
                question = random.choice(questions["math"][quest1])
                answer = questions["math"][f"{quest1}Answers"][questions["math"][quest1].index(question)]
                useranswer = int(input(f"p1: {question}"))
                useranswer2 = int(input(f"p2: {question}"))
                if useranswer == answer:
                    print("Player 1 is Correct!")
                    p1points = p1points + 1
                else:
                    print(f"Player 1 is Incorrect! the answer was {answer}")
                if useranswer2 == answer:
                    print("Player 2 is Correct!")
                    p2points = p2points + 1
                else:
                    print(f"Player 2 is Incorrect! the answer was {answer}")
            elif subject == "science":
                quest1 = random.choice(questions["science"]["subjects"])
                question = random.choice(questions["science"][quest1])
                answer = questions["science"][f"{quest1}Answers"][questions["science"][quest1].index(question)]
                useranswer = input(f"p1: {question}")
                useranswer2 = input(f"p2: {question}")
                if useranswer == answer:
                    print("Player 1 is Correct!")
                    p1points = p1points + 1
                else:
                    print(f"Player 1 is Incorrect! the answer was {answer}")
                if useranswer2 == answer:
                    print("Player 2 is Correct!")
                    p2points = p2points + 1
                else:
                    print(f"Player 2 is Incorrect! the answer was {answer}")
            elif subject == "history":
                quest1 = random.choice(questions["history"]["subjects"])
                question = random.choice(questions["history"][quest1])
                answer = questions["history"][f"{quest1}Answers"][questions["history"][quest1].index(question)]
                useranswer = int(input(f"p1: {question}"))
                useranswer2 = int(input(f"p2: {question}"))
                if useranswer == answer:
                    print("Player 1 is Correct!")
                    p1points = p1points + 1
                else:
                    print(f"Player 1 is Incorrect! the answer was {answer}")
                if useranswer2 == answer:
                    print("Player 2 is Correct!")
                    p2points = p2points + 1
                else:
                    print(f"Player 2 is Incorrect! the answer was {answer}")
            if p1points == 5:
                print("Player 1 wins! they beat the multiplayer quiz!")
                points = 5
            elif p2points == 5:
                print("Player 2 wins! they beat the multiplayer quiz!")
                points = 5

def NumberGuesser():
    print("Welcome to number guesser!")
    difficulty = input("What difficulty would you like? easy, normal, hard, or impossible?")
    match difficulty:
        case "easy" | "Easy" | "E" | "e":
            randnum = random.randint(1, 10)
            hint = True
            tries = 5
            range = "your range is 1 through 10"
        case "normal" | "Normal" | "N" | "n" | "norm" | "Norm":
            randnum = random.randint(1, 50)
            hint = True
            tries = 5
            range = "your range is 1 through 50"
        case "hard" | "Hard" | "H" | "h":
            randnum = random.randint(1, 100)
            hint = True
            tries = 10
            range = "your range is 1 through 100"
        case "impossible" | "Impossible" | "I" | "i" | "Imp" | "imp":
            randnum = random.randint(1, 1000)
            hint = False
            tries = 10
            range = "your range is 1 through 1000"
    win = False
    while tries > 0 and win == False:
        guess = int(input(f"Guess your first number! you have {tries} tries left! {range} "))
        
        if guess > randnum and hint == True:
            print("Incorrect! you're too high! bring it down!")
            tries = tries - 1
        elif guess < randnum and hint == True:
            print("Incorrect! you're too low! bring it up!")
            tries = tries - 1
        elif (guess > randnum and hint == False) or (guess < randnum and hint == False):
            print("Incorrect! try again!")
            tries = tries - 1
        elif guess == randnum:
            print(f"You win! you beat {difficulty} mode!")
            win = True
    if tries == 0:
        print(f"you lose, you ran out of tries! the number was {randnum}")

def RockPaperScissors():
    pscore = 0
    cscore = 0
    print("Welcome to Rock Paper Scissors!")
    difficulty = int(input("how many rounds would you like? 1, 3, 5, or 7?"))
    difficulty2 = difficulty
    win = False
    while win == False:
        player = input("Rock, Paper, or Scissors?").upper()
        computer = random.choice(["Rock", "Paper", "Scissors"])
        
        if player == "Rock" and computer == "Rock":
            print("Tie! you both chose rock!")
            difficulty = difficulty + 1
            print(f"your score: {pscore} computer score: {cscore}")
        elif player == "Rock" and computer == "Paper":
            print("You lose! the computer chose paper!")
            cscore = cscore + 1
            print(f"your score: {pscore} computer score: {cscore}")
        elif player == "Rock" and computer == "Scissors":
            print("You win! the computer chose scissors!")
            pscore = pscore + 1
            print(f"your score: {pscore} computer score: {cscore}")
        elif player == "Paper" and computer == "Rock":
            print("You win! the computer chose rock!")
            pscore = pscore + 1
            print(f"your score: {pscore} computer score: {cscore}")
        elif player == "Paper" and computer == "Paper":
            print("Tie! you both chose paper!")
            difficulty = difficulty + 1
            print(f"your score: {pscore} computer score: {cscore}")
        elif player == "Paper" and computer == "Scissors":
            print("You lose! the computer chose scissors!")
            cscore = cscore + 1
            print(f"your score: {pscore} computer score: {cscore}")
        elif player == "Scissors" and computer == "Rock":
            print("You lose! the computer chose rock!")
            cscore = cscore + 1
            print(f"your score: {pscore} computer score: {cscore}")
        elif player == "Scissors" and computer == "Paper":
            print("You win! the computer chose paper!")
            pscore = pscore + 1
            print(f"your score: {pscore} computer score: {cscore}")
        elif player == "Scissors" and computer == "Scissors":
            print("Tie! you both chose scissors!")
            difficulty = difficulty + 1
            print(f"your score: {pscore} computer score: {cscore}")
        difficulty = difficulty - 1
        if pscore == math.ceil((difficulty2)/2):
            print("You win! you beat the computer!")
            win = True
        elif cscore == math.ceil((difficulty2)/2):
            print("You lose! you lost to the computer!")
            win = True
while True:

    partyGame()