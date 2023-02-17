from random import randint

list_choice = ["Rock", "Paper", "Scissors"]

class player:
    def __init__(self):
        self.choice = "None"
        self.score = 0

    def get_input(self, choice, run):
        z = 0
        for x in range(3):
            if choice == list_choice[x]:
                z = 1
        if z == 0:
            print("Wrong input")
            run = False
            return run
        if z == 1:
            print("Input accepted")
            self.choice = choice
            return run

    def return_choice(self):
        return self.choice
    
    def check(self, computer_choice):
        if self.choice != "None":
            if self.choice == "Rock" and computer_choice == "Rock":
                self.score = self.score + 0
                print("Tie")
            if self.choice == "Rock" and computer_choice == "Scissors":
                self.score = self.score + 1
                print("You Won")
            if self.choice == "Rock" and computer_choice == "Paper":
                self.score == self.score - 1
                print("You Lost")
            if self.choice == "Scissors" and computer_choice == "Scissors":
                self.score = self.score + 0
                print("Tie")
            if self.choice == "Scissors" and computer_choice == "Paper":
                self.score == self.score + 1
                print("You Won")
            if self.choice == "Scissors" and computer_choice == "Rock":
                self.score == self.score - 1
                print("You Lost")
            if self.choice == "Paper" and computer_choice == "Paper":
                self.score = self.score + 0
                print("Tie")
            if self.choice == "Paper" and computer_choice == "Rock":
                self.score == self.score + 1
                print("You Won")
            if self.choice == "Paper" and computer_choice == "Scissors":
                self.score == self.score - 1
                print("You LOst")


    def return_score(self):
        return self.score

player = player()   
run = True
while run:
    run = player.get_input(input("Enter your choice: "), run)
    if run == True:
        computer_choice = list_choice [randint(0,2)]
        print (f"the computer choice is: {computer_choice}")
        player.check(computer_choice)
    print(player.return_score())
