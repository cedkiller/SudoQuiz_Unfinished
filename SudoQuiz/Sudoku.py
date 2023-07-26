# import pygame library
import pygame

from pygame import mixer
pygame.init()
# initialise the pygame font
pygame.font.init()

# Total window
screen = pygame.display.set_mode((1280, 950))

# Title and Icon
pygame.display.set_caption("SUDOQUIZ")
icon = pygame.image.load("C:\\SudoQuiz\\icon.png")
pygame.display.set_icon(icon)


wr = 0
wr1 = 0
wr2 = 0
wr3 = 0
wr4 = 0
wr5 = 0
wr6 = 0
wr7 = 0
wr8 = 0
wr9 = 0
box = 0
wrong = 0
levels = 0
text = 0
p1 = 0
img = pygame.image.load("C:\\SudoQuiz\\start.png")
imgx = 780
imgy = 0
button = pygame.Rect(595,170,110,60)
button2 = pygame.Rect(595,250,110,60)
button3 = pygame.Rect(595,330,110,60)
mixer.music.load("C:\\SudoQuiz\\Sounds\\Canon in D - Pachelbel.mp3")
mixer.music.play(-1)
music = mixer.Sound("C:\\SudoQuiz\\Sounds\\mixkit-arcade-game-jump-coin-216.wav")
wins = mixer.Sound("C:\\SudoQuiz\\Sounds\\mixkit-ethereal-fairy-win-sound-2019.wav")
los = mixer.Sound("C:\\SudoQuiz\\Sounds\\mixkit-horror-lose-2028.wav")


x = 0
y = 0
dif = 500 / 9
val = 0
# Default Sudoku Board.
grid = [
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0]
                ]


# Load test fonts for future use
font1 = pygame.font.SysFont("comicsans", 40)
font2 = pygame.font.SysFont("comicsans", 20)
font3 = pygame.font.SysFont("comicsans", 37)
font4 = pygame.font.SysFont("comicsans", 30)


def get_cord(pos):
    global x
    x = pos[0] // dif
    global y
    y = pos[1] // dif


# Highlight the cell selected
def draw_box():
    for i in range(2):
        pygame.draw.line(screen, (255, 0, 0), (x * dif - 3, (y + i) * dif), (x * dif + dif + 3, (y + i) * dif), 7)
        pygame.draw.line(screen, (255, 0, 0), ((x + i) * dif, y * dif), ((x + i) * dif, y * dif + dif), 7)


# Function to draw required lines for making Sudoku grid
def draw():
    # Draw the lines

    for i in range(9):
        for j in range(9):
            if grid[i][j] != 0:
                # Fill blue color in already numbered grid
                pygame.draw.rect(screen, (0, 153, 153), (i * dif, j * dif, dif + 1, dif + 1))

                # Fill grid with default numbers specified
                text1 = font1.render(str(grid[i][j]), 1, (0, 0, 0))
                screen.blit(text1, (i * dif + 15, j * dif + 5))
    # Draw lines horizontally and verticallyto form grid
    for i in range(10):
        if i % 3 == 0:
            thick = 7
        else:
            thick = 1
        pygame.draw.line(screen, (0, 0, 0), (0, i * dif), (500, i * dif), thick)
        pygame.draw.line(screen, (0, 0, 0), (i * dif, 0), (i * dif, 500), thick)


# Fill value entered in cell
def draw_val(val):
    text1 = font1.render(str(val), 1, (0, 0, 0))
    screen.blit(text1, (x * dif + 15, y * dif + 5))


# Raise error when wrong value entered
def raise_error1(wrong, box, wr):
    text1 = font1.render("Wrong Try Again!", 1, (0, 0, 0))
    screen.blit(text1, (470, 520))

    w = 9 - wr
    percent = int(((box - wrong)/ box) * 100)
    math = int(((9 - w) / 9) * 100)
    text2 = font1.render("Your Logical Reasoning Percent is "+str(percent)+"%", 1, (0, 0, 0))
    screen.blit(text2, (290, 570))

    text4 = font1.render("Your Problem Solving Skill Percent is "+str(math)+"%", 1, (0, 0, 0))
    screen.blit(text4, (290, 620))

    text3 = font3.render("Do you want to try again? Press 'Y' to try again and 'N' to quit the game", 1, (0, 0, 0))
    screen.blit(text3, (30, 670))


def raise_error2():
    text1 = font1.render("Wrong !!! Not a valid Key", 1, (0, 0, 0))
    screen.blit(text1, (20, 570))


# Check if the value entered in board is valid
def valid(m, i, j, val):
    for it in range(9):
        if m[i][it] == val:
            return False
        if m[it][j] == val:
            return False
    it = i // 3
    jt = j // 3
    for i in range(it * 3, it * 3 + 3):
        for j in range(jt * 3, jt * 3 + 3):
            if m[i][j] == val:
                return False
    return True


# Solves the sudoku board using Backtracking Algorithm
def solve(grid, i, j):
    while grid[i][j] != 0:
        if i < 8:
            i += 1
        elif i == 8 and j < 8:
            i = 0
            j += 1
        elif i == 8 and j == 8:
            return True
    pygame.event.pump()
    for it in range(1, 10):
        if valid(grid, i, j, it) == True:
            grid[i][j] = it
            global x, y
            x = i
            y = j
            # white color background\
            screen.fill((255, 255, 255))
            draw()
            draw_box()
            pygame.display.update()
            pygame.time.delay(20)
            if solve(grid, i, j) == 1:
                return True
            else:
                grid[i][j] = 0
            # white color background\
            screen.fill((255, 255, 255))

            draw()
            draw_box()
            pygame.display.update()
            pygame.time.delay(50)
    return False


# Display instruction for the game
def instruction(text, p1):
    text1 = font1.render("SQ", 1, (0, 0, 0))
    text2 = font1.render("Level: "+str(levels), 1, (0, 0, 0))
    screen.blit(text1, (610, 30))
    screen.blit(text2, (580, 80))

    if text == 0:
        text3 = font1.render("Welcome to SudoQuiz Press 'S' to start!", 1, (0, 0, 0))
        screen.blit(text3, (270, 520))
    elif text == 4:
        info1 = font1.render("Help", 1,(0, 0, 0))
        info2 = font2.render("lvl 1-10 ( only +, -, ÷, × ) ", 1, (0, 0, 0))
        info3 = font2.render(": 1-6 ( + and - )", 1, (0, 0, 0))
        info5 = font2.render(": 7-8 ( +, -, × )", 1, (0, 0, 0))
        info6 = font2.render(": 9-10 ( +, -, ×, ÷ )", 1, (0, 0, 0))
        info7 = font2.render("lvl 11-20 ( with power and square root )", 1, (0, 0, 0))
        info8 = font2.render(": 11-15 ( +, -, ×, ÷, and power ex. (²,³,⁴, and etc. )", 1, (0, 0, 0))
        info9 = font2.render(": 16-20 ( all with power and square root )", 1, (0, 0, 0))
        info10 = font2.render("lvl 21-30 ( mathematical equation with existing variables )", 1, (0, 0, 0))
        info11 = font2.render(": 21-30", 1, (0, 0, 0))
        info12 = font2.render("example:", 1, (0, 0, 0))
        info13 = font2.render("if x = 4 and y = 3", 1, (0, 0, 0))
        info14 = font2.render("x+3+y = 9", 1, (0, 0, 0))
        screen.blit(info1, (600, 520))
        screen.blit(info2, (0, 570))
        screen.blit(info3, (0, 590))
        screen.blit(info5, (0, 610))
        screen.blit(info6, (0, 630))
        screen.blit(info7, (0, 670))
        screen.blit(info8, (0, 690))
        screen.blit(info9, (0, 710))
        screen.blit(info10, (0, 750))
        screen.blit(info11, (0, 790))
        screen.blit(info12, (0, 830))
        screen.blit(info13, (0, 850))
        screen.blit(info14, (0, 890))
    elif text == 5:
        help1 = font1.render("Information", 1, (0, 0, 0))
        help2 = font2.render("Sudoku is played on a grid of 9 x 9 spaces. Within the rows and columns are 9 “squares” (made up", 1, (0, 0, 0))
        help3 = font2.render("of 3 x 3 spaces). Each row, column and square (9 spaces each) needs to be filled out with the ", 1, (0, 0, 0))
        help4 = font2.render("numbers 1-9, without repeating any numbers within the row, column or square.", 1, (0, 0, 0))
        help5 = font2.render("As additions, the game was twisted in to the next level, you must first execute some sort of ", 1, (0, 0, 0))
        help6 = font2.render("mathematical equation to fill up the right number in the box. Every level have a different ", 1, (0, 0, 0))
        help7 = font2.render("equation need to solve.", 1, (0, 0, 0))
        help8 = font2.render("Press 'Enter' after solving the puzzle to identify the items!", 1, (0, 0, 0))
        screen.blit(help1, (530, 520))
        screen.blit(help2, (0, 570))
        screen.blit(help3, (0, 590))
        screen.blit(help4, (0, 610))
        screen.blit(help5, (0, 650))
        screen.blit(help6, (0, 670))
        screen.blit(help7, (0, 690))
        screen.blit(help8, (0, 730))
    if p1 == 1:
        text4 = font2.render("Answer Here", 1, (0, 0, 0))
        text5 = font2.render("Math Quiz", 1, (0, 0, 0))
        screen.blit(text4, (190, 500))
        screen.blit(text5, (980, 500))

# Display options when solved
def result(wrong, box, wr):
    text1 = font1.render("Good Job! You solve it!", 1, (0, 0, 0))
    text2 = font1.render("Congrats now you have level up!", 1, (0, 0, 0))
    text3 = font1.render("Press 'E' to proceed to the next level!", 1, (0, 0, 0))
    screen.blit(text1, (450, 520))
    screen.blit(text2, (330, 670))
    screen.blit(text3, (290, 720))

    w = 9 - wr
    percent = int(((box - wrong) / box) * 100)
    math = int(((9 - w) / 9) * 100)
    text4 = font1.render("Your Logical Reasoning Percent is "+str(percent)+"%", 1, (0, 0, 0))
    screen.blit(text4, (290, 570))
    text5 = font1.render("Your Problem Solving Skill Percent is "+str(math)+"%", 1, (0, 0, 0))
    screen.blit(text5, (290, 620))


run = True
flag1 = 0
flag2 = 0
rs = 0
error = 0
btext = font1.render("info", 1, (0, 0, 0))
btext2 = font1.render("help", 1, (0, 0, 0))
btext3 = font1.render("exit", 1, (0, 0, 0))
# The loop thats keep the window running
while run:
    # White color background
    screen.fill((255, 255, 255))
    # Loop through the events stored in event.get()
    for event in pygame.event.get():
        # Quit the game window
        if event.type == pygame.QUIT:
            run = False
        # Get the mouse position to insert number
        if event.type == pygame.MOUSEBUTTONDOWN:
            flag1 = 1
            pos = pygame.mouse.get_pos()
            get_cord(pos)
            if button.collidepoint(event.pos):
                text = 5
            if button2.collidepoint(event.pos):
                text = 4
            if button3.collidepoint(event.pos):
                pygame.quit()
        # Get the number to be inserted if key pressed
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x -= 1
                flag1 = 1
            if event.key == pygame.K_RIGHT:
                x += 1
                flag1 = 1
            if event.key == pygame.K_UP:
                y -= 1
                flag1 = 1
            if event.key == pygame.K_DOWN:
                y += 1
                flag1 = 1
            if event.key == pygame.K_1:
                val = 1
            if event.key == pygame.K_2:
                val = 2
            if event.key == pygame.K_3:
                val = 3
            if event.key == pygame.K_4:
                val = 4
            if event.key == pygame.K_5:
                val = 5
            if event.key == pygame.K_6:
                val = 6
            if event.key == pygame.K_7:
                val = 7
            if event.key == pygame.K_8:
                val = 8
            if event.key == pygame.K_9:
                val = 9
            if event.key == pygame.K_RETURN:
                flag2 = 1
            # If R pressed clear the sudoku board
            if event.key == pygame.K_r:
                rs = 0
                error = 0
                flag2 = 0
                grid = [
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0]
                ]
            # If D is pressed reset the board to default
            if event.key == pygame.K_d:
                text = 10
            if event.key == pygame.K_e:
                rs = 0
                error = 0
                flag2 = 0
                wrong = 0
                wr = 0
                levels = levels + 1
                if levels == 1:
                    wrong = 0
                    box = 33
                    grid = [
                    [3, 0, 5, 4, 0, 2, 0, 6, 0],
                    [4, 9, 0, 7, 6, 0, 1, 0, 8],
                    [6, 0, 0, 1, 0, 3, 2, 4, 5],
                    [0, 0, 3, 9, 0, 0, 5, 8, 0],
                    [9, 6, 0, 0, 5, 8, 7, 0, 3],
                    [0, 8, 1, 3, 0, 4, 0, 9, 2],
                    [0, 5, 0, 6, 0, 1, 4, 0, 0],
                    [2, 0, 0, 5, 4, 9, 0, 7, 0],
                    [1, 4, 9, 0, 0, 7, 3, 0, 6]
                ]
                elif levels == 2:
                    wr = 0
                    wrong = 0
                    box = 34
                    wr1 = 0
                    wr2 = 0
                    wr3 = 0
                    wr4 = 0
                    wr5 = 0
                    wr6 = 0
                    wr7 = 0
                    wr8 = 0
                    wr9 = 0
                    img = pygame.image.load("C://SudoQuiz//easy//lvl_2.png")
                    grid = [
                    [0, 5, 0, 3, 1, 4, 0, 6, 0],
                    [8, 7, 0, 0, 0, 9, 4, 0, 3],
                    [6, 4, 3, 5, 0, 7, 1, 9, 2],
                    [0, 0, 7, 8, 0, 5, 2, 1, 0],
                    [4, 1, 0, 9, 0, 0, 0, 0, 0],
                    [0, 2, 5, 0, 6, 1, 9, 0, 7],
                    [7, 9, 0, 2, 5, 0, 8, 4, 0],
                    [0, 0, 4, 0, 9, 6, 0, 0, 5],
                    [0, 3, 0, 1, 0, 8, 6, 7, 0]
                    ]
                elif levels == 3:
                    wr1 = 0
                    wr2 = 0
                    wr3 = 0
                    wr4 = 0
                    wr5 = 0
                    wr6 = 0
                    wr7 = 0
                    wr8 = 0
                    wr9 = 0
                    wr = 0
                    wrong = 0
                    box = 38
                    img = pygame.image.load("C://SudoQuiz//easy//lvl_3.png")
                    grid = [
                    [0, 0, 0, 0, 4, 0, 3, 0, 9],
                    [0, 6, 0, 2, 5, 8, 4, 0, 1],
                    [1, 7, 4, 0, 6, 9, 0, 8, 2],
                    [6, 0, 0, 8, 0, 5, 0, 0, 0],
                    [7, 4, 1, 9, 3, 0, 0, 5, 0],
                    [5, 0, 8, 0, 0, 4, 0, 3, 6],
                    [2, 0, 0, 0, 0, 1, 0, 9, 3],
                    [0, 9, 0, 5, 0, 2, 7, 1, 4],
                    [0, 0, 7, 0, 9, 0, 0, 0, 5]
                ]
                elif levels == 4:
                    wr1 = 0
                    wr2 = 0
                    wr3 = 0
                    wr4 = 0
                    wr5 = 0
                    wr6 = 0
                    wr7 = 0
                    wr8 = 0
                    wr9 = 0
                    wr = 0
                    wrong = 0
                    box = 38
                    img = pygame.image.load("C://SudoQuiz//easy//lvl_4.png")
                    grid = [
                    [0, 0, 1, 3, 0, 0, 2, 5, 8],
                    [6, 0, 9, 2, 5, 0, 1, 0, 0],
                    [0, 0, 0, 0, 0, 7, 0, 3, 0],
                    [0, 0, 0, 0, 0, 5, 7, 0, 4],
                    [0, 8, 0, 0, 1, 4, 6, 9, 3],
                    [4, 1, 7, 9, 0, 6, 0, 2, 5],
                    [8, 5, 0, 4, 7, 0, 3, 0, 9],
                    [0, 0, 0, 0, 0, 0, 5, 8, 2],
                    [0, 6, 0, 5, 8, 2, 0, 7, 1]
                ]
                elif levels == 5:
                    wr1 = 0
                    wr2 = 0
                    wr3 = 0
                    wr4 = 0
                    wr5 = 0
                    wr6 = 0
                    wr7 = 0
                    wr8 = 0
                    wr9 = 0
                    wr = 0
                    wrong = 0
                    box = 38
                    img = pygame.image.load("C://SudoQuiz//easy//lvl_5.png")
                    grid = [
                    [6, 0, 0, 9, 0, 0, 0, 3, 0],
                    [0, 4, 0, 6, 5, 7, 0, 0, 1],
                    [9, 1, 8, 0, 0, 4, 5, 6, 0],
                    [0, 8, 6, 1, 0, 0, 0, 0, 5],
                    [0, 5, 3, 7, 6, 0, 9, 1, 2],
                    [0, 2, 9, 0, 3, 5, 0, 0, 0],
                    [0, 0, 7, 0, 0, 0, 4, 0, 6],
                    [2, 0, 0, 0, 4, 6, 7, 8, 9],
                    [5, 6, 0, 8, 0, 0, 0, 2, 3]
                ]
                elif levels == 6:
                    wr1 = 0
                    wr2 = 0
                    wr3 = 0
                    wr4 = 0
                    wr5 = 0
                    wr6 = 0
                    wr7 = 0
                    wr8 = 0
                    wr9 = 0
                    wr = 0
                    wrong = 0
                    box = 38
                    img = pygame.image.load("C://SudoQuiz//easy//lvl_6.png")
                    grid = [
                    [8, 0, 0, 0, 1, 0, 6, 0, 3],
                    [7, 0, 4, 3, 0, 6, 0, 0, 2],
                    [0, 0, 0, 2, 0, 5, 0, 0, 1],
                    [0, 3, 0, 0, 0, 8, 7, 1, 4],
                    [0, 5, 0, 7, 4, 1, 9, 0, 0],
                    [1, 4, 0, 6, 0, 9, 0, 2, 5],
                    [0, 8, 0, 0, 0, 4, 3, 0, 0],
                    [4, 7, 0, 9, 0, 3, 2, 0, 8],
                    [0, 6, 9, 8, 5, 2, 0, 0, 7]
                ]
                elif levels == 7:
                    wr1 = 0
                    wr2 = 0
                    wr3 = 0
                    wr4 = 0
                    wr5 = 0
                    wr6 = 0
                    wr7 = 0
                    wr8 = 0
                    wr9 = 0
                    wr = 0
                    wrong = 0
                    box = 38
                    img = pygame.image.load("C://SudoQuiz//easy//lvl_7.png")
                    grid = [
                    [5, 0, 8, 6, 0, 0, 4, 0, 0],
                    [0, 3, 0, 7, 0, 0, 5, 2, 0],
                    [4, 1, 0, 0, 2, 8, 0, 9, 6],
                    [0, 0, 6, 0, 0, 7, 2, 8, 0],
                    [2, 0, 0, 0, 9, 0, 0, 7, 4],
                    [1, 7, 4, 2, 0, 5, 9, 0, 3],
                    [9, 0, 3, 1, 0, 4, 0, 0, 2],
                    [8, 5, 2, 0, 6, 0, 0, 4, 0],
                    [7, 0, 1, 0, 0, 0, 0, 3, 9]
                ]
                elif levels == 8:
                    wr1 = 0
                    wr2 = 0
                    wr3 = 0
                    wr4 = 0
                    wr5 = 0
                    wr6 = 0
                    wr7 = 0
                    wr8 = 0
                    wr9 = 0
                    wr = 0
                    wrong = 0
                    box = 38
                    img = pygame.image.load("C://SudoQuiz//easy//lvl_8.png")
                    grid = [
                    [5, 6, 0, 8, 9, 1, 0, 0, 4],
                    [0, 0, 0, 2, 0, 0, 0, 0, 7],
                    [2, 3, 0, 5, 0, 7, 8, 9, 1],
                    [0, 0, 0, 6, 0, 8, 9, 0, 0],
                    [0, 7, 0, 0, 1, 0, 3, 4, 0],
                    [0, 1, 0, 3, 4, 5, 0, 7, 8],
                    [1, 2, 0, 4, 0, 6, 7, 8, 0],
                    [0, 0, 9, 1, 2, 3, 0, 5, 6],
                    [0, 5, 0, 0, 0, 0, 1, 0, 3]
                ]
                elif levels == 9:
                    wr1 = 0
                    wr2 = 0
                    wr3 = 0
                    wr4 = 0
                    wr5 = 0
                    wr6 = 0
                    wr7 = 0
                    wr8 = 0
                    wr9 = 0
                    wr = 0
                    wrong = 0
                    box = 38
                    img = pygame.image.load("C://SudoQuiz//easy//lvl_9.png")
                    grid = [
                    [0, 3, 6, 0, 0, 0, 2, 5, 8],
                    [8, 2, 5, 0, 0, 9, 1, 4, 7],
                    [1, 4, 0, 5, 0, 2, 3, 0, 9],
                    [0, 9, 3, 0, 4, 0, 8, 0, 0],
                    [0, 1, 0, 2, 0, 8, 9, 0, 6],
                    [5, 8, 0, 0, 3, 6, 7, 1, 4],
                    [0, 0, 9, 7, 0, 0, 0, 0, 0],
                    [0, 7, 0, 8, 2, 0, 6, 0, 0],
                    [2, 0, 0, 0, 0, 0, 0, 7, 1]
                ]
                elif levels == 10:
                    wr1 = 0
                    wr2 = 0
                    wr3 = 0
                    wr4 = 0
                    wr5 = 0
                    wr6 = 0
                    wr7 = 0
                    wr8 = 0
                    wr9 = 0
                    wr = 0
                    wrong = 0
                    box = 38
                    img = pygame.image.load("C://SudoQuiz//easy//lvl_10.png")
                    grid = [
                    [6, 3, 9, 8, 5, 0, 0, 0, 7],
                    [0, 0, 0, 0, 0, 9, 0, 2, 5],
                    [5, 0, 0, 0, 4, 0, 0, 0, 6],
                    [1, 7, 4, 3, 9, 6, 0, 0, 0],
                    [3, 9, 0, 0, 2, 8, 7, 1, 4],
                    [2, 8, 0, 0, 1, 0, 0, 9, 0],
                    [0, 0, 0, 2, 0, 5, 4, 7, 1],
                    [0, 5, 0, 1, 0, 0, 3, 6, 0],
                    [7, 0, 1, 0, 0, 0, 2, 5, 8]
                ]
                elif levels == 11:
                    wr1 = 0
                    wr2 = 0
                    wr3 = 0
                    wr4 = 0
                    wr5 = 0
                    wr6 = 0
                    wr7 = 0
                    wr8 = 0
                    wr9 = 0
                    wr = 0
                    wrong = 0
                    box = 38
                    grid = [
                    [7, 4, 0, 0, 6, 0, 0, 0, 5],
                    [0, 3, 0, 0, 0, 0, 7, 0, 4],
                    [5, 0, 0, 7, 4, 1, 0, 9, 0],
                    [3, 0, 6, 0, 2, 8, 0, 7, 1],
                    [0, 1, 0, 0, 0, 0, 5, 0, 2],
                    [2, 8, 5, 4, 0, 0, 3, 6, 0],
                    [9, 0, 3, 0, 8, 5, 0, 4, 0],
                    [0, 5, 2, 0, 0, 0, 9, 3, 6],
                    [1, 0, 4, 0, 9, 6, 0, 5, 8]
                ]
                elif levels == 12:
                    wr1 = 0
                    wr2 = 0
                    wr3 = 0
                    wr4 = 0
                    wr5 = 0
                    wr6 = 0
                    wr7 = 0
                    wr8 = 0
                    wr9 = 0
                    wr = 0
                    wrong = 0
                    box = 38
                    grid = [
                    [3, 6, 9, 0, 5, 0, 4, 0, 0],
                    [2, 0, 8, 1, 4, 7, 0, 6, 0],
                    [0, 0, 0, 9, 3, 6, 2, 5, 8],
                    [7, 1, 4, 0, 9, 0, 0, 0, 5],
                    [8, 0, 0, 0, 1, 0, 9, 0, 6],
                    [0, 3, 0, 8, 2, 0, 0, 0, 7],
                    [0, 7, 1, 3, 6, 0, 5, 0, 2],
                    [0, 0, 0, 0, 7, 1, 0, 0, 3],
                    [0, 0, 0, 5, 8, 2, 0, 0, 4]
                ]
                elif levels == 13:
                    wr1 = 0
                    wr2 = 0
                    wr3 = 0
                    wr4 = 0
                    wr5 = 0
                    wr6 = 0
                    wr7 = 0
                    wr8 = 0
                    wr9 = 0
                    wr = 0
                    wrong = 0
                    box = 38
                    grid = [
                    [2, 1, 9, 0, 4, 0, 0, 8, 7],
                    [0, 0, 0, 2, 0, 9, 3, 0, 0],
                    [5, 0, 0, 8, 0, 6, 9, 2, 1],
                    [0, 5, 0, 0, 0, 0, 0, 0, 0],
                    [3, 2, 0, 0, 0, 4, 7, 0, 8],
                    [0, 8, 7, 3, 0, 0, 4, 6, 5],
                    [4, 0, 0, 0, 6, 5, 0, 1, 9],
                    [0, 6, 5, 0, 9, 0, 0, 4, 3],
                    [1, 0, 8, 0, 3, 0, 5, 7, 6]
                ]
                elif levels == 14:
                    wr1 = 0
                    wr2 = 0
                    wr3 = 0
                    wr4 = 0
                    wr5 = 0
                    wr6 = 0
                    wr7 = 0
                    wr8 = 0
                    wr9 = 0
                    wr = 0
                    wrong = 0
                    box = 38
                    grid = [
                    [3, 4, 0, 0, 7, 0, 9, 1, 2],
                    [9, 0, 2, 0, 0, 3, 6, 7, 0],
                    [0, 0, 8, 2, 1, 0, 3, 0, 5],
                    [0, 2, 0, 6, 0, 0, 0, 8, 0],
                    [0, 0, 0, 0, 0, 7, 0, 0, 0],
                    [0, 8, 0, 3, 2, 1, 4, 5, 6],
                    [5, 0, 0, 1, 9, 8, 0, 0, 4],
                    [2, 3, 0, 7, 0, 5, 0, 0, 1],
                    [8, 9, 0, 4, 0, 2, 0, 6, 7]
                ]
                elif levels == 15:
                    wr1 = 0
                    wr2 = 0
                    wr3 = 0
                    wr4 = 0
                    wr5 = 0
                    wr6 = 0
                    wr7 = 0
                    wr8 = 0
                    wr9 = 0
                    wr = 0
                    wrong = 0
                    box = 38
                    grid = [
                    [8, 0, 0, 0, 4, 7, 0, 0, 6],
                    [9, 3, 6, 0, 5, 0, 0, 1, 7],
                    [0, 0, 7, 3, 0, 9, 5, 2, 8],
                    [4, 0, 1, 0, 0, 3, 8, 0, 2],
                    [0, 0, 8, 0, 7, 1, 6, 0, 9],
                    [0, 6, 0, 5, 0, 0, 0, 0, 1],
                    [0, 0, 3, 8, 0, 0, 0, 0, 0],
                    [5, 0, 2, 7, 0, 4, 0, 0, 3],
                    [0, 1, 4, 9, 0, 6, 2, 8, 5]
                ]
                elif levels == 16:
                    wr1 = 0
                    wr2 = 0
                    wr3 = 0
                    wr4 = 0
                    wr5 = 0
                    wr6 = 0
                    wr7 = 0
                    wr8 = 0
                    wr9 = 0
                    wr = 0
                    wrong = 0
                    box = 38
                    grid = [
                    [1, 2, 9, 0, 6, 7, 0, 0, 0],
                    [4, 5, 0, 2, 9, 0, 6, 0, 8],
                    [0, 0, 6, 5, 3, 4, 0, 1, 0],
                    [3, 0, 2, 1, 0, 0, 5, 0, 0],
                    [6, 7, 0, 0, 2, 0, 0, 0, 0],
                    [0, 1, 8, 7, 0, 6, 2, 3, 0],
                    [8, 0, 7, 0, 4, 0, 0, 0, 3],
                    [0, 3, 0, 9, 7, 8, 4, 5, 0],
                    [0, 6, 0, 3, 0, 0, 0, 8, 9]
                ]
                elif levels == 17:
                    wr1 = 0
                    wr2 = 0
                    wr3 = 0
                    wr4 = 0
                    wr5 = 0
                    wr6 = 0
                    wr7 = 0
                    wr8 = 0
                    wr9 = 0
                    wr = 0
                    wrong = 0
                    box = 38
                    grid = [
                    [0, 5, 0, 0, 6, 0, 0, 0, 9],
                    [0, 8, 0, 1, 9, 2, 0, 0, 3],
                    [1, 2, 0, 4, 0, 0, 0, 0, 0],
                    [0, 0, 2, 0, 0, 0, 0, 0, 8],
                    [6, 7, 5, 0, 0, 0, 4, 3, 0],
                    [9, 1, 0, 0, 2, 0, 7, 0, 5],
                    [8, 9, 7, 2, 0, 0, 0, 0, 4],
                    [2, 3, 1, 5, 0, 6, 0, 8, 0],
                    [5, 6, 4, 8, 7, 9, 3, 2, 1]
                ]
                elif levels == 18:
                    wr1 = 0
                    wr2 = 0
                    wr3 = 0
                    wr4 = 0
                    wr5 = 0
                    wr6 = 0
                    wr7 = 0
                    wr8 = 0
                    wr9 = 0
                    wr = 0
                    wrong = 0
                    box = 38
                    grid = [
                    [5, 4, 0, 6, 0, 8, 0, 0, 2],
                    [0, 0, 9, 3, 4, 0, 7, 0, 8],
                    [0, 0, 0, 0, 1, 2, 0, 0, 5],
                    [9, 8, 7, 0, 2, 0, 0, 0, 6],
                    [0, 0, 1, 4, 5, 6, 0, 7, 9],
                    [6, 5, 0, 7, 0, 0, 0, 1, 3],
                    [0, 9, 0, 2, 3, 4, 0, 0, 7],
                    [0, 3, 2, 5, 0, 7, 0, 0, 1],
                    [0, 0, 0, 8, 0, 0, 3, 2, 4]
                ]
                elif levels == 19:
                    wr1 = 0
                    wr2 = 0
                    wr3 = 0
                    wr4 = 0
                    wr5 = 0
                    wr6 = 0
                    wr7 = 0
                    wr8 = 0
                    wr9 = 0
                    wr = 0
                    wrong = 0
                    box = 38
                    grid = [
                    [1, 8, 9, 4, 0, 0, 0, 0, 7],
                    [0, 2, 3, 0, 0, 0, 0, 9, 0],
                    [7, 0, 0, 1, 8, 9, 0, 3, 4],
                    [6, 4, 5, 0, 7, 8, 0, 0, 0],
                    [9, 7, 0, 3, 1, 2, 0, 5, 0],
                    [0, 1, 0, 0, 0, 0, 0, 8, 0],
                    [8, 6, 0, 2, 0, 1, 3, 4, 0],
                    [2, 0, 0, 5, 3, 4, 6, 0, 8],
                    [5, 0, 0, 8, 6, 0, 0, 0, 2]
                ]
                elif levels == 20:
                    wr1 = 0
                    wr2 = 0
                    wr3 = 0
                    wr4 = 0
                    wr5 = 0
                    wr6 = 0
                    wr7 = 0
                    wr8 = 0
                    wr9 = 0
                    wr = 0
                    wrong = 0
                    box = 38
                    grid = [
                    [3, 0, 0, 9, 1, 0, 6, 0, 7],
                    [6, 5, 7, 0, 0, 0, 0, 8, 0],
                    [0, 0, 1, 0, 0, 5, 0, 0, 4],
                    [2, 0, 3, 8, 9, 7, 5, 0, 0],
                    [0, 7, 0, 0, 6, 4, 0, 1, 0],
                    [5, 0, 6, 2, 0, 1, 0, 0, 9],
                    [0, 0, 2, 7, 0, 6, 4, 3, 0],
                    [7, 0, 8, 0, 0, 3, 0, 9, 2],
                    [4, 3, 0, 0, 2, 9, 0, 6, 8]
                ]
                elif levels == 21:
                    wr1 = 0
                    wr2 = 0
                    wr3 = 0
                    wr4 = 0
                    wr5 = 0
                    wr6 = 0
                    wr7 = 0
                    wr8 = 0
                    wr9 = 0
                    wr = 0
                    wrong = 0
                    box = 38
                    grid = [
                    [0, 2, 0, 4, 0, 0, 0, 8, 9],
                    [0, 5, 4, 7, 8, 9, 1, 2, 3],
                    [0, 0, 7, 0, 0, 0, 4, 5, 6],
                    [0, 1, 0, 0, 0, 0, 0, 7, 8],
                    [0, 4, 3, 6, 7, 8, 0, 0, 0],
                    [0, 7, 6, 9, 0, 0, 3, 0, 5],
                    [0, 9, 0, 2, 3, 4, 0, 6, 0],
                    [0, 0, 5, 0, 0, 1, 2, 0, 4],
                    [0, 0, 2, 5, 0, 0, 8, 9, 1]
                ]
                elif levels == 22:
                    wr1 = 0
                    wr2 = 0
                    wr3 = 0
                    wr4 = 0
                    wr5 = 0
                    wr6 = 0
                    wr7 = 0
                    wr8 = 0
                    wr9 = 0
                    wr = 0
                    wrong = 0
                    box = 38
                    grid = [
                    [7, 4, 0, 2, 8, 5, 0, 3, 9],
                    [8, 0, 0, 3, 9, 0, 0, 4, 0],
                    [9, 0, 0, 0, 1, 7, 0, 5, 0],
                    [6, 3, 0, 0, 7, 0, 5, 0, 8],
                    [0, 2, 8, 9, 6, 0, 0, 1, 0],
                    [4, 0, 7, 0, 0, 2, 3, 0, 0],
                    [0, 0, 4, 0, 0, 0, 0, 6, 0],
                    [2, 0, 0, 0, 3, 9, 1, 0, 0],
                    [0, 9, 6, 7, 4, 1, 2, 8, 5]
                ]
                elif levels == 23:
                    wr1 = 0
                    wr2 = 0
                    wr3 = 0
                    wr4 = 0
                    wr5 = 0
                    wr6 = 0
                    wr7 = 0
                    wr8 = 0
                    wr9 = 0
                    wr = 0
                    wrong = 0
                    box = 38
                    grid = [
                    [6, 9, 3, 0, 0, 0, 5, 2, 0],
                    [7, 0, 4, 0, 5, 0, 0, 3, 9],
                    [8, 2, 0, 0, 0, 0, 0, 4, 1],
                    [0, 7, 1, 0, 2, 8, 3, 9, 6],
                    [5, 0, 2, 0, 3, 9, 0, 0, 0],
                    [3, 6, 0, 0, 1, 7, 0, 0, 5],
                    [0, 0, 8, 3, 0, 0, 1, 7, 4],
                    [0, 0, 6, 0, 7, 0, 0, 5, 2],
                    [1, 4, 0, 0, 8, 0, 0, 0, 3]
                ]
                elif levels == 24:
                    wr1 = 0
                    wr2 = 0
                    wr3 = 0
                    wr4 = 0
                    wr5 = 0
                    wr6 = 0
                    wr7 = 0
                    wr8 = 0
                    wr9 = 0
                    wr = 0
                    wrong = 0
                    box = 38
                    grid = [
                    [4, 0, 0, 3, 0, 0, 0, 0, 2],
                    [5, 0, 0, 4, 0, 0, 6, 0, 0],
                    [6, 3, 9, 5, 8, 2, 7, 1, 4],
                    [0, 0, 0, 0, 9, 0, 8, 0, 0],
                    [8, 0, 2, 7, 0, 4, 9, 0, 6],
                    [0, 6, 3, 8, 2, 5, 0, 0, 0],
                    [1, 7, 4, 0, 0, 0, 0, 5, 8],
                    [0, 8, 0, 1, 0, 7, 0, 0, 0],
                    [3, 9, 6, 2, 5, 8, 0, 0, 1]
                ]
                elif levels == 25:
                    wr1 = 0
                    wr2 = 0
                    wr3 = 0
                    wr4 = 0
                    wr5 = 0
                    wr6 = 0
                    wr7 = 0
                    wr8 = 0
                    wr9 = 0
                    wr = 0
                    wrong = 0
                    box = 38
                    grid = [
                    [2, 0, 0, 6, 9, 3, 0, 0, 0],
                    [1, 0, 0, 5, 0, 0, 0, 0, 9],
                    [3, 0, 9, 7, 0, 4, 0, 8, 0],
                    [7, 0, 4, 0, 0, 8, 9, 3, 6],
                    [8, 2, 0, 0, 6, 9, 1, 0, 7],
                    [9, 3, 0, 4, 0, 1, 2, 0, 8],
                    [4, 0, 1, 0, 0, 5, 0, 0, 0],
                    [5, 0, 2, 9, 0, 6, 7, 0, 0],
                    [6, 0, 3, 1, 4, 0, 0, 0, 5]
                ]
                elif levels == 26:
                    wr1 = 0
                    wr2 = 0
                    wr3 = 0
                    wr4 = 0
                    wr5 = 0
                    wr6 = 0
                    wr7 = 0
                    wr8 = 0
                    wr9 = 0
                    wr = 0
                    wrong = 0
                    box = 38
                    grid = [
                    [0, 0, 3, 9, 1, 0, 6, 5, 7],
                    [0, 7, 0, 0, 0, 2, 9, 0, 1],
                    [0, 0, 9, 6, 0, 5, 3, 2, 4],
                    [0, 9, 8, 5, 6, 0, 0, 1, 3],
                    [0, 3, 0, 0, 0, 7, 0, 4, 0],
                    [4, 0, 0, 2, 3, 0, 0, 7, 0],
                    [0, 8, 0, 4, 0, 0, 0, 9, 2],
                    [3, 0, 0, 1, 0, 0, 0, 6, 8],
                    [0, 0, 0, 7, 8, 6, 4, 3, 5]
                ]
                elif levels == 27:
                    wr1 = 0
                    wr2 = 0
                    wr3 = 0
                    wr4 = 0
                    wr5 = 0
                    wr6 = 0
                    wr7 = 0
                    wr8 = 0
                    wr9 = 0
                    wr = 0
                    wrong = 0
                    box = 38
                    grid = [
                    [2, 0, 0, 5, 0, 3, 8, 7, 6],
                    [0, 0, 0, 8, 0, 0, 2, 0, 0],
                    [8, 0, 0, 2, 1, 9, 0, 0, 3],
                    [6, 0, 5, 0, 8, 7, 0, 0, 0],
                    [9, 0, 8, 0, 2, 0, 6, 0, 4],
                    [3, 1, 0, 0, 5, 0, 9, 8, 7],
                    [4, 2, 3, 7, 6, 0, 1, 0, 0],
                    [7, 0, 6, 1, 9, 8, 4, 0, 0],
                    [0, 8, 0, 4, 0, 0, 0, 0, 5]
                ]
                elif levels == 28:
                    wr1 = 0
                    wr2 = 0
                    wr3 = 0
                    wr4 = 0
                    wr5 = 0
                    wr6 = 0
                    wr7 = 0
                    wr8 = 0
                    wr9 = 0
                    wr = 0
                    wrong = 0
                    box = 38
                    grid = [
                    [6, 9, 3, 1, 0, 0, 2, 5, 8],
                    [0, 2, 0, 3, 9, 6, 0, 7, 0],
                    [7, 0, 4, 2, 8, 0, 0, 0, 0],
                    [5, 8, 0, 9, 6, 0, 0, 4, 0],
                    [0, 6, 0, 0, 0, 1, 0, 0, 5],
                    [4, 0, 0, 8, 0, 2, 9, 0, 6],
                    [9, 3, 6, 4, 0, 7, 5, 0, 0],
                    [0, 0, 0, 6, 0, 0, 7, 1, 4],
                    [1, 0, 0, 5, 0, 0, 6, 0, 3]
                ]
                elif levels == 29:
                    wr1 = 0
                    wr2 = 0
                    wr3 = 0
                    wr4 = 0
                    wr5 = 0
                    wr6 = 0
                    wr7 = 0
                    wr8 = 0
                    wr9 = 0
                    wr = 0
                    wrong = 0
                    box = 38
                    grid = [
                    [4, 2, 0, 0, 0, 0, 7, 6, 5],
                    [0, 5, 0, 3, 0, 0, 0, 9, 8],
                    [1, 8, 0, 6, 5, 0, 0, 0, 2],
                    [0, 4, 0, 0, 1, 3, 9, 8, 7],
                    [9, 0, 8, 0, 0, 6, 3, 0, 0],
                    [0, 1, 0, 0, 7, 9, 6, 5, 4],
                    [0, 6, 7, 4, 3, 5, 2, 1, 0],
                    [0, 0, 0, 0, 0, 8, 5, 0, 0],
                    [0, 3, 0, 0, 0, 2, 0, 7, 6]
                ]
                elif levels == 30:
                    wr1 = 0
                    wr2 = 0
                    wr3 = 0
                    wr4 = 0
                    wr5 = 0
                    wr6 = 0
                    wr7 = 0
                    wr8 = 0
                    wr9 = 0
                    wr = 0
                    wrong = 0
                    box = 38
                    grid = [
                    [9, 0, 0, 7, 0, 0, 5, 2, 8],
                    [0, 0, 5, 0, 3, 0, 7, 4, 0],
                    [0, 0, 4, 0, 2, 0, 6, 0, 9],
                    [4, 1, 7, 0, 5, 8, 9, 6, 3],
                    [0, 9, 6, 0, 4, 0, 8, 0, 0],
                    [0, 2, 0, 0, 0, 9, 1, 0, 4],
                    [0, 0, 9, 0, 7, 1, 0, 8, 5],
                    [8, 0, 2, 0, 0, 3, 0, 0, 0],
                    [7, 0, 1, 5, 0, 2, 3, 0, 6]
                ]
            if event.key == pygame.K_s:
                rs = 0
                error = 0
                flag2 = 0
                img = pygame.image.load("C://SudoQuiz//easy//lvl_1.png")
                text = 10
                p1 = 1
                levels = levels + 1
                if levels == 1:
                    wr = 0
                    box = 33
                    wrong = 0
                    grid = [
                    [3, 0, 5, 4, 0, 2, 0, 6, 0],
                    [4, 9, 0, 7, 6, 0, 1, 0, 8],
                    [6, 0, 0, 1, 0, 3, 2, 4, 5],
                    [0, 0, 3, 9, 0, 0, 5, 8, 0],
                    [9, 6, 0, 0, 5, 8, 7, 0, 3],
                    [0, 8, 1, 3, 0, 4, 0, 9, 2],
                    [0, 5, 0, 6, 0, 1, 4, 0, 0],
                    [2, 0, 0, 5, 4, 9, 0, 7, 0],
                    [1, 4, 9, 0, 0, 7, 3, 0, 6]
                ]
            if event.key == pygame.K_y:
                rs = 0
                error = 0
                flag2 = 0
                if levels == 1:
                    wr = 0
                    box = 33
                    wrong = 0
                    img = pygame.image.load("C://SudoQuiz//easy//lvl_1.png")
                    grid = [
                    [3, 0, 5, 4, 0, 2, 0, 6, 0],
                    [4, 9, 0, 7, 6, 0, 1, 0, 8],
                    [6, 0, 0, 1, 0, 3, 2, 4, 5],
                    [0, 0, 3, 9, 0, 0, 5, 8, 0],
                    [9, 6, 0, 0, 5, 8, 7, 0, 3],
                    [0, 8, 1, 3, 0, 4, 0, 9, 2],
                    [0, 5, 0, 6, 0, 1, 4, 0, 0],
                    [2, 0, 0, 5, 4, 9, 0, 7, 0],
                    [1, 4, 9, 0, 0, 7, 3, 0, 6]
                ]
                elif levels == 2:
                    wr = 0
                    wrong = 0
                    box = 34
                    wr1 = 0
                    wr2 = 0
                    wr3 = 0
                    wr4 = 0
                    wr5 = 0
                    wr6 = 0
                    wr7 = 0
                    wr8 = 0
                    wr9 = 0
                    img = pygame.image.load("C://SudoQuiz//easy//lvl_2.png")
                    grid = [
                    [0, 5, 0, 3, 1, 4, 0, 6, 0],
                    [8, 7, 0, 0, 0, 9, 4, 0, 3],
                    [6, 4, 3, 5, 0, 7, 1, 9, 2],
                    [0, 0, 7, 8, 0, 5, 2, 1, 0],
                    [4, 1, 0, 9, 0, 0, 0, 0, 0],
                    [0, 2, 5, 0, 6, 1, 9, 0, 7],
                    [7, 9, 0, 2, 5, 0, 8, 4, 0],
                    [0, 0, 4, 0, 9, 6, 0, 0, 5],
                    [0, 3, 0, 1, 0, 8, 6, 7, 0]
                    ]
                elif levels == 3:
                    wr1 = 0
                    wr2 = 0
                    wr3 = 0
                    wr4 = 0
                    wr5 = 0
                    wr6 = 0
                    wr7 = 0
                    wr8 = 0
                    wr9 = 0
                    wr = 0
                    wrong = 0
                    box = 38
                    img = pygame.image.load("C://SudoQuiz//easy//lvl_3.png")
                    grid = [
                    [0, 0, 0, 0, 4, 0, 3, 0, 9],
                    [0, 6, 0, 2, 5, 8, 4, 0, 1],
                    [1, 7, 4, 0, 6, 9, 0, 8, 2],
                    [6, 0, 0, 8, 0, 5, 0, 0, 0],
                    [7, 4, 1, 9, 3, 0, 0, 5, 0],
                    [5, 0, 8, 0, 0, 4, 0, 3, 6],
                    [2, 0, 0, 0, 0, 1, 0, 9, 3],
                    [0, 9, 0, 5, 0, 2, 7, 1, 4],
                    [0, 0, 7, 0, 9, 0, 0, 0, 5]
                ]
                elif levels == 4:
                    wr1 = 0
                    wr2 = 0
                    wr3 = 0
                    wr4 = 0
                    wr5 = 0
                    wr6 = 0
                    wr7 = 0
                    wr8 = 0
                    wr9 = 0
                    wr = 0
                    wrong = 0
                    box = 38
                    img = pygame.image.load("C://SudoQuiz//easy//lvl_4.png")
                    grid = [
                    [0, 0, 1, 3, 0, 0, 2, 5, 8],
                    [6, 0, 9, 2, 5, 0, 1, 0, 0],
                    [0, 0, 0, 0, 0, 7, 0, 3, 0],
                    [0, 0, 0, 0, 0, 5, 7, 0, 4],
                    [0, 8, 0, 0, 1, 4, 6, 9, 3],
                    [4, 1, 7, 9, 0, 6, 0, 2, 5],
                    [8, 5, 0, 4, 7, 0, 3, 0, 9],
                    [0, 0, 0, 0, 0, 0, 5, 8, 2],
                    [0, 6, 0, 5, 8, 2, 0, 7, 1]
                ]
                elif levels == 5:
                    wr1 = 0
                    wr2 = 0
                    wr3 = 0
                    wr4 = 0
                    wr5 = 0
                    wr6 = 0
                    wr7 = 0
                    wr8 = 0
                    wr9 = 0
                    wr = 0
                    wrong = 0
                    box = 38
                    img = pygame.image.load("C://SudoQuiz//easy//lvl_5.png")
                    grid = [
                    [6, 0, 0, 9, 0, 0, 0, 3, 0],
                    [0, 4, 0, 6, 5, 7, 0, 0, 1],
                    [9, 1, 8, 0, 0, 4, 5, 6, 0],
                    [0, 8, 6, 1, 0, 0, 0, 0, 5],
                    [0, 5, 3, 7, 6, 0, 9, 1, 2],
                    [0, 2, 9, 0, 3, 5, 0, 0, 0],
                    [0, 0, 7, 0, 0, 0, 4, 0, 6],
                    [2, 0, 0, 0, 4, 6, 7, 8, 9],
                    [5, 6, 0, 8, 0, 0, 0, 2, 3]
                ]
                elif levels == 6:
                    wr1 = 0
                    wr2 = 0
                    wr3 = 0
                    wr4 = 0
                    wr5 = 0
                    wr6 = 0
                    wr7 = 0
                    wr8 = 0
                    wr9 = 0
                    wr = 0
                    wrong = 0
                    box = 38
                    img = pygame.image.load("C://SudoQuiz//easy//lvl_6.png")
                    grid = [
                    [8, 0, 0, 0, 1, 0, 6, 0, 3],
                    [7, 0, 4, 3, 0, 6, 0, 0, 2],
                    [0, 0, 0, 2, 0, 5, 0, 0, 1],
                    [0, 3, 0, 0, 0, 8, 7, 1, 4],
                    [0, 5, 0, 7, 4, 1, 9, 0, 0],
                    [1, 4, 0, 6, 0, 9, 0, 2, 5],
                    [0, 8, 0, 0, 0, 4, 3, 0, 0],
                    [4, 7, 0, 9, 0, 3, 2, 0, 8],
                    [0, 6, 9, 8, 5, 2, 0, 0, 7]
                ]
                elif levels == 7:
                    wr1 = 0
                    wr2 = 0
                    wr3 = 0
                    wr4 = 0
                    wr5 = 0
                    wr6 = 0
                    wr7 = 0
                    wr8 = 0
                    wr9 = 0
                    wr = 0
                    wrong = 0
                    box = 38
                    img = pygame.image.load("C://SudoQuiz//easy//lvl_7.png")
                    grid = [
                    [5, 0, 8, 6, 0, 0, 4, 0, 0],
                    [0, 3, 0, 7, 0, 0, 5, 2, 0],
                    [4, 1, 0, 0, 2, 8, 0, 9, 6],
                    [0, 0, 6, 0, 0, 7, 2, 8, 0],
                    [2, 0, 0, 0, 9, 0, 0, 7, 4],
                    [1, 7, 4, 2, 0, 5, 9, 0, 3],
                    [9, 0, 3, 1, 0, 4, 0, 0, 2],
                    [8, 5, 2, 0, 6, 0, 0, 4, 0],
                    [7, 0, 1, 0, 0, 0, 0, 3, 9]
                ]
                elif levels == 8:
                    wr1 = 0
                    wr2 = 0
                    wr3 = 0
                    wr4 = 0
                    wr5 = 0
                    wr6 = 0
                    wr7 = 0
                    wr8 = 0
                    wr9 = 0
                    wr = 0
                    wrong = 0
                    box = 38
                    img = pygame.image.load("C://SudoQuiz//easy//lvl_8.png")
                    grid = [
                    [5, 6, 0, 8, 9, 1, 0, 0, 4],
                    [0, 0, 0, 2, 0, 0, 0, 0, 7],
                    [2, 3, 0, 5, 0, 7, 8, 9, 1],
                    [0, 0, 0, 6, 0, 8, 9, 0, 0],
                    [0, 7, 0, 0, 1, 0, 3, 4, 0],
                    [0, 1, 0, 3, 4, 5, 0, 7, 8],
                    [1, 2, 0, 4, 0, 6, 7, 8, 0],
                    [0, 0, 9, 1, 2, 3, 0, 5, 6],
                    [0, 5, 0, 0, 0, 0, 1, 0, 3]
                ]
                elif levels == 9:
                    wr1 = 0
                    wr2 = 0
                    wr3 = 0
                    wr4 = 0
                    wr5 = 0
                    wr6 = 0
                    wr7 = 0
                    wr8 = 0
                    wr9 = 0
                    wr = 0
                    wrong = 0
                    box = 38
                    img = pygame.image.load("C://SudoQuiz//easy//lvl_9.png")
                    grid = [
                    [0, 3, 6, 0, 0, 0, 2, 5, 8],
                    [8, 2, 5, 0, 0, 9, 1, 4, 7],
                    [1, 4, 0, 5, 0, 2, 3, 0, 9],
                    [0, 9, 3, 0, 4, 0, 8, 0, 0],
                    [0, 1, 0, 2, 0, 8, 9, 0, 6],
                    [5, 8, 0, 0, 3, 6, 7, 1, 4],
                    [0, 0, 9, 7, 0, 0, 0, 0, 0],
                    [0, 7, 0, 8, 2, 0, 6, 0, 0],
                    [2, 0, 0, 0, 0, 0, 0, 7, 1]
                ]
                elif levels == 10:
                    wr1 = 0
                    wr2 = 0
                    wr3 = 0
                    wr4 = 0
                    wr5 = 0
                    wr6 = 0
                    wr7 = 0
                    wr8 = 0
                    wr9 = 0
                    wr = 0
                    wrong = 0
                    box = 38
                    img = pygame.image.load("C://SudoQuiz//easy//lvl_10.png")
                    grid = [
                    [6, 3, 9, 8, 5, 0, 0, 0, 7],
                    [0, 0, 0, 0, 0, 9, 0, 2, 5],
                    [5, 0, 0, 0, 4, 0, 0, 0, 6],
                    [1, 7, 4, 3, 9, 6, 0, 0, 0],
                    [3, 9, 0, 0, 2, 8, 7, 1, 4],
                    [2, 8, 0, 0, 1, 0, 0, 9, 0],
                    [0, 0, 0, 2, 0, 5, 4, 7, 1],
                    [0, 5, 0, 1, 0, 0, 3, 6, 0],
                    [7, 0, 1, 0, 0, 0, 2, 5, 8]
                ]
                elif levels == 11:
                    wr1 = 0
                    wr2 = 0
                    wr3 = 0
                    wr4 = 0
                    wr5 = 0
                    wr6 = 0
                    wr7 = 0
                    wr8 = 0
                    wr9 = 0
                    wr = 0
                    wrong = 0
                    box = 38
                    grid = [
                    [7, 4, 0, 0, 6, 0, 0, 0, 5],
                    [0, 3, 0, 0, 0, 0, 7, 0, 4],
                    [5, 0, 0, 7, 4, 1, 0, 9, 0],
                    [3, 0, 6, 0, 2, 8, 0, 7, 1],
                    [0, 1, 0, 0, 0, 0, 5, 0, 2],
                    [2, 8, 5, 4, 0, 0, 3, 6, 0],
                    [9, 0, 3, 0, 8, 5, 0, 4, 0],
                    [0, 5, 2, 0, 0, 0, 9, 3, 6],
                    [1, 0, 4, 0, 9, 6, 0, 5, 8]
                ]
                elif levels == 12:
                    wr1 = 0
                    wr2 = 0
                    wr3 = 0
                    wr4 = 0
                    wr5 = 0
                    wr6 = 0
                    wr7 = 0
                    wr8 = 0
                    wr9 = 0
                    wr = 0
                    wrong = 0
                    box = 38
                    grid = [
                    [3, 6, 9, 0, 5, 0, 4, 0, 0],
                    [2, 0, 8, 1, 4, 7, 0, 6, 0],
                    [0, 0, 0, 9, 3, 6, 2, 5, 8],
                    [7, 1, 4, 0, 9, 0, 0, 0, 5],
                    [8, 0, 0, 0, 1, 0, 9, 0, 6],
                    [0, 3, 0, 8, 2, 0, 0, 0, 7],
                    [0, 7, 1, 3, 6, 0, 5, 0, 2],
                    [0, 0, 0, 0, 7, 1, 0, 0, 3],
                    [0, 0, 0, 5, 8, 2, 0, 0, 4]
                ]
                elif levels == 13:
                    wr1 = 0
                    wr2 = 0
                    wr3 = 0
                    wr4 = 0
                    wr5 = 0
                    wr6 = 0
                    wr7 = 0
                    wr8 = 0
                    wr9 = 0
                    wr = 0
                    wrong = 0
                    box = 38
                    grid = [
                    [2, 1, 9, 0, 4, 0, 0, 8, 7],
                    [0, 0, 0, 2, 0, 9, 3, 0, 0],
                    [5, 0, 0, 8, 0, 6, 9, 2, 1],
                    [0, 5, 0, 0, 0, 0, 0, 0, 0],
                    [3, 2, 0, 0, 0, 4, 7, 0, 8],
                    [0, 8, 7, 3, 0, 0, 4, 6, 5],
                    [4, 0, 0, 0, 6, 5, 0, 1, 9],
                    [0, 6, 5, 0, 9, 0, 0, 4, 3],
                    [1, 0, 8, 0, 3, 0, 5, 7, 6]
                ]
                elif levels == 14:
                    wr1 = 0
                    wr2 = 0
                    wr3 = 0
                    wr4 = 0
                    wr5 = 0
                    wr6 = 0
                    wr7 = 0
                    wr8 = 0
                    wr9 = 0
                    wr = 0
                    wrong = 0
                    box = 38
                    grid = [
                    [3, 4, 0, 0, 7, 0, 9, 1, 2],
                    [9, 0, 2, 0, 0, 3, 6, 7, 0],
                    [0, 0, 8, 2, 1, 0, 3, 0, 5],
                    [0, 2, 0, 6, 0, 0, 0, 8, 0],
                    [0, 0, 0, 0, 0, 7, 0, 0, 0],
                    [0, 8, 0, 3, 2, 1, 4, 5, 6],
                    [5, 0, 0, 1, 9, 8, 0, 0, 4],
                    [2, 3, 0, 7, 0, 5, 0, 0, 1],
                    [8, 9, 0, 4, 0, 2, 0, 6, 7]
                ]
                elif levels == 15:
                    wr1 = 0
                    wr2 = 0
                    wr3 = 0
                    wr4 = 0
                    wr5 = 0
                    wr6 = 0
                    wr7 = 0
                    wr8 = 0
                    wr9 = 0
                    wr = 0
                    wrong = 0
                    box = 38
                    grid = [
                    [8, 0, 0, 0, 4, 7, 0, 0, 6],
                    [9, 3, 6, 0, 5, 0, 0, 1, 7],
                    [0, 0, 7, 3, 0, 9, 5, 2, 8],
                    [4, 0, 1, 0, 0, 3, 8, 0, 2],
                    [0, 0, 8, 0, 7, 1, 6, 0, 9],
                    [0, 6, 0, 5, 0, 0, 0, 0, 1],
                    [0, 0, 3, 8, 0, 0, 0, 0, 0],
                    [5, 0, 2, 7, 0, 4, 0, 0, 3],
                    [0, 1, 4, 9, 0, 6, 2, 8, 5]
                ]
                elif levels == 16:
                    wr1 = 0
                    wr2 = 0
                    wr3 = 0
                    wr4 = 0
                    wr5 = 0
                    wr6 = 0
                    wr7 = 0
                    wr8 = 0
                    wr9 = 0
                    wr = 0
                    wrong = 0
                    box = 38
                    grid = [
                    [1, 2, 9, 0, 6, 7, 0, 0, 0],
                    [4, 5, 0, 2, 9, 0, 6, 0, 8],
                    [0, 0, 6, 5, 3, 4, 0, 1, 0],
                    [3, 0, 2, 1, 0, 0, 5, 0, 0],
                    [6, 7, 0, 0, 2, 0, 0, 0, 0],
                    [0, 1, 8, 7, 0, 6, 2, 3, 0],
                    [8, 0, 7, 0, 4, 0, 0, 0, 3],
                    [0, 3, 0, 9, 7, 8, 4, 5, 0],
                    [0, 6, 0, 3, 0, 0, 0, 8, 9]
                ]
                elif levels == 17:
                    wr1 = 0
                    wr2 = 0
                    wr3 = 0
                    wr4 = 0
                    wr5 = 0
                    wr6 = 0
                    wr7 = 0
                    wr8 = 0
                    wr9 = 0
                    wr = 0
                    wrong = 0
                    box = 38
                    grid = [
                    [0, 5, 0, 0, 6, 0, 0, 0, 9],
                    [0, 8, 0, 1, 9, 2, 0, 0, 3],
                    [1, 2, 0, 4, 0, 0, 0, 0, 0],
                    [0, 0, 2, 0, 0, 0, 0, 0, 8],
                    [6, 7, 5, 0, 0, 0, 4, 3, 0],
                    [9, 1, 0, 0, 2, 0, 7, 0, 5],
                    [8, 9, 7, 2, 0, 0, 0, 0, 4],
                    [2, 3, 1, 5, 0, 6, 0, 8, 0],
                    [5, 6, 4, 8, 7, 9, 3, 2, 1]
                ]
                elif levels == 18:
                    wr1 = 0
                    wr2 = 0
                    wr3 = 0
                    wr4 = 0
                    wr5 = 0
                    wr6 = 0
                    wr7 = 0
                    wr8 = 0
                    wr9 = 0
                    wr = 0
                    wrong = 0
                    box = 38
                    grid = [
                    [5, 4, 0, 6, 0, 8, 0, 0, 2],
                    [0, 0, 9, 3, 4, 0, 7, 0, 8],
                    [0, 0, 0, 0, 1, 2, 0, 0, 5],
                    [9, 8, 7, 0, 2, 0, 0, 0, 6],
                    [0, 0, 1, 4, 5, 6, 0, 7, 9],
                    [6, 5, 0, 7, 0, 0, 0, 1, 3],
                    [0, 9, 0, 2, 3, 4, 0, 0, 7],
                    [0, 3, 2, 5, 0, 7, 0, 0, 1],
                    [0, 0, 0, 8, 0, 0, 3, 2, 4]
                ]
                elif levels == 19:
                    wr1 = 0
                    wr2 = 0
                    wr3 = 0
                    wr4 = 0
                    wr5 = 0
                    wr6 = 0
                    wr7 = 0
                    wr8 = 0
                    wr9 = 0
                    wr = 0
                    wrong = 0
                    box = 38
                    grid = [
                    [1, 8, 9, 4, 0, 0, 0, 0, 7],
                    [0, 2, 3, 0, 0, 0, 0, 9, 0],
                    [7, 0, 0, 1, 8, 9, 0, 3, 4],
                    [6, 4, 5, 0, 7, 8, 0, 0, 0],
                    [9, 7, 0, 3, 1, 2, 0, 5, 0],
                    [0, 1, 0, 0, 0, 0, 0, 8, 0],
                    [8, 6, 0, 2, 0, 1, 3, 4, 0],
                    [2, 0, 0, 5, 3, 4, 6, 0, 8],
                    [5, 0, 0, 8, 6, 0, 0, 0, 2]
                ]
                elif levels == 20:
                    wr1 = 0
                    wr2 = 0
                    wr3 = 0
                    wr4 = 0
                    wr5 = 0
                    wr6 = 0
                    wr7 = 0
                    wr8 = 0
                    wr9 = 0
                    wr = 0
                    wrong = 0
                    box = 38
                    grid = [
                    [3, 0, 0, 9, 1, 0, 6, 0, 7],
                    [6, 5, 7, 0, 0, 0, 0, 8, 0],
                    [0, 0, 1, 0, 0, 5, 0, 0, 4],
                    [2, 0, 3, 8, 9, 7, 5, 0, 0],
                    [0, 7, 0, 0, 6, 4, 0, 1, 0],
                    [5, 0, 6, 2, 0, 1, 0, 0, 9],
                    [0, 0, 2, 7, 0, 6, 4, 3, 0],
                    [7, 0, 8, 0, 0, 3, 0, 9, 2],
                    [4, 3, 0, 0, 2, 9, 0, 6, 8]
                ]
                elif levels == 21:
                    wr1 = 0
                    wr2 = 0
                    wr3 = 0
                    wr4 = 0
                    wr5 = 0
                    wr6 = 0
                    wr7 = 0
                    wr8 = 0
                    wr9 = 0
                    wr = 0
                    wrong = 0
                    box = 38
                    grid = [
                    [0, 2, 0, 4, 0, 0, 0, 8, 9],
                    [0, 5, 4, 7, 8, 9, 1, 2, 3],
                    [0, 0, 7, 0, 0, 0, 4, 5, 6],
                    [0, 1, 0, 0, 0, 0, 0, 7, 8],
                    [0, 4, 3, 6, 7, 8, 0, 0, 0],
                    [0, 7, 6, 9, 0, 0, 3, 0, 5],
                    [0, 9, 0, 2, 3, 4, 0, 6, 0],
                    [0, 0, 5, 0, 0, 1, 2, 0, 4],
                    [0, 0, 2, 5, 0, 0, 8, 9, 1]
                ]
                elif levels == 22:
                    wr1 = 0
                    wr2 = 0
                    wr3 = 0
                    wr4 = 0
                    wr5 = 0
                    wr6 = 0
                    wr7 = 0
                    wr8 = 0
                    wr9 = 0
                    wr = 0
                    wrong = 0
                    box = 38
                    grid = [
                    [7, 4, 0, 2, 8, 5, 0, 3, 9],
                    [8, 0, 0, 3, 9, 0, 0, 4, 0],
                    [9, 0, 0, 0, 1, 7, 0, 5, 0],
                    [6, 3, 0, 0, 7, 0, 5, 0, 8],
                    [0, 2, 8, 9, 6, 0, 0, 1, 0],
                    [4, 0, 7, 0, 0, 2, 3, 0, 0],
                    [0, 0, 4, 0, 0, 0, 0, 6, 0],
                    [2, 0, 0, 0, 3, 9, 1, 0, 0],
                    [0, 9, 6, 7, 4, 1, 2, 8, 5]
                ]
                elif levels == 23:
                    wr1 = 0
                    wr2 = 0
                    wr3 = 0
                    wr4 = 0
                    wr5 = 0
                    wr6 = 0
                    wr7 = 0
                    wr8 = 0
                    wr9 = 0
                    wr = 0
                    wrong = 0
                    box = 38
                    grid = [
                    [6, 9, 3, 0, 0, 0, 5, 2, 0],
                    [7, 0, 4, 0, 5, 0, 0, 3, 9],
                    [8, 2, 0, 0, 0, 0, 0, 4, 1],
                    [0, 7, 1, 0, 2, 8, 3, 9, 6],
                    [5, 0, 2, 0, 3, 9, 0, 0, 0],
                    [3, 6, 0, 0, 1, 7, 0, 0, 5],
                    [0, 0, 8, 3, 0, 0, 1, 7, 4],
                    [0, 0, 6, 0, 7, 0, 0, 5, 2],
                    [1, 4, 0, 0, 8, 0, 0, 0, 3]
                ]
                elif levels == 24:
                    wr1 = 0
                    wr2 = 0
                    wr3 = 0
                    wr4 = 0
                    wr5 = 0
                    wr6 = 0
                    wr7 = 0
                    wr8 = 0
                    wr9 = 0
                    wr = 0
                    wrong = 0
                    box = 38
                    grid = [
                    [4, 0, 0, 3, 0, 0, 0, 0, 2],
                    [5, 0, 0, 4, 0, 0, 6, 0, 0],
                    [6, 3, 9, 5, 8, 2, 7, 1, 4],
                    [0, 0, 0, 0, 9, 0, 8, 0, 0],
                    [8, 0, 2, 7, 0, 4, 9, 0, 6],
                    [0, 6, 3, 8, 2, 5, 0, 0, 0],
                    [1, 7, 4, 0, 0, 0, 0, 5, 8],
                    [0, 8, 0, 1, 0, 7, 0, 0, 0],
                    [3, 9, 6, 2, 5, 8, 0, 0, 1]
                ]
                elif levels == 25:
                    wr1 = 0
                    wr2 = 0
                    wr3 = 0
                    wr4 = 0
                    wr5 = 0
                    wr6 = 0
                    wr7 = 0
                    wr8 = 0
                    wr9 = 0
                    wr = 0
                    wrong = 0
                    box = 38
                    grid = [
                    [2, 0, 0, 6, 9, 3, 0, 0, 0],
                    [1, 0, 0, 5, 0, 0, 0, 0, 9],
                    [3, 0, 9, 7, 0, 4, 0, 8, 0],
                    [7, 0, 4, 0, 0, 8, 9, 3, 6],
                    [8, 2, 0, 0, 6, 9, 1, 0, 7],
                    [9, 3, 0, 4, 0, 1, 2, 0, 8],
                    [4, 0, 1, 0, 0, 5, 0, 0, 0],
                    [5, 0, 2, 9, 0, 6, 7, 0, 0],
                    [6, 0, 3, 1, 4, 0, 0, 0, 5]
                ]
                elif levels == 26:
                    wr1 = 0
                    wr2 = 0
                    wr3 = 0
                    wr4 = 0
                    wr5 = 0
                    wr6 = 0
                    wr7 = 0
                    wr8 = 0
                    wr9 = 0
                    wr = 0
                    wrong = 0
                    box = 38
                    grid = [
                    [0, 0, 3, 9, 1, 0, 6, 5, 7],
                    [0, 7, 0, 0, 0, 2, 9, 0, 1],
                    [0, 0, 9, 6, 0, 5, 3, 2, 4],
                    [0, 9, 8, 5, 6, 0, 0, 1, 3],
                    [0, 3, 0, 0, 0, 7, 0, 4, 0],
                    [4, 0, 0, 2, 3, 0, 0, 7, 0],
                    [0, 8, 0, 4, 0, 0, 0, 9, 2],
                    [3, 0, 0, 1, 0, 0, 0, 6, 8],
                    [0, 0, 0, 7, 8, 6, 4, 3, 5]
                ]
                elif levels == 27:
                    wr1 = 0
                    wr2 = 0
                    wr3 = 0
                    wr4 = 0
                    wr5 = 0
                    wr6 = 0
                    wr7 = 0
                    wr8 = 0
                    wr9 = 0
                    wr = 0
                    wrong = 0
                    box = 38
                    grid = [
                    [2, 0, 0, 5, 0, 3, 8, 7, 6],
                    [0, 0, 0, 8, 0, 0, 2, 0, 0],
                    [8, 0, 0, 2, 1, 9, 0, 0, 3],
                    [6, 0, 5, 0, 8, 7, 0, 0, 0],
                    [9, 0, 8, 0, 2, 0, 6, 0, 4],
                    [3, 1, 0, 0, 5, 0, 9, 8, 7],
                    [4, 2, 3, 7, 6, 0, 1, 0, 0],
                    [7, 0, 6, 1, 9, 8, 4, 0, 0],
                    [0, 8, 0, 4, 0, 0, 0, 0, 5]
                ]
                elif levels == 28:
                    wr1 = 0
                    wr2 = 0
                    wr3 = 0
                    wr4 = 0
                    wr5 = 0
                    wr6 = 0
                    wr7 = 0
                    wr8 = 0
                    wr9 = 0
                    wr = 0
                    wrong = 0
                    box = 38
                    grid = [
                    [6, 9, 3, 1, 0, 0, 2, 5, 8],
                    [0, 2, 0, 3, 9, 6, 0, 7, 0],
                    [7, 0, 4, 2, 8, 0, 0, 0, 0],
                    [5, 8, 0, 9, 6, 0, 0, 4, 0],
                    [0, 6, 0, 0, 0, 1, 0, 0, 5],
                    [4, 0, 0, 8, 0, 2, 9, 0, 6],
                    [9, 3, 6, 4, 0, 7, 5, 0, 0],
                    [0, 0, 0, 6, 0, 0, 7, 1, 4],
                    [1, 0, 0, 5, 0, 0, 6, 0, 3]
                ]
                elif levels == 29:
                    wr1 = 0
                    wr2 = 0
                    wr3 = 0
                    wr4 = 0
                    wr5 = 0
                    wr6 = 0
                    wr7 = 0
                    wr8 = 0
                    wr9 = 0
                    wr = 0
                    wrong = 0
                    box = 38
                    grid = [
                    [4, 2, 0, 0, 0, 0, 7, 6, 5],
                    [0, 5, 0, 3, 0, 0, 0, 9, 8],
                    [1, 8, 0, 6, 5, 0, 0, 0, 2],
                    [0, 4, 0, 0, 1, 3, 9, 8, 7],
                    [9, 0, 8, 0, 0, 6, 3, 0, 0],
                    [0, 1, 0, 0, 7, 9, 6, 5, 4],
                    [0, 6, 7, 4, 3, 5, 2, 1, 0],
                    [0, 0, 0, 0, 0, 8, 5, 0, 0],
                    [0, 3, 0, 0, 0, 2, 0, 7, 6]
                ]
                elif levels == 30:
                    wr1 = 0
                    wr2 = 0
                    wr3 = 0
                    wr4 = 0
                    wr5 = 0
                    wr6 = 0
                    wr7 = 0
                    wr8 = 0
                    wr9 = 0
                    wr = 0
                    wrong = 0
                    box = 38
                    grid = [
                    [9, 0, 0, 7, 0, 0, 5, 2, 8],
                    [0, 0, 5, 0, 3, 0, 7, 4, 0],
                    [0, 0, 4, 0, 2, 0, 6, 0, 9],
                    [4, 1, 7, 0, 5, 8, 9, 6, 3],
                    [0, 9, 6, 0, 4, 0, 8, 0, 0],
                    [0, 2, 0, 0, 0, 9, 1, 0, 4],
                    [0, 0, 9, 0, 7, 1, 0, 8, 5],
                    [8, 0, 2, 0, 0, 3, 0, 0, 0],
                    [7, 0, 1, 5, 0, 2, 3, 0, 6]
                ]
            if event.key == pygame.K_n:
                pygame.quit()
    if flag2 == 1:
        if solve(grid, 0, 0) == False:
            error = 1
        else:
            rs = 1
        flag2 = 0
    if val != 0:
        draw_val(val)
        # print(x)
        # print(y)
        if valid(grid, int(x), int(y), val) == True:
            music.play()
            grid[int(x)][int(y)] = val
            flag1 = 0
            if levels == 1:
                if grid[2][2] == 8 and wr1 == 0:
                    wr = wr + 1
                    wr1 = 1
                elif grid[3][0] == 7 and wr2 == 0:
                    wr = wr + 1
                    wr2 = 1
                elif grid[7][1] == 3 and wr3 == 0:
                    wr = wr + 1
                    wr3 = 1
                elif grid[8][3] == 8 and wr4 == 0:
                    wr = wr + 1
                    wr4 = 1
                elif grid[0][4] == 8 and wr5 == 0:
                    wr = wr + 1
                    wr5 = 1
                elif grid[5][4] == 7 and wr6 == 0:
                    wr = wr + 1
                    wr6 = 1
                elif grid[0][8] == 7 and wr7 == 0:
                    wr = wr + 1
                    wr7 = 1
                elif grid[3][8] == 4 and wr8 == 0:
                    wr = wr + 1
                    wr8 = 1
                elif grid[7][8] == 1 and wr9 == 0:
                    wr = wr + 1
                    wr9 = 1
            elif levels == 2:
                if grid[0][0] == 2 and wr1 == 0:
                    wr = wr + 1
                    wr1 = 1
                elif grid[3][1] == 6 and wr2 == 0:
                    wr = wr + 1
                    wr2 = 1
                elif grid[7][1] == 8 and wr3 == 0:
                    wr = wr + 1
                    wr3 = 1
                elif grid[1][3] == 6 and wr4 == 0:
                    wr = wr + 1
                    wr4 = 1
                elif grid[5][3] == 4 and wr5 == 0:
                    wr = wr + 1
                    wr5 = 1
                elif grid[8][4] == 4 and wr6 == 0:
                    wr = wr + 1
                    wr6 = 1
                elif grid[0][8] == 8 and wr7 == 0:
                    wr = wr + 1
                    wr7 = 1
                elif grid[3][8] == 4 and wr8 == 0:
                    wr = wr + 1
                    wr8 = 1
                elif grid[8][8] == 9 and wr9 == 0:
                    wr = wr + 1
                    wr9 = 1
            elif levels == 3:
                if grid[0][0] == 8 and wr1 == 0:
                    wr = wr + 1
                    wr1 = 1
                elif grid[7][0] == 3 and wr2 == 0:
                    wr = wr + 1
                    wr2 = 1
                elif grid[3][1] == 3 and wr3 == 0:
                    wr = wr + 1
                    wr3 = 1
                elif grid[2][3] == 3 and wr4 == 0:
                    wr = wr + 1
                    wr4 = 1
                elif grid[7][4] == 8 and wr5 == 0:
                    wr = wr + 1
                    wr5 = 1
                elif grid[4][5] == 6 and wr6 == 0:
                    wr = wr + 1
                    wr6 = 1
                elif grid[1][7] == 7 and wr7 == 0:
                    wr = wr + 1
                    wr7 = 1
                elif grid[3][8] == 7 and wr8 == 0:
                    wr = wr + 1
                    wr8 = 1
                elif grid[8][7] == 2 and wr9 == 0:
                    wr = wr + 1
                    wr9 = 1
            elif levels == 4:
                if grid[0][0] == 7 and wr1 == 0:
                    wr = wr + 1
                    wr1 = 1
                elif grid[3][1] == 9 and wr2 == 0:
                    wr = wr + 1
                    wr2 = 1
                elif grid[7][1] == 7 and wr3 == 0:
                    wr = wr + 1
                    wr3 = 1
                elif grid[2][4] == 4 and wr4 == 0:
                    wr = wr + 1
                    wr4 = 1
                elif grid[5][4] == 3 and wr5 == 0:
                    wr = wr + 1
                    wr5 = 1
                elif grid[7][5] == 3 and wr6 == 0:
                    wr = wr + 1
                    wr6 = 1
                elif grid[2][6] == 9 and wr7 == 0:
                    wr = wr + 1
                    wr7 = 1
                elif grid[5][6] == 8 and wr8 == 0:
                    wr = wr + 1
                    wr8 = 1
                elif grid[6][7] == 6 and wr9 == 0:
                    wr = wr + 1
                    wr9 = 1
            elif levels == 5:
                if grid[1][0] == 3 and wr1 == 0:
                    wr = wr + 1
                    wr1 = 1
                elif grid[3][0] == 7 and wr2 == 0:
                    wr = wr + 1
                    wr2 = 1
                elif grid[6][1] == 9 and wr3 == 0:
                    wr = wr + 1
                    wr3 = 1
                elif grid[2][4] == 1 and wr4 == 0:
                    wr = wr + 1
                    wr4 = 1
                elif grid[4][5] == 8 and wr5 == 0:
                    wr = wr + 1
                    wr5 = 1
                elif grid[6][5] == 3 and wr6 == 0:
                    wr = wr + 1
                    wr6 = 1
                elif grid[1][7] == 9 and wr7 == 0:
                    wr = wr + 1
                    wr7 = 1
                elif grid[5][7] == 7 and wr8 == 0:
                    wr = wr + 1
                    wr8 = 1
                elif grid[6][7] == 5 and wr9 == 0:
                    wr = wr + 1
                    wr9 = 1
            elif levels == 6:
                if grid[2][0] == 0 and wr1 == 0:
                    wr = wr + 1
                    wr1 = 1
                elif grid[3][0] == 0 and wr2 == 0:
                    wr = wr + 1
                    wr2 = 1
                elif grid[8][0] == 0 and wr3 == 0:
                    wr = wr + 1
                    wr3 = 1
                elif grid[0][3] == 0 and wr4 == 0:
                    wr = wr + 1
                    wr4 = 1
                elif grid[3][4] == 0 and wr5 == 0:
                    wr = wr + 1
                    wr5 = 1
                elif grid[7][4] == 0 and wr6 == 0:
                    wr = wr + 1
                    wr6 = 1
                elif grid[2][7] == 0 and wr7 == 0:
                    wr = wr + 1
                    wr7 = 1
                elif grid[4][8] == 0 and wr8 == 0:
                    wr = wr + 1
                    wr8 = 1
                elif grid[6][8] == 0 and wr9 == 0:
                    wr = wr + 1
                    wr9 = 1
            elif levels == 7:
                if grid[1][0] == 6 and wr1 == 0:
                    wr = wr + 1
                    wr1 = 1
                elif grid[3][1] == 9 and wr2 == 0:
                    wr = wr + 1
                    wr2 = 1
                elif grid[8][1] == 4 and wr3 == 0:
                    wr = wr + 1
                    wr3 = 1
                elif grid[8][3] == 4 and wr4 == 0:
                    wr = wr + 1
                    wr4 = 1
                elif grid[1][4] == 6 and wr5 == 0:
                    wr = wr + 1
                    wr5 = 1
                elif grid[4][5] == 8 and wr6 == 0:
                    wr = wr + 1
                    wr6 = 1
                elif grid[6][6] == 7 and wr7 == 0:
                    wr = wr + 1
                    wr7 = 1
                elif grid[5][7] == 6 and wr8 == 0:
                    wr = wr + 1
                    wr8 = 1
                elif grid[0][8] == 8 and wr9 == 0:
                    wr = wr + 1
                    wr9 = 1
            elif levels == 8:
                if grid[1][0] == 8 and wr1 == 0:
                    wr = wr + 1
                    wr1 = 1
                elif grid[3][0] == 3 and wr2 == 0:
                    wr = wr + 1
                    wr2 = 1
                elif grid[7][1] == 8 and wr3 == 0:
                    wr = wr + 1
                    wr3 = 1
                elif grid[2][4] == 6 and wr4 == 0:
                    wr = wr + 1
                    wr4 = 1
                elif grid[4][5] == 2 and wr5 == 0:
                    wr = wr + 1
                    wr5 = 1
                elif grid[8][5] == 9 and wr6 == 0:
                    wr = wr + 1
                    wr6 = 1
                elif grid[7][6] == 4 and wr7 == 0:
                    wr = wr + 1
                    wr7 = 1
                elif grid[0][7] == 3 and wr8 == 0:
                    wr = wr + 1
                    wr8 = 1
                elif grid[3][8] == 2 and wr9 == 0:
                    wr = wr + 1
                    wr9 = 1
            elif levels == 9:
                if grid[0][0] == 9 and wr1 == 0:
                    wr = wr + 1
                    wr1 = 1
                elif grid[4][0] == 7 and wr2 == 0:
                    wr = wr + 1
                    wr2 = 1
                elif grid[6][1] == 6 and wr3 == 0:
                    wr = wr + 1
                    wr3 = 1
                elif grid[1][4] == 6 and wr4 == 0:
                    wr = wr + 1
                    wr4 = 1
                elif grid[3][5] == 7 and wr5 == 0:
                    wr = wr + 1
                    wr5 = 1
                elif grid[7][5] == 5 and wr6 == 0:
                    wr = wr + 1
                    wr6 = 1
                elif grid[2][7] == 6 and wr7 == 0:
                    wr = wr + 1
                    wr7 = 1
                elif grid[3][8] == 5 and wr8 == 0:
                    wr = wr + 1
                    wr8 = 1
                elif grid[7][8] == 3 and wr9 == 0:
                    wr = wr + 1
                    wr9 = 1
            elif levels == 10:
                if grid[1][0] == 0 and wr1 == 0:
                    wr = wr + 1
                    wr1 = 1
                elif grid[4][2] == 0 and wr2 == 0:
                    wr = wr + 1
                    wr2 = 1
                elif grid[6][0] == 0 and wr3 == 0:
                    wr = wr + 1
                    wr3 = 1
                elif grid[1][4] == 0 and wr4 == 0:
                    wr = wr + 1
                    wr4 = 1
                elif grid[5][5] == 0 and wr5 == 0:
                    wr = wr + 1
                    wr5 = 1
                elif grid[6][4] == 0 and wr6 == 0:
                    wr = wr + 1
                    wr6 = 1
                elif grid[2][7] == 0 and wr7 == 0:
                    wr = wr + 1
                    wr7 = 1
                elif grid[3][8] == 0 and wr8 == 0:
                    wr = wr + 1
                    wr8 = 1
                elif grid[7][8] == 0 and wr9 == 0:
                    wr = wr + 1
                    wr9 = 1
        else:
            music.play()
            grid[int(x)][int(y)] = val
            wrong = wrong + 1

        val = 0

    if error == 1:
        text = 10
        los.play()
        raise_error1(wrong, box, wr)
    if rs == 1:
        text = 10
        wins.play()
        result(wrong, box, wr)
    draw()
    if flag1 == 1:
        draw_box()
    instruction(text, p1)
    screen.blit(img, (imgx, imgy))
    screen.blit(btext,(button.x+5, button.y+5))
    screen.blit(btext2,(button2.x+5, button2.y+5))
    screen.blit(btext3,(button3.x+5, button3.y+5))

    # Update window
    pygame.display.update()

# Quit pygame window
pygame.quit()

