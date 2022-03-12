#ART BG Shrine evening
label start:

    #INIT RELETIONSHIP 0

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
    Kan frown worried ec "Okay...Here I go."
    Kan smile worried ec "Uh... Hello? Spirit?"
    Kan frown worried eo "It’s me, Kanna."
    Kan smile worried ec "I know we don’t talk often... or at all, and I know I haven’t really visited your shrine before, or even thought about you."
    Kan "Actually, I’m not even sure what kind of spirit you are."
    # CODE
    # Change size tag below to a more adequate value when font and font size are decided.
    # Kanna should be muterring, so the text shown should be smaller than usual.
    Kan frown skeptic "{size=-10}Spirits are usually animals right, or is that just a myth?{/size}"
    Kan smile worried ec "Well, your shrine was the closest to my house, so I guess you get my wish!"
    Kan "I just have to write it down and leave it here, right?"
    "..."
    #SFX Cicadas, environmental

    Kan frown worried ec "So if you could please grant my wish, I’d worship you forever! I’ll visit everyday and bring you all kinds of tasty treats!"
    Kan "You name it, I’ll do it! So please grant this wish. You’re my only hope."
    Kan eo "Will you do it for me?"
    "..."
    Kan smile worried ec "I’ll, uh...take that as a maybe."

    #SFX Footsteps "Kanna turns away from the shrine and begins to go home."

    Kan frown pout ec "Oh, and if you’re the spirit of bad relationships, you can just pretend this never happened!"
    Kan smile happy ec "Well anyway, goodnight."
    #SFX Kanna walking away
    #ART
    #Ringo appears faintly from the top of the shrine, not enough to fully make out that he's a little #bear, but enough to make out that he's small, and clearly a spirit of some sort
    "..."
    show shrine onlayer master:
        ease 3 zoom .95
    "..."
    na "Well, she’s not exactly my ideal client."
    na "Teenagers don't have any knack for proper wishmaking."
    na "They're always so short-sighted, wishing for love or popularity, or good grades they haven't earned."
    na "They want everything handed to them on a silver tray. Never willing to leave things up to {i}chance.{/i}"
    na "Of course it doesn't really matter {i}what{/i} her wish is."
    na "Just one more wish granted, and I'll have earned back my freedom."
    na "No more sleeping on wooden floors, getting splinters in my back."
    na "No more tourists, no more noise, and no more of this dead-end wish granting business."
    na "Just me, a nice fluffy cloud, and all the peace and quiet a spirit could want."
    na "*{i}sigh{/i}* "
    na "The girl left a envelope at the base of my shrine..."
    na "...It's sealed with a heart-shaped sticker."
    na "Just one last wish. Then I’ll finally get out of this inconvenient form."
    na "Alright, Fortune. I’m feeling pretty motivated!"
    na "With these legs, I'll be lucky to make it before sundown."
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
    Kan sleeping "Zzzz"

    #ART #SFX Ringo Entrance
    #The lights are out. Kanna is cocooned in various blankets, sleeping peacefully. Her window is open, and the blue glow of the moon gently illuminates her room.
    #A large circular portal forms in the center of the room. Golden sparks, and flashes light up the room. A large explosion erupts from the circle, filling the room with smoke.
    #Ringo is summoned from the explosion, and floats in the smoke, wearing a smug expression.
    #Upon hearing the explosion, Kanna falls off of her bed, and sits awestruck on the ground with blankets all around her. She begins to run out of the room, too shocked to scream. She reaches the door, and hears a strange voice from behind her.
    scene black with fade
    show cgs ringo_ent_shadow with dissolve:
        zoom .5
        xpos -.33
    "???" "Wake up feeble human, and behold!"
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
    "Bear" "Actually, not really. But I’m as close to the real thing as you’re gonna get."
    Kan smile surprised crazy"...Ha. Ahaha. There's a talking teddy bear in my room."
    Kan frown pout ec "This is a dream, right? I usually wake up after I fall out of bed."
    Kan "I'll just get back in and try again..."
    "Bear" "Bzzzt! Wrong. You’re wide awake, and you’re about to get your wish granted."
    Kan frown skeptic "My wish?"
    Kan speaking surprised crazy "You mean {i}that{/i} wish?"
    "Bear" "Ding ding ding! We have a winner."
    Kan "You're the spirit from the shrine!"
    "Bear" "Please allow me to introduce myself."
    "Bear" "The name's Ringo. I'm a spirit of Fortune. Master of chance, of fate."
    $ hide_sides = ['Ringo']
    Rin "Nice to meet ya!"
    Kan "But wait, I don't understand! Why are you in my room? What happe...Why are you a bear?"
    Rin "Nevermind that! Do you want your wish granted or not?"
    Kan speaking pleading "Yes!"
    Kan speaking confident "Please grant my wish!"
    Rin "That's what I thought."
    scene room night with squares:
        zoom .75
        xanchor .5
        yanchor .5
        xpos .5
        ypos .5
    "I present the letter she left for me earlier."
    $ hide_sides = []
    Rin smile normal "Alright, now let's see what you wished for."
    # CODE Set the appropriate time in the wait tag to match the VAs performance.
    Rin speaking happy "I, Kanna, wish for my classmate, Kyousuke..."
    Rin curious "...to notice me and...{w=0.5}"
    Rin annoyed "...To go on a date with me."
    Rin headache mc "..."
    Rin headache mo "Seriously? Your wish is to turn your life into a bad rom-com?"
    Kan smile worried ec "Why not? What’s wrong with that?"
    Rin angry speaking noarm "Why'd you put a love wish on a fortune shrine? There are different types of shrines for a reason, you know."
    Kan frown worried eo "I thought I could go to any shrine and make a wish. What’s the problem? You’re a magical spirit bear!"
    Rin speaking normal "Well, more like his representative in this case."
    Kan frown worried eo "So...you can't grant my wish?"
    Rin angry speaking noarm "Listen, kid, do you know how hard it is to make people fall in love?"
    Rin angry speaking armout "It's not exactly a snap of the fingers. Love, actual love, doesn't just happen."
    Rin laughing ec "It would take a miracle worker!"
    Kan speaking curious"Aren’t you a miracle worker, though?"
    Rin smile normal "Course I am. But I’m also about to retire, and I want an easy gig before I go."
    Kan frown skeptic "Retire?"
    Rin grin "And your wish would’ve been my last job, but this is more trouble than it's worth."
    Rin happy ec "Try the love goddess in the next town over."
    Kan speaking confident "Hold on! You can’t just barge in here, smoke out my room and get my hopes up!"
    Rin speaking happy "Look kid, I get this is all very confusing, but I’m in a rush. I need to find my next client."
    Kan speaking pleading "Wait! You said you'd grant my wish. You come in here with that whole fireworks display and now you wanna back out?"
    #VOICE dejected
    Kan frown pout ec "Stupid dream bear can't even grant my wish."
    Rin annoyed "Hey, I never said I couldn't do it."
    #Kanna Wink
    Kan speaking sarcastic ec "No I get it. I guess it's just too hard on you then, being so old and close to retirement."
    Rin angry speaking noarm "I didn't say that either! Do you even know what I can do? I could make you rich in a day. I could make you a popstar before lunch."
    Rin "I've even raised the dead before! That one was gross and I couldn't sleep for weeks, but hey, I did it."
    Rin angry speaking armout "I'm Ringo Fortune! I can do literally any dumb thing you humans want. So don’t go questioning me, brat."
    Kan speaking confident "Prove it."
    Rin "Prove it? I don't have to prove anything to you."
    Rin "Now, good night. Have a nice youth, or whatever."
    "Straightening my tie, I climb up the bed sheet and back to the window."
    "Kanna" "..."
    "Kanna" "Stupid bear."
    Rin shockedannoyed "..."
    Rin veryannoyed "..."
    "{i}Just one last wish.{/i}"
    Rin sigh"{i}Sigh{/i}"
    Rin "Tell me about this guy you like."

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
    Kan drooling happy ec "When he does talk, his voice sounds like liquefied diamonds, pouring right into my ears."
    Kan speaking surprised crazy "And he's got this... presence. Like whenever he’s in the room, it's like the world revolves around him."
    Rin happy ec "I’m sure it does."
    Kan speaking skeptic eo "Oh, I know no one's perfect, and everyone has flaws. But Kyousuke is the most perfect person I’ve ever met!"
    Rin "I’m sure he is."
    Kan speaking sad crazy "It’s just, whenever I get close to him, I freeze! My heart sinks and my legs turn to jelly!"
    Kan speaking embarrassed ec "How's a Jane Doe like me supposed to approach a Greek Adonis like him?"
    Rin headache mo "Alright, alright, kid. Just dial it back a notch."
    Kan "Oh, please please please, I'll do anything Mr. Bear, just grant my wish!"
    Rin speaking normal "It's Ringo. And even if I were to help you, it won't be easy. And you have to do everything I say."
    Kan smile worried eo "Really? You’ll do it?"
    Rin "That depends; repeat what I just said."
    Kan Kan smile concerned ec "I have to do everything you say?"
    Rin evil grin "Absolutely everything. Oh, and I get unlimited food and beverage options. You promised me food back at the shrine."
    Kan speaking confident "Of course! I'll make you anything you want!"
    Kan smile happy blushing "Anything at all to be with sweet, sweet Kyousuke!"
    Kan salivating "Ehehe..."
    Rin angry speaking noarm "You can start by toning it down! I've got some planning to do and would prefer some peace and quiet."
    "*rip*"
    Kan speaking sad crazy "Hey, my poster!"
    Rin smile normal "Hey, we're about to replace it with the real thing, right?"
    Rin speaking happy "I'll hitch a ride in your backpack tomorrow, so get back to sleep and try not to freak out until then."
    Kan smile happy speaking ec "Man, what a nice dream! Maybe I placed the charm on the dream spirit's shrine."
    Rin "Yeah yeah, you’ll see when you wake up, kid."
    #ART The camera pans outside of Kanna’s room, showing the night sky.
    "I guess finishing my career with a love wish ain’t so bad."
    #ART show pocket watch. 
    "Well that's just typical."
    "You're not going to cut me any slack with this one, are you Fortune?"
    #Art Card Table - A table where Ringo has some playing cards. He's flipping them over, shuffling etc. 
    "A week is hardly enough time to bring two people together by chance alone."
    "I won't know for sure how the cards are laid out until I get a look at the guy we're dealing with."
    "This 'Kyousuke'."
    "I mean hey, they're just teenagers. They fall in and out of love with a change in the weather."
    "And you'd know better than any, Fortune, that the right card played at the right time can tilt the odds in anyone's favor."
    "And nobody stacks the deck like me."
    "Hell, this might not be as bad as I thought. I can play Cupid!"
    # Pause for a bit. Consider cutting any BGM or Ambience playing.
    Rin "...Right?"
    scene black with fade
    jump chapter1
