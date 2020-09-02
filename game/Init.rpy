init:
    #Text outlines
    $ style.say_thought.outlines = [(1, "000000", 0, 0), (1, "#202020", 0, 0)]
    $ style.say_dialogue.outlines = [(1, "000000", 0, 0), (1, "#202020", 0, 0)]
    $ style.pref_label_text.outlines = [(0.2, "000000", 0, 0), (1, "#202020", 0, 0)]

# Character Initialization: These lines represent all the possible characters you can call up.
# When adding new characters, this is where you define them. Image links them to an image tag.
# voice_tag links them to their particular slider in the sound settings
# The "Color" value lets you choose a six hexadecimal color code for each character's name.
    define Kan = Character("Kanna", image = "Kan",voice_tag = "Kanna",who_color="#ffffff",what_prefix = '"', what_suffix = '"')
    define Maya = Character("Maya", image = "Maya",voice_tag = "Maya",who_color="#ffffff",what_prefix = '"', what_suffix = '"')
    define Char = Character("Charlotte", image = "Char",voice_tag = "Charlotte",who_color="#ffffff",what_prefix = '"', what_suffix = '"')
    define Rin = Character("Ringo", image = "Rin",voice_tag = "Ringo",who_color="#ffffff",what_prefix = '"', what_suffix = '"')
    define Youk = Character("Youko", image = "Youk",voice_tag = "Youko",who_color="#ffffff",what_prefix = '"', what_suffix = '"')
    define Kyou = Character("Kyousuke", image = "Kyou",voice_tag = "Kyousuke",who_color="#ffffff",what_prefix = '"', what_suffix = '"')
    define na = Character()

init python:
#Dynamic Sprite System-Each category represents a folder in the Images section. These will be auto-defined.
   # Automatically define the BGs, CGs, and some UI elements
   DefineImages('cgs')
   DefineImages('bgs', prepend='bg')
   DefineImages('mainmenu', prepend='mm')
   # define the composite sprites with LayeredImages, blinking eyes and flapping mouth
   DefineImages("sprites", composite=True)

   layerorder = ['hair', 'base', 'arms', 'tail','mouth','eyes','brow',]
   DefineImages('images/sprites', composite=True, overrideLayerOrder=layerorder, offsets=(0, 100), zooms={'Kan':.85,'Rin':.85,'Kyou':.85, 'Maya': .85, 'Youk':.85, 'Char':.7}, sides=['Kan', 'Rin', 'Kyou','Maya','Youk','Char'])
   hide_sides = []


   #Dynamic Sprite Emote Maps
   #MapEmote('war hugesmile',  'war md_hugesmile ed_bigsmile blush')
   # override some default eye blink and mouth flap behaviours
   #image war_ed_default = BlinkEyes("war_e_default", "war_ec_grin")
   # image war_md_hugesmile = FlapMouth("war_mc_smug", "war_m_bigsmile")



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
