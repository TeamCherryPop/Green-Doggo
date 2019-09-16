# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("???")
define s = Character("Emily")
define m = Character("Matthew")
define be = Character("")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg proto

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.
    play music "clockwork.mp3"
    show movie poster
    # These display lines of dialogue.

    e "Hey! Wake up!"

    s "….."

    show movie adult

    e "C’mon! You need to wake up!"

    scene bg energy

    e "Here…WAKE UP!"

    show movie poster

    s "ugh……"
    be"*wakes up on a floor of a classroom with two males looking down at her*"
    s"Huh? Where am I?"

    show movie ded

    e"We don’t have any clue either. Everyone else doesn’t remember how they got here either."
    m"Well, I’m Matthew Walts. Unlike seemingly everyone else, I don’t have any Ultimate talent. Kinda disappointing, isn’t it?
"
    e""
    e""
    e""
    e""
    e""
    e""
    e""
    e""
    e""
    e""


    # This ends the game.

    return
