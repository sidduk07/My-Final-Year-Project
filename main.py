import random
import sys
import pygame
from pygame.locals import *
from butn1 import Button
import os
import tkinter as tk
from tkinter import messagebox

# SCORE_FILE = f'{username}.txt'
USER_PASS_FILE = "user_pass.txt"
highest_score = 0
# if os.path.exists(SCORE_FILE):
#     with open(SCORE_FILE, "r") as file:
#         highest_score = int(file.read())

def get_font(size):
    return pygame.font.Font(pygame.font.get_default_font(), size)

def login_screen():
    global username_entry, password_entry, login_window
    
    def center_window(window, width, height):
     screen_width = window.winfo_screenwidth()
     screen_height = window.winfo_screenheight()

     x = (screen_width - width) // 2
     y = (screen_height - height) // 2

     window.geometry(f"{width}x{height}+{x}+{y}")

    login_window = tk.Tk()
    # login_window.geometry("289x511")
    login_window.title("Flappy Bird - Login")
    login_window.configure(bg="#3C3F41")

# Set window size
    window_width = 290
    window_height = 511

# Center the window on the screen
    center_window(login_window, window_width, window_height)

    frame = tk.Frame(login_window,bg="#3C3F41")
    
    login_label=tk.Label(frame, text="""Login to Flappy 
Bird""", bg='black', fg="Yellow", font=("Arial Black", 20))
    username_label = tk.Label(frame,text="Username",bg='#8F00FF',fg="#FFFFFF",font=("Arial", 10, 'bold'))
    password_label=tk.Label(frame, text="Password", bg='#8F00FF', fg="#FFFFFF", font=("Arial", 10, 'bold'))
    username_entry = tk.Entry (frame, font=("Arial", 10))
    password_entry = tk.Entry(frame, show="*", font=("Arial", 10))
    login_button = tk.Button(frame, text="Login", bg="#DC143C", fg="#FFFFFF", font=("Arial", 10), command=validate_login)
    # signup_button = tk.Button(frame, text="Sign-up", bg="#DC143C", fg="#FFFFFF", font=("Arial", 10), command=validate_login)
    #grid placing
    login_label.grid(row=0, column=0, columnspan=2, sticky="news", pady=20)
    username_label.grid (row=1, column=0)
    username_entry.grid(row=1, column=1, pady=5)
    password_label.grid(row=2, column=0)
    password_entry.grid(row=2, column=1, pady=5)
    login_button.grid(row=3, column=0,columnspan=2, pady=15)
    # signup_button.grid(row=3, column=1, )
    frame.pack()
    login_window.mainloop()

def validate_login():
    global username_entry, password_entry, login_window

    global username
    username = username_entry.get()
    password = password_entry.get()

    with open("user_pass.txt", "r") as file:
        for line in file:
            stored_username, stored_password = line.strip().split()
            if username == stored_username and password == stored_password:
                # Successful login
                messagebox.showinfo("Login Successful", "Welcome, " + username + "!")
                login_window.destroy()
                start_game()
                endScreen(score,username)
                return

    # Invalid login
    messagebox.showerror("Login Failed", "Invalid username or password")

def start_game():
    action = "menu"
    while True:
        if action == "menu":
            action = welcomeScreen(username)
        elif action == "start":
            score = mainGame(username)
            action = endScreen(score,username)
        elif action == "resume":
            # Placeholder code for resume functionality
            print("Resuming the game...")
            action = "menu"  # Go back to the menu after resuming (modify as needed)
        elif action == "level":
            # Placeholder code for level functionality
            print("Changing level...")
            action = "menu"  # Go back to the menu after changing level (modify as needed)
        elif action == "restart":
            score = mainGame(username)
            action = endScreen(score,username)
        else:
            pygame.quit()
            sys.exit()


# Global Variables for the game
FPS = 32
SCREENWIDTH = 289
SCREENHEIGHT = 511
SCREEN = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))
GROUNDY = SCREENHEIGHT * 0.8
GAME_SPRITES = {}
GAME_SOUNDS = {}
PLAYER = 'gallery/sprites/bird.png'
BACKGROUND = 'gallery/sprites/background.png'
PIPE = 'gallery/sprites/pipe.png'
BG = pygame.image.load("fbird(4).jpg")

def get_font(size):
    return pygame.font.Font(pygame.font.get_default_font(), size)

def welcomeScreen(username):
    global difficulty
    difficulty="easy"
    while True:
        MENU_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.blit(BG, (0, 0))
        PLAY_BUTTON = Button(image=pygame.image.load("Options Recting4.png"), pos=(130, 250), 
                            text_input="PLAY", font=get_font(15), base_color="#ffffff", hovering_color="#6aa84f")
        OPTIONS_BUTTON = Button(image=pygame.image.load("Options Recting4.png"), pos=(130, 290), 
                            text_input="LEVELS", font=get_font(13), base_color="#ffffff", hovering_color="#6aa84f")
        INFO_BUTTON = Button(image=pygame.image.load("Options Recting4.png"), pos=(130, 330), 
                            text_input="HELP", font=get_font(15), base_color="#ffffff", hovering_color="#6aa84f")
        QUIT_BUTTON = Button(image=pygame.image.load("Options Recting4.png"), pos=(130, 370), 
                            text_input="QUIT", font=get_font(15), base_color="#ffffff", hovering_color="#6aa84f")

        for button in [PLAY_BUTTON, OPTIONS_BUTTON, INFO_BUTTON,QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN and (event.key == K_SPACE):
                mainGame(username,difficulty)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                        mainGame(username,difficulty)
                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                        levels()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                        pygame.quit()
                        sys.exit()
                if INFO_BUTTON.checkForInput(MENU_MOUSE_POS):
                        infoScreen()

        pygame.display.update()
#this is help screeen info
def infoScreen():
    while True:
        INFO_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.fill((26, 188, 156))  # Set a beautiful background color (RGB values)
        BORDER_COLOR = (189, 195, 199)  # Define a beautiful border color (RGB values)
        BORDER_WIDTH = 5  # Set the border width

        BACK_BUTTON = Button(image=pygame.image.load("Options Recting4.png"), pos=(130, 450), 
                             text_input="BACK", font=get_font(15), base_color="#ffffff", hovering_color="#6aa84f")

        info_text = """How to Play:
        * Press SPACEBAR or PLAY button 
          to make the bird fly upwards.
        * The bird will fall automatically.
          Avoid hitting the pipes.
        * Press p to pause the game,
          press c to continue and q to quit.
        * Click on LEVELS to choose between
          Easy, Medium, and Hard.
        * Click on QUIT to exit the game.
        * Click on PLAY to start the game.

        Have fun and good luck!"""

        font = pygame.font.SysFont("Arial", 17 )
        lines = info_text.split("\n")
        y_offset = 100
        x_offset = 8  # Adjust the left margin

        # Draw the border rectangle around the text
        info_rect_width = max([font.size(line)[0] for line in lines]) + 2 * BORDER_WIDTH
        info_rect_height = len(lines) * 25 + 2 * BORDER_WIDTH
        info_rect = pygame.Rect(x_offset - BORDER_WIDTH, y_offset - BORDER_WIDTH, info_rect_width, info_rect_height)
        pygame.draw.rect(SCREEN, BORDER_COLOR, info_rect)

        for line in lines:
            info_line = font.render(line, True, (0,0,0))
            SCREEN.blit(info_line, (x_offset, y_offset))
            y_offset += 25

        BACK_BUTTON.changeColor(INFO_MOUSE_POS)
        BACK_BUTTON.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if BACK_BUTTON.checkForInput(INFO_MOUSE_POS):
                    return

        pygame.display.update()

#this block is for levels of the game
def levels():
    global difficulty
    while True:
        LEVELS_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.blit(BG, (0, 0))
       
        EASY_BUTTON = Button(image=pygame.image.load("Options Recting4.png"), pos=(130, 250), 
                            text_input="EASY",font=get_font(15), base_color="#ffffff", hovering_color="#6aa84f")
        MEDIUM_BUTTON = Button(image=pygame.image.load("Options Recting4.png"), pos=(130, 290), 
                            text_input="MEDIUM", font=get_font(15), base_color="#ffffff", hovering_color="#6aa84f")
        HARD_BUTTON = Button(image=pygame.image.load("Options Recting4.png"), pos=(130, 330), 
                            text_input="HARD", font=get_font(15), base_color="#ffffff", hovering_color="#6aa84f")
        BACK_BUTTON = Button(image=pygame.image.load("Options Recting4.png"), pos=(130, 370), 
                            text_input="BACK", font=get_font(15), base_color="#ffffff", hovering_color="#6aa84f")

        for button in [EASY_BUTTON, MEDIUM_BUTTON, HARD_BUTTON, BACK_BUTTON]:
            button.changeColor(LEVELS_MOUSE_POS)
            button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if EASY_BUTTON.checkForInput(LEVELS_MOUSE_POS):
                    # global difficulty  
                    difficulty = 'easy'
                    mainGame(username,difficulty)   
                if MEDIUM_BUTTON.checkForInput(LEVELS_MOUSE_POS):
                    difficulty = 'medium'
                    mainGame(username,difficulty)
                if HARD_BUTTON.checkForInput(LEVELS_MOUSE_POS):
                    difficulty = 'hard'
                    mainGame(username,difficulty)
                if BACK_BUTTON.checkForInput(LEVELS_MOUSE_POS):
                    return

        pygame.display.update()


def mainGame(username,difficulty="easy"):
    
    score = 0
    playerx = int(SCREENWIDTH/5)
    playery = int(SCREENWIDTH/2)
    basex = 0

    # Create 2 pipes for blitting on the screen
    newPipe1 = getRandomPipe(difficulty)
    newPipe2 = getRandomPipe(difficulty)

    # my List of upper pipes
    upperPipes = [
        {'x': SCREENWIDTH+200, 'y': newPipe1[0]['y']},
        {'x': SCREENWIDTH+200+(SCREENWIDTH/2), 'y': newPipe2[0]['y']},
    ]
    # my List of lower pipes
    lowerPipes = [
        {'x': SCREENWIDTH+200, 'y': newPipe1[1]['y']},
        {'x': SCREENWIDTH+200+(SCREENWIDTH/2), 'y': newPipe2[1]['y']},
    ]

    pipeVelX = -4

    # Game difficulty settings
    if difficulty == "easy":
        playerVelY = -6
        pipeVelX =-4
    elif difficulty == "medium":
        playerVelY = -9
        pipeVelX = -6
    elif difficulty == "hard":
        playerVelY = -12
        pipeVelX = -8

    playerMaxVelY = 10
    playerMinVelY = -8
    playerAccY = 1

    playerFlapAccv = -8
    playerFlapped = False

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_p:
                    # Pause the game
                    pause()
                
                elif event.key == K_SPACE or event.key == K_UP:
                    # Handle jump/flap logic
                    if playery > 0:
                        playerVelY = playerFlapAccv
                        playerFlapped = True
                        GAME_SOUNDS['wing'].play()
        
        
        crashTest = isCollide(playerx, playery, upperPipes, lowerPipes)
        if crashTest:
            endScreen(score,username)
            return score
        
        if difficulty == 'easy' or difficulty == 'medium':
            playerMidPos = playerx + GAME_SPRITES['player'].get_width()/2
            for pipe in upperPipes:
                pipeMidPos = pipe['x'] + GAME_SPRITES['pipe'][0].get_width()/2
                if pipeMidPos <= playerMidPos < pipeMidPos + 4:
                    score += 1
                    GAME_SOUNDS['point'].play()
                    print(f"Your score is {score}")

        if difficulty == 'hard':
            playerMidPos = playerx + GAME_SPRITES['player'].get_width()/2
            for pipe in upperPipes:
                pipeMidPos = pipe['x'] + GAME_SPRITES['pipe'][0].get_width()/2
                if pipeMidPos <= playerMidPos < pipeMidPos + 10:
                    score += 1
                    GAME_SOUNDS['point'].play()
                    print(f"Your score is {score}")            

        if playerVelY < playerMaxVelY and not playerFlapped:
            playerVelY += playerAccY

        if playerFlapped:
            playerFlapped = False

        playerHeight = GAME_SPRITES['player'].get_height()
        playery = playery + min(playerVelY, GROUNDY - playery - playerHeight)

        # move pipes to the left
        for upperPipe, lowerPipe in zip(upperPipes, lowerPipes):
            upperPipe['x'] += pipeVelX
            lowerPipe['x'] += pipeVelX

        # Add a new pipe when the first is about to cross the leftmost part of the screen
        if difficulty == 'easy' or difficulty == 'hard':
            if 0 < upperPipes[0]['x'] < 5:   
                newpipe = getRandomPipe(difficulty)
                upperPipes.append(newpipe[0])
                lowerPipes.append(newpipe[1])

        if difficulty == 'medium':
            if 4 < upperPipes[0]['x'] < 10:   
                newpipe = getRandomPipe(difficulty)
                upperPipes.append(newpipe[0])
                lowerPipes.append(newpipe[1])        

        # if the pipe is out of the screen, remove it
        if upperPipes[0]['x'] < -GAME_SPRITES['pipe'][0].get_width():
            upperPipes.pop(0)
            lowerPipes.pop(0)

        SCREEN.blit(GAME_SPRITES['background'], (0, 0))
        for upperPipe, lowerPipe in zip(upperPipes, lowerPipes):
            SCREEN.blit(GAME_SPRITES['pipe'][0], (upperPipe['x'], upperPipe['y']))
            SCREEN.blit(GAME_SPRITES['pipe'][1], (lowerPipe['x'], lowerPipe['y']))

        SCREEN.blit(GAME_SPRITES['base'], (basex, GROUNDY))
        SCREEN.blit(GAME_SPRITES['player'], (playerx, playery))

        myDigits = [int(x) for x in list(str(score))]
        width = 0
        for digit in myDigits:
            width += GAME_SPRITES['numbers'][digit].get_width()
            Xoffset = (SCREENWIDTH - width) / 2

        for digit in myDigits:
            SCREEN.blit(GAME_SPRITES['numbers'][digit], (Xoffset, SCREENHEIGHT*0.12))
            Xoffset += GAME_SPRITES['numbers'][digit].get_width()

        FPSCLOCK.tick(FPS)
        pygame.display.update()
       

def isCollide(playerx, playery, upperPipes, lowerPipes):
    if playery> GROUNDY - 25  or playery<0:
        GAME_SOUNDS['hit'].play()
        return True
       
    for pipe in upperPipes:
        pipeHeight = GAME_SPRITES['pipe'][0].get_height()
        if(playery < pipeHeight + pipe['y'] and abs(playerx - pipe['x']) < GAME_SPRITES['pipe'][0].get_width()):
            GAME_SOUNDS['hit'].play()
            return True
        

    for pipe in lowerPipes:
        if (playery + GAME_SPRITES['player'].get_height() > pipe['y']) and abs(playerx - pipe['x']) < GAME_SPRITES['pipe'][0].get_width():
            GAME_SOUNDS['hit'].play()
            return True 
        
    return False

def getRandomPipe(difficulty ='easy'):
    pipeHeight = GAME_SPRITES['pipe'][0].get_height()
    offset = SCREENHEIGHT / 3

    if difficulty == 'easy':
        # For easy difficulty, generate random heights for the pipes within a smaller range
        y2 = offset + random.randrange(0, int(SCREENHEIGHT * 0.4))
    elif difficulty == 'medium':
        # For medium difficulty, generate random heights for the pipes within a medium range
        y2 = offset + random.randrange(0, int(SCREENHEIGHT * 0.6))
    else:
        # For hard difficulty, generate random heights for the pipes within a larger range
        y2 = offset + random.randrange(0, int(SCREENHEIGHT - GAME_SPRITES['base'].get_height() - 1.2 * offset))

    pipeX = SCREENWIDTH + 10
    y1 = pipeHeight - y2 + offset

    pipe = [
        {'x': pipeX, 'y': -y1},  # Upper Pipe
        {'x': pipeX, 'y': y2}  # Lower Pipe
    ]

    return pipe

# Global variable to keep track of the highest score

paused = False
def pause():
    
    paused = True
    while paused:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    paused = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()

        pygame.display.set_caption('Paused')
        font = pygame.font.SysFont("Arial", 35)
        display_paused = font.render("Game paused", True, "black")
        SCREEN.blit(display_paused,(48,17))
        font = pygame.font.SysFont("Arial", 20)
        display_paused = font.render("Press c to continue or q to quit", True, "black")
        SCREEN.blit(display_paused,(24,400))
        pygame.display.update()


def endScreen(score,username):
    
    global highest_score,SCORE_FILE
    SCORE_FILE = f'{username}.txt'
    # global username_entry  # Make sure the username_entry is accessible here

    # Debug print statements
    print("DEBUG: Inside endScreen")
    print("DEBUG: username_entry =", username)

    if os.path.exists(SCORE_FILE):
        with open(SCORE_FILE, "r") as file:
            highest_score = int(file.read())

    SCREEN.fill((0, 0, 0))

    # Update the highest score if the current score is higher
    if score > highest_score:
        highest_score = score
        print(highest_score)
        # Save the new highest score to the file
        with open(SCORE_FILE, "w") as file:
            file.write(str(highest_score))
       
    
    # Clear the screen
    # SCREEN.fill((0, 0, 0))

    # Display the total score and highest score
    font = pygame.font.Font(None, 40)
    font1 = pygame.font.Font(None, 60)
    font2 = pygame.font.Font(None, 30 )
    over_text = font1.render(f"Game Over", True, (255,0,0))
    over_rect = over_text.get_rect(center=(SCREENWIDTH // 2, SCREENHEIGHT // 2 - 220))
    highest_score_text = font2.render(f"{username} Highest Score: {highest_score}", True, (255, 255, 255))
    highest_score_rect = highest_score_text.get_rect(center=(SCREENWIDTH // 2, SCREENHEIGHT // 2-110))
    score_text = font.render(f"Total Score: {score}", True, (255, 255, 255))
    score_rect = score_text.get_rect(center=(SCREENWIDTH // 2, SCREENHEIGHT // 2 - 70))
    SCREEN.blit(over_text, over_rect)
    SCREEN.blit(highest_score_text, highest_score_rect)
    SCREEN.blit(score_text, score_rect)

    # Create buttons
    back_to_menu_button = pygame.Rect(70, 300, 150, 50)
    restart_button = pygame.Rect(70, 360, 150, 50)
    quit_button = pygame.Rect(70, 420, 150, 50)

    # Draw buttons
    pygame.draw.rect(SCREEN, (255, 0, 0), back_to_menu_button)
    pygame.draw.rect(SCREEN, (255, 0, 0), restart_button)
    pygame.draw.rect(SCREEN, (255, 0, 0), quit_button)

    # Text on buttons
    font = pygame.font.Font(None, 30)
    back_text = font.render("Back to Menu", True, (255, 255, 255))
    restart_text = font.render("Restart", True, (255, 255, 255))
    quit_text = font.render("Quit", True, (255, 255, 255))
    SCREEN.blit(back_text, (80, 310))
    SCREEN.blit(restart_text, (80, 370))
    SCREEN.blit(quit_text, (80, 430))

    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Check if the mouse click is on any button
                if back_to_menu_button.collidepoint(event.pos):
                    # return "menu"
                    welcomeScreen(username)
                elif restart_button.collidepoint(event.pos):
                    # return "restart"
                    mainGame(username,difficulty)
                elif quit_button.collidepoint(event.pos):
                    print(highest_score)
                    pygame.quit()
                    sys.exit()


if __name__ == "__main__":
    # pygame.init()
    # FPSCLOCK = pygame.time.Clock()
    # pygame.display.set_caption('Flappy Bird')
    # This will be the main point from where our game will start
    pygame.init() # Initialize all pygame's modules
    FPSCLOCK = pygame.time.Clock()
    pygame.display.set_caption('Flappy Bird')
    GAME_SPRITES['numbers'] = ( 
        pygame.image.load('gallery/sprites/0.png').convert_alpha(),
        pygame.image.load('gallery/sprites/1.png').convert_alpha(),
        pygame.image.load('gallery/sprites/2.png').convert_alpha(),
        pygame.image.load('gallery/sprites/3.png').convert_alpha(),
        pygame.image.load('gallery/sprites/4.png').convert_alpha(),
        pygame.image.load('gallery/sprites/5.png').convert_alpha(),
        pygame.image.load('gallery/sprites/6.png').convert_alpha(),
        pygame.image.load('gallery/sprites/7.png').convert_alpha(),
        pygame.image.load('gallery/sprites/8.png').convert_alpha(),
        pygame.image.load('gallery/sprites/9.png').convert_alpha(),
    )

    # GAME_SPRITES['message'] =pygame.image.load('gallery/sprites/message.png').convert_alpha()
    GAME_SPRITES['base'] =pygame.image.load('gallery/sprites/base.png').convert_alpha()
    GAME_SPRITES['pipe'] =(pygame.transform.rotate(pygame.image.load( PIPE).convert_alpha(), 180), 
    pygame.image.load(PIPE).convert_alpha()
    )

    # Game sounds
    GAME_SOUNDS['die'] = pygame.mixer.Sound('gallery/audio/die.wav')
    GAME_SOUNDS['hit'] = pygame.mixer.Sound('gallery/audio/hit.wav')
    GAME_SOUNDS['point'] = pygame.mixer.Sound('gallery/audio/point.wav')
    GAME_SOUNDS['swoosh'] = pygame.mixer.Sound('gallery/audio/swoosh.wav')
    GAME_SOUNDS['wing'] = pygame.mixer.Sound('gallery/audio/wing.wav')

    GAME_SPRITES['background'] = pygame.image.load(BACKGROUND).convert()
    GAME_SPRITES['player'] = pygame.image.load(PLAYER).convert_alpha()

    action = "menu"
    login_screen()
    while True:
        if action == "menu":
            action = welcomeScreen(username)
        elif action == "start":
            score = mainGame(username_entry)
            action = endScreen(score,username)
        elif action == "resume":
            # Placeholder code for resume functionality
            print("Resuming the game...")
            action = "menu"  # Go back to the menu after resuming (modify as needed)
        elif action == "level":
            # Placeholder code for level functionality
            print("Changing level...")
            action = "menu"  # Go back to the menu after changing level (modify as needed)
        elif action == "restart":
            score = mainGame(username)
            action = endScreen(score,username)
        else:
            pygame.quit()
            sys.exit()
    login_screen()



    