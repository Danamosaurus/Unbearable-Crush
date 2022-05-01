label chapter3:

    $ game_day = "Day 3"
    scene hallway onlayer master with squares:
        subpixel True xpos 0.5 ypos 2.2 xanchor 0.5 yanchor 1.0 rotate None
        parallel:
            xpos -0.02
            ease_cubic 3.17 xpos 0.45
    #Begin Ch3 part 1
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
    Kan smile worried ec "But what do I say? I can't just ask him to sit with me out of the blue."
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
    Kyou  "Ok, got it. Sure, let’s be partners."
    Rin  "You're slaying it, kid."
    Kan speaking pleading "Shut up!"
    Kyou  "Oh, sorry."
    Kan neutral surprised crazy "-"
    Kan questioning embarrassed "Nononono, I meant like, 'shut up I can't believe you totally want to be partners with me!' Haha."
    Kyou  "Um, are you alright? You're acting funny."
    Kan speaking excited crazy blush "Yeah, why would I..."

    #ART, CG, Dating Sim GUI. Ask hamu for an update on this.
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

    # TEST adding an optional thought that wasn't in script
    show screen thought(["'Ice cream...'"],
                        block_progress = False)
    Rin  "Let me handle this."
    "I climb up onto Kyousuke's shoulder."

    # TEST be sure to force hide the thought screen occasionally, since renpy skip and rollback sometimes fails to hide it
    hide screen thought

    Rin  "Let's see what we got here."

    # TEST changing an existing thought in script to the new clickable one that blocks progress
    call screen thought(["'Press her further about the ominous voice.'",
                        "'Reject this weird girl.'"])
    hide screen thought
    # "'Press her further about the ominous voice.'"
    # "'Reject this weird girl.'"
    "Oof, that's not good. I should {i}inspire{/i} him with a better choice."
    "But what should I have him do instead?"
    "I have to keep the idea simple enough so he can't screw it up."

    menu(choice_type="thought",
        original_thought=["'Press her further about the ominous voice.'",
                        "'Reject this weird girl.'"]):
        # "Choices to send to Kyousuke"
        "Laugh it off, forgive Kanna for yelling at you.":
            "I  make the selection for Kyousuke, then float back to Kanna to hide in her backpack again. "
            jump ch3choice1option1
        "Kanna's nervous about something. Make her feel comfortable.":
            "I  make the selection for Kyousuke, then float back to Kanna to hide in her backpack again. "
            jump ch3choice1option2

label ch3choice1option1:
    #Chapter 3 choice 1 option 1: "Laugh it off, forgive Kanna for yelling at you."
    hide Kyou with dissolve
    $ hide_sides = []

    Kyou happy "Hahaha, it's alright, Kanna. I know what ya mean."
    Kyou smirk "Like 'Oh shut up! No way!' right?"
    Kan  "Erm...Yeah, exactly! I'm just excited to get started, ya know?"
    Kyou surprised "But what was that voice that came from behind you?"
    Kan neutral surprised crazy "..."
    # CODE  Have Kyousuke's sprite move closer to Kanna
    Kyou frown "It sounded like it came from your backpack or something."
    Kyou frown "No one is behind you. So what was tha..."
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
    Rin  "Is that a dent in the wall?"
    Kan frown confident ec "It's not that bad!"
    Rin  "Hey, big guy! Wake up."
    #SFX some kind of sound effect.
    Rin "Wake up!"
    Kyou "Ooh, what happened?"
    Kan smile worried eo "Oh! Kyousuke, are you alright?"
    Kyou  "Hey, Can-oh! What are you doing here? I had this weird dream..."
    Kan smile concerned ec "W-we were just talking, remember?"
    Kyou  "Yeah, we were talking and then..."
    Kan smile happy speaking ec "O-oh! It wasn't important."
    $Kanna = game_player.getRelationship("Kanna")
    $game_player.increaseRelationship("Kanna",-1)
    #Choice1.1.end.
label ch3choice1option2:
    #ChoiceChapter 3 choice 1 option 2: "Kanna's nervous about something. Make her feel comfortable."
    #Kanna gets +1 points
    Kyou frown "It's alright Can-oh, I'm not that great at math either."
    Kan speaking curious "What?"
    Kyou frown "It's ok to be nervous when asking for help. We're all bad at something, so we gotta help each other out, right?"
    Kan smile happy speaking ec "Um, right!"
    Kyou happy "Just ignore that weird voice that came from behind you, that's just the sound of stress."
    Kan smile concerned ec "What? You heard that?"
    Kyou happy "Don't worry about it now! Like I said, it's the sound of stress, right?"
    Kan happy eo "Right!"
    Kyou happy "We'll do our best together!"
    Kan smile worried ec "Oh, Kyousuke, only you could say something as kind as that."
    $Kanna = game_player.getRelationship('Kanna')
    $game_player.increaseRelationship("Kanna",1)
    "We have [Kanna] from Kanna"
    #Choice1-2:end
    #Kanna gets 1 points

#Show example
$Kanna_points = game_player.getRelationship('Kanna')
"DEBUG: We have [Kanna_points] points for Kanna"
##End of Ch3 Part 1.
##Begin ch3 Part 2
label chapter3p2:

    #ART enter Maya.
    #Mid conversation, Maya walks up to Kyousuke, clearly annoyed that Kanna is there talking to him.
    Maya smile happy mo "Good morning Kyousuke! Who's your little friend here?"
    Kyou  "Oh, this is Can-oh! She's our classmate, remember?"
    Maya hopeless ec "Can't say that I do. I meet so many people daily."
    Maya smile happy ec "How can I remember each copy-paste face? Nice to meet you Can-oh, I'm Maya."
    Kan  "It's Kanna, actually. The pleasure's mine, I guess."
    Maya smile happy ec"Pretty sure it's Can-oh; that's how Kyousuke said it."
    Kan  "Of course not, he simply forgot. Happens to everyone."
    Maya flirting eo "Kyousuke is the most sophisticated man I have ever met. His intellectual prowess is something mere normies can't comprehend."
    Maya speaking normal "The fact he's wasting his time in this lugubrious school is beyond even my own grasp."
    Maya speaking normal "And I've never received anything less than a perfect score in any of my classes. So, darling, I think I can quite tell someone of the same intellectual status as me when I see them."
    Kyou happy "Wow! That's really nice of you Maya! I don't really know what any of that means, but I think it was a compliment!"
    Maya flirting eo "It's not simple flattery! It's a fact."
    Kan  smile concerned ec "Yeah, ok, cool. But me and Kyousuke were just talking about being math partners next period."
    Maya "I’m sorry? Kyousuke and I will be math partners next period."
    Kan frown worried eo "Huh?"
    Kyou surprised "Oh I forgot, Can-oh; me and Maya are always math partners."
    Maya smile happy mc "That's right."
    Kan smile worried ec "But-"
    Maya annoyed eo "You heard him, ditzy. We're working on math together."
    Kan angry crazy "Ok, listen here you bit-"
    #ART CG Two more VN GUI choices appear in front of Kyousuke.
    #VOICE  Whispering#
    Rin "PAUSE!"
    Rin "Whew, that almost got out of hand."
    Kyou "Yeah I'll say."
    "I float behind Kyousuke once again."
    Rin "Alright, let's see what kind of options we have this time."
    # SFX or ART portray this "something" isn't right through a strange sound or some kind of visual glitch?
    "Wait, something isn't right here."
    "I sense something familiar."
    "I look around, trying to locate the weird sensation."
    "Huh, is there another spirit around?"
    "Doesn't matter, gotta stay focused on the game."

    # CG Display the two choices below.
    "'Choose Maya as a math partner.'"
    "\" Head to the bathroom.'"
    Rin "What kind of terrible options are these?"
    Kyou "I dunno."

    Rin "You really can't think for yourself at all in these types of situations, can you big guy?"
    Rin "Well, I guess that’s where I come in."
    "Really, what would Kanna ever do without me?"
    "Now, what’s the best way to go about this?"
    menu:
        "Choices to give to Kyousuke"
        "Choose Kanna as a math partner.":
            Rin "Here man, do this instead. Your guardian wingman commands it."
            Kyou "Wow thanks buddy! That's a great idea!"
            jump ch3choice2option1
        "Work in a group with Kanna and Maya.":
            Rin "Here man, do this instead. Your guardian wingman commands it."
            Kyou "Wow thanks buddy! That's a great idea!"
            jump ch3choice2option1

label ch3choice2option1:
        #Choice: "Choose Kanna as a math partner.
        Kyou surprised "Ya know, Maya, This other girl may need more help in math then you do. Maybe I should help her this time. It's the right thing to do."
        Maya flirting eo "Oh, Kyousuke, your commitment to justice and helping the less fortunate is only matched by the strength and sharpness of your jawline."
        Maya sad speaking "Are you sure you don't mind working with her? I know you're only doing it out of pity, but are you absolutely positive this is what you want to do?"
        Kyou frown "It's ok Maya, we can be math partners tomorrow. I'll sacrifice myself for the greater good."
        Maya hopeless ec "Kyousuke, your valiance knows no bounds. Have a nice class...Kanna."
        Kan frown pout ec "Gee, thanks for the sincerity... Let's get to studying, then I guess."
        "Kanna will spend some time with Kyousuke today. Getting her noticed must do at least {i}something{/i} for their relationship, right?"
        #Kanna looks better, she gains a point. Maya sucks up and doesn't lose any at least.
        $Kanna = game_player.getRelationship('Kanna')
        $game_player.increaseRelationship("Kanna",1)
        #Choice2.1: End

label ch3choice2option2:
        #Choice: "Work in a group with Kanna and Maya."
        Kyou happy "Wait, I have an idea! Maybe we can all work together in a group!"
        Maya annoyed eo "What!?"
        Kan sad smile "Well..."
        Kyou  "Yeah, theres no reason it has to be just two of us. You guys are getting along so well anyway. It'll be fun!"
        Maya sad speaking "If you really insist, Kyousuke. While I think it should be just me and you, I guess we can let her in, for her own sake."
        Kyou  "Come on Kanna, it'll be fun!"
        Kan smile happy ec "Well, alright. I guess it won't be too bad as long as you are there, Kyousuke."
        "Well, at least this shouldn't hurt her chances. I don't think it helps much either."
        #Choice 2.B: Neither girl receives a point.
        #Choice2.B End

label chapter3p3:
#ART Kanna's room
    scene room with squares
    Rin  "Alright kid. Here's how Kyousuke is feeling about both you and Maya so far."
    $Kanna_points = game_player.getRelationship('Kanna')
    $Maya_points = game_player.getRelationship('Maya')
    "Kanna has [Kanna_points] and Maya has [Maya_points]"
# ART or CODE
    #Show total scores so far.
    #Possible scores from day 3 .
    #Kanna +2, Maya +1.     Choice 1.B and choice 2.B
    #Kanna 0, Maya +1.         Choice 1.A and choice 2.B
    #Kanna +1,Maya 0        Choice 1.B and choice 2.A
    #Kanna-1,Maya+0        Choice 1.A and choice 2.A

#opportunities for different results.

    Rin  "By the way, I noticed a weird sensation while we were at school today."
    Kan speaking curious "What do you mean?"
    Rin  "All I can really say is there was a strange energy floating around the school."
    Kan speaking confident "It was probably that horrible Maya girl. She was driving me up the wall today."
    Rin  "No, it wasn't teenage hormones. Something like me. A spirit, maybe."
    "Or maybe I'm underestimating teenage emotions."
    Kan speaking curious "You mean another spirit? Like you?"
    Kan smile happy eo "I hope it's another cute stuffed animal spirit!"
    Rin "Well, actually that's kind of just a {i}me{/i} thing."
    Rin "Most spirits are somewhat dangerous actually."
    Kan frown worried eo "Dangerous?"
    Rin "But don't worry. I doubt he'd be bold enough to try anything in a place as public as the school."
    Rin "It does change our situation somewhat though. If there's another spirit around, things could get complicated."
    Kan speaking curious "Well, what should we do?"
    Rin "For now, proceed as planned. We'll take another stab at that partner thing tomorrow."
    Kan smile happy speaking ec "Yeah! That stupid Maya can't keep Kyousuke all to herself. If it's only her we have to deal with, we can manage, right?"
    Rin "Right!"
    "{i}I hope...{/i}"
    scene black with fade
    jump chapter4
