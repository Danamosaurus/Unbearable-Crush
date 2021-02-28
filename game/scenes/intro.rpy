#Testing github integration2

#ART BG Shrine evening
label start:
    show screen flower_menu_button with easeinright

    # Update the day shown on the upper corner... to nothing!
    $ game_day = ""
    $ hide_sides = ['Kanna']
    scene black
    Kan frown worried ec "Okay...Here I go."
    show shrine:
        zoom .75 ypos .5 xpos .5 xanchor .5 yanchor.5 alpha 0 subpixel True
        parallel:
            easein 5 zoom .85
        parallel:
            easein 5 alpha 1
    $ hide_sides = []
    Kan smile worried ec "Uh... Hello? God? Is this thing on? Hello?"
    Kan frown worried eo "Hey God, it’s me, Kanna."
    Kan smile worried ec "I know we don’t talk often... or at all, and I know I haven’t really offered you anything before, or visited you, or even thought about you."
    Kan "Honestly I’m not even sure which one you are."
    # CODE
    # Change size tag below to a more adequate value when font and font size are decided.
    # Kanna should be muterring, so the text shown should be smaller than usual.
    Kan frown skeptic "{size=-10}Are all gods animals, or is that just a myth?{/size}"
    Kan smile worried ec "Anywayy, your shrine happens to be the closest to my house, so I guess you get my wish!"
    Kan "I just have to write it on a charm and leave it here, right?"
    "..."
    #SFX Cicadas, environmental

    Kan frown worried ec "So if you could please grant my wish, God, I’d worship you forever! I’ll visit everyday, and pray, and offer food!"
    Kan "You name it, I’ll do it! So please grant this wish. You’re my only hope."
    Kan eo "Will you do it for me, God?"
    "..."
    Kan smile worried ec "I’ll, uh...take that as a maybe."

    #SFX Footsteps "Kanna turns away from the shrine and begins to go home."

    Kan frown pout ec "Oh, and if you’re the god of bad relationships,  you can just pretend this never happened!"
    Kan smile happy ec "Well anyway, goodnight."
    #SFX Kanna walking away
    #ART
    #Ringo appears faintly from the top of the shrine, not enough to fully make out that he's a little #bear, but enough to make out that he's small, and clearly a spirit of some sort
    "..."
    show shrine:
        ease 3 zoom .95
    "..."
    na "Well, she’s not exactly my ideal client."
    na "Teenagers don't have any knack for wishmaking."
    na "They always ask for love or popularity, or good grades they haven't earned."
    na "Of course it doesn't really matter {i}what{/i} the wish is."
    na "If I just grant this one last request, I can finally get out of this dump."
    na "No more sleeping on wooden floors, getting splinters in my back."
    na "No more tourists, no more noise, and no more of this dead-end wish granting gig."
    na "Just me, a nice fluffy cloud, and all the peace and quiet a spirit could want!"
    na "I pick up the envelope the girl had left on the shrine..."
    na "...It's sealed with a heart-shaped sticker."
    na "*{i}sigh{/i}* "
    na "Just one last wish...Then I’ll finally get out of this inconvenient form."
    na "Alright, I’m feeling motivated! Let's get started!"
    na "With these legs, I'll be lucky to make it before sundown."
    #ART BG Kanna's Bedroom
    scene room night with squares:
        xanchor .5
        yanchor .5
        xpos .15
        ypos .15
    $camera_move(7000, 500, 0, 0, duration=5)
    "..."
    Kan sleeping "Zzzz"

    #ART #SFX Ringo Entrance
    #The lights are out, welcoming in the dark of night. Kanna is cocooned in various blankets, sleeping peacefully. Her window is open, and the blue glow of the moon gently illuminates her room.
    #A large circular portal forms in the center of the room. Golden sparks, and flashes light up the room. A large explosion erupts from the circle, filling the room with smoke.
    #Ringo is summoned from the explosion, and floats in the smoke, wearing a smug expression.
    #Upon hearing the explosion, Kanna falls off of her bed, and sits awestruck on the ground with blankets all around her. She begins to run out of the room, too shocked to scream. She reaches the door, and hears a strange voice from behind her.

    $camera_move(-9000, -4371, -1264, 0, duration=1)
    scene black with fade
    $camera_move(2535, 2709, 238, -18, duration=0)
    show cgs ringo_ent_shadow:
        zoom .5
        xpos -.33
    $camera_move(2535, 2709, 238, -18, duration=0)
    Rin "Wake up feeble human, and behold! It is I, the God of Fortune!"
    Kan neutral surprised crazy "..."
    #ART CG Kanna turns around. She stares, overwhelmed by the smoke and effects. She braces #herself in anticipation for whoever or whatever the voice was that spoke through the smoke.
    #The smoke dissipates, revealing a small, floating, bear-like spirit.
    $camera_move(-406, 2050, -525, 0, duration=2)
    $renpy.pause(2.0)
    show cgs ringo_ent with dissolve:
        zoom .5
        xpos -.33
    Rin "Actually, not really. But I’m as close to the real thing as you’re gonna get."
    Kan neutral surprised crazy "A teddy bear?"
    Rin "The name's Ringo."
    Kan smile surprised crazy"...Ha. Ahaha."
    Kan frown pout ec "This is a dream, right? I usually wake up after I fall out of bed."
    Kan "I'll just get back in and try again..."
    Rin "Bzzzt! Wrong. You’re wide awake, and you’re about to get your wish granted."
    Kan frown skeptic "My wish?"
    Kan speaking surprised crazy "You mean {i}that{/i} wish?"
    Rin "Ding ding ding! We have a winner. You placed a wish on my shrine, and now I'm here to deliver!"
    Kan "Wait, I'm confused. What are you? Why did you pick my wish? What happe...Why are you a bear?"
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

    "I begin to unfold the paper she left for me earlier."
    Rin "Alright, now let's see what you asked for."
    # CODE Set the appropriate time in the wait tag to match the VAs performance.
    Rin "I, Kanna, wish for my classmate, Kyousuke, to notice me {i}deep sigh{/i}{w=0.5} and go out with me."
    Rin "Seriously? You want your life to be a bad rom com?"
    Kan smile worried ec "Why not? What’s wrong with that?"
    Rin "Why'd you put a love wish on a fortune shrine? There are different types of shrines for a reason, you know."
    Kan frown worried eo "I thought I could go to any shrine and make a wish. What’s the problem? You’re a god!"
    Rin "Well, more like a representative of one."
    Kan frown worried eo "So...you can't grant my wish?"
    Rin "Listen, kid, do you know how hard it is to make people fall in love?"
    Rin "It's not exactly a snap of the fingers. Love, actual love, doesn't just happen."
    Rin "It would take a miracle worker!"
    Kan speaking curious"Aren’t you a miracle worker, though?"
    Rin "Course I am. But I’m also about to retire, and I want an easy gig before I go."
    Kan frown skeptic "Retire? From being a spirit?"
    Rin "And your wish would’ve been my last job, but this is more trouble than it's worth."
    Rin "Try the love goddess in the next town over."
    Kan speaking confident "Hold on! You can’t just barge in here, smoke out my room and get my hopes up!"
    Rin "Look kid, I get this is all very confusing, but I’m in a rush. I need to find my next client."
    Kan speaking pleading "Wait! You said you'd grant my wish. You and your fireworks display. Now you wanna back out?"
    #VOICE dejected
    Kan frown pout ec "Stupid dream ghost can't even grant my wish."
    Rin "Hey, I never said I couldn't do it."
    #Kanna Wink
    Kan speaking sarcastic ec "No I get it. I guess it's just too hard on you then, being so old and close to retirement."
    Rin "I didn't say that either! Do you even know what I can do? I could make you rich in a day. I could make you a popstar before lunch."
    Rin "I've even raised the dead before! That one was gross and I couldn't sleep for weeks, but hey, I did it."
    Rin "I'm Ringo Fortune! I can do literally any dumb thing you humans want. So don’t go questioning me, brat."
    Kan speaking confident "Prove it."
    Rin "Prove it? I don't have to prove anything to you."
    Rin "Now, good night, have a nice life or whatever."
    "I climb up the bed and back to the window, preparing to exit."
    "Kanna" "..."
    "Kanna" "Stupid bear."
    Rin  "..."
    "{i}Just one last wish.{/i}"
    Rin "{i}sigh{/i}"
    Rin "Tell me about this guy you like."

    #Animation have Kanna's sprite suddenly become very happy.

    Kan smile happy eo "Really?"
    Rin "I just wanna know why you like him, that’s all."

    #MUSIC Something fun here for when Kanna starts up about Kyousuke.
    Kan smile happy speaking ec "Ohh, he’s just the best! He’s got long, flowing, chocolate colored hair. It drapes over his stunning, electric eyes."
    Kan speaking confident "Well, I’ve never seen his eyes... but I KNOW they’re stunning!"
    Kan frown confident ec "He’s the strong and silent type, so he doesn't say much."
    Kan drooling happy ec "When he does talk, his voice sounds like liquefied diamonds, pouring right into my ears."
    Kan speaking surprised crazy "And he's got this... presence. Like whenever he’s in the room, it's like the world revolves around him."
    Rin "I’m sure it does."
    Kan speaking skeptic eo "Oh, I know no one's perfect, and everyone has flaws. But Kyousuke is the most perfect person I’ve ever met!"
    Rin "I’m sure he is."
    Kan speaking sad crazy "It’s just, whenever I get close to him, I freeze! My heart sinks and my legs turn to jelly!"
    Kan speaking embarrassed ec "How's a Jane Doe like me supposed to approach a Greek Adonis like him?"
    Rin "Alright, alright, kid. Just dial it back a notch."
    Kan "Oh, please please please, I'll do anything Mr. Bear, just grant my wish!"
    Rin "It's Ringo. And even if I were to help you, it won't be easy. And you have to do everything I say."
    Kan smile worried eo "Really? You’ll do it?"
    Rin "That depends; repeat what I just said."
    Kan Kan smile concerned ec "I have to do everything you say?"
    Rin "Absolutely everything. Oh, and I get unlimited food and beverage options. You promised me food back at the shrine."
    Kan speaking confident "I promise, Rango!"
    Kan smile happy blushing "As long as I end up with sweet, sweet Kyousuke!"
    Kan salivating"Ehehe..."
    Rin "Ringo...and I told you to dial it down."
    Rin "We’ll get started in the morning, so for now go back to sleep."

    Kan smile happy speaking ec "Man, what a nice dream! Maybe I placed the charm on the dream god’s shrine."
    Rin "You’ll see when you wake up, kid. Get some sleep."

    #ART The camera pans outside of Kanna’s room, showing the night sky.
    "I guess finishing my career with a love wish ain’t so bad."
    "We'll aim for a week. I mean, you're just two teenagers oozing hormones, how hard could it be? I'm a spirit of fortune, I can play cupid!"
    # Pause for a bit. Consider cutting any BGM or Ambience playing.
    Rin "...Right?"
    scene black with fade
    jump chapter1
