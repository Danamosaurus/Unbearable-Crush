label chapter2:

    # Update the day shown on the upper corner... to nothing!
    $ game_day = "Day 2"
    $ hide_sides = []
    scene room day with fade

    Rin "Wakey wakey!"

    Rin "Time to get up! Let's go, let's go, we've got a busy day!"

    Kan frown upset ec "Nnn..."

    Rin "Get up!"

    Kan "Nnnnn..."

    Kan frown worried ec "Too. Many. Brownies."
    Kan frown worried ec "So. Good. Yet. So. Bad."
    Kan "Nnnnn..."

    Rin "How can you get sick at a time like this? What about school? What about our plan?"

    Kan "Can't. Go on. Stomach. Hurt. Let me sleep."

    Rin "Who's fault is that?"

    "*{i}sigh{/i}*"
    "Looks like she’s gonna be a {i}ton{/i} of help today."

    "Maybe I can take this opportunity for a solo mission. With Kanna bedridden, I can do a little sleuthing."

    "Dig up some dirt on Kyousuke - find something useful for granting Kanna's wish."
    "Find out thar Maya girl's secrets - get her out of the way so he only thinks about Kanna."

    "Solo Ringo mode-o is a go."

    "After raiding her fridge, of course."

    #scene 2.2

    scene hallway onlayer master with squares:
        subpixel True xpos 0.5 ypos 2.2 xanchor 0.5 yanchor 1.0 rotate None
        parallel:
            xpos -0.02
            ease_cubic 3.17 xpos 0.45
    #ART CG
    #show image CGDetectiveRingo

    "Woah, gotta hide!"

    "Boy" "Did you see something, pres?"

    "President" "I’m not sure… let me check it out."

    "No, no, no, no, no! I can't blow my cover already!"

    "Boy" "Uh, Pres, you’ve got that paranoid look again. Things never go well when you make that face."

    "Boy" "Come on, you don’t wanna be late to the student council meeting."

    "President" "...Yeah, alright. It was probably nothing."

    "That was close - they almost saw me."

    "It's lunchtime now, so this place is just crawling with students."

    "But there's one in particular I'm looking for."

    "Just where is lover-boy?"

    show Maya smile happy mc at center with dissolve

    $ hide_sides = ['Maya']
    Maya "Kyousuke!"

    "It's that girl from yesterday!"
    "She really does pop up at the worst possible times."

    Maya smile happy mo "Oh Kyousuke, I have something for you!"

    Kyou "Hm? Oh, good afternoon, Maya!"

    Maya "My mom and I made rice balls this morning for lunch! We had some extras, so I thought I'd bring you some!"

    Kyou normal "Hmm?"

    Maya flirting eo "Won't you try one, Kyousuke? I know how much you like maple flavored things."

    Maya flirting eo "And I put a lot of hot, sticky, messy maple syrup in them~"

    "Notes on Kyousuke:"

    "Likes maple flavor..."

    "...maple syrup rice balls?"

    Maya flirting eo "And theres a little extra surprise inside. I'm sure you'll love them~"

    "Ugh, she's one of those girls."
    "The {i}'flirt, bribe, manipulate to get what I want'{/i} type."
    "Has no shame in trying to butter up her 'man' as much as possible."

    "I don't have a problem with her type in most situations."
    "Under different circumstances, I might even find her a bit cute. She's trying so hard to get this clown to like her, it's adorable."

    "But, right now, she's putting my mission in jeopardy."

    "I gotta find a way to eliminate her."

    Maya speaking normal "...Kyousuke?"

    #Music stop. Awkward pause.

    Kyou "...Hm?"

    Rin "...Are you just going to leave her hanging?"

    Rin "HEY DUMBO-DINGUS! TRY ONE ALREADY!"

    Kyou frown "Huh?"

    # ART (sprite artist) Create a surprised sprite for Kyousuke??
    #Kyousuke's eyes open. He heard something.


    #ART CG Dating sim GUI appears to Kyousuke.
    #Show CG Maya with the choice "Try a rice ball" in a dating sim format
    #Ringo is looking up at Kyousuke who's surprised to see a choice button appear in front of him

    #ART Ringo pop-in surprised pikachu

    #CG closeup. He puts his finger on the button.

    Kyou normal "I guess I'll try one."

    #SFX "{i}Crunch{/i}"
    "{i}*Crunch*{/i}"

    Maya smile happy mc "Well?"

    Kyou surprised "Is there a rice cracker in here?"

    Maya smile happy ec "Told you there was a surprise inside, didn't I?"

    "Who puts rice crackers in rice balls?"

    "Notes on Maya:"
    "Can't cook."

    Maya smile happy mo "So, how does it taste?"

    Kyou frown "It tastes ricey."
    Kyou frown "And crackery."
    Kyou frown "But I wouldn't say it's ricey crackery."

    Maya annoyed ec "Oh Kyousuke, after slaving away all morning making them. That's not the answer I was hoping for."

    Kyou normal "Sorry, Maya."

    #ART Pop-in Smug Ringo
    "I think you just lost points, Kyousuke"

    Maya hopeless ec "I hate to leave you, but I’m meeting up with a friend. Feel free to eat the rest and swing by my locker to return the box, okay?"

    hide Maya with dissolve
    "With a flip of her hair, she's gone."

    Kyou happy "Um...Okay. Sure."

    Kyou smirk "..."

    Kyou normal "....."

    Kyou frown "What just happened to me...?"

    Rin "I think you just triggered a flag there, buddy."

    Kyou "A flag? Who said that?"

    Rin "Down here."

    show Kyou surprised at center with dissolve
    $ hide_sides = ['Kyousuke']

    Kyou "Hmm?"

    Kyou happy "Woah dude! A bear at this hour? What are the chances!"

    Rin "Come on, don't act so surprised. It’s me! Your...your-uh..."

    Kyou "My teddy bear I lost when I was in first grade?"
    Rin "No! I'm your what's it called, spirit guide, magic angel...thing."

    Kyou "A guardian angel?"

    Rin "Ah-yes! It is I, your guardian angel!"
    Kyou "The teddy bear I lost in first grade is my guardian angel?...I KNEW IT!"

    Rin "And I'm here today to tell you that the spirits have chosen {i}you{/i} to win the heart of a very lovely girl."

    Kyou surprised "Me?"

    Rin "Yes, you! Of the hundreds of deserving and far more interesting guys in this school, you have been selected to receive the ultimate girlfriend acquisition aid."

    Rin "Which is, you guessed it, me, Ringo!"

    Rin "Your very own personal guardian wingman!"

    Kyou happy "Wow. I've always wanted a guardian wingman!"

    Rin "Yep. Didn't we all."

    Rin "Now, you just gotta do everything I tell you, and I'll make sure you end up with the best girlfriend a guy could hope for."

    Kyou smirk "That's it? No catch? You got it, dude!"

    Rin "Great. Now, crouch down and let me get in your backpack. We guardian wingmen need to stay hidden."

    Kyou "This is awesome. I'm gonna get a girlfriend. Heck yeah!"

    "Well, at least he's not picky."

    hide Kyou with dissolve

    "Now, how’s this gonna go?"

    "With my power of suggestion, I can whisper ideas in Kyousuke's ear."

    "I'll just feed Kyousuke the right ideas to push him towards Kanna, and away from other girls."

    "Kanna won't even have to try! I'm going to bring this idiot right to her, wrapped in a nice bow!"

    "This plan is perfect! It's so simple."

    Kyou frown "Hey, Mr. Guardian wingman?"

    Rin "What's up, buddy?"

    Kyou "Do you think returning Maya's lunchbox counts as a date?"

    "*{i}Sigh{/i}*"

    Rin "I don't think so."

    "This moron is going to make this so easy."

    "This is also a good opportunity to get some insider info for Kanna."
    "Two birds, one stone."
    "Or should I say, two rice balls, one cracker."

    scene black with fade
    $ hide_sides = ['']

    scene room night with dissolve:
        zoom .35
    Kan smile happy eo "You spent the whole day with Kyousuke?"
    Kan smile happy speaking ec "I'm so jealous~"
    Kan "What did you learn about him? What did his hair smell like?"
    Kan "I bet it's something masculine, like a lumberjack."
    Rin "Hmm. More like tree bark I'd say. Bit sticky too."
    "He was probably wearing some of that maple syrup now that I think about it."
    Rin "I dunno. He seemed pretty boring if you're asking me."
    Kan "You mean humble."
    Rin "He watched cooking videos on his phone until two in the morning, then passed out. That ain't humble."
    Kan "He's so relatable!"
    Rin "Whatever, just listen."
    Rin "You've got some tough competition. She's a real flirt, and seems to have had her eye on him awhile."
    Rin "Now I've got a plan to bring you and Kyousuke together, and push her out at the same time."
    Rin "It's risky, but I think it'll work. But you gotta do everything I say."
    Rin "Capeesh?"
    Kan "Capeesh! Whatever that means."
    Rin "Okay, listen up kid, here's the plan."
    scene black with fade
jump chapter3
