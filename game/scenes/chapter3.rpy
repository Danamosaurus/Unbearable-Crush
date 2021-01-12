label chapter3:

    $ game_day = "Day 3"
    scene hallway_1 with squares
    Rin "Alright, we're going to do this just like we talked about."
    Rin "And remember, the most essential thing for right now is that Kyousuke doesn't find out I'm working with you."
    Kan speaking curious "Because you're his...guardian wingman?"
    Rin "Ya know, a little push here, a little nudge there, and it'll be all over for that Maya girl."
    Rin "But it wont work if Kyousuke knows I'm helping you."
    Rin "I gotta make him think it was his idea, you know?"
    Kan "So, you want him to like me naturally?"
    Rin "That's how true love works."
    Kan "And you're going to use your magic spirit powers to manipulate him..."
    Kan "...into liking me..."
    Kan "...naturally?"
    Rin  "Don't think so hard about it. Just don't let him see me with you."
    show hallway_1_guy_1 with dissolve
    Kan "But what do I say? I can't just ask him to be my math partner out of the blue, I need a reason! Maybe I can drop my books in front of him? Or crash into him when I turn the corner? Or maybe-"
    Rin  "Time's up, he's right there! Ask him to be your partner. Be yourself.  Go get 'im, tiger."
    Kan "Wait, Ringo, I-H...he-h-heeeeeeyyy, Kyousuke."
    Kyou  "Oh. Hey, Can-oh! What are you doing here?"
    Kan  "Just, uh, just hanging out, ya know. Also, uh, it's Kanna, but you can call me Can-oh if you really want to. I was wondering, Kyousuke, if you wanted to be math partners next period."
    Kan  "When we go back to class. After this break. When we stop talking. After we walk back to the classroom. Once the break's over. When we're back at our desks. Am I talking too much? Does that make sense?"
    Kyou  "Hmm. Do we go back to class before we're at our desks, or after?"
    Kan  "Uh, before."
    Kyou  "Ok, got it. Sure, let’s be partners!"
    Rin  "You're slaying it, kid."
    Kan  "Shut up!"
    Kyou  "Oh, sorry."
    Kan  "Nononono, I meant like, 'shut up I can't believe you totally want to be partners with me!' Haha."
    Kyou  "Um, are you alright? You're acting funny."
    Kan  "Yeah, why would I..."

    #ART, CG, Dating Sim GUI
    "Before Kanna could finish speaking, a set of VN GUI choices appears in front of Kyousuke and Kanna. They are facing Kyousuke, so Kanna can't quite make out what they are supposed to say."

    Kan  "Uh, Kyousuke, what are those? Kyousuke? You alright?"
    Rin  "You can see those?"
    Kan  "Kyousuke?"
    Kyou  "Hmmm."
    Rin "He can't hear you. Those are the choices in his conscience. He's trying to figure out what to do in this situation."
    Kan  "We wouldn't be in this situation if you just kept quiet!"
    Rin  "We all need moral support sometimes, excuse me for trying to help."
    Kan "Woah, so you mean I can see what Kyousuke is thinking."
    Rin  "It's due to our contract. Let me handle this."
    Kan "How intimate."
    "I climb up onto Kyousuke's shoulder."

    Rin  "Let's see what we got here."
    "'Ask about the second voice you think you heard.'"
    "'Decline being partners with Kanna.'"
    "Oof, that's not good. What should I have him do instead?"
    "I have to keep the idea simple enough so he can't screw it up."

    menu:
        "Choices to send to Kyousuke":
            "Laugh it off, forgive Kanna for yelling at you."
            "Kanna's nervous about something. Make her feel comfortable."

    #Choice: "Laugh it off, forgive Kanna for yelling at you."

    "I  make the selection for Kyousuke, then float back to Kanna to hide in her backpack again. "

    Kyou  "Hahaha, it's alright, Kanna. I know what ya mean."
    Kyou  "Like 'Oh shut up! No way!' right?"
    Kan  "Erm... Yeah, exactly! I'm just excited to get started, ya know?"
    Kyou  "But what was that voice that came from behind you?"
    Kan  "What!?"

    # CODE  Have Kyousuke's sprite move closer to Kanna

    Kyou  "It sounded like it came from your backpack or something."
    Kyou  "No one is behind you. So what was tha…"

    # CG ?
    "Without missing a beat, Kanna turns and throws a right jab, hitting Kyousuke square in the face, knocking him out. He slumps back against the wall."

    Rin  "WHAT!? WHY!//?"
    Kan  "He - he was gonna find out about you. A-a-and you said you couldn't fulfill my wish if that happened."
    Rin  "And your first response is punching him in the face? Seriously?"
    Kan  "I don't know! I panicked! I thought I was gonna lose you and my chance with Kyousuke!"
    Rin "Are you a yandere or a tsundere? Make up your mind!"
    Kan "I don’t even know what that means! Oh god, what am I gonna do?"
    Rin  "Cool it, I'll try and fix this. I don't think he's gonna be happy about this, though."
    Rin  "Next time, instead of unleashing the god hand on the poor kid, try using words first, ok?"
    Kan  "Okay..."
    Rin  "You knocked 'im out in one hit! Jeez, what are your parents feeding you? Dumbbells?"
    Kan  "Anybody can do that!"
    Rin  "Sweety, normal teenage girls don't throw a punch like that. I'm pretty sure you dented the wall."
    Kan  "It wasn't that bad!"
    Rin  "Whatever, I'll get him awake."

    "I  float over to Kyousuke, clap my hands, rub them together, and place them on Kyousuke's cheeks, healing his sullen face instantly, and waking him up."

    Kyou  "Ooh, what happened?"
    Kan  "Oh! Kyousuke, are you alright?"
    Kyou  "Hey, Can-oh! What are you doing here? I had this weird dream that you punched me asleep, haha."
    Kan  "W-we were just talking, remember?"
    Kyou  "Nope. What were we talking about?"
    Kan "O-oh! It wasn't important."

    #Choice1.A: Kanna gets -1 points.
    #Choice1.A:end.

    #Choice: "Kanna's nervous about something. Make her feel comfortable."

    Kyou  "It's alright Can-oh, I'm not that great at math either."
    Kan  "Wha?"
    Kyou  "It's ok to be nervous when asking for help. We're all bad at something, so we gotta help each other out, right?"
    Kan  "Um, right!"
    Kyou  "Just ignore that weird voice that came from behind you, that's just the sound of stress."
    Kan  "What? You heard that?"
    Kyou  "Don't worry about it now! Like I said, it's the sound of stress, right?"
    Kan  "Um, right!"
    Kyou  "We'll do our best together!"
    Kan  "Oh, Kyousuke, only you could say something as kind as that."

    #Choice1.BKanna gets +1 points
    #Choice1.B:end

    #ART enter Maya.
    #Mid conversation, Maya walks up to Kyousuke, clearly annoyed that Kanna is there talking to him.

    Maya  "Good morning Kyousuke! Who's your little friend here?"
    Kyou  "Oh, this is Can-oh! She's our classmate, remember?"
    Maya  "Can't say that I do. I meet so many people daily, how can I remember each copy-paste face? Nice to meet you Can-oh, I'm Maya."
    Kan  "It's Kanna, actually. The pleasure's mine, I guess."
    Maya  "Pretty sure it's Can-oh; that's how Kyousuke said it. You calling him a liar?"
    Kan  "Of course not, he simply forgot. Happens to everyone."
    Maya  "Oh, so you're calling him simple now? Kyousuke is the most sophisticated man I have ever met. His intellectual prowess is something mere normies can't comprehend."
    Maya  "The fact he's wasting his time in this lugubrious school is beyond even my own grasp."
    Maya  "And I've never received anything less than 103% in any subject. So, darling, I think I can quite tell someone of the same intellectual status as me when I see them."
    Kyou  "Wow! That's really nice of you Maya! I don't really know what any of that means, but I think it was a compliment!"
    Maya  "It's not simple flattery! It's a fact."
    Kan  "Yeah, ok, cool. But me and Kyousuke were just talking about being math partners next period."
    Maya  "I’m sorry? Kyousuke and I will be math partners next period."
    Kan  "Huh?"
    Kyou  "Oh I forgot, Can-oh; me and Maya are always math partners."
    Maya  "That's right."
    Kan  "But-"
    Maya  "You heard him, ditzy. We're working on math together."
    Kan  "Ok, listen here, you stupid..."

    #ART CG Two more VN GUI choices appear in front of Kyousuke.

    #VOICE  Whispering#
    "Here we go again."

    "I float behind Kyousuke once again."

    "Alright, let's see what we have this time."

    # SFX or ART portray this "something" isn't right through a strange sound or some kind of visual glitch?
    "Wait, something isn't right here."
    "I sense… something familiar."

    "I  look around, trying to locate the weird sensation."

    "Huh, is there another spirit around?"
    "Doesn't matter, gotta stay focused on the game."

    # CG Display the two choices below.
    "'Choose Maya as a math partner.'"
    "\" Head to the bathroom.'"
    "What kind of options are those? He really can't think for himself at all."
    "I guess that’s where I come in."
    "Really, what would that girl do without me?"
    "Now, what’s the best way to go about this?"

    # Code
    menu:
        "Choose Kanna as a math partner.":
            #Choice: "Choose Kanna as a math partner.

            Kyou  "Ya know, Maya, This other girl may need more help in math then you do. Maybe I should help her this time. It's the right thing to do."
            Maya  "Oh, Kyousuke, your commitment to justice and helping the less fortunate is only matched by the strength and sharpness of your jawline."
            Maya  "Are you sure you don't mind working with her? I know you're only doing it out of pity, but are you absolutely positive this is what you want to do?"
            Kyou  "It's ok Maya, we can be math partners tomorrow. I'll sacrifice myself for the greater good."
            Maya  "Kyousuke, your valiance knows no bounds. I’ll get him back tomorrow. Have a nice class...Kanna."
            Kan  "Gee, thanks for the sincerity... Let's get to studying, then I guess."
            #Choice2.A: Both Kanna and Maya receive no points
            #Choice2.A: End


        "Work in a group with Kanna and Maya.":
            #Choice: "Work in a group with Kanna and Maya."

            Kyou  "Wait, maybe we can all work together in a group!"
            Maya  "What!?"
            Kan  "Uh..."
            Kyou  "Yeah, we can ask the teacher if it can be the three of us! You guys are getting along so well anyway. It'll be fun!"
            Maya  "If you really insist, Kyousuke. While I think it should be just me and you, I guess we can let her in, for her own sake."
            Kyou  "Come on Kanna, it'll be fun!"
            Kan  "Well, alright. I guess it won't be too bad as long as you are there, Kyousuke."
            #Choice 2.B: Both Kanna and Maya receive +1 points.
            #Choice2.B End

    #ART Kanna's room
    scene room

    Rin  "Alright kid. Here's how Kyousuke is feeling about both you and Maya so far."

    # ART or CODE
        #Show total scores so far.
        #Possible scores from day 3 .
        #Kanna +2, Maya +1.     Choice 1.B and choice 2.B
        #Kanna 0, Maya +1.         Choice 1.A and choice 2.B
        #Kanna +1,Maya 0        Choice 1.B and choice 2.A
        #Kanna-1,Maya+0        Choice 1.A and choice 2.A

    #Show total results thus far.

    #opportunities for different results.

    Rin  "So, I got this weird feeling today while you were in class."
    Kan  "Oh? What do you mean?"
    Rin  "I'm not sure. There was a strange energy floating around the school."
    Kan  "It was probably that horrible Maya girl. She was driving me up the wall today."
    Rin  "No, it wasn't teenage hormones. Something like me. A spirit, maybe."
    "Or maybe I'm underestimating teenage emotions."
    Kan  "Hm, I guess I never considered the existence of other spirits. It makes sense that there’s more than just you though."
    Kan "Are they all cute little animals?"
    Rin "Heh. No, that’s a me thing. This form is a punishment for a failed mission."
    Kan "...Oh. Well, uh, let me know if something happens."
    Rin  "Will do. Get some sleep, kiddo, we're taking another stab at that partner thing tomorrow."
    Kan  "Yeah! She can't keep Kyousuke all to herself. If it's only her we have to deal with, we can manage, right?"
    Rin  "Right!"
jump day4
