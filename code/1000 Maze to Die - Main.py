import pygame
import math
from sys import exit
import levels
import random
import tkinter
from tkinter import messagebox

pygame.init()

#game settings ==========================================================================================================================================
height = 768
width = 1024
playerSize = 0.32
tileSize = 64
playerSpeed = 5
diagSpeed = math.sqrt(2)
meleeSize = 0.25
enemySpeed = 2
rangedSize = 0.35
weaponCooldown = 15
bulletSpeed = 10
bulletTime = 1
bulletSize = 2
enemyCooldown = 30
playerHealth = 100
meleeDamage = 24
invincibilityFrames = 1
foodSize = 0.15
rangedDamage = 10
maxEnergy = 100
currentEnergy = maxEnergy
energyDepletion = 0.04
score = 0
WHITE = (255, 255, 255)
GREY = (150, 150, 150)
BLUE = (65, 105, 225)
collectibleSize = 0.4
portalSize = 1
username = ""
totalScore = 0

#Setting up pygame window
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("1000 maze to die")
clock = pygame.time.Clock()

#Level select
levelList = [levels.first_level, levels.second_level]
current_level = levelList[0]

#Menus ==========================================================================================================================================

#PLACEHOLDER MENUS
def controls_menu():
    print("placeholder")

def leaderboard_menu():
    print("placeholder")


#Define font for menu text
menu_font = pygame.font.Font(None, 36)
title_font = pygame.font.Font(None, 50)

#Button define
start_button = pygame.Rect(width // 2 - 100, height // 2 - 100, 200, 50)
leaderboard_button = pygame.Rect(width // 2 - 100, height // 2 - 30, 200, 50)
controls_button = pygame.Rect(width // 2 - 100, height // 2 + 40, 200, 50)
main_menu_quit_button = pygame.Rect(width // 2 - 100, height // 2 + 110, 200, 50)

#Main menu define
main_menu_text = title_font.render("1000 Maze to Die", True, WHITE)
controls_text = menu_font.render("Controls", True, WHITE)
start_text = menu_font.render("Start", True, WHITE)
leaderboard_text = menu_font.render("Leaderboard", True, WHITE)
quit_text = menu_font.render("Quit", True, WHITE)


#Main menus
def display_main_menu():
    #Clear the screen
    screen.fill((80, 80, 80))
    #Display main menu text
    screen.blit(main_menu_text, (width // 2 - main_menu_text.get_width() // 2,
                                 height // 4 - main_menu_text.get_height() // 2))
    #Draw start game button
    pygame.draw.rect(screen, BLUE, start_button)
    screen.blit(start_text, (start_button.x + start_button.width // 2 - start_text.get_width() // 2,
                             start_button.y + start_button.height // 2 - start_text.get_height() // 2))
    #Draw leaderboard button
    pygame.draw.rect(screen, BLUE, leaderboard_button)
    screen.blit(leaderboard_text, (leaderboard_button.x + leaderboard_button.width // 2 - leaderboard_text.get_width() // 2,
                                   leaderboard_button.y + leaderboard_button.height // 2 - leaderboard_text.get_height() // 2))
    #Draw controls button
    pygame.draw.rect(screen, BLUE, controls_button)
    screen.blit(controls_text, (controls_button.x + controls_button.width // 2 - controls_text.get_width() // 2,
                                controls_button.y + controls_button.height // 2 - controls_text.get_height() // 2))
    #Draw quit button
    pygame.draw.rect(screen, BLUE, main_menu_quit_button)
    screen.blit(quit_text, (main_menu_quit_button.x + main_menu_quit_button.width // 2 - quit_text.get_width() // 2,
                            main_menu_quit_button.y + main_menu_quit_button.height // 2 - quit_text.get_height() // 2))
    #Update the display
    pygame.display.flip()

def main_menu(currentScore):
    while True:
        display_main_menu()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                #Check if start game button is clicked
                if start_button.collidepoint(mouse_pos):
                    return
                #Check if leaderboard button is clicked
                elif leaderboard_button.collidepoint(mouse_pos):
                    leaderboard_menu(currentScore)
                #Check if controls button is clicked
                elif controls_button.collidepoint(mouse_pos):
                    controls_menu(currentScore)
                #Check if quit button is clicked
                elif main_menu_quit_button.collidepoint(mouse_pos):
                    pygame.quit()
                    exit()

#Define controls text and buttons
controls_title = title_font.render("Controls", True, WHITE)
back_text = menu_font.render("Back", True, WHITE)
back_button = pygame.Rect(width // 2 - 100, height // 2 + 130, 200, 50)

def display_controls_menu():
    screen.fill((80, 80, 80))
    #Display controls title
    screen.blit(controls_title, (width // 2 - controls_title.get_width() // 2,
                                 height // 4 - controls_title.get_height() // 2))
    #Render and blit controls
    up_text = menu_font.render("Up: W", True, WHITE)
    screen.blit(up_text, (width // 2 - up_text.get_width() // 2, height // 4 + 40))
    down_text = menu_font.render("Down: S", True, WHITE)
    screen.blit(down_text, (width // 2 - down_text.get_width() // 2, height // 4 + 80))
    left_text = menu_font.render("Left: A", True, WHITE)
    screen.blit(left_text, (width // 2 - left_text.get_width() // 2, height // 4 + 120))
    right_text = menu_font.render("Right: D", True, WHITE)
    screen.blit(right_text, (width // 2 - right_text.get_width() // 2, height // 4 + 160))
    fire_text = menu_font.render("Fire: Left Mouse or Space Bar", True, WHITE)
    screen.blit(fire_text, (width // 2 - fire_text.get_width() // 2, height // 4 + 200))
    break_wall_text = menu_font.render("Break secret walls by firing bullets at them until they break", True, WHITE)
    screen.blit(break_wall_text, (width // 2 - break_wall_text.get_width() // 2, height // 4 + 260))
    #Draw return button
    pygame.draw.rect(screen, BLUE, back_button)
    screen.blit(back_text, (back_button.x + back_button.width // 2 - back_text.get_width() // 2,
                            back_button.y + back_button.height // 2 - back_text.get_height() // 2))
    pygame.display.flip()
    
def controls_menu(currentScore):
    while True:
        display_controls_menu()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                #Check if return button is clicked
                if back_button.collidepoint(mouse_pos):
                    main_menu(currentScore)
                    return

def scores_only(username_and_scores):
    #returns part of line which is the score
    return username_and_scores[1]

def leaderboard_menu(currentScore):
    while True:
        screen.fill((80, 80, 80))
        #Display leaderboard title
        leaderboard_title = title_font.render("Leaderboard", True, WHITE)
        screen.blit(leaderboard_title, (width // 2 - leaderboard_title.get_width() // 2,
                                        height // 4 - leaderboard_title.get_height() // 2))
        
        #Open the leaderboard file in read mode
        lb = open("leaderboard.txt", "r")
        #Initialize variables to track the top three scores
        top_scores = []
        #Iterate over each line in the file
        for line in lb:
            #Split the line into fields
            fields = line.split(";")
            #Assuming the fields are username and score
            username = fields[0]
            score = int(fields[2].strip()) #Strip removes whitespace
            top_scores.append((username, score))
            
        #Sort the top_scores list based on the score (highest first)
        top_scores_only = scores_only #Gets the scores separate from username
        #sort method will internally call compare_scores for each pair for order
        top_scores.sort(key=top_scores_only, reverse = True)
            
        #Display the top three scores using [:5] (everything up to third index)
        for i, (username, score) in enumerate(top_scores[:5]): #enumerate iterates and gets index of each element and element
            score_text = menu_font.render(f"{i+1}. {username}: {score}", True, WHITE)
            screen.blit(score_text, (width // 2 - score_text.get_width() // 2,
                                         height // 4 + 40 + i*40))
        lb.close()
        
        #Display the current user's high score
        current_score_text = menu_font.render(f"Your High Score: {currentScore}", True, WHITE)
        screen.blit(current_score_text, (width // 2 - current_score_text.get_width() // 2,
                                         height // 4 + 260))
        
        #Draw back button
        pygame.draw.rect(screen, BLUE, back_button)
        screen.blit(back_text, (back_button.x + back_button.width // 2 - back_text.get_width() // 2,
                                back_button.y + back_button.height // 2 - back_text.get_height() // 2))
        
        pygame.display.flip()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                # Check if back button is clicked
                if back_button.collidepoint(mouse_pos):
                    main_menu(currentScore)
                    return

#Login
window = tkinter.Tk()
window.title("1000 maze to die")
window.geometry('1024x768')
window.configure(bg="#505050")
window.protocol("WM_DELETE_WINDOW", quit)


def login():
    print("login")
    #Opens file
    lb = open("leaderboard.txt", "r")
    #Iterates through lines
    for line in lb:
      #Splits lines at semicolons
        fields = line.split(";")
        #Checks if the fields match the text inputted
        if username_entry.get()== fields[0] and password_entry.get()== fields[1]:
            messagebox.showinfo(title="Access Granted", message="Login Successful")
            window.destroy()
            lb.close()
            global username
            username = fields[0]
            currentScore = fields[2]
            main_menu(currentScore)
            return
    #Displays message none of the fields are the same
    messagebox.showerror(title="Error", message="Access Denied")
    lb.close()

def register():
    lenUser = len(username_entry.get())
    lenPass = len(password_entry.get())
    lb = open("leaderboard.txt", "a")
    if lenUser < 1 or lenPass < 1:
        messagebox.showinfo(title="Error", message="You must enter and username and password")
    elif lenUser > 13:
        messagebox.showinfo(title="Error", message="The username must be no longer than 13 characters")
    elif lenPass > 20:
        messagebox.showinfo(title="Error", message="Please shorten your password")
    elif lenPass < 8:
        messagebox.showinfo(title="Error", message="Please makwe your password longer")
    else:
        lb.write(f"\n{username_entry.get()};{password_entry.get()};0")
        messagebox.showinfo(title="Success", message="You have now registered your account")
    lb.close()

#Initiliases tkinter login screen
frame = tkinter.Frame(bg="#505050")
frame2 = tkinter.Frame(bg="#505050")
login_label = tkinter.Label(frame, text="Login", bg="#505050", fg="white", font=(None, 50))
username_label = tkinter.Label(frame, text="Username:", bg="#505050", fg="white", font=(None, 30))
username_entry = tkinter.Entry(frame, font=(None, 30))
password_entry = tkinter.Entry(frame, show="*", font=(None, 30))
password_label = tkinter.Label(frame, text="Password:", bg="#505050", fg="white", font=(None, 30))
login_button = tkinter.Button(frame2, text="Login", bg="royal blue", fg="white", font=(None, 30), width=8, command=login)
register_button = tkinter.Button(frame2, text="Register", bg="royal blue", fg="white", font=(None, 30), width=8, command=register)

login_label.grid(row=0, column=0, columnspan=2, sticky="news", pady=110)
username_label.grid(row=1, column=0)
username_entry.grid(row=1, column=1, pady=5)
password_label.grid(row=2, column=0)
password_entry.grid(row=2, column=1, pady=37.5)
login_button.grid(row=3, column=1,pady= 100)
register_button.grid(row=3, column=0, pady=100, padx=25)

frame.pack()
frame2.pack()
window.mainloop()

#In-game menus

#Define buttons for retry and quit
retry_button = pygame.Rect(width // 2 - 61.5, height // 2 + 20, 125, 50)
quit_button = pygame.Rect(width // 2 - 61.5, height // 2 + 90, 125, 50)

#Define text for buttons
retry_text = menu_font.render("Retry", True, WHITE)
quit_text = menu_font.render("Quit", True, WHITE)

#Define game over text
game_over_text = menu_font.render("Game Over", True, WHITE)

#Game over menu
def display_game_over_screen():
    #Clear the screen
    screen.fill((80, 80, 80))
    #Display game over text
    screen.blit(game_over_text, (width // 2 - game_over_text.get_width() // 2,
                                 height // 2 - game_over_text.get_height() // 2))
    #Draw retry button
    pygame.draw.rect(screen, BLUE, retry_button)
    screen.blit(retry_text, (retry_button.x + retry_button.width // 2 - retry_text.get_width() // 2,
                             retry_button.y + retry_button.height // 2 - retry_text.get_height() // 2))
    #Draw quit button
    pygame.draw.rect(screen, BLUE, quit_button)
    screen.blit(quit_text, (quit_button.x + quit_button.width // 2 - quit_text.get_width() // 2,
                            quit_button.y + quit_button.height // 2 - quit_text.get_height() // 2))
    #Update the display
    pygame.display.flip()

def game_over_menu():
    for item in noPlayerGroup:
        item.kill()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                # Check if retry button is clicked
                if retry_button.collidepoint(mouse_pos):
                    player1.setStartPosition()
                    player1.health = playerHealth
                    player1.currentEnergy = maxEnergy
                    player1.speed = playerSpeed
                    spawn_sprites()
                    return
                # Check if quit button is clicked
                elif quit_button.collidepoint(mouse_pos):
                    pygame.quit()
                    exit()
        # Display the menu screen
        display_game_over_screen()

#Draw continue button
continue_button = pygame.Rect(width // 2 - 61.5, height // 2 + 20, 125, 50)

#Define text
next_level_text = menu_font.render("You've reached the next level!", True, WHITE)
continue_text = menu_font.render("Next Level", True, WHITE)
score_menu_text = menu_font.render(f"Your score was: {score}", True, WHITE) #Problem was score was defined as zero and then this was defined so always remained as 0

def display_next_level_screen():
    #fixed score 0 problem
    score_menu_text = menu_font.render(f"Your score was: {score}", True, WHITE)
    #Clear the screen
    screen.fill((80, 80, 80))
    #Draw continue button
    pygame.draw.rect(screen, BLUE, continue_button)
    #Display next level text
    screen.blit(next_level_text, (width // 2 - next_level_text.get_width() // 2,
                                  height // 2 - 50 - next_level_text.get_height() // 2))
    screen.blit(score_menu_text, (width // 2 - score_menu_text.get_width() // 2,
                                  height // 2 - score_menu_text.get_height() // 2))
    screen.blit(continue_text, (continue_button.x + continue_button.width // 2 - continue_text.get_width() // 2,
                                continue_button.y + continue_button.height // 2 - continue_text.get_height() // 2))
    pygame.draw.rect(screen, BLUE, quit_button)
    screen.blit(quit_text, (quit_button.x + quit_button.width // 2 - quit_text.get_width() // 2,
                            quit_button.y + quit_button.height // 2 - quit_text.get_height() // 2))
    #Update the display
    pygame.display.flip()


def next_level_menu():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                #Check if continue button is clicked
                if continue_button.collidepoint(mouse_pos):
                    return
                elif quit_button.collidepoint(mouse_pos):
                    pygame.quit()
                    exit()
        #Display the menu screen
        display_next_level_screen()

#Define main menu button and text and redefine quit
main_menu_text = menu_font.render("Main Menu", True, WHITE)
main_menu_button = pygame.Rect(width // 2 - 64.5, height // 2 + 20, 135, 50)
new_quit_button = pygame.Rect(width // 2 - 64.5, height // 2 + 90, 135, 50)


def display_final_score_screen(totalScore):
    global username
    #Clear the screen
    screen.fill((80, 80, 80))
    updated_lines = []
    lb = open("leaderboard.txt", "r")
    #Iterate over the lines to find and update the score for the specified user
    for line in lb:
        fields = line.split(";")
        if fields[0] == username:
            #Update the score if the new score is higher
            if int(fields[2]) < totalScore:
                fields[2] = str(totalScore)
                updated_lines.append(";".join(fields) + "\n")
            else:
                updated_lines.append(line)
        else:
            updated_lines.append(line)
    int(totalScore)
    lb.close()

    #Rewrite the contents of the text file with the updated score
    lb = open("leaderboard.txt", "w")
    lb.writelines(updated_lines)
    lb.close()
    #Defines final score text
    final_score_text = menu_font.render(f"Final Score: {totalScore}", True, WHITE)    
    #Display final score text
    screen.blit(final_score_text, (width // 2 - final_score_text.get_width() // 2,
                                   height // 2 - final_score_text.get_height() // 2))
    #Draw main menu button
    pygame.draw.rect(screen, BLUE, main_menu_button)
    screen.blit(main_menu_text, (main_menu_button.x + main_menu_button.width // 2 - main_menu_text.get_width() // 2,
                            main_menu_button.y + main_menu_button.height // 2 - main_menu_text.get_height() // 2))
    #Draw exit game button
    pygame.draw.rect(screen, BLUE, new_quit_button)
    screen.blit(quit_text, (new_quit_button.x + new_quit_button.width // 2 - quit_text.get_width() // 2,
                            new_quit_button.y + new_quit_button.height // 2 - quit_text.get_height() // 2))
    #Update the display
    pygame.display.flip()

def final_score_menu(totalScore):
    while True:
        #Display the final score menu
        display_final_score_screen(totalScore)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                #Check if exit game button is clicked
                if new_quit_button.collidepoint(mouse_pos):
                    pygame.quit()
                    exit()
                if main_menu_button.collidepoint(mouse_pos):
                    main_menu(totalScore)

#Gameplay ==========================================================================================================================================

def update_score(points):
  global score
  score = score + points

def display_score():
  score_font = pygame.font.Font(None, 36)
  score_text = score_font.render(f'Score: {score}', True, WHITE)
  screen.blit(score_text, (10, 10))

class player(pygame.sprite.Sprite):
    def __init__(self):
        #Calls the parent class for inheritence
        super().__init__()
        #convert alpha helps with performance
        self.image = pygame.transform.rotozoom(pygame.image.load("0.png").convert_alpha(), 0, playerSize)
        self.baseImage = self.image
        #set up start position coordinates
        self.startPosition = (0,0)
        self.rect = self.baseImage.get_rect(center = self.startPosition)
        self.drawRect = self.rect.copy()
        self.speed = playerSpeed
        #Whether the player is shooting or not
        self.shoot = False
        self.attackCooldown = 15
        #Health bar
        self.health = playerHealth
        #Incibility cooldown
        self.invincibilityCooldown = 0
        self.invincibilityDuration = invincibilityFrames
        #Mask hitbox
        self.mask = pygame.mask.from_surface(self.image)
        #Energy System
        self.maxEnergy = maxEnergy
        self.currentEnergy = self.maxEnergy

    def setPosition(self, x, y):
        self.startPosition.x = x
        self.startPosition.y = y
        self.rect.x = x
        self.rect.y = y

    def setStartPosition(self):
        for rowIndex, row in enumerate(current_level):
            for colIndex, char in enumerate(row):
                if char == 'P':
                    self.startPosition = pygame.math.Vector2((colIndex * tileSize, rowIndex * tileSize))
                    self.setPosition(self.startPosition.x, self.startPosition.y)
                    print(self.startPosition)

    #Rotation to cursor
    def rotation(self):
        #Gets location of mouse coordinates
        self.cursorPosition = pygame.mouse.get_pos()
        #Makes the cursor position relative to the center of the scree (where the player is)
        self.changedCursorx = (self.cursorPosition[0] - width //2)
        self.changedCursory = (self.cursorPosition[1] - height //2)
        #Angle of rotation
        self.angle = math.degrees(math.atan2(self.changedCursory, self.changedCursorx))
        #rotates image to now be facing the cursor
        self.image = pygame.transform.rotate(self.baseImage, -self.angle)
        #Center player rectangle onto hitbox rectangle
        self.drawRect
        #Updates the mask hitbox
        self.mask = pygame.mask.from_surface(self.image)

    def input(self):
        #sets speed to 0 as no keys have been pressed
        self.velocityx = 0
        self.velocityy = 0
        #Any key pressed pressed by user will be stored in keys
        keys = pygame.key.get_pressed()

        #shows how the keys pressed affects movement (move up or down in a negative or positive direction)
        if keys[pygame.K_w]:
          self.velocityy = -self.speed
        if keys[pygame.K_a]:
          self.velocityx = -self.speed
        if keys[pygame.K_s]:
          self.velocityy = self.speed
        if keys[pygame.K_d]:
          self.velocityx = self.speed
        #due to pythagorus if moving diagnoally the player will be quicker so this fixes it
        if self.velocityx != 0 and self.velocityy != 0:
          self.velocityx = self.velocityx / diagSpeed
          self.velocityy = self.velocityy / diagSpeed

        #Attack
        if pygame.mouse.get_pressed() == (1, 0, 0) or keys[pygame.K_SPACE]: #(1, 0, 0) is left click)
          self.shoot = True
          self.shooting()
        else:
          self.shoot = False


    def checkCollision(self, x ,y):
        #Check if the next position collides with a wall
        row = int(y/tileSize)
        col = int(x/tileSize)
        if current_level[row][col] == "X" or current_level[row][col] == "S":
          return True
        else:
          return False

    def collide_mask(self, other):
        # Override collide_mask method
        return pygame.sprite.collide_mask(self, other)

    def move(self):
        #Calculate next position based on velocity
        newPosition = self.startPosition + pygame.math.Vector2(self.velocityx, self.velocityy)
        #check collision with walls
        if not self.checkCollision(newPosition.x, newPosition.y):
          #Find what tile they're on
          tileType = current_level[int(newPosition.y / tileSize)][int(newPosition.x / tileSize)]
          #If there's a collision with ice terrain, simulate sliding
          if tileType == "B":
            self.startPosition = newPosition
            self.startPosition.x += self.velocityx * 0.75
            self.startPosition.y += self.velocityy * 0.75
          if tileType == "T":
            self.startPosition.x += self.velocityx * 0.5
            self.startPosition.y += self.velocityy * 0.5
            self.damageTaken(8)
          else:
              self.startPosition = newPosition
          #update hitbox
          self.rect.center = self.startPosition
          self.drawrect = self.rect.center
          
    def shooting(self):
        #delay between bullets
        if self.attackCooldown == 0:
          self.attackCooldown = weaponCooldown
          #Make the psawn location infront of the the player
          spawnOffset = pygame.math.Vector2(45,20)
          spawnPos = self.startPosition + spawnOffset.rotate(self.angle)
          #Setting variable so the bullet instance has position vectors
          spawnLocationx = spawnPos[0]
          spawnLocationy = spawnPos[1]
          #Create instance of bullet
          self.bullet = bullet(spawnLocationx, spawnLocationy, self.angle)
          #Adding bullets to groups
          spriteGroup.add(self.bullet)
          bulletGroup.add(self.bullet)
          noPlayerGroup.add(self.bullet)

    def damageTaken(self, damage):
        if self.invincibilityCooldown <= 0:
          self.health = self.health - damage
          print("damage")
          if self.health <= 0:
            print("dead")
          else:
            #Make player image red
            self.image.fill((255, 0, 0), special_flags=pygame.BLEND_RGB_MULT)
            #Schedule normal image after a delay
            pygame.time.set_timer(pygame.USEREVENT, 400)
            #Invinciblity
            self.invincibilityCooldown = int(self.invincibilityDuration * 60) #converts seconds to frames

    def draw_healthBar(self):
        #Calculate the position of the health bar relative to the player center and camera offset
        barPos_x = self.rect.centerx - playerHealth // 4 + camera_offset.x
        barPos_y = self.rect.y - 10 + camera_offset.y  # Adjusted to be above the player
        #Sets health bar to red
        pygame.draw.rect(screen, (255, 0, 0), (barPos_x, barPos_y, playerHealth // 2, 5))
        #Makes it so the current health is shown on the red bar as green
        remainingHealth = int(self.health)
        #Draws green part
        pygame.draw.rect(screen, (0, 255, 0), (barPos_x, barPos_y, remainingHealth // 2, 5))

    def eat(self):
        self.health += 40
        if self.health > 100:
          self.health = 100
        self.currentEnergy = self.maxEnergy
        self.speed = playerSpeed
      
    def energyDepletion(self):
        self.currentEnergy -= energyDepletion
        if self.currentEnergy <= 0:
            self.speed = playerSpeed // 2

    def draw_energyBar(self):
        width = 100
        height = 10
        pos_x = 10
        pos_y = 750
        #Draw background
        pygame.draw.rect(screen, (100, 100, 100), (pos_x, pos_y, width, height))
        #Width of filled part of the bar
        fill_width = int((self.currentEnergy / self.maxEnergy) * width)
        #Draw the filled part of the energy bar
        pygame.draw.rect(screen, (255, 255, 0), (pos_x, pos_y, fill_width, height))
              
    #calls all functions
    def update(self):
        self.input()
        self.move()
        self.rotation()
        self.draw_healthBar()
        self.energyDepletion()
        self.draw_energyBar()

        #Checks for collision with melee enemy
        for enemy in enemiesGroup:
            if pygame.sprite.collide_mask(self, enemy):
                self.damageTaken(meleeDamage)
                
        if self.invincibilityCooldown > 0:
          self.invincibilityCooldown -= 1

        #Checks collision with enemy bullets
        for bulletSprite in enemyBulletGroup:
          if pygame.sprite.collide_mask(self, bulletSprite):
            self.damageTaken(10)
            bulletSprite.kill()
          
        #Alters cooldown so can't shoot too much
        if self.attackCooldown > 0:
          self.attackCooldown -= 1

class meleeEnemy(pygame.sprite.Sprite):
  def __init__(self, pos):
    #automatically adds all enemies tp groups
    super().__init__(enemiesGroup, spriteGroup, noPlayerGroup)
    self.image = pygame.transform.rotozoom(pygame.image.load("meleeEnemy.png").convert_alpha(), 0, meleeSize)
    self.rect = self.image.get_rect()
    #sets enemy to position
    self.rect.center = pos
    #Chase player by direction of player
    self.direction = pygame.math.Vector2()
    self.velocity = pygame.math.Vector2()
    self.speed = enemySpeed
    self.position = pygame.math.Vector2(pos)
    self.health = 100

  def followPlayer(self):
    #Gets position of player and enemy and transforms to vector
    playerVector = pygame.math.Vector2(player1.rect.center)
    enemyVector = pygame.math.Vector2(self.rect.center)
    #calculate distance between vector so we know if enemy has to move or not
    distance = self.vectorDistance(playerVector, enemyVector)
    #if enemy isn't too close to player, move towards player
    if distance > 0:
      #updates direction to point to player
      self.direction = (playerVector - enemyVector).normalize() #normalise makes it a unit vector (length of 1)
    else:
      #if distance = 0 then direction will be 0 so it stops moving
      self.direction = pygame.math.Vector2()
    #Multiply unit vector by speed to get velocity
    self.velocity = self.direction * self.speed
    #Calculates new position for collision check with assignment later
    new_position = self.position + self.velocity
    if not self.checkCollision(new_position.x, new_position.y):
        #update position of enemy
        self.position = new_position
        #update position of hitbox (rectangle)
        self.rect.centerx = int(self.position.x)
        self.rect.centery = int(self.position.y)

  #Find distance between player and enemy
  def vectorDistance(self, playerVector, enemyVector):
    return (playerVector - enemyVector).magnitude()


  def checkCollision(self, x ,y):
    #Check if the next position collides with a wall
    row = int(y/tileSize)
    col = int(x/tileSize)
    if current_level[row][col] == "X" or current_level[row][col] == "I" or current_level[row][col] == "S":
        return True
    else:
        return False

  def bulletCollision(self):
    self.health = self.health - 18
    if self.health <= 0:
        self.kill()
        update_score(10)

  def update(self):
    self.followPlayer()

class rangedEnemy(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__(enemiesGroup, spriteGroup, noPlayerGroup)
        self.image = pygame.transform.rotozoom(pygame.image.load("ranged enemy.png").convert_alpha(), 0, rangedSize)
        self.rect = self.image.get_rect()
        self.rect.center = pos
        self.speed = enemySpeed
        self.direction = pygame.math.Vector2()
        self.velocity = pygame.math.Vector2()
        self.position = pygame.math.Vector2(pos)
        self.attackCooldown = enemyCooldown
        self.health = 85

    def moveAway(self):
      #Gets position of player and enemy and transforms to vector
      playerVector = pygame.math.Vector2(player1.rect.center)
      enemyVector = pygame.math.Vector2(self.rect.center)
      #calculate distance between vector so we know if enemy has to move or not
      distance = self.vectorDistance(playerVector, enemyVector)
      self.direction = (playerVector - enemyVector).normalize()
      #Multiply unit vector by speed to get velocity
      self.velocity = self.direction * self.speed
      #Calculates new position for collision check with assignment later
      new_position = self.position - self.velocity
      #Checks collision with walls and if player is within 500 units, move away from the player
      if not self.checkCollision(new_position.x, new_position.y) and distance < 500:
        #update position of enemy
        self.position = new_position
        #update position of hitbox (rectangle)
        self.rect.centerx = int(self.position.x)
        self.rect.centery = int(self.position.y)

    #Find distance between player and enemy
    def vectorDistance(self, playerVector, enemyVector):
      return (playerVector - enemyVector).magnitude()

    def checkCollision(self, x ,y):
      #Check if the next position collides with a wall
      row = int(y/tileSize)
      col = int(x/tileSize)
      if current_level[row][col] == "X" or current_level[row][col] == "I" or current_level[row][col] == "S":
          return True
      else:
         return False


    def attack(self, playerVector):
        if self.attackCooldown == 0:
            self.attackCooldown = enemyCooldown
            angle = math.degrees(math.atan2(playerVector.y - self.rect.centery, playerVector.x - self.rect.centerx))
            spawnPos = self.position
            #Setting variable so the bullet instance has position vectors
            spawnLocationx = spawnPos[0]
            spawnLocationy = spawnPos[1]
            #Create a bullet instance
            self.bullet = enemyBullet(spawnLocationx, spawnLocationy, angle)
            spriteGroup.add(self.bullet)
        else:
            self.attackCooldown = self.attackCooldown - 1

    def bulletCollision(self):
        self.health = self.health - 18
        if self.health <= 0:
          self.kill()
          update_score(10)

    def update(self):
        self.moveAway()

        playerVector = pygame.math.Vector2(player1.rect.center)
        enemyVector = pygame.math.Vector2(self.rect.center)
        distance = self.vectorDistance(playerVector, enemyVector)

        if distance < 500:
            # Fire bullets at the player
            self.attack(playerVector) 

class enemyBullet(pygame.sprite.Sprite):
  def __init__(self, x, y, angle):
    super().__init__(enemyBulletGroup)
    self.image = pygame.transform.rotozoom(pygame.image.load("pistolBullet.png").convert_alpha(), 0, bulletSize)
    self.image.fill((0, 255, 0), special_flags=pygame.BLEND_RGB_MULT)
    #Hitbox
    self.rect = self.image.get_rect()
    #Center bullet hitbox
    self.rect.center = (x, y)
    self.angle = angle
    self.x = x
    self.y = y
    self.speed = bulletSpeed
    #SOHCAHTOA used for triangles and traversing at the angle shot, radians as maths.cos used radians
    self.xVelocity = math.cos(self.angle * (2*math.pi/360)) * self.speed
    self.yVelocity = math.sin(self.angle * (2*math.pi/360)) * self.speed
    self.bulletDisapear = bulletTime
    #Gets time when bullet was created
    self.spawnTime = pygame.time.get_ticks() * 1000

  def bulletMove(self):
    self.x = self.x + self.xVelocity
    self.y = self.y + self.yVelocity
    #Rect object must be integers
    self.rect.x = int(self.x)
    self.rect.y = int(self.y)
    #Deletes bullets if they've been on screen for longer than their lifetime
    if pygame.time.get_ticks() - self.spawnTime > self.bulletDisapear:
      self.kill()
    if self.checkCollision():
        self.kill()

  def checkCollision(self):
    #Check if the next position collides with a wall
    row = int(self.y / tileSize)
    col = int(self.x / tileSize)
    return current_level[row][col] == "X"


  def update(self):
    self.bulletMove()

class bullet(pygame.sprite.Sprite):
  def __init__(self, x, y, angle):
    super().__init__()
    self.image = pygame.transform.rotozoom(pygame.image.load("pistolBullet.png").convert_alpha(), 0, bulletSize)
    #Hitbox
    self.rect = self.image.get_rect()
    #Center bullet hitbox
    self.rect.center = (x, y)
    self.angle = angle
    self.x = x
    self.y = y
    self.speed = bulletSpeed
    #SOHCAHTOA used for triangles and traversing at the angle shot, radians as maths.cos used radians
    self.xVelocity = math.cos(self.angle * (2*math.pi/360)) * self.speed
    self.yVelocity = math.sin(self.angle * (2*math.pi/360)) * self.speed
    self.bulletDisapear = bulletTime
    #Gets time when bullet was created
    self.spawnTime = pygame.time.get_ticks() * 1000

  def bulletMove(self):
    self.x = self.x + self.xVelocity
    self.y = self.y + self.yVelocity
    #Update Rect (must be integers)
    self.rect.x = int(self.x)
    self.rect.y = int(self.y)
    #Deletes bullets if they've been on screen for longer than their lifetime
    if pygame.time.get_ticks() - self.spawnTime > self.bulletDisapear:
      self.kill()
    if self.checkCollision():
        self.kill()
                
  def checkCollision(self):
    #Check if the next position collides with a wall
    row = int(self.y / tileSize)
    col = int(self.x / tileSize)
    if current_level[row][col] == "X":
        return True
    else:
        return False

  def update(self):
    self.bulletMove()


class health(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__(spriteGroup, noPlayerGroup, healthGroup)
        self.image = pygame.transform.rotozoom(pygame.image.load("food.png").convert_alpha(), 0, foodSize)
        self.rect = self.image.get_rect()
        self.rect.topleft = pos

    def eat(self):
        self.kill()

class collectible(pygame.sprite.Sprite):
  def __init__(self, pos):
    super().__init__(spriteGroup, noPlayerGroup, collectibleGroup)
    self.image = pygame.transform.rotozoom(pygame.image.load("egg3.png").convert_alpha(), 0, collectibleSize)
    self.rect = self.image.get_rect()
    self.rect.topleft = pos
    self.points = 50

  def collect(self):
    update_score(self.points)
    self.kill()
    
class portal(pygame.sprite.Sprite):
  def __init__(self, pos):
    super().__init__(spriteGroup, noPlayerGroup)
    self.image = pygame.transform.rotozoom(pygame.image.load("pixel_portal1.png").convert_alpha(), 0, portalSize)
    self.rect = self.image.get_rect()
    self.rect.topleft = pos

class secretWall(pygame.sprite.Sprite):
    def __init__(self, pos, image):
        super().__init__(spriteGroup, noPlayerGroup, secretWallGroup)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = pos
        self.hits = 0

    def collision(self):
        self.hits += 1
        if self.hits >= 3:
            self.kill()
            row = self.rect.y // tileSize
            col = self.rect.x // tileSize
            #:col slices the code from beginning up to col but not including
            #col+1: slices from character after the secret wall to end
            #The line goes over the row that the secret wall is in, splits the colum up and changes it to have the empty string where the secret wall was
            current_level[row] = current_level[row][:col] + ' ' + current_level[row][col+1:]


#Grouping sprites
spriteGroup = pygame.sprite.Group()
enemiesGroup = pygame.sprite.Group()
noPlayerGroup = pygame.sprite.Group()
bulletGroup = pygame.sprite.Group()
enemyBulletGroup = pygame.sprite.Group()
healthGroup = pygame.sprite.Group()
collectibleGroup = pygame.sprite.Group()
secretWallGroup = pygame.sprite.Group()

player1 = player()
player1.setStartPosition()

#adds to group
spriteGroup.add(player1)

def spawn_sprites():
  #Spawn Enemy
  for rowIndex, row in enumerate(current_level):
    for colIndex, char in enumerate(row):
      if char == 'M':
          #Calculate the position for the enemy based on the tile size and current index
          enemy_pos = (colIndex * tileSize, rowIndex * tileSize)
          #Create a new meleeEnemy instance at this position
          new_melee_enemy = meleeEnemy(enemy_pos)
      #Ranged enemies
      elif char == 'R':
          enemy_pos = (colIndex * tileSize, rowIndex * tileSize)
          new_ranged_enemy = rangedEnemy(enemy_pos)
      #Health items
      elif char == "H":
          health_pos = (colIndex * tileSize, rowIndex *tileSize)
          new_health = health(health_pos)
      #Collectibles
      elif char == 'C':
          collectible_pos = (colIndex * tileSize, rowIndex * tileSize)
          new_collectible = collectible(collectible_pos)
      #Portal
      elif char == 'F':
          portal_pos = (colIndex * tileSize, rowIndex * tileSize)
          new_portal = portal(portal_pos)
          spriteGroup.add(new_portal)
      #Secret wall
      elif char == "S":
          secretWall_pos = (colIndex * tileSize, rowIndex * tileSize)
          new_secret_wall = secretWall(secretWall_pos, secretWall_image)

spawn_sprites()

wall = pygame.transform.scale(pygame.image.load("wall.png").convert_alpha(), (tileSize, tileSize))
ice = pygame.transform.scale(pygame.image.load("ice.png").convert_alpha(), (tileSize, tileSize))
toxic = pygame.transform.scale(pygame.image.load("slime.png").convert_alpha(), (tileSize, tileSize))
secretWall_image = pygame.transform.scale(pygame.image.load("secret wall.png").convert_alpha(), (tileSize, tileSize))


while True:
    #Any key pressed pressed by user will be stored in keys
    keys = pygame.key.get_pressed()
    #looping through events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    
    #Clear the screen
    screen.fill((80,80,80))

    #Moves camera to follow player
    camera_offset = pygame.math.Vector2(width // 2 - player1.rect.centerx, height // 2 - player1.rect.centery)
    #Draw Tiles
    for rowIndex, row in enumerate(current_level):
      for col_index, character in enumerate(row):
        #Wall
        if character == "X":
          wall_rect = pygame.Rect(col_index * tileSize + camera_offset.x, rowIndex * tileSize + camera_offset.y, tileSize, tileSize)
          screen.blit(wall, wall_rect.topleft)
        #Invisible walls
        elif character == "I":
          invisibleWall_rect = pygame.Rect(col_index * tileSize + camera_offset.x, rowIndex * tileSize + camera_offset.y, tileSize, tileSize)
        #Ice tile
        elif character == "B":
          ice_rect = pygame.Rect(col_index * tileSize + camera_offset.x, rowIndex * tileSize + camera_offset.y, tileSize, tileSize)
          screen.blit(ice, ice_rect.topleft)
        #Toxic tile
        elif character == "T":
          toxic_rect = pygame.Rect(col_index * tileSize + camera_offset.x, rowIndex * tileSize + camera_offset.y, tileSize, tileSize)
          screen.blit(toxic, toxic_rect.topleft)

    #Blit every sprite onto the screen
    for sprite in spriteGroup:
      screen.blit(sprite.image, sprite.rect.topleft + camera_offset)
      
    spriteGroup.update()

    #Health and player collision
    for banana in pygame.sprite.spritecollide(player1, healthGroup, True):
      if isinstance(banana, health):
        banana.eat()
        player1.eat()

    #Enemies and bullet collision
    for enemy in enemiesGroup:
      for bulletSprite in pygame.sprite.spritecollide(enemy, bulletGroup, True):
        if isinstance(bulletSprite, bullet):
          enemy.bulletCollision()

    #Check for collisions between player and sprites in collectibleGroup
    for collectibleSprite in pygame.sprite.spritecollide(player1, collectibleGroup, True):
      #Checks if the collided sprite is a collectible
      if isinstance(collectibleSprite, collectible):
        collectibleSprite.collect()

    for secretWallInstance in secretWallGroup:
      for bulletSprite in pygame.sprite.spritecollide(secretWallInstance, bulletGroup, True):
        if isinstance(bulletSprite, bullet):
          secretWallInstance.collision()

    #Check for collision with portal
    for sprite in spriteGroup:
        #Checks if the sprite is a portal and if it collides with player
        if isinstance(sprite, portal) and pygame.sprite.collide_rect(player1, sprite):
            #Clear enemies and other entities
            for item in noPlayerGroup:
              item.kill()
            totalScore += score
            print(totalScore)
            #Check if that was the last level
            if current_level == levelList[-1]:
              final_score_menu(totalScore)
              break
            #Load the next level
            current_level = levelList[levelList.index(current_level) + 1]
            #Reset factors
            player1.setStartPosition()
            player1.health = playerHealth
            player1.currentEnergy = maxEnergy
            player1.speed = playerSpeed
            next_level_menu()
            score = 0
            spawn_sprites()

    if player1.health <= 0:
      game_over_menu()

    display_score()
    
    pygame.display.update()
    #sets fps to 60
    clock.tick(60)
