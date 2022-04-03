init:
    #Text outlines
    $ style.say_thought.outlines = [(1, "000000", 0, 0), (1, "#202020", 0, 0)]
    $ style.say_dialogue.outlines = [(1, "000000", 0, 0), (1, "#202020", 0, 0)]
    $ style.pref_label_text.outlines = [(0.2, "000000", 0, 0), (1, "#202020", 0, 0)]

# Character Initialization: These lines represent all the possible characters you can call up.
# When adding new characters, this is where you define them. Image links them to an image tag.
# voice_tag links them to their particular slider in the sound settings
# The "Color" value lets you choose a six hexadecimal color code for each character's name.
    define Kan = Character("Kanna", image = "Kan",voice_tag = "Kan",callback=speaker("Kan"),who_color="#ffffff",what_prefix = '"', what_suffix = '"')
    define Maya = Character("Maya", image = "Maya",voice_tag = "Maya",callback=speaker("Maya"),who_color="#ffffff",what_prefix = '"', what_suffix = '"')
    define Char = Character("Charlotte", image = "Char",voice_tag = "Char",callback=speaker("Char"),who_color="#ffffff",what_prefix = '"', what_suffix = '"')
    define Rin = Character("Ringo", image = "Rin",voice_tag = "Rin",callback=speaker("Rin"),who_color="#ffffff",what_prefix = '"', what_suffix = '"')
    define Youk = Character("Youko", image = "Youk",voice_tag = "Youk",callback=speaker("Youk"),who_color="#ffffff",what_prefix = '"', what_suffix = '"')
    define Kyou = Character("Kyousuke", image = "Kyou",voice_tag = "Kyou",callback=speaker("Kyou"),who_color="#ffffff",what_prefix = '"', what_suffix = '"')
    define na = Character()
    #Backgrounds
    image room = "bgs/room day.png"
    image room night = "bgs/room night.png"
    image roomwposter = "bgs/roomwposter.png"
    image white = "bgs/white.png"
    image hallway_1 = "bgs/hallway1/hallway.png"
    image orange = "bgs/orange.png"
    #cgs
    image cgs ringo_ent = "cgs/cgs ringo_ent.png"
    image cgs ringo_ent_shadow = "cgs/cgs ringo_ent_shadow.png"
    image cgs charlotte_intro = "cgs/cgs charlotte intro.png"
    image cgs mayaintro kyousuke = "cgs/mayaintro/kyousuke.png"
    #Popins
    image pop kannashocked = "popins/kanna_shocked.png"
    image kannabox focused = "popins/kannabox/focused.png"
    image kannabox focused_ringo = "popins/kannabox/focused_ringo.png"
    image kannabox shout_ringo = "popins/kannabox/shout_ringo.png"
    image kannabox grimace_ringo = "popins/kannabox/grimace_ringo.png"
    image kannabox angry_ringo = "popins/kannabox/angry_ringo.png"
    #Main Menu Images
    image bearmenu_bg = "mainmenu/bearmenubg.png"
    image bearmenu_char = "mainmenu/bearmenu_char.png"
    image bearmenu_kan = "mainmenu/bearmenu_kan.png"
    image bearmenu_maya = "mainmenu/bearmenu_maya.png"

define config.say_attribute_transition = Dissolve(.2)
$ _game_menu_screen = "circle_menu"
#Splash Screen and Update Script
label splashscreen:
    python:
        if not persistent.set_volumes:
            persistent.set_volumes = True

            _preferences.volumes['music'] *= .3
            _preferences.volumes['voice'] *= .8
            _preferences.volumes['sfx'] *= .75
    $ renpy.music.play(config.main_menu_music)
    scene white
    show sarchalenlogo at center with Dissolve(.5):
        zoom 0.3
        yanchor .5
        ypos .5
    $ renpy.pause(2, hard=True)
    hide sarchalenlogo with Dissolve(1.0)

    # FANCY MAIN MENU INTRO ANIMATION
    # scene black with Dissolve(1.0)
    # pause
    show unbearable_logo:
        anchor (0.5, 1.0) align (0.5, 0.5)
        yoffset -1000
        linear 0.3 yoffset 0
        linear 0.15 xzoom 1.05 yzoom 0.9 yoffset 50
        linear 0.3 xzoom 1 yzoom 1 yoffset 0
    show bearmenubg_left zorder 1000:
        anchor (1.0, 0.5) transform_anchor True align (0.5, 0.5) zoom 2 rotate 90 yoffset -600 xoffset -100
        parallel:
            linear 2.0 xoffset 0
        parallel:
            ease 0.5 yoffset -400
            pause 1.0
            ease 0.2 yoffset -450
            easeout 0.3 yoffset 0
            ease 0.8 rotate 380
            easeout 0.3 rotate 330 xoffset -650
    show bearmenubg_right zorder 1000:
        anchor (1.0, 0.5) transform_anchor True align (0.5, 0.5) zoom 2 rotate 90 yoffset 600 xoffset 100
        parallel:
            linear 2.0 xoffset 0
        parallel:
            ease 0.5 yoffset 400
            pause 1.0
            ease 0.2 yoffset 450
            easeout 0.3 yoffset 0
            ease 0.8 rotate 380
            easeout 0.3 rotate 335 xoffset -110
    $ renpy.pause(2.8, hard=True)
    hide unbearable_logo
    $ renpy.pause(0.1, hard=True)
    show bearmenu_kan zorder 1003:
        align (0.5, 0.5) zoom 1.0 xoffset -300 alpha 0
        easein 0.3 xoffset 0 alpha 1
    show bearmenu_maya zorder 1002:
        align (0.5, 0.5) zoom 1.0 xoffset 200 alpha 0
        pause 0.1
        easein 0.3 xoffset 0 alpha 1
    show bearmenu_char zorder 1001:
        align (0.5, 0.5) zoom 1.0 xoffset 100 alpha 0
        pause 0.2
        easein 0.3 xoffset 0 alpha 1
    $ renpy.pause(0.5, hard=True)
    jump update

label update:
    $ UPDATE_URL = "http://sarchalen.com/bear2020/update/updates.json"
    $ new_version = updater.UpdateVersion(url=UPDATE_URL, simulate=None)
    if new_version != None:
        $ updater.update(url=UPDATE_URL, base=None, force=False, public_key=None, simulate=None, add=[], restart=True)
    else:
        #Return to main menu
        return
return
# label main_menu:
#     call screen main_menu
#     return
