label chapter1:

    # Update the day shown on the upper corner... to nothing!
    $ game_day = "Day 1"
    $ hide_sides = ["Maya"]
    $all_moves(camera_check_points={u'y': [(0, 0, u'linear')], u'x': [(0, 0, u'linear')], u'z': [(0, 0, u'linear')]}, layer_check_points={}, subpixel=True, **{})
    scene hallway_1 onlayer master with squares:
        subpixel True xpos 0.52 ypos 0.52 xanchor 0.5 yanchor 0.5 xoffset 0 zoom 0.36 rotate None 
    "Girl2" "Hey, Who's the creep?"
    "Girl1" "Why's she sneaking around like that?"
    "Girl2" "Maybe she's a spy on a secret mission!"
    Kan frown confident ec "You know I can hear you guys."
    Kan smile concerned ec "I don't care what they say. No one can stop me from achieving my goals. I have resolved myself to claim my-"
    Rin panting "{i}Gasp!{/i} Air! I need air!"
    Kan speaking confident "Get back in there! You're supposed to stay hidden!"
    Rin speaking happy "I'm just messing with you. It's surprisingly comfy for a cramped place. I even get to write a bucket list for my retirement!"
    Kan speaking pleading "Hey! Is that my pen and notebook? Don't play around with that!"
    Rin "What else am I gonna do? Bore myself to death? I’ve done enough of that at the shrine."
    #ART maybe cut out a Kyousuke art and show him on the BG?
    #show hallway_1_guy_1 with Dissolve(.2)
    Kan speaking confident "It's not my fault that-"
    Kan speaking excited crazy blush "{i}-It's Kyousuke!{/i}"
    Rin curious "That's... the Kyousuke you're looking at?"
    #ART CG? Kanna adores him while she imagines him being her prince charming. While Ringo's face is blank...
    Kan smile happy blushing "Yes! Kyousuke! The glorious, the handsome, the one and only..."
    #Code Set the correct time in the wait tag, based on the VA performance.
    "He looks like...{w=0.5} the most boring looking person in the world."
    "Oh well, that just makes things easier!"
    Rin "Well if you like him, why don't you just go confess already?"
    Kan sad speaking normal "I was going to, really!"
    Kan "Yesterday, during lunch..."
    Kan smile worried ec "...I got myself all pumped up and everything."
    Rin "What happened?"
    Kan speaking confident "I was going to slip a note into his lunch. I was five steps from the table when..."
    Rin sarcastic "You chickened out?"
    Kan smile worried ec "No not exactly..."
    Kan smile crazy eo "...But it wasn't a complete failure. I managed to obtain the newest piece of my collection!"
    Kan smile happy blushing "Tada! Kyousuke's yakisoba bread!"
    Rin annoyed "You stole his lunch?"
    Kan smile concerned ec "Only the part he didn't eat."
    Rin "...Why?"
    Kan salivating "Kyousuke-flavored yakisoba bread~"
    Rin shockedannoyed "..."
    Kan speaking embarrassed ec "Oh Ringo, I know it's weird! But that's why I need your help."
    Kan "I just don't know what to do."
    Rin speaking normal "He's just a guy, he can't be that hard to talk to."
    Kan frown worried ec "I don't know. He- he makes me all fluttery!"
    Rin "Come on, Ill be right here with you. Look, he's at his locker right now. Go on."
    Kan speaking embarrassed ec "But what if I say something stupid or creep him out or-"
    Rin "Look, think of it like this..."
    Rin speaking armout "Won't it be great to go home tonight knowing that today was the day you finally got to speak to Kyousuke?"
    Kan questioning embarrassed "What am I supposed to say?"
    Rin "It doesn't matter. Just start talking. He's right there waiting for you, come on, you got this!"
    Kan smile concerned ec "O-okay... s-s-sure. I-I-I-I got this..."
    Rin "Come on, take a step forward... that's it. Almost there, there you go-"
    show Maya smile happy mc with dissolve:
        subpixel True xpos 0.54 ypos 1.4 xanchor 0.5 yanchor 1.0 zoom 1.46 rotate None
    $ hide_sides = ["Maya"]
    "???" "Kyousuke!"
    #hide hallway_1_guy_1
    Rin surprised "Eh-"
    with Dissolve(.2)
    scene white with Dissolve(.2)
    scene orange onlayer master with dissolve:
        subpixel True xpos 0.5 ypos 1.0 xanchor 0.5 yanchor 1.0 zoom 0.36 rotate None 
    $ hide_sides = ['Maya','Kyousuke','Kanna', 'Ringo']
    
    show cgs mayaintro kyousuke onlayer master with dissolve:
        subpixel True xpos 0.68 ypos 1.37 xanchor 0.5 yanchor 1.0 zoom 0.47 rotate None 
    Kyou "Oh, good morning Maya. What's up?"
    show Maya speaking normal with dissolve:
        subpixel True xpos 0.43 ypos 1.4 xanchor 0.5 yanchor 1.0 zoom 1.46 rotate None 
    Maya "I just wanted to see you, that's all."
    show kannabox focused onlayer master with easeinright:
        subpixel True xpos -0.13 ypos 1.14 xanchor -0.43 yanchor 1.5 zoom 0.25 rotate None
    Kan "{i}Hn...{/i}"
    show kannabox focused_ringo onlayer master with dissolve:
        subpixel True xpos -0.13 ypos 1.14 xanchor -0.43 yanchor 1.5 zoom 0.25 rotate None
    Kyou "See me? Of course you can! I'm right here after all."
    Rin "Woah who the heck is that?"
    show kannabox shout_ringo onlayer master with Dissolve(.2):
        subpixel True xpos -0.13 ypos 1.14 xanchor -0.43 yanchor 1.5 zoom 0.25 rotate None
    Kan "Get down! Enemy in sight!"
    hide kannabox
    hide cgs mayaintro kyousuke with dissolve
    show Maya intropose_smile onlayer master with dissolve:
        subpixel True xpos 1000 ypos 876 xanchor 0.5 yanchor 1.0 zoom 0.78 rotate None
    $ hide_sides = ['Maya', 'Kyousuke']
    Rin angry shouting "What the hell Kanna! What's with this love interest appearing out of nowhere?"
    Kan shouting crazy "Maya...She appeared yesterday out of nowhere..."
    Kan shouting crazy "Long hair...a slender build...She's easily one of the most dangerous girls Kyousuke has ever encountered."
    Kan speaking pleading "And what's worse is she thinks she's way better than everyone else!"
    Rin angry shouting "You didn't say anything about a rival!"
    Kan speaking pleading "Don't shout they'll hear you!"
    hide Maya with dissolve
    show cgs mayaintro kyousuke onlayer master with dissolve:
        subpixel True xpos 0.68 ypos 1.37 xanchor 0.5 yanchor 1.0 zoom 0.47 rotate None 
    show Maya smile happy mc onlayer master with dissolve:
        subpixel True xpos 1000 ypos 876 xanchor 0.5 yanchor 1.0 zoom 0.78 rotate None
    Kyou "So Maya, what brings you back to my locker?"
    Kyou "Do you need help finishing your lunch again?"
    Maya sad speaking "*Sigh* Oh it's nothing like that. I'm actually on my way to volleyball practice."
    Maya flirting eo "You know, it would be really nice to have someone there to cheer me on~"
    Kyou "You mean like a fan club?"
    Maya annoyed ec "No I mean, I, er maybe if boys were there to watch us play, the girls would perform better~"
    Kyou "But it’s an all-girls volleyball team. Why would guys be there?"
    Maya annoyed eo "No, Kyousuke, I mean-"
    # SFX School bell rings.
    Maya hopeless ec "Nevermind. I gotta go to class. See you later!"
    hide Maya with dissolve
    show kannabox angry_ringo onlayer master with easeinright:
        subpixel True xpos -0.13 ypos 1.14 xanchor -0.43 yanchor 1.5 zoom 0.25 rotate None
    $ hide_sides = ['Ringo', 'Kanna']
    Rin "That hopeless guy is our romance target?"
    Rin "What the hell do you even see in him?"
    show kannabox shout_ringo onlayer master with Dissolve(.2):
        subpixel True xpos -0.13 ypos 1.14 xanchor -0.43 yanchor 1.5 zoom 0.25 rotate None
    Kan "Why does this always happen?!"
    $ hide_sides = []
    scene room day with dissolve
    Kan speaking pleading "Urrrrrrrgggghhhhhhhhh!"
    "She's been screaming into that pillow since we got back."
    Rin sarcastic "So let me get this straight..."
    Rin "Every time you try to talk to the guy you like, a random love interest pops up and tries to take him away?"
    Kan "Who does she even think she is trying to steal my KYOUSUKE!"
    "How long is she planning on keeping this up?"
    "Well, I guess in this state she won't mind if I help myself to some of these brownies..."
    "Ah, the savory perks a cooking club member."
    Kan speaking confident "You, spirit! Make her disappear!"
    Rin speaking normal "What? I can't do that."
    Kan speaking confident "Sure you can! You can do anything, remember?"
    "Well, I mean I guess I {i}technically{/i} could..."
    "Nah, better not. I'm sure Fortune wouldn't like his powers being used in that way."
    Rin speaking happy "Look, kid. There are some things I can do, and some I can't. Making people disappear isn't part of our contract."
    Kan frown confident ec "And somehow drinking all my Ramune is? I was saving those."
    Rin "{i}Gulp... gulp...{/i} Ah!"
    Rin "It seems like you've got some competition is all. Nothing wrong with that."
    Rin "Another player has enterred the game to win the boy's heart."
    Rin "If we want to win, we must first understand our opponent. I'm going to do some investigating around school tomorrow."
    Rin "I'll need to hitch a ride in your backpack again. It would be catastrophic if someone were to see me in this form."
    Kan speaking curious "Would someone seeing you break our magical contract or something?"
    Rin "Yeah, sure it's something like that."
    Rin "Just don't let anyone see me."
    Rin "Just get me into the school and I'll handle the investigation from there."
    Rin "Oh, and pack some snacks too. Can't work on an empty stomach."
    Kan smile concerned ec "You sure seem to eat a lot for your size."
    Rin headache mo "Don't remind me."
    scene black with fade
    "There's defenitely something going on here. All I wanted was an easy wish."
    "Why do you never make it easy on me?"
    "..."
    "...Six days."
    jump chapter2