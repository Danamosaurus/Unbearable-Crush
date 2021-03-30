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
    Rin "{i}Gasp!{/i} Air! I need air!"
    Kan speaking confident "Get back in there! You're supposed to stay hidden!"
    Rin "Nah, I'm just messing with you. It's surprisingly comfy for a cramped place. I even get to write a bucket list for my retirement!"
    Kan speaking pleading "Hey! Is that my pen and notebook? Don't play around with that!"
    Rin "What else am I gonna do? Bore myself to death? I’ve done enough of that at the shrine."
    #ART maybe cut out a Kyousuke art and show him on the BG?
    #show hallway_1_guy_1 with Dissolve(.2)
    Kan "It's not my fault that-"
    Kan speaking excited crazy blush "{i}-It's Kyousuke!{/i}"
    Rin "That's... the Kyousuke you're looking at?"
    #ART CG? Kanna adores him while she imagines him being her prince charming. While Ringo's face is blank...
    Kan "Yes! Kyousuke! The glorious, the handsome, the one and only..."
    #Code Set the correct time in the wait tag, based on the VA performance.
    "He looks like...{w=0.5} the most boring looking person in the world."
    "Oh well, that just makes things easier!"
    Kan "Yesterday during lunch, when he wasn't looking, I obtained his yakisoba bread."
    Rin "You stole his lunch?"
    Kan "Only the part he didn't eat!"
    Rin "...Why?"
    Kan salivating "Kyousuke-flavored yakisoba bread~"
    Rin "All right! I get it! God, are all teenagers this creepy? If you like him so much, then why not just confess to him already?"
    Kan frown worried ec "I don't know. He- he makes me all fluttery!"
    Rin "Fluttery how?"
    Kan speaking embarrassed ec "I don't know! What if I say something stupid and offend him?! Or-"
    Rin "Jeez! Just go talk to him already!"
    Kan questioning embarrassed "What am I supposed to say?"
    Rin "It doesn't matter. Just start talking. He's right there waiting for you, come on, you got this!"
    Kan smile concerned ec "O-okay... s-s-sure. I-I-I-I got this..."
    Rin "Come on, take a step forward... that's it. Almost there, there you go-"
    show Maya smile happy mc with dissolve:
        subpixel True xpos 0.54 ypos 1.4 xanchor 0.5 yanchor 1.0 zoom 1.46 rotate None
    $ hide_sides = ["Maya"]
    "???" "Kyousuke!"
    #hide hallway_1_guy_1
    Kan smile surprised crazy "Eh-"
    with Dissolve(.2)
    scene white with Dissolve(.2)
    scene orange onlayer master with dissolve:
        subpixel True xpos 0.5 ypos 1.0 xanchor 0.5 yanchor 1.0 zoom 0.36 rotate None 
    $ hide_sides = ['Maya','Kyousuke','Kanna']
    
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
    Rin "Uh-oh."
    "Just when we're about to get started...Kanna is stopped dead in her tracks."
    Rin "Oh no..."
    hide kannabox with dissolve
    Kyou "See me? Do you want to see my math notes? Do you need me to help you finish your lunch again?"
    Maya sad speaking "*Sigh* I don't want to go to volleyball today. If I’m gonna work hard everyday, it would be nice to have someone there to cheer me on~"
    Kyou "You mean like a fan club?"
    Maya annoyed ec "No I mean, I, er maybe if boys were there to watch us play, the girls would perform better~"
    Kyou "But it’s an all-girls volleyball team. Why would guys be there?"
    Maya annoyed eo "No, Kyousuke, I mean-"
    # SFX School bell rings.
    Maya hopeless ec "Nevermind. I gotta go to class. See you later!"
    hide Maya with dissolve
    show kannabox angry_ringo onlayer master with easeinright:
        subpixel True xpos -0.13 ypos 1.14 xanchor -0.43 yanchor 1.5 zoom 0.25 rotate None
    Rin "That guy is my target? A brainless dork who can’t read a room?"
    Rin "What the hell do you even see in him?"
    show kannabox shout_ringo onlayer master with Dissolve(.2):
        subpixel True xpos -0.13 ypos 1.14 xanchor -0.43 yanchor 1.5 zoom 0.25 rotate None
    Kan "What's with this love interest appearing out of nowhere!?"
    $ hide_sides = []
    scene room day with dissolve
    Kan speaking pleading "Urrrrrrrgggghhhhhhhhh!"
    "She's been screaming into that pillow since we got back."
    "How long is she planning on keeping this up?"
    "Well, I guess in this state she won't mind if I help myself to some of these brownies..."
    "Ah, the savory perks a cooking club member."
    Kan "Who does she even think she is trying to steal my KYOUSUKE!"
    Kan speaking confident "You, spirit! Make her disappear!"
    Rin "{i}Sigh{/i} You know I can't do that."
    Kan "Why not?!"
    Rin "Look, kid. There are some things I can do, and some I can't. Making people disappear isn't part of our contract."
    Kan frown confident ec "And somehow drinking all my Ramune is? I was saving those."
    Rin "{i}Gulp... gulp...{/i} Ah! Well anyway, it seems like you've got some competition. If we're going to defeat this Maya girl, I'm going to need to gather more information on both of them."
    # Art (Sprite Artist) Ringo wears a hat or glasses
    Kan speaking curious "Huh?"
    Kan smile concerned ec "What's with that getup?"
    Rin "I'm going to do some investigating around school tomorrow."
    Rin "This disguise is just for extra saftey. It would be catastrophic if someone were to see me in this form."
    Kan speaking curious "Would it break our magical contract or something?"
    Rin "Yeah...it's something like that."
    Rin "Just don't let anyone see me."
    Kan "What should I do tomorrow?"
    Rin "Just sneak me into school in your backpack again."
    Rin "Oh, and pack some snacks too."
    Kan smile concerned ec "You sure seem to eat a lot for your size."
    Rin "Don't remind me."
    scene black with fade
    jump chapter2