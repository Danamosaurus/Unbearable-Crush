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

    Kan frown worried ec "...I didn't mean to eat all those brownies."

    Rin "How can you get sick at a time like this? What about school? What about our plan?"

    Kan "My stomach hurts. Let me sleep."

    Rin "Who's fault is that?"

    "{i}sigh{/i}"
    "I don't think she’s gonna be much help today."

    "Maybe I can take this opportunity for a solo mission... With Kanna bedridden, I can do a little sleuthing."

    "Dig up some dirt on  Kyousuke - find something useful for granting Kanna's wish."

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

    "Pres" "...No, it’s nothing."

    "That was close - they almost saw me."

    "It's lunchtime now, so this place is just crawling with students."

    "But there's one in particular I'm looking for."

    "Just where is the lover-boy?"

    show Maya smile happy mc at center with dissolve

    $ hide_sides = ['Maya']
    Maya "Kyousuke!"

    "Damn. It's that girl from yesterday."

    Maya smile happy mo "Oh Kyousuke darling, I have something for you!"

    Kyou "Hm?"

    Maya "My mom and I made rice balls this morning for lunch! We had some extras, so I thought I'd bring you some!"
   
    Kyou normal "Hmm?"

    Maya flirting eo "Won't you try one, Kyousuke? I know how much you like maple flavored things."

    "Notes on Kyousuke:"

    "Likes maple flavor..."

    "...maple flavored rice balls?" 
    
    Maya flirting eo "And theres a little something extra inside too. I'm sure you'll like them~"

    "This girl...Maya, was it?"

    "I don't have a problem with her type in most situations."

    "Under different circumstances, I might even find her a bit cute."

    "But, right now, this girl is putting my mission in jeopardy."

    # SFX of a sword being drawn

    "I might have to eliminate her."

    Maya speaking normal "...Kyousuke?"

    #Music stop. Awkward pause.

    Kyou "...Hm?"

    Rin "...Are you just going to leave her hanging?"

    Rin "HEY DUMBO! TRY ONE ALREADY!"

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
    "*Crunch*"

    Maya smile happy mc "Well?"

    Kyou surprised "Is there a rice cracker in here?"

    Maya smile happy ec "Told you there was a surprise inside, didn't I?"

    "Who puts rice crackers in rice balls?"

    "Notes on Maya:"
    "Can't cook."

    Maya smile happy mo "So, how does it taste?"

    Kyou frown "It tastes ricey."

    Maya annoyed ec "That's not the answer I was hoping for."

    Kyou normal "Sorry."

    #ART Pop-in Smug Ringo
    "I think you just lost points, Kyousuke"

    Maya hopeless ec "I hate to leave you, but I’m meeting up with a friend. Feel free to eat the rest and swing by my place to return the box, okay?"

    hide Maya with dissolve
    "And with a flip of her hair, she's gone."

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

    Kyou happy "Woah dude! What is that?"

    Rin "Jeez, no need to be rude. It’s me! Your...your-uh..."

    Kyou "My angel? My angel is a bear?"

    Kyou "A...detective bear?"

    Rin "Oh, yeah no, nevermind that..."

    Rin "Achem-"

    Rin "Yes! It is I, your guardian angel bear."

    Rin "And I'm here today to tell you that the spirits have chosen {i}you{/i} to win the heart of a very lovely girl."

    Kyou surprised "Me?"

    Rin "You. Of the hundreds of deserving and far more interesting guys in this school, you have been selected to receive the ultimate girlfriend acquisition aid."

    Rin "That's right! Me, Ringo!"

    Rin "Your personal guardian wingman!"

    Kyou happy "Wow. I've always wanted a guardian wingman!"

    Rin "Yep. Didn't we all."

    Rin "Now, you just gotta do everything I tell you, and I'll make sure you end up with the best girlfriend a guy could hope for."
    
    Kyou smirk "That's it? No catch? You got it, dude!"

    Rin "Great. Now, crouch down and let me get in your backpack. We guardian wingmen need to stay hidden."

    Kyou "This is awesome. I'm gonna get a girlfriend. Hell yeah!"

    "Well, at least he doesn't seem to picky."

    hide Kyou with dissolve

    "Now, how’s this gonna go?"

    "With my power of suggestion, I can whisper ideas in Kyousuke's ear."

    "I'll just feed Kyousuke the right ideas to push him towards Kanna, and away from other girls."

    "Kanna won't even have to try! I'm going to bring this idiot right to her, wrapped in a nice bow!"

    "This plan is perfect! It's so simple."

    "It's almost a shame that this is my last wish."

    Kyou frown "Hey, Ringo?"

    Rin "Yes, buddy?"

    Kyou "Do you think returning Maya's lunchbox counts as a date?"

    "{i}sigh{/i}"

    Rin "I don't think so."

    "This idiot is going to make this so easy."

    "This is also a good opportunity to get some insider info for Kanna."
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
    Rin  "He watched cooking videos on his phone until 2am, then passed out. That ain't humble."
    Kan "He's so relatable!"
    Rin "Whatever, just listen."
    Rin "You've got some tough competition. She's a real flirt, and seems to have had her eye on him awhile."
    Rin "Now I've got a plan to bring you and Kyousuke together, and push her out at the same time."
    Rin "It's risky, but I think it'll work. But you gotta do everything I say."
    scene black with fade
jump chapter3
