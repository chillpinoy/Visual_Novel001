# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")

image great = "pen.jpg"
image land = "Island.png"
image beach = Frame("beachside.jpeg", 10, 10)
image cave = Frame("cave.jpg", 10, 10,)
image bg room = Frame("man.jpg", 10, 10,)
image main = Frame("menu.jpg", 10, 10)








# The game starts here.

label start:

    

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.


    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.
    

    show island
    
    "The sun hits your face, you blink, and you see a deep gaze of figure, but what is it"
    "A mirage? A dream? Reality?"
    "GAME START"
    
    
    hide island
    
    

    # These display lines of dialogue.
    
    show beach
    
    show eileen happy at left
    
    e "Where am I? Is this an island"

    e "How did I get here?"
    
    e "It vast island that has risen through the horizons"
    
    e "Ugh, my head, I don't get how I got here, I must find clues to know exactly what is going on."
    
    
    
    show great
    
    "I should avoid that creature for now"
    
    hide great
    
    "You take more steps and you stumble across a rock figure"
    hide beach
    show cave
    "it is a cave!"
   
    
    menu:
        "Go enter the cave":
            e "It sure is cold in here"
            jump cave
        
        
        
        "Do not go into the cave":
            e "Maybe we'll look around first"
        
        
    

label cave:
    "A crevice opens and a light shines upon you"
    "Looks like a riddle you must solve"
    e "Alright then, let's do this"
    
    
    $ quiz_score = 0
    
    
    # 1st question
    "What is question 1?"
    
    menu:
        "This is incorrect":
            "Next Question"
        "This is incorrect":
            "Next Question"
        "this is the right answer":
            "Next Question"
            $ quiz_score +=1
            
    "You got a quiz score of [quiz_score]"
    "The END"

    # This ends the game.

    return
