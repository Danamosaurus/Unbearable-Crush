#ART BG Shrine evening
label start:

    #INIT RELETIONSHIP 0
    #Testing
    $game_player.addRelationship("Kanna")
    $game_player.addRelationship("Maya")
    $game_player.addRelationship("Charlotte")
    camera:
        perspective True
    # Update the day shown on the upper corner... to nothing!
    $ game_day = ""
    $ hide_sides = ['Kanna']
    show bearmenubg
    show bearmenu_char
    show bearmenu_maya
    show bearmenu_kan
    show shrine:
        subpixel True xpos 0.5 ypos 0.5 xanchor 0.5 yanchor 0.5 rotate None blur None
        parallel:
            alpha 0.0
            easein 3.5 alpha 1.0
        parallel:
            zoom 0.8
            easein 2 zoom 0.9
    $ hide_sides = []
    hide bearmenu_char with Dissolve (1.0)
    pause .2
    hide bearmenu_maya with Dissolve(.5)
    pause .2
    hide bearmenu_kan with Dissolve(1.5)
    Kan frown worried ec "Okay. Here I go."
    Kan smile worried ec "Uh...Hello? God? Spirit? Whatever you are?"
    Kan frown worried eo "It’s me, Kanna."
    Kan smile worried ec "I know we don’t talk often... or at all, and I know I haven’t really visited your shrine before, or even thought about you."
    Kan "Actually, I’m not even sure what kind of God-spirit-thingy you are."
    # CODE
    # Change size tag below to a more adequate value when font and font size are decided.
    # Kanna should be muterring, so the text shown should be smaller than usual.
    Kan frown skeptic "{size=-10}Spirits are usually animals, right? Or is that just a myth?{/size}"
    Kan smile worried ec "Well, your shrine was the closest to my house, so I guess you get to grant my wish!"
    Kan "I just have to write it down and leave it here, right?"
    "..."
    #SFX Cicadas, environmental

    Kan frown worried ec "A-alright, h-here you go! If you could please make my wish come true, I’d worship you forever! I’ll visit everyday and bring you all kinds of tasty treats!"
    Kan "You name it, I’ll do it! So please. PLEASE. Make it happen. You’re my only hope."
    Kan eo "Can you? Will you?"
    "..."
    Kan smile worried ec "I’ll, um...take that as a maybe."

    #SFX Footsteps "Kanna turns away from the shrine and begins to go home."

    Kan frown pout ec "Oh, and if you’re the spirit of bad relationships, just pretend this never happened!"
    Kan smile happy ec "Well anyway, goodnight."
    #SFX Kanna walking away
    #ART
    #Ringo appears faintly from the top of the shrine, not enough to fully make out that he's a little #bear, but enough to make out that he's small, and clearly a spirit of some sort
    "..."
    show shrine onlayer master:
        ease 3 zoom .95
    "..."
    na "Not exactly my ideal client."
    na "Teenagers have no knack for proper wish-making. These lazy losers only ever wish for love, popularity, and grades they didn't earn."
    na "They always expect life to offer everything up to them on a silver tray! Atleast teenage wishes are usual quick and easy. "
    na "Whatever. One last wish and I'll get my sweet freedom back."

    #na "Teenagers don't have any knack for proper wishmaking."
    #na "They're always so short-sighted, wishing for love, popularity, or good grades they haven't earned."
    #na "They want everything handed to them on a silver tray. Never willing to leave things up to {i}chance.{/i}"
    #na "Of course it doesn't really matter {i}what{/i} her wish is."
    #na "Just one more wish granted, and I'll have earned back my freedom."

    na "No more sticky, smelly fur."
    na "No more hunger pangs and feeling lazy all the time."
    na "{i}Hasta la vista{/i} stupid curse!"
    na "I'll finally be back to my good old fashioned, motivated, sweet smelling, non-sticky self again!"
    na "*{i}sigh{/i}*"
    na "The girl left an envelope at the base of my shrine..."
    na "...It's sealed with a heart-shaped sticker."
    na "Screw it, I'm not spending another miserable second away from my beautiful body!"
    na "Let's get this party started!"

    #ART BG Kanna's Bedroom
    scene room night onlayer master with squares:
        xanchor .5
        yanchor .5
        xpos .15
        ypos .15
    #$camera_move(7000, 500, 0, 0, duration=5)
        subpixel True
        parallel:
            xpos 0.73
            easein 5 xpos 0.16
        parallel:
            ypos 0.24
            easein 5 ypos 0.16

    $ hide_sides = ['Ringo']
    "..."
    Kan sleeping "Zzzz."

    #ART #SFX Ringo Entrance
    #The lights are out. Kanna is cocooned in various blankets, sleeping peacefully. Her window is open, and the blue glow of the moon gently illuminates her room.
    #A large circular portal forms in the center of the room. Golden sparks, and flashes light up the room. A large explosion erupts from the circle, filling the room with smoke.
    #Ringo is summoned from the explosion, and floats in the smoke, wearing a smug expression.
    #Upon hearing the explosion, Kanna falls off of her bed, and sits awestruck on the ground with blankets all around her. She begins to run out of the room, too shocked to scream. She reaches the door, and hears a strange voice from behind her.
    scene black with fade
    show cgs ringo_ent_shadow with dissolve:
        zoom .5
        xpos -.33
    #Half asleep
    "???" "Wake up, feeble human, and behold!"
    Kan sleeping "Wha? Beetle? Just five more minutes, Mr. Beetle. Zzzz~"
    "???" "I said, {i}WAKE UP, FEEBLE HUMAN, AND BEHOLD!{/i}"
    Kan sleeping "I don't care if it's not legal. What does a beetle know about law anyway? Zzzz~"
    "???" "FEEBLE. Fee-ble. You have five seconds to open up those cute little eyes of yours before I show you first hand what that word means!"
    Kan sleeping "*{i}Yawn{/i}*"
    Kan neutral surprised crazy "..."
    #ART CG Kanna turns around. She stares, overwhelmed by the smoke and effects. She braces #herself in anticipation for whoever or whatever the voice was that spoke through the smoke.
    #The smoke dissipates, revealing a small, floating, bear-like spirit.
    camera:
        subpixel True
        parallel:
            linear 1.86 zpos -157.0
        parallel:
            linear 1.86 xpos 0.0
        parallel:
            linear 1.86 rotate 0
        parallel:
            linear 1.86 ypos 87
    $renpy.pause(1.0)
    show cgs ringo_ent with dissolve:
        zoom .5
        xpos -.33
    Kan neutral surprised crazy "A bear?"
    $ hide_sides = ['Ringo']
    "Bear" "I'm not a bear. But I'm as close to the real thing as you’re gonna get."
    Kan neutral surprised crazy "What happened to the feeble paralegal beetle?"
    "Bear" "That was your sleep crazed delusion. And I don't do law wishes. Way too boring."
    Kan smile surprised crazy"...Ha. Ahaha. There's a talking teddy bear in my room."
    Kan frown pout ec "This is a dream, right? I usually wake up after I fall out of bed."
    Kan "I'll just get back in and try again..."
    "Bear" "{i}Bzzzt!{/i} Wrong. You’re wide awake, and you’re about to get your wish granted."
    Kan frown skeptic "My wish?"
    Kan speaking surprised crazy "You mean {i}that{/i} wish? From the shrine!?"
    "Bear" "{i}Ding ding ding!{/i} We have a winner."
    Kan "You're the God-spirit-thingy from the shrine!"
    "Bear" "Please allow me to introduce myself."
    "Bear" "The name's Ringo. Fortune spirit! Master of chance, fate, luck, and all things prosperous."
    $ hide_sides = ['Ringo']
    Rin "Nice to meet ya!"
    Kan "Wait... Why are you in my room? What happe...Why are you a bear?"
    Rin "Don't sweat the small stuff! Do you want your wish granted or not?"
    Kan speaking pleading "Yes!"
    Kan speaking confident "Please grant my wish!"
    Rin "That's what I thought."
    scene room night with squares:
        zoom .75
        xanchor .5
        yanchor .5
        xpos .5
        ypos .5
    "Let's crack open that letter."
    $ hide_sides = []
    Rin smile normal "Alright, what did you wished for?"
    # CODE Set the appropriate time in the wait tag to match the VAs performance.
    Rin speaking happy "I, Kanna, wish for my classmate, Kyousuke..."
    Rin curious "...to notice me and...{w=0.5}"
    Rin annoyed "...go on a date with me."
    Rin headache mc "..."
    Rin headache mo "Seriously? You wanna turn your life into a bad rom-com?"
    Kan smile worried ec "What’s wrong with that?"
    Rin angry speaking noarm "I can grant you infnite prosperity and you ask for a date?"
    Kan smile worried ec "How was I supposed to know that? Besides, finding true love is the most fortunate a person can be!"
    Rin angry speaking noarm "God, teenagers really don't know the meaning of nuance or critical thought."
    Rin angry speaking noarm "Why'd you put a love wish on a fortune shrine anyway? There are different types of shrines for a reason, you know."
    Kan frown worried eo "I thought any shrine and would wor... what’s the problem? You’re a magical spirit bear!"
    Rin angry speaking noarm "I'm not a bear. I just look like one at the moment."
    Rin angry speaking noarm "And the issue is that your wish is more trouble than it's worth."
    Kan frown worried eo "So...you can't grant my wish?"
    Rin angry speaking noarm "Listen, kiddo, do you know how hard it is to make people fall in love?"
    Rin angry speaking armout "It's not exactly a snap of the fingers. Love, actual love, doesn't just happen."
    Rin angry speaking armout "Love takes commitment, trust, understanding, empathy, and most importantly, time."
    Rin angry speaking noarm "I could grant ten other wishes in the time it takes to grant yours!"
    Kan smile happy speaking ec "But you can grant the wish! There's no rush, I'll wait as long as I need to get my Kyousuke."
    Rin angry speaking noarm "I CAN grant it, but I'm not going to."
    Kan frown worried eo "What? Why not!?"
    Rin angry speaking noarm "It's too much time and a huge hassle for just one wish."
    Kan smile happy speaking ec "Just do it quick!"
    Rin laughing ec "Quick!? Did you even listen to anything I just said? That'd take a miracle worker!"
    Kan speaking curious"Aren’t you a miracle worker, though?"
    Rin smile normal "Of course I am. But if I grant one more wish I get out of this stupid bear form."
    Rin smile normal "I'm looking for something quick and dirty, a one day wish, tops. I.E., not a love wish."
    Kan speaking curious "Just wave your little bear paws around and have Kyousuke go on a date with me. Easy-peasy, lemon-squeezy."
    Rin angry speaking noarm "That is not how magic works."
    Kan frown worried eo "It's magic. How complicated can it be?"
    Rin angry speaking armout "Fine. You want to go on a date with this guy? I can put you both in a fancy restaurant right now and you guys can wing it. There's your date."
    Kan speaking surprised crazy "W-w-wait! I want him to notice me first and then we go on a date!"
    Kan speaking surprised crazy "It's got to be real! I ask him out or he asks me out, that type of thing."
    Kan speaking surprised crazy "A fancy restaurant in the middle of the night is {i}not{/i} real!"
    Rin angry speaking noarm "See? True love is specific to each person and each couple. It's a bunch of nonsense I'm not dealing with."
    Rin grin "More trouble than it's worth. So I'm outta here. Try the love Goddess in the next town over."
    Kan speaking confident "Hold on! You can’t just barge in here, smoke out my room, get my hopes up, and bail!"
    Rin speaking happy "Look kiddo, I get this is all very confusing, but I’m in a rush. I need to find my next client."
    #Kan speaking pleading "Wait! You said you'd grant my wish. You come in here with that whole fireworks display and now you wanna back out?"
    #VOICE dejected
    Kan frown pout ec "Stupid dream bear can't even grant my wish."
    Rin annoyed "Hey, I said I could do it. I just don't want to."
    #Kanna Wink
    Kan speaking sarcastic ec "No, I get it. I guess it's just too hard for you, being a big grumpy fat bear and all."
    Rin angry speaking noarm "I didn't say that either! Do you even know what I can do? I could make you rich in a day. I could make you a popstar before lunch."
    Rin "I've even raised the dead before! That one was gross and I couldn't sleep for weeks, but hey, I did it."
    Rin angry speaking armout "I'm Ringo Fortune! I can do any stupid thing you humans want. So don’t go questioning me, ya dumb brat."
    Kan speaking confident "Prove it."
    Rin "Excuse me? I don't have to prove anything to you."
    Rin "Now, good night. Have a nice youth, or whatever."
    "Should've expected this sort of thing from a teen. Time to head back to the shrine and play the waiting game again."
    "Kanna" "..."
    "Kanna" "Stupid bear."
    Rin shockedannoyed "..."
    Rin veryannoyed "..."
    Rin sigh"*{i}Sigh{/i}*"
    "{i}Just one last wish.{/i}"
    Rin "Tell me about this crush of yours."

    #Animation have Kanna's sprite suddenly become very happy.

    Kan smile happy eo "Really?"
    Rin sarcastic "I just wanna know why you like him, that’s all."

    #MUSIC Something fun here for when Kanna starts up about Kyousuke.

    camera:
        subpixel True ypos 87 zpos -157.0
        parallel:
            zpos -157.0
            ease 30.0 zpos -557.0
        parallel:
            xpos 0.0
            ease 30.0 xpos 0.247916666667
        parallel:
            ypos 87
            ease 30.0 ypos -99
    Kan smile happy speaking ec "Ohh, he’s just the best! He’s got long, flowing, chocolate colored hair. It drapes over his stunning, electric eyes."
    Kan speaking confident "Well, I’ve never seen his eyes... but I KNOW they’re stunning!"
    Kan frown confident ec "He’s the strong and silent type, so he doesn't say much."
    Kan drooling happy ec "But when he does talk, his voice sounds like liquid diamonds, pouring directly into my ears."
    Kan speaking surprised crazy "And he's got this... presence. Like whenever he’s in the room, it's like the world revolves around him."
    Rin happy ec "I’m sure it does."
    Kan speaking skeptic eo "Oh, I know no one's perfect, and everyone has flaws. But Kyousuke is the most perfect person I’ve ever met!"
    Rin "I’m sure he is."
    Kan speaking sad crazy "It’s just, whenever I get close to him, I freeze! My heart sinks and my legs turn to jelly!"
    Kan speaking embarrassed ec "How's a Jane Doe like me supposed to approach a Greek Adonis like him?"
    Rin headache mo "Alright, alright, dial down the gushing back a notch."
    Kan "Oh, please please please, I'll do anything Mr. Bear, just grant my wish!"
    Rin speaking normal "It's Ringo. And even if I were to help you, it won't be easy. You'll have to do everything I say."
    Kan smile worried eo "Really? You’ll do it?"
    Rin "Repeat what I just said."
    Kan Kan smile concerned ec "I have to do everything you say?"
    Rin evil grin "Absolutely everything. And I get unlimited food and beverage options. You promised me food back at the shrine."
    Kan speaking confident "Of course! I'll make you anything you want!"
    Kan smile happy blushing "Anything  to be with my sweet, sweet Kyousuke!"
    Kan salivating "Ehehe..."
    Rin angry speaking noarm "You can start by toning it down! I've got some planning to do and would prefer some peace and quiet."
    "*rip*"
    Kan speaking sad crazy "Hey, my limited edition Kyousuke poster!"
    Rin smile normal "Hey, we're about to replace it with the real thing, right?"
    Rin speaking happy "I'll hitch a ride in your backpack tomorrow to see what we're working with. So get back to sleep and try not to freak out until then."
    Kan smile happy speaking ec "Man, what a nice dream! Maybe I placed my wish on the dream spirit's shrine."
    Rin "Yeah yeah, you’ll see when you wake up, kiddo."
    #ART The camera pans outside of Kanna’s room, showing the night sky.
    "God, had to be a love wish. Typical."
    "I won't know the hand I've been dealt until I get a good look at this Kyousuke guy."
    "They're just teenagers after all. They fall in and out of love with a change in the weather."
    "As long as I play the right card at the right time, it should be a cakewalk to tilt the odds into Kanna's favor."
    "I've been doing this wish granting thing for hundreds, thousands, hundreds of thousands of years!"
    "I've granted the wishes of amoebas and cells all the way to kings and queens of nations!"
    "A love wish isn't the easiest thing in the world, but I've done way worse."
    "Maybe this won't even be as bad as I think. I haven't played Cupid in a while, it could be fun!"
    "Tomorrow is the beginning of the end for this bear form. And that's all that matters at the end of the day."
    "It can't be that hard to make a couple of ditsy high schoolers fall for each other."
    "..."
    "...Right?"

    #Cut out ending to Prologue
    #ART show pocket watch.
    #"Well that's just typical."
    #"You're not going to cut me any slack with this one, are you Fortune?"
    #Art Card Table - A table where Ringo has some playing cards. He's flipping them over, shuffling etc.
    #"A week is hardly enough time to bring two people together by chance alone."
    #"I won't know for sure how the cards are laid out until I get a look at the guy we're dealing with."
    #"This 'Kyousuke'."
    #"I mean hey, they're just teenagers. They fall in and out of love with a change in the weather."
    #"And you'd know better than any, Fortune, that the right card played at the right time can tilt the odds in anyone's favor."
    #"And nobody stacks the deck like me."
    #"Hell, this might not be as bad as I thought. I can play Cupid!"
    # Pause for a bit. Consider cutting any BGM or Ambience playing.
    #Rin "...Right?"
    scene black with fade
    jump chapter1
