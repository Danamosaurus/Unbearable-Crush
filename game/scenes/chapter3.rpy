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
    Kan smile happy ec "Because you're his {i}guardian wingman?{/i}"
    Rin "Ya know, a little push here, a little nudge there, and it'll be all over for that Maya girl and Kyousuke will fall right into your arms."
    Rin "It's what us wingman's do."
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
    Rin "Anyway, time's up, he's right there! Ask him to be your math partner. Be yourself. Go get 'im, tiger."
    Kan speaking surprised crazy "Wait, Ringo, I-I..."
    Kan smile concerned ec "He-h-heeeeeeyyy, Kyousuke."
    Kyou "Oh. Hey, you're Can-oh, right? What are you doing here?"
    Kan  "Just, uh, just hanging out, ya know haha. Also, uh, it's Kanna, but you can call me Can-oh if you really want to."
    Kan "I-I was wondering, Kyousuke, if you wanted to be m-math partners next period."
    Kan  "When we go back to class. After this break. When we stop talking. After we walk back to the classroom. Once the break's over. When we're back at our desks. Am I talking too much? Does that make sense?"
    Kyou  "Hmm. Do we go back to class before we're at our desks, or after?"
    Kan  speaking sarcastic ec "Uh, before."
    Kyou  "Ok, got it. Sure, let’s be partners."
    Rin  "You're slaying it, kid."
    Kan speaking pleading "Shut up!"
    Kyou  "Oh, sorry."
    Kan neutral surprised crazy "-"
    Kan questioning embarrassed "Nononono, I meant like, {i}'shut up I can't believe you totally want to be partners with me!'{/i} Haha."
    Kyou  "Um, are you alright? You're acting funny."
    Kan speaking excited crazy blush "Y-yeah, why would I be acting funny? I'm not funny at all, I'm always serious. Not an ounce of humor in my body."
    Kyou "..."
    Kyou "..."
    Kyou "..."

    Kan frown skeptic "Uh..."
    show Kyou normal at center with Dissolve(3.0)
    Kan "...Kyousuke?"
    Rin "It's as if he's been put on pause."
    Kan "Kyousuke? What's wrong?"
    Rin "Oh. It's one of these. This sometimes happens in these sorts of situations."
    Kan smile concerned ec "Kyousuke?"
    $ hide_sides = ['Kyousuke']
    Kyou  "..."
    Rin "I'm pretty sure he can't hear you. He's trying to figure out what to do in this situation."
    Kan  "We wouldn't be in this situation if you just kept quiet!"
    Rin  "We all need moral support sometimes, excuse me for trying to help."

    Kan speaking curious "What do we do? What happens now?"
    Rin "Mophead here needs some help figuring out what to do or say."
    Rin "He has some choices to make, and it looks like he lacks the strength of will to make them."
    Kan speaking curious "Strength of will? How does he make day to day choices then?"
    Rin "I mean, at somepoint he picks one. But it looks like he's stumped this time."
    Rin "Probably because you yelled at him to shut up."
    Kan "THAT WAS YOUR FAULT!"
    Rin "I'll see what his thinking and {i}help him{/i} decide the best choice."
    Kan smile worried eo "You can read his thoughts?"
    Kan salivating "How intimate~"
    Kan smile worried eo "But isn't that sorta like manipulative?"
    Rin "What did we say about not thinking so hard?"

    # TEST adding an optional thought that wasn't in script
    #show screen thought(["'Ice cream...'"],
    #                    block_progress = False)
    Rin  "Just let me handle this."
    "I fly up onto Kyousuke's shoulder."

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
            "I make the selection for Kyousuke, then float back to Kanna to hide in her backpack again. "
            jump ch3choice1option1
        "Kanna's nervous about something. Make her feel comfortable.":
            "I make the selection for Kyousuke, then float back to Kanna to hide in her backpack again. "
            jump ch3choice1option2

label ch3choice1option1:
    #Chapter 3 choice 1 option 1: "Laugh it off, forgive Kanna for yelling at you."
    hide Kyou with dissolve
    $ hide_sides = []

    Kyou happy "Hahaha, it's alright, Kanna. I know what ya mean."
    Kyou smirk "Like, {i}'oh shut up! No way!'{/i} right?"
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
    Rin  "WHAT? W-WHY?"
    Kan speaking embarrassed ec "He - he was gonna find out about you. A-a-and you said you couldn't fulfill my wish if that happened."
    Rin "And your first response is to mess up his face?"
    Rin "Why have you been giving me the {i}ditsy down-on-her luck girl{/i} shtick if you're just gonna act like a delinquent?!"
    Kan speaking sad crazy "Oh God, what am I gonna do?"
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
    Kyou  "We were? I thought that wasy my dream. We were talking and then all of a sudden you-"
    Kan smile happy speaking ec "O-oh! That sure sounds like a crazy dream, Kyousuke!"
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
    # $Kanna = game_player.getRelationship('Kanna')
    $game_player.increaseRelationship("Kanna",1)
    # "We have [Kanna] from Kanna"
    #Choice1-2:end
    #Kanna gets 1 points

#Show example
$Kanna_points = game_player.getRelationship('Kanna')
# "DEBUG: We have [Kanna_points] points for Kanna"
$game_player.showRelationshipUI(["Kanna"], duration=0.5)
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
    Maya smile happy ec "Kanna? Pretty sure it's Can-oh; that's how Kyousuke said it."
    Kan  "Huh? Of course not, I think I know how to pronounce my own name."
    Maya smile happy ec "Are you calling Kyousuke a liar?"
    Kan "What? No no no I'm just saying-"
    Maya flirting eo "Kyousuke is the most sophisticated man I have ever met. His intellectual prowess is something mere normies like you can't comprehend."
    Maya speaking normal "The fact he's wasting his time in this lugubrious school is beyond even my own grasp."
    Maya speaking normal "And I've never received anything less than a perfect score in any of my classes. So, Can-oh, I think I can quite tell someone of the same intellectual status as me when I see them."
    Kyou happy "Wow! That's really nice of you Maya! I don't really know what any of that means, but I think it was a compliment!"
    Maya flirting eo "It's not simple flattery! It's a fact."
    Maya speaking normal "And it's the truth. Kyousuke would never lie about anyones name."
    Kan  smile concerned ec "Yeah, ok, that's cool and all. But me and Kyousuke were just talking about being math partners next period."
    Kan  smile concerned ec "So you can, you know, go away now."
    Maya "I’m sorry? Kyousuke and I will be math partners next period."
    Kan frown worried eo "Huh?"
    Kyou surprised "Oh I forgot, Can-oh; me and Maya are always math partners."
    Maya smile happy mc "That's right."
    Kan smile worried ec "But-"
    Maya annoyed eo "You heard him, ditzy. We're working on math together."
    Kan angry crazy "Ok, I'm not talking this from someone who's hair color is the same as dish soap."
    Kan angry crazy "Is that what you wish it with?"
    Maya annoyed eo "EXCUSE ME?"

    "Uh oh, I better do something."
    Kyou "PAUSE!"
    "..."
    Kyou "I uh... need to think for a minute and talk with my um...brain about what to say next."
    Kyou "So just...uh...stop talking and let me...say something...in...a second."
    Kyou "I'll just turn around for a minute to uh...think to myself."
    Maya "Of course, Kyousuke. Your time to think is more important then anything this homely girl has to say. Please take all the time you need."
    Kan "Are you like this all the time?"
    Maya "Sweet, understanding, and caring? Why, of course I am."

    # Ringo and Kyousuke whispering to each other
    Rin "Whew, that almost got out of hand."
    Kyou "Yeah I'll say. Glad you came and told me to say something Mr. guardian wingman."
    Kyou "That went so smooth~"
    Rin "Whatever you say, bud."
    Kyou "But what should I say?"
    Rin "I'm sure you'll think of something kid. You just do what you think is best and I'll support you!"
    Kyou "Thanks Mr. guardian wingman."
    Rin "Knock em dead!"

    "As if I'm going to let this guy make his own choices."
    "Alright, let's see what kind of options we have this time."

    #Some kind of visual / sound effect / something aside from writing to indicate ringo is sensing something
    "..."
    "Wait, something isn't right here."
    "I sense something. Somekind of presence."
    "Is there another spirit around?"
    "..."
    "Huh. Maybe it's my own spiritual energy?"
    "*{i}Sniff, sniff.{/i}*"
    "Yeah, that's probably it. I need to talk a shower later tonight."
    "Whatever, doesn't matter, gotta stay focused on the game."

    # CG Display the two choices below.
    "'Choose Maya as a math partner.'"
    "\" Head to the bathroom.'"
    "What kind of terrible options are these?"
    "You really can't think for yourself at all in these types of situations, can you big guy?"
    "Well, I guess that’s where I come in."
    "Really, what would Kanna ever do without me?"
    "Now, what’s the best way to go about this?"
    menu:
        "Choices to give to Kyousuke"
        "Choose Kanna as a math partner.":
            #Rin "Here man, do this instead. Your guardian wingman commands it."
            #Kyou "Wow thanks buddy! That's a great idea!"
            jump ch3choice2option1

        "Work in a group with Kanna and Maya.":
            Rin "Here man, do this instead. Your guardian wingman commands it."
            Kyou "Wow thanks buddy! That's a great idea!"
            #Kanna gains 1 point
            $game_player.increaseRelationship("Kanna",1)
            jump ch3choice2option2

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
        # $Kanna = game_player.getRelationship('Kanna')
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
    # "Kanna has [Kanna_points] and Maya has [Maya_points]"
    $game_player.showRelationshipUI(["Kanna", "Maya"], duration=0.5)

    Rin  "By the way, I noticed a weird sensation while we were at school today."
    Kan speaking curious "What do you mean?"
    Rin  "All I can really say is there was a strange energy floating around the school."
    Kan speaking confident "It was probably that horrible Maya girl. She was driving me up the wall today."
    Rin  "No, it wasn't teenage hormones. Something like me, I think."
    "Or maybe I'm underestimating teenage emotions."
    Kan speaking curious "You mean another spirit?"
    Kan smile happy eo "I hope it's another cute stuffed animal!"
    Rin "Well, actually that's kind of just a {i}me{/i} thing."
    Rin "Most spirits are somewhat dangerous actually."
    Kan frown worried eo "Dangerous?"
    Rin "But don't worry. I think it might have been some of may own magic I was sensing. Magic came sometimes go off and do it's own thing."
    Rin "And besides, I doubt any spirit would be bold enough to try anything in a place as public as a high school."
    Kan "Aren't you a spirit using magic in a public high school?"
    Rin "Yes, but that's beside the point!"
    Rin "If there's another spirit around, and that's a big if, things could get complicated."
    Kan speaking curious "Well, what should we do?"
    Rin "For now, go with the plan. We'll take another stab at that math partner thing tomorrow."
    Kan smile happy speaking ec "Yeah! That stupid Maya can't keep Kyousuke all to herself. If it's only her we have to deal with, we can manage, right?"
    Rin "Right!"
    "{i}I hope...{/i}"
    scene black with fade
    jump chapter4
