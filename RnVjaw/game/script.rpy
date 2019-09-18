# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("???")
define s = Character("Emily")
define m = Character("Matthew")
define be = Character("")
define n = Character("Nayoki")
define k = Character("Katin")
define i = Character("Ishai")

init:
    $ my_left = Position(xpos=0.1, ypos=1)

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
    hide character happy
    hide stout hout
    # These display lines of dialogue.
    e "Hey! Wake up!"
    s "….."
    e "C’mon! You need to wake up!"
    scene bg energy
    show movie poster at left with easeinleft
    show character happy at right with easeinright
    e "Here…WAKE UP!"
    s "ugh……"
    be "*wakes up on a floor of a classroom with two males looking down at her*"
    s "Huh? Where am I?"
    e "We don’t have any clue either. Everyone else doesn’t remember how they got here either."
    m "Well, I’m Matthew Walts. Unlike seemingly everyone else, I don’t have any Ultimate talent. Kinda disappointing, isn’t it?"
    be "*Matthew Walts, Ultimate talent N/A*"
    m "Hey, how about you introduce yourself as well? "
    e "Me?"
    n "Well, I’m Nayoki Furns, the Ultimate Surfer!"
    be "*Nayoki Furns, Ultimate Surfer*"
    n "Also, sorry for yelling at you."
    e "It’s fine. I should introduce myself as well…"
    s "My name is Emily Natzuki, and I am the Ultimate Secretary. It’s nice to meet you."
    be "*Emily Natzuki, Ultimate Secretary*"
    s "You said there are others?"
    m "Yes! I’ll introduce them to you, if you want!"
    s "I’ll take you up on that offer, thank you."
    n "Well, I’ve got other places I want to check out, so see ya later!"
    m "There are several places we can go, so I’ll let you decide."
label Istart:
screen imagemap_example:

    imagemap:
        ground "choices 9x9.png"
        hover "selected.png"

        hotspot (16,18,378,179) action Jump("outside") alt "Outside"
        hotspot (16,199,378,358) action Jump("search") alt "Search"
        hotspot (14,369,376,531) action Jump("warehouse") alt "Warehouse"
        hotspot (456,18,822,181) action Jump("garden") alt "Garden"
        hotspot (454,190,822,357) action Jump("cafe") alt "Cafe"
        hotspot (456,370,825,534) action Jump("room") alt "Room"
        hotspot (884,19,1247,180) action Jump("bathrooms") alt "Bathrooms"
        hotspot (881,201,1250,363) action Jump("nurse") alt "Nurse"
        hotspot (881,373,1249,537) action Jump("lab") alt "Lab"
        hotspot (496,535,774,607) action Jump("end") alt "End"


label imagemap_example:

    # Call the imagemap_example screen.
    call screen imagemap_example

label outside:

    m "That’s a pretty good idea. You get to see the layout of everything here, and we can talk to anyone that we find."

    s "Swimming seems like a lot of fun, but I didn't bring my bathing suit with me."

    jump Istart

label search:
    show bg energy
    m "That’s a pretty good idea. You get to see the layout of everything here, and we can talk to anyone that we find."
    hide movie poster
    hide character happy
    hide stout hout
    show bg proto
    with dissolve
    show movie poster at left with easeinleft
    show character happy at right with easeinright
    e "Who are you?"
    s "I am Emily Natzuki, Ultimate Secretary."
    k "Well, I am Katin Minoko, the Ultimate Dancer."
    be "*Katin Minoko, Ultimate Dancer*"
    m "Wait, didn’t you say you were going to get some rest?"
    k "Someone kept trying to wake me up. They said something like, 'Now’s not the time to rest.'"
    k " Plus, I can just get some rest later. Don’t you have other people to introduce yourself to Emily? You should get going."
    show stout hout at center with easeinleft
    e "Hello. Mind giving me an introduction?"
    s "Well, I am Emily,Emily Natzuki, and who might you be?"
    i "Ishai Nomoka"
    s "But what's yor talent?"
    i "It doesnt concern you"
    be "*Ishai Nomoka, Ultimate ???*"
    m "Why? We are all trapped in this situation together!"
    i "Which is exactly my point. We don’t know what’s going to happen, and it is unlikely that whoever trapped us will willingly let us leave."
    i "Well, I’m going. I don’t want to be stuck answering stupid questions."
    m "Oh well..."
    m "That did not go as planned"
    m "Lets... go somewhere else"
    jump Istart

label warehouse:
    m "That’s a pretty good idea. You get to see the layout of everything here, and we can talk to anyone that we find."

    e "Really good background art is hard to make, which is why so many games use filtered photographs. Maybe you can change that."

    jump Istart
label garden:
    m "That’s a pretty good idea. You get to see the layout of everything here, and we can talk to anyone that we find."

    e "Really good background art is hard to make, which is why so many games use filtered photographs. Maybe you can change that."

    jump Istart
label cafe:
    m "That’s a pretty good idea. You get to see the layout of everything here, and we can talk to anyone that we find."

    e "Really good background art is hard to make, which is why so many games use filtered photographs. Maybe you can change that."

    jump Istart
label room:
    m "That’s a pretty good idea. You get to see the layout of everything here, and we can talk to anyone that we find."

    e "Really good background art is hard to make, which is why so many games use filtered photographs. Maybe you can change that."

    jump Istart
label bathrooms:
    m "That’s a pretty good idea. You get to see the layout of everything here, and we can talk to anyone that we find."

    e "Really good background art is hard to make, which is why so many games use filtered photographs. Maybe you can change that."

    jump Istart
label nurse:
    m "That’s a pretty good idea. You get to see the layout of everything here, and we can talk to anyone that we find."

    e "Really good background art is hard to make, which is why so many games use filtered photographs. Maybe you can change that."

    jump Istart
label lab:
    m "That’s a pretty good idea. You get to see the layout of everything here, and we can talk to anyone that we find."

    e "Really good background art is hard to make, which is why so many games use filtered photographs. Maybe you can change that."

    jump Istart

label end:
    m "that should be all..."
    m "let's go to bed"

    # This ends the game.

    return
