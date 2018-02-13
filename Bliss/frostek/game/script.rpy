# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")

image great = "pen.jpg"
image land = "Island.png"
image beach = Frame("beachside.jpeg", 10, 10)






# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.
    
    
    show land
    
    "The sun hits your face, you blink, and you see a deep gaze of figure, but what is it"
    "A mirage? A dream? Reality?"
    "GAME START"
    
    hide land
    
    show eileen happy

    # These display lines of dialogue.
    
    show beach
    
    
    e "Where am I?is this an island"

    e "How did I get here?"
    
    e "What is that creature?"
   
    hide eileen happy
    
    show great
    
    "The END"

    # This ends the game.

    return
