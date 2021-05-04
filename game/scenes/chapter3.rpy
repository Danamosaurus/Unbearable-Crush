label chapter3:

    $ game_day = "Day 3"
    scene hallway onlayer master with squares:
        subpixel True xpos 0.5 ypos 2.2 xanchor 0.5 yanchor 1.0 rotate None 
        parallel:
            xpos -0.02
            ease_cubic 3.17 xpos 0.45
    

    show kannabox focused onlayer master with easeinright:
        subpixel True xpos -0.13 ypos 1.14 xanchor -0.43 yanchor 1.5 zoom 0.25 rotate None 
    Rin "Alright, we're going to do this just like we talked about."
    hide kannabox with dissolve
    Rin "And remember, the most essential thing for right now is that Kyousuke doesn't find out I'm working with you."
    Kan smile happy ec "Because you're his guardian wingman?"
    Rin "Ya know, a little push here, a little nudge there, and it'll be all over for that Maya girl."
    Rin "But it wont work if Kyousuke knows I'm helping you."
    Rin "I gotta make him think it was his idea, you know?"
    Kan smile happy eo "So, you want him to like me naturally?"
    Rin "That's how true love works."
    Kan frown worried eo "And you're going to use your magic spirit powers to manipulate him..."
    Kan "...into liking me..."
    Kan  "...naturally?"
    Rin  "Don't think so hard about it. Just don't let him see me with you."
    #ART Cutout of Kyousuke on BG
    #show hallway_1_guy_1 with dissolve
    Kan concerned ec "But what do I say? I can't just ask him to sit with me out of the blue."
    Kan speaking confident "Theres always an inciting incident!"
    Kan neutral surprised crazy "Maybe I should drop my books in front of him? Or crash into him when I turn the corner? Or maybe-"
    Rin "Don't be a walking cliche!"
    Rin "Anyway, time's up, he's right there! Ask him to be your partner. Be yourself.  Go get 'im, tiger."
    Kan speaking surprised crazy "Wait, Ringo, I-H..."
    Kan smile concerned ec "He-h-heeeeeeyyy, Kyousuke."
    Kyou "Oh. Hey, Can-oh! What are you doing here?"
    Kan  "Just, uh, just hanging out, ya know. Also, uh, it's Kanna, but you can call me Can-oh if you really want to. I was wondering, Kyousuke, if you wanted to be math partners next period."
    Kan  "When we go back to class. After this break. When we stop talking. After we walk back to the classroom. Once the break's over. When we're back at our desks. Am I talking too much? Does that make sense?"
    Kyou  "Hmm. Do we go back to class before we're at our desks, or after?"
    Kan  speaking sarcastic ec "Uh, before."
    Kyou  "Ok, got it. Sure, let’s be partners!"
    Rin  "You're slaying it, kid."
    Kan speaking pleading "Shut up!"
    Kyou  "Oh, sorry."
    Kan neutral surprised crazy "-"
    Kan questioning embarrassed "Nononono, I meant like, 'shut up I can't believe you totally want to be partners with me!' Haha."
    Kyou  "Um, are you alright? You're acting funny."
    Kan speaking excited crazy blush "Yeah, why would I..."

    #ART, CG, Dating Sim GUI
    Kan frown skeptic "Uh..."
    show Kyou normal at center with Dissolve(3.0)
    Kan "...Kyousuke?"
    "It's as if he's been put on pause."
    Kan "Kyousuke? What's wrong?"
    "Oh. I see. This sometimes happens in these sorts of situations."
    Kan smile concerned ec "Kyousuke?"
    $ hide_sides = ['Kyousuke']
    Kyou  "Hmmm."
    Rin "I'm pretty sure he can't hear you. He's trying to figure out what to do in this situation."
    Kan  "We wouldn't be in this situation if you just kept quiet!"
    Rin  "We all need moral support sometimes, excuse me for trying to help."
    Kan speaking curious "Are these what Kyousuke is thinking about?"
    Rin "Well, more the choice he has in front of him."
    "Literally..."
    Kan smile worried eo "I can read his thoughts?"
    Kan smile happy speaking ec "How intimate..."
    Rin  "Let me handle this."
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
    hide Kyou with dissolve
    $ hide_sides = []
    "I  make the selection for Kyousuke, then float back to Kanna to hide in her backpack again. "

    Kyou happy "Hahaha, it's alright, Kanna. I know what ya mean."
    Kyou smirk "Like 'Oh shut up! No way!' right?"
    Kan  "Erm...Yeah, exactly! I'm just excited to get started, ya know?"
    Kyou surprised "But what was that voice that came from behind you?"
    Kan "What?"

    # CODE  Have Kyousuke's sprite move closer to Kanna

    Kyou  "It sounded like it came from your backpack or something."
    Kyou  "No one is behind you. So what was tha..."
    Kan "-"
    Kan neutral surprised crazy '-'

    # CG ?
    "A right jab hits Kyousuke square in the face. He slumps back against the wall." with vpunch
    Rin  "W-Why?"
    Kan speaking embarrassed ec "He - he was gonna find out about you. A-a-and you said you couldn't fulfill my wish if that happened."
    Rin "And your first response is to mess up his face?"
    Rin "Yandere or Tsundere?! Make up your mind!"
    Kan speaking sad crazy "Oh god, what am I gonna do?"
    Rin  "Cool it, I'll try and fix this. I don't think he's gonna be happy about this, though."
    Rin  "Next time, instead of unleashing the god hand on the poor kid, try using words first, ok?"
    Kan sad smile "Okay..."
    Rin  "You knocked 'im out in one hit! Jeez, what are your parents feeding you? Dumbbells?"
    Kan frown pout ec "Anybody can do that!"
    Rin  "I'm pretty sure you put a dent in the wall."
    Kan frown confident ec "It's not that bad!"
    Rin  "Whatever, I'll get him awake."
    #SFX some kind of sound effect. 
    Rin "Hey...Wake up!"
    Kyou "Ooh, what happened?"
    Kan smile worried eo "Oh! Kyousuke, are you alright?"
    Kyou  "Hey, Can-oh! What are you doing here? I had this weird dream that you punched me asleep, haha."
    Kan smile concerned ec "W-we were just talking, remember?"
    Kyou  "Nope. What were we talking about?"
    Kan smile happy speaking ec "O-oh! It wasn't important."

    #Choice1.A: Kanna gets -1 points.
    #Choice1.A:end.

    #Choice: "Kanna's nervous about something. Make her feel comfortable."

    menu:
        "Kanna's nervous about something. Make her feel comfortable.":
            #Kanna gets -1 points
            $game_player.increaseRelationship("Kanna",-1)

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

            #Show example
            $Kanna = game_player.getRelationship('Kanna')
            "We have [Kanna] from Kanna"

        "Choice1.BKanna gets +1 points":   

            #Choice1.BKanna gets +1 points
            #Choice1.B:end

            #Kanna gets -1 points
            $game_player.increaseRelationship("Kanna",1)

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

            #Show example
            $Kanna = game_player.getRelationship('Kanna')
            "We have [Kanna] from Kanna"

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
            $game_player.increaseRelationship("Kanna",1)
            $game_player.increaseRelationship("Maya",1)

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

    "SHOW SCORE"

    $Kanna = game_player.getRelationship('Kanna')
    $Maya = game_player.getRelationship('Maya')
    "We Kanna has [Kanna] and Maya has [Maya]"

    #opportunities for different results.

    Rin  "So, I got this weird feeling today while you were in class."
    Kan  "Oh? What do you mean?"
    Rin  "I'm not sure. There was a strange energy floating around the school."
    Kan  "It was probably that horrible Maya girl. She was driving me up the wall today."
    Rin  "No, it wasn't teenage hormones. Something like me. A spirit, maybe."
    "Or maybe I'm underestimating teenage emotions."
    Kan  "Hm, I guess I never considered the existence of other spirits. It makes sense that there’s more than just you though."
    Kan "Are they all cute little animals?"
    Rin "Heh. No, not usually. That's kind of just a {i}me{/i} thing."
    Kan "...Oh. Well, uh, let me know if something happens."
    Rin  "Will do. Get some sleep, kiddo, we're taking another stab at that partner thing tomorrow."
    Kan  "Yeah! She can't keep Kyousuke all to herself. If it's only her we have to deal with, we can manage, right?"
    Rin  "Right!"
jump day4
