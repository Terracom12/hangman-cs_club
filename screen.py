import os

def drawUI(word_state, lives, letters_tried):
    os.system('cls' if os.name == 'nt' else 'clear') # this is sexy
    drawTitle()
    drawMan(lives)
    drawWord(word_state)
    drawLetters(letters_tried)

def drawTitle():
    with open("hangman.txt") as f:
        lines = f.readlines();
        for line in lines:
            print(line, end = "");

def drawMan(lives):
    with open("lives-" + str(lives)) as f:
        lines = f.readlines();
        for line in lines:
            print(line, end = "")
        print("\n")

def drawWord(word_state):
    outstr = ""
    for l in word_state:
        #outstr += l;
        print(l, end=" ")
    print("\n")

#def drawLetters(letters_tried):
#    print("Tried Letters:")
#    i = 0
#    while i < 26:
#        for n in range(0, 13):
#            if i < 26:
#                print(letters_tried[i], end = " ")
#            else break

def drawLetters(letters_tried):
    print("Letters Tried:")
    for l in letters_tried:
        print(l, end = " ")
    print()

#for i in range(0, 7):
#    drawUI(word_state, 6 - i, letters_tried)
#    time.sleep(1)

#drawUI(word_state, lives, letters_tried)
