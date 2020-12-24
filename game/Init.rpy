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
    image hallway_1_guy_1 = "bgs/hallway1/hallway 1 guy 1.png"
    image hallway_1_guy_2 = "bgs/hallway1/hallway 1 guy 2.png"
    image hallway_1_girl_1 = "bgs/hallway1/hallway 1 girl 1.png"
    #cgs
    image cgs ringo_ent = "cgs/cgs ringo_ent.png"
    image cgs ringo_ent_shadow = "cgs/cgs ringo_ent_shadow.png"
    #Popins
    image pop kannashocked = "popins/kanna_shocked.png"

define config.say_attribute_transition = Dissolve(.2)

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
    jump update

label update:
    $ UPDATE_URL = "http://sarchalen.com/bear2020/update/updates.json"
    $ new_version = updater.UpdateVersion(url=UPDATE_URL, simulate=None)
    if new_version != None:
        $ updater.update(url=UPDATE_URL, base=None, force=False, public_key=None, simulate=None, add=[], restart=True)
    else:
        return
