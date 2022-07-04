label chapter1:

    # Update the day shown on the upper corner... to nothing!
    $ game_day = "Day 1"
    $ hide_sides = ["Maya"]
    scene hallway_1 onlayer master with squares:
        subpixel True xpos 0.52 ypos 0.52 xanchor 0.5 yanchor 0.5 xoffset 0 zoom 0.36 rotate None
    Rin "So this is your school. It's so...clean."
    Kan speaking curious "Why are you surprised by that?"
    Rin laughing ec "You know, kids, teenagers, delinquents. Not exactly what I would call clean and tidey people."
    Kan speaking sarcastic ec "Don't generalize! I'm a very clean and tidy person!"
    Rin laughing ec "Your room says otherwise."
    Kan speaking sarcastic ec "What's wrong with my room!"
    Kan speaking confident "Wait, we're on a Kyousuke hunt. You're not supposed to be seen or heard, otherwise our cover will be blown!"
    Kan speaking pleading "Quick! Get down, back in the pack!"
    Rin "What are you AH-"
    Kan speaking pleading "I can't let Kyousuke see me before we come up with a plan."
    Kan frown confident ec "Remember Kanna, this is a sneaking mission. Try not to get caught."
    #Kanna singing a sneaking theme (Maybe reference the metal gear solid sneaking theme / james bond theme / whatever sneaking song you'd like! Maybe a fun idea, we can change this if we want.)
    #I'd like to display a music note symbol here in the text. But I was not sure how to do so.
    Kan smile happy eo "{i}Da da. Da da da da da. Da da da da da. Da da~{/i}"
    "Girl 1" "Hey, Who's the creep?"
    "Girl 2" "Why's she sneaking around like that?"
    "Girl 2" "Oh, maybe she's a spy on a secret mission!"
    "Girl 1" "Or she's a creep. Let's get away from her."
    Kan frown confident ec "You know I can hear you guys."
    Kan smile concerned ec "I don't care what they say. No one can stop me from achieving my goals. I have resolved myself to claim my-"
    Rin panting "{i}Gasp!{/i} Air! I need air!"
    Kan speaking confident "Get back in there! You're supposed to stay hidden!"
    Rin speaking happy "It's surprisingly comfy for a cramped place. Were you singing something? Everything sounded muffled."
    Kan speaking pleading "Maybe I was, maybe I wasn't it. What's it to you?"
    Rin speaking happy "I was trying to write the lyrics of your song, but all I got was 'Da da'."
    Kan frown angry "Hey! Is that my pen and notebook? Don't play around with that!"
    Rin "What else am I gonna do? Bore myself to death? I’ve done enough of that at the shrine."
    #ART maybe cut out a Kyousuke art and show him on the BG?
    #show hallway_1_guy_1 with Dissolve(.2)
    Kan speaking confident "It's not my fault that-"
    Kan speaking excited crazy blush "{i}-It's Kyousuke!{/i}"
    Rin "What? Where?"
    "..."
    Rin curious "That's... the Kyousuke you're looking at?"
    #ART CG? Kanna adores him while she imagines him being her prince charming. While Ringo's face is blank...
    Kan smile happy blushing "Yes! Kyousuke! The glorious, the handsome, the one and only..."
    #Code Set the correct time in the wait tag, based on the VA performance.
    "He looks like...{w=0.5} the most boring looking person in the world."
    Rin "Well if you like him, why don't you just go confess already?"
    Kan sad speaking normal "I was going to, really!"
    Kan "Yesterday, during lunch..."
    Kan smile worried ec "...I got myself all pumped up and everything."
    Rin "And? What happened?"
    Kan speaking confident "I was going to slip a note into his lunch when he wasn't looking. I was five steps from his table when..."
    Rin sarcastic "You chickened out?"
    Kan smile worried ec "No, not exactly..."
    Kan smile crazy eo "...But it wasn't a complete failure. I managed to obtain the newest piece for my designer Kyousuke collection!"
    Kan smile happy blushing "Tada! Kyousuke's melon bread!"
    Rin annoyed "You stole his lunch?"
    Kan smile concerned ec "Only the part he didn't eat."
    Rin "...Why?"
    Kan smile concerned ec "He wasn't going to eat it! And I {i}never{/i} let food go to waste!"
    Rin annoyed "And how exactly did you know he wasn't going to eat it?"
    Kan salivating "Kyousuke-flavored melon bread~"
    Rin shockedannoyed "..."
    Kan speaking embarrassed ec "Oh Ringo, I know it's weird! But that's why I need your help."
    Kan "I just don't know what to do."
    Rin speaking normal "He's just a guy, he can't be that hard to talk to."
    Kan frown worried ec "I don't know. He- he makes me all fluttery!"
    Rin "Come on, Ill be right here with you. Look, he's at his locker right now. Go on."
    Kan speaking embarrassed ec "But what if I say something stupid or creep him out or-"
    Rin "You already creep people out, it's fine!"
    Kan "That doesn't help!"
    Rin "Okay look, think of it like this..."
    Rin speaking armout "Won't it be great to go home tonight knowing that today was the day you finally got to speak to Kyousuke?"
    Kan questioning embarrassed "What am I supposed to say?"
    Rin "It doesn't matter. Just start talking."
    Kan questioning embarrassed "Just keep talking? About what? Ringo you gotta give me something!"
    Rin "Just wing it, kid. He's right there waiting for you, come on, you got this!"

    camera:
        subpixel True xpos 0.247916666667 ypos -99 zpos -557.0
        parallel:
            zpos -557.0
            ease 4 zpos -650.0
        parallel:
            xpos 0.247916666667
            ease 4 xpos -0.04
    Kan smile concerned ec "O-okay... s-s-sure. I-I-I-I got this..."
    Rin "Come on, take a step forward... that's it. Almost there, there you go-"
    show Maya smile happy mc:
        subpixel True xpos 0.52 ypos 0.81 zpos -174.0 xanchor 0.5 yanchor 1.0 zoom 0.7 alpha 0 rotate None blur None
        parallel:
            easein .5 xpos .50
        parallel:
            linear .5 alpha 1
    $ hide_sides = ["Maya"]
    "???" "Kyousuke!"
    #hide hallway_1_guy_1
    Rin surprised "Eh-"
    with Dissolve(.2)
    scene white with Dissolve(.2)
    scene orange onlayer master:
        subpixel True xpos 0.5 ypos 1.0 xanchor 0.5 yanchor 1.0 zoom 0.36 rotate None
    camera:
        ypos 0 xpos 0
        easein .5 zpos -91.0
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
    Rin "Woah, who the heck is that?"
    show kannabox shout_ringo onlayer master with Dissolve(.2):
        subpixel True xpos -0.13 ypos 1.14 xanchor -0.43 yanchor 1.5 zoom 0.25 rotate None
    Kan "Get down! Enemy spotted!"
    hide kannabox
    hide cgs mayaintro kyousuke with dissolve
    show Maya intropose_smile onlayer master with dissolve:
        subpixel True xpos 1000 ypos 876 xanchor 0.5 yanchor 1.0 zoom 0.78 rotate None
    $ hide_sides = ['Maya', 'Kyousuke']
    Rin angry shouting "Kanna, mind explaining to me why a love interest JUST APPEARED OUT OF THIN AIR?"
    Rin angry shouting "DO YOU KNOW HOW MUCH HARDER THIS MAKES MY JOB?"
    Kan shouting crazy "Maya...She appeared last friday..."
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
    Maya sad speaking "{i}*Sigh*{/i} Oh it's nothing like that. I'm actually on my way to volleyball practice."
    Maya flirting eo "You know, it would be really nice to have someone there to cheer me on~"
    Kyou "You mean like a fan club?"
    Maya annoyed ec "No I mean, I, er maybe if boys were there to watch us play, the girls would perform better~"
    Kyou "But it’s an all-girls volleyball team. Why would guys be there?"
    Maya annoyed eo "No, Kyousuke, I mean-"
    # SFX School bell rings.
    Maya hopeless ec "Nevermind. I gotta go to class."
    Maya flirting eo "But real quick Kyousuke, do you have any plans for {i}Kumamatsuri{/i} this weekend?"
    Kyou "Kumamatsuri? That big festival that only happens once a year?"
    Kyou "I don't think so, no. I kinda forgot about it honestly."
    Maya flirting eo "Interesting. We'll have to talk about it later. See you around, Kyousuke~"
    Kyou "Bye Maya! Good luck in uh...whatever you're practicing!"

    hide Maya with dissolve
    show kannabox angry_ringo onlayer master with easeinright:
        subpixel True xpos -0.13 ypos 1.14 xanchor -0.43 yanchor 1.5 zoom 0.25 rotate None
    $ hide_sides = ['Ringo', 'Kanna']
    Rin "That hopeless guy is our romance target?"
    Rin "He instantly forgot what she told him. What do you even see in him?"
    show kannabox shout_ringo onlayer master with Dissolve(.2):
        subpixel True xpos -0.13 ypos 1.14 xanchor -0.43 yanchor 1.5 zoom 0.25 rotate None
    Kan "Why does this always happen?!"

    #Wasn't sure how to change the CG scene back to the school hallway, but I needed to in able to shift the conversation about
    scene hallway_1 onlayer master with squares:
        subpixel True xpos 0.52 ypos 0.52 xanchor 0.5 yanchor 0.5 xoffset 0 zoom 0.36 rotate None
    Kan shouting crazy "AHH! Everytime I get close to Kyousuke, something gets in the way."
    Rin "What was she talking about? {i}Kumamatsuri?{/i} What is that?"
    Kan speaking sad crazy "It's some dumb festival that happens once a year. It's to celebrate bears or something."
    Rin annoyed "How cute. How fitting. Gee, what a wonderful idea for a festival."
    Kan speaking sad crazy "It's super romantic and Maya is going to snatch him up to go on a hot, steamy festival date before I get the chance to talk to him."
    Kan frown worried eo "The game is over before it even starts."
    Kan frown worried ec "Even though I didn't even get caught, it looks like the sneaking mission was a failure."
    Kan "I gotta get to class. Get back in the pack."
    Rin "Wait, wait WAIT WE'RE STILL TALKIN-"
    #Kanna shoves Ringo into her backpack


    $ hide_sides = []
    scene room day with dissolve
    Kan speaking pleading "Urrrrrrrgggghhhhhhhhh!"
    "She's been screaming into that pillow since we got back."
    "What did the pillow do to deserve so much verbal abuse?"
    Rin sarcastic "So let me get this straight..."
    Rin "Every time you try to talk to the guy you like, a random love interest pops up and tries to take him away?"
    Kan "Who does she even think she is trying to steal my KYOUSUKE!"
    "How long is she planning on keeping this up?"
    "Well, I guess in this state she won't mind if I help myself to some of these brownies."
    "Finally, something to quell my dumb bear body appetite."
    "Ah, the savory perks a cooking club member~"
    Kan speaking confident "You, spirit! Make her disappear!"
    Rin speaking normal "What? I can't do that."
    Kan speaking confident "Sure you can! You can do anything, remember?"
    "Well, I mean I guess I {i}technically{/i} could..."
    Rin speaking happy "Look, kid. There are some things I can do, and some I can't. Making people disappear isn't part of our contract."
    Kan frown confident ec "And somehow drinking all my melon soda is? I was saving those to sneak into Kyousuke's lunches."
    Rin "{i}Gulp... gulp...{/i} Ah!"
    Rin "Yeah, because if he didn't eat his melon bread, I'm sure he'll {i}love{/i} melon soda. Great plan."
    Kan "Hey, atleast it was something right? Better then nothing {i}'Mr. Miracle Worker'{/i}. "
    Rin "Unlike your bad plans, I actually got a plan that might be able to work here."
    Rin "That Maya chick wants to ask Kyousuke to that Kumamatsuri festival, right?"
    Rin "Well if {i}YOU{/i} go to the festival with him, wouldn't that count as a date?"
    Kan "..."
    Kan speaking excited crazy blush "{i}GOING ON A FESTIVAL DATE WITH KYOUSUKE!?{/i}"
    Kan "..."
    Kan drooling happy ec "Going on a festival date with Kyousuke~"
    Rin "Sounds like it's a plan then! We'll get you and Kyousuke to go to that festival together somehow by the end of the week!"
    Kan frown worried eo "What about the Maya girl though?"

    Rin "It just means we got some competition. Nothing wrong with that, makes the game more challenging."
    Rin "Another player has enterred to win the boy's heart."
    Rin "And if we want to win, we must first understand our opponent. I'm going to do some investigating around school tomorrow."
    Rin "I'll need to hitch a ride in your backpack again. It would be catastrophic if someone were to see me in this form."
    Kan speaking curious "Would someone seeing you break our magical contract or something?"
    Rin "Yeah, sure it's something like that."
    Rin "Just don't let anyone see me."
    Rin "Just get me into the school and I'll handle the investigation from there."
    Rin "Oh, and pack some snacks too. Can't work on an empty stomach."
    Kan smile concerned ec "You sure seem to eat a lot for your size."
    Rin headache mo "Don't remind me."
    Rin speaking happy "And we should be celebrating! We're starting the quest to catch the man of your dreams."
    Rin speaking happy "Have some of these brownies! You don't want me to eat them by myself, do you?"
    Kan frown skeptic "Hey! Have you been eating my brownies? Those were for Kyousuke!"
    Rin speaking happy "And now they're for us! Come on, dig in!"
    scene black with fade
    "There's defenitely something going on here. All I wanted was an easy wish."
    "But if I land Kanna on some sort of festival, we should be golden!"
    "..."
    "I hope."
    "Looks like I have til this weekend to figure it out."
    "Six days..."
    jump chapter2
