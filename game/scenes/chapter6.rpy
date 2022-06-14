label chapter6:
    $ game_day = "Day 6"
    scene hallway
    camera:
        subpixel True zpos 1039.0
        xpos 0
        ypos 0
        xanchor .5
        yanchor .5
    show hallway:
        subpixel True ypos 0.5
        xanchor .5
        yanchor .5
        xpos 0
        ypos 0
    $ hide_sides = []
    Kan "Hello. Maya, was it?"
    Maya smile happy mc "Oh, Can-oh, what do you want?"
    Kan "Listen, I know you don't really like me, but I think we can help each other."
    Kan "We seem to have a... mutual problem."
    Maya "Oh? And what exactly would that be?"
    Kan "I'll give you a hint."
    Kan "She laughs like a hyena and talks like a middle schooler who's played a little too much D&D."
    Maya "I think I have a pretty good idea about who you're talking about."
    Maya "Now why exactly should we work together?"
    Kan "We both can agree that we just want Kyousuke to be happy, right?"
    Maya "I mean, as long as he is with me, his happiness is assured."
    Kan "Right, I'm pretty sure Kyousuke will be a lot happier with either one of us than with Charlotte."
    Maya "You mean happier with me."
    Kan "Whatever. Truce?"
    Maya "Hm. I suppose I see your point. Truce."
    Maya "You don't have any hope of winning over Kyousuke, you know."
    Kan "Kyousuke is the coolest, handsomest, and most good-natured person I've met."
    Kan "He'll know what to do and who to pick when the time comes."
    Kan "And I've no doubt that person will be me."
    Maya "Wooowww, so confident! Where's this coming from?"
    Kan "It's gonna happen Maya; I know Kyousuke will do the right thing, no matter what. I believe in him"
    Maya "That's nice and all, but you're just in denial. He'll never choose you."
    Maya "He's not exactly the brightest.  He needs a little... persuasion in order to understand who he really likes."
    Kan "What do you mean?"
    Maya "He's dumber than a sack of potatoes, Can-oh. Even you must have noticed it by now."
    Kan "No! Kyousuke is the smartest person in this school, hands down."
    Maya "Oh, please. Have you seen his grades? I tutor him in math, not the other way around."
    Maya "Although I make sure he thinks he's teaching me."
    Maya "Giving people choices they feel they think of themselves is the easiest way to groom them to do what you want."
    Kan "That's..."

    #VOICE Whispering (Next two lines.)
    Kan "Am I manipulating Kyousuke with Ringo?"
    Kan "I just want him to be happy..."

    Maya "What was that?"
    Kan "...Look, you gonna help me take Charlotte down a peg or not?"
    Maya "Might as well. Let's hear the plan."
    window hide
    camera:
        subpixel True
        #Camera Pan Right
        parallel:
            ease 1 pos (1472, -276)
        #Push In
        parallel:
            pause .5
            ease .5 zpos 266
        #Blur Focus
        parallel:
            pause .5
            easein .7 blur 20
            pause .1
            ease .3 blur 0
    pause 1


    #*Continuing with the guardian angel idea from Day 2*#
    #Cut to another part of the hallway, Kyousuke is walking down the hall, Ringo is in his backpack.
    #SFX footsteps up the stairs

    Kyou "So... you can only pop up every few days?"
    Rin "That's right, kiddo. I had to run a few... heavenly errands."
    Kyou "You're still helping me get a girlfriend, right?"
    Kyou "It's been tricky these last few days. More and more girls keep showing up. I can't keep track of them all"
    Rin "Don't worry, Casanova, I'll make sure you end up with your special someone."
    Kyou "Can I have all of them?"
    Rin "Erm, no, bud. That's not really how this works."
    Rin "I promise you I'll help you get true love, the next girl that comes around that corner may just be the one you spend the rest of your life with."
    Kyou "Really?"
    Char "WAHAHAHA!"
    Rin "Not that one, maybe the girl after that."

    #Ringo slides back into Kyousuke's backpack.

    Char "Good morning, Kyousuke! After carrying my books yesterday, I'm here to officially give you your wizard learner's permit!"
    Char "A magic-user in training license, if you will."

    #Charlotte pulls out a rock, seemingly from nowhere, and hands it to Kyousuke.

    Kyou "Good morning Charlotte! Thanks for... are there googly eyes on that rock?"
    Char "Yes! How else is it supposed to see?"
    Kyou "What's written on it? Is that sharpie?"
    Kyou "1e+22. What's that mean?"
    Char "That's how many picoseconds you charged my mana yesterday."
    Char "I need a power source capable of pumping out one gallon of mana every trillionth of a second. And you, Kyousuke, performed your duty magnificently."
    Char "No mere mortal could generate that much output that fast!"
    Kyou "Um, thanks, Charlotte. I'm doing the best I can."
    Char "If you can beat yesterday's score, I'll place the third eye of Micolash upon the rock!"
    Kyou "Cool! Does that mean you'll glue more googly eyes to it?"
    Char "Naturally! The eyes mean we can gain insight!"
    Char "Grant us eyes, o' powerful Micolash. Grant us vision to see past the delusions of our mere existence, so we may gaze into the metaphysical realm of the true cosmos."
    Char "Bless us with your omnipotent-"
    Maya "Ok, you are acting exceptionally weird today."
    #Char "N-"
    Kyou "Good morning, Maya!"
    Maya "Morning, Kyousuke! Are you getting your fortune told? Should I come back later?"
    Kyou "Oh, no, Charlotte was showing me her arts and crafts project."
    Char "Kyousuke! You dare compare my studies of the world beyond man to that of a simple humanistic expression?"
    Maya"I think he does dare. Maybe if you could do something cool, like fortune telling, or maybe, mind reading, he would take you seriously."
    Maya "Kyousuke's intellect is unrivaled, Charlotte. Just the other day, he was telling me about having boy cheerleaders to liven the girls as they play volleyball."
    Maya "Which the school is currently talking about implementing, as they also thought it was  brilliant."
    Kyou "I don't remember doing that."
    Maya "You told me all about it a few days ago, remember? I did all the specifics and wrote your plans down and submitted them to the school."
    Maya "It's all just busy paperwork, Kyousuke, trust me; but you get all the credit, don't worry!"
    Kyou "Wow! Thanks Maya. I appreciate you helping me flesh out my ideas."
    Kyou "It was a tricky problem to solve, but I'm sure the girls will love the support."
    #EDITING Show her being flustered
    "Charlotte is clearly flustered about the lack of attention."
    "The shadow beneath her feet is flickering again."

    Char "Wait just a minute. I'll have you know I can perform such childish tricks as fortune telling AND mind reading."
    Char "Pick your poison, Kyousuke. Which would you like to see?"
    Maya "Hold on, how are we supposed to test this so-called magic of yours?"
    Char "You really don't know? {i}Phhhbbt{/i}, of course you don't. Tell her Kyousuke."
    Kyou "Umm, I'm actually not sure how to test that."
    Char "Correct!"
    Maya "Oh my god... Ok, if Kyousuke wants you to do fortune telling, you'll have to predict what will happen when the school bell rings."
    Maya "If Kyousuke picks mind reading, both you and him will say what you're thinking in unison."
    Char "Child's play! Something so easy is but a game for the child of the creator. The associate natural law breaker. Th..."
    Maya "Can we just skip to the 'wahaha' part please?"
    Char "WAHAHAHA!"
    Maya "Thank you."
    Char "Alright, Kyousuke, decide which magic you would like me to perform!"

    # ART The usual VN choice GUI
    "Two more choices appear in front of Kyousuke."
    "Fortune-telling"
    "Mind-reading"
    #ART Show this Youko's big ass grown adult body stuffed into Kanna's backpack hanging like a sack of potatoes. She doesn't notice.
    #ART Ringo comments there's not enough room in here for two of them.
    "Youko appears in Kyousuke's backpack, right next to Ringo."

    Rin "'About time you showed up."
    Youk "Little Kanna is slipping out of the boy's mind, Mr. Fortune."
    Youk "Are you even representing her? Maybe you should give her my card after this is over, I can find someone she'll like just as much as Kyousuke."
    Rin "Not a chance, fancy pants. Kanna will win his heart, just you wait!"
    Rin "But I am feeling generous. You make the first move today."
    Youk "What move is there to make? Let's see what he picks, then go from there."
    Rin "We both know that hyena is no fortune teller. You're gonna want to read his mind."
    Youk "On the contrary. I can pull off whichever decision Kyousuke makes, mind reading is just more convenient"
    Rin "Then make your move already."
    Youk "Very well."
    #ART Youko "Poof" back into Charlotte's shadow. How do we show that?
    # ART
    #Mind-reading begins to glow the familiar purple sparkle glow.
    #Put Charlotte's effects on Mind-reading

    Rin "(Alright, I know either way we go, we got this one in the bag.)"
    Rin "(I can tell Kanna did her job, otherwise Maya wouldn't have brought up fortune telling or mind reading.)"
    Rin "(Anyway, we need to tread carefully with these two clowns here.)"
    Rin "(I could also highlight 'mind reading' and, if all goes to plan, shame Charlotte.)"
    Rin "(I need Kanna here for 'fortune telling,' so maybe I can inject something to stall for time?)"

    # CODE
    #Menu: Choices for Kyousuke.
    #"Highlight Mind reading"
    #"Do a different magic trick."

    #Choice 1.A "Mind reading."

    Kyou "Try reading my mind!"
    Char "Easy! You're thinking about..."

    "The shadow beneath Charlotte begins to warp a little, tugging at her feet."

    Char "Er, how should we judge this? Maybe someone should give a topic?"
    Maya "Ok, Kyousuke thinks of a color and says it outloud."
    Char "Easy! Alright on the count of two."
    Maya "On the count of three, can you be normal for, like, a minute?"
    Char "I've avidly studied normality. Hence why I blend in so well at this school."
    Char "How else would a priestess of my magnitude be allowed into such a common, mortal realm?"
    Maya "Everything you spew is hot garbage. Let's just go."

    Rin "You gonna cheat again?"
    Youk "Override his brain, you mean? No need, we both know he's going to say red."
    Youk "Nonetheless, I must commend you for trying to trick me into using my powers for matters so trivial."

    "Youko vanishes from sight, returning to Charlotte's shadow to inform her of what Kyousuke will say."
    "That idiot has no idea."

    Maya "Three."
    Maya "Two."
    Maya "One."
    "Charlotte &  Kyousuke" "Red."

    Kyou "Woah!"
    Char "See? There is nothing my powers cannot do!"
    Maya "Red is the second most common favorite color."
    Char "And? Do you not see his amazement at my abilities?"
    Maya "And I'm saying it's a lucky guess. Let's try something a little trickier."
    Maya "Favorite animal."

    "Kanna turns the corner of the hall, sprinting at full speed."

    Maya "Three."
    Maya "Two."
    Maya "One."

    #SFX Kanna crashing into Charlotte.
    #ART maybe a CG? If we have time and you guys want to.
    Kan "GIRAAH!"
    Char "ALLIRRGH!"
    Kyou "Giraffe!"

    "Kanna slams directly into Charlotte, knocking her clean off her feet to the floor."
    "Kanna lays on top of her, reeling."

    Kyou "Good morning, Kanna! Where are you off to in such a hurry?"
    Char "Release your weight from my chest! The flow of mana cannot reach my lungs!"
    Kan "Oh my gosh, I'm so sorry, are you alright?"
    Char "Yes, I'm fine. Please, do be more careful, you almost awakened my alter ego. She’s even scarier than I."
    Maya "Sorry, Charlotte. Looks like you guessed wrong."
    Char " {i}Excusez moi?{/i}"
    Maya "Honestly, Kanna sounded like she was going to say giraffe. You sounded like you were going to say alligator."
    Char "That is absurd! This young woman hit me with the strength of a 5.8 magnitude earthquake."
    Char "And I'll have you know, I've created earthquakes that break the magnitude scale."
    Kyou "Sorry, Charlotte, I think Maya's right. Good job, Kanna! I didn't know you knew magic."

    # CODE
    #Choice 1.A    -1 Charlotte
    #0 Maya
    #+1 Kanna
    $game_player.increaseRelationship("Kanna",1)
    $game_player.increaseRelationship("Charlotte",-1)

    #Choice 1.B "Do a different magic trick."

    Kyou "Maybe instead of some mental stuff, you can do a classic card trick!"

    #Show Rin and Youk

    Youk "Did he... just pick yours?"
    Rin "The kid just wants to see some card tricks or a rabbit out of a hat or something."
    Youk "No matter, I can make this work."

    Char "Um, I... er, Yes! Of course! What sort of magic trick were you thinking?"
    Kyou "Can you pull a rabbit out of a hat? Wait, none of us are wearing hats. Um, can you do a card trick?"
    #WRITING She's literally holding cards in her sprite image
    Char "I am afraid I am not currently equipped with such a thing. You’ll just have to choose something else."
    Maya "I carry cards in my backpack all the time. Poker club insists we all have our own deck."
    Maya "Here."
    Char "Pick a card there, tender Kyousuke. Memorize it. Commit your mental capacity to fully enter the card before you to memory."
    Kyou "Got it. Then I put it back in the deck, right?"
    Char "Yes! Now, observe."

    "Charlotte places the deck of cards on the floor. She stomps down hard, keeping her foot on the top of the cards."

    Maya "Hey, don't do that!"
    Char "It is fully necessary for this to happen in order for the trick to work. You'd be surprised how often people wish me to step on cards."
    Maya "I don't want to think about that. And I also don't want you to ruin my RED cards."

    "Awkward silence."

    Kyou "Why did you just yell that Maya? I think my card was black anyway."
    Rin "(Come on Kanna, hurry up.)"

    Char "Hush, both of you! I'm spoon feeding myself the knowledge of this particular pack of cards."
    Char "It's telling a story. How it was created in a factory, played hundreds of hands of poker by the delicate and single eyebrowed Maya."
    Maya "Excuse me? I clearly have both my ey-"
    Char " The cards are now telling me about the time, not long ago, when Kyousuke held one in his muscular fingers."
    Char "Kyousuke! Your card is the red eight of..."

    #SFX Kanna crashing into Charlotte.
    #ART maybe a CG? If we have time and you guys want to.
    Kan "GIRAAH!"
    Char "ARRGH"

    "Kanna slams directly into Charlotte, knocking her clean off her feet to the floor."
    "Kanna lays on top of her, reeling from ramming headfirst into Charlotte."
    "Cards blast up into the air, causing a mini explosion of playing cards to erupt around them."
    # ART Maybe a CG of this, if possible?
    "I leap out of Kyousuke's backpack, snagging a card out of midair, and hand it to Kyousuke."

    Kyou "Good morning, Kanna! Where are you off to in such a hurry?"
    Char "Release your weight from my chest! The flow of mana cannot reach my lungs!"
    Kan "Oh my gosh, I'm so sorry, are you alright?"
    Char "Yes, I'm fine. Please be more careful, you almost activated the emergency self destruct."
    Maya "My cards! Oh, come on!"
    Kyou "Sorry Charlotte, your guess is wrong."
    Char "{i}Excusez moi?{/i}"
    Kyou "I have the black three of clubs, see?"

    "Kyousuke shows her the card."

    Char "What? The card I had - before this ten ton rerun of a girl body checked me - was definitely the correct card."
    Kyou "But look, see?"
    Char "Did you not grab that card when they exploded everywhere?"
    Maya "You calling Kyousuke a liar?"
    Char "No, but..."
    Maya "But nothing. Good job Kyousuke, looks like you're the real magician here!"

    # CODE
    #Choice 1.B
    #    Charlotte -1 points
    #Maya +1 points
    #Kanna 0 points
    $game_player.increaseRelationship("Kanna",1)
    $game_player.increaseRelationship("Charlotte",-1)


    #New choice, reorganized dialogue, and new dialogue after this point:

    #Maybe do another set of choices before Charlotte's humiliation here?

    #Cut back to Ringo and Youko in Kyousuke's bag".

    Youk "You put Kanna up to that, didn't you? There was some sort of cue for her to barge in and tackle my Charlotte to the ground..."
    Youk "Was it the color? Was the codeword 'red'?"
    Rin "Yep. Kinda lucky it turned out this way, huh?"
    Youk "Yes... very fortunate..."

    #Back to the group.


    Kan " Sorry for running into you Charlotte."
    Char "Why exactly were you sprinting through the halls, anyway?"
    Kan "I... was really excited to see Kyousuke. I just wanted to talk to you guys, that's all."
    Char "That's the most suspicious answer you could have given."
    Maya "Well now that Kanna's here, she's got to see some of your splendid magic right?"
    Kan "No that's alright. I don't want to force anyone into doing anything."
    Char "After dramatically crashing into me like the loveable ditzy school girl that you are, Kanna, I would love to show you some of my magic."
    Kan "Oh you don't have to do that."
    Kyou "I want to see more magic!"
    Kan "Well I mean if Kyousuke wants to see more, then I guess it's alright."
    Char "It's decided! The ethereal spectacle shall continue!"
    Maya "You mean magic show?"
    Char "If by 'magic' you mean 'ethereal' and by 'show' you mean 'spectacle' then yes, that's what I mean."
    Maya "God it's like talking to an infant."
    Char "If by 'infant'  you mean 'starchild of the celestial spaceborne multi-dimensional witch-monk-lizard tribe' then yes, that's what it's like."
    Maya "O.K. So Ms. Lizard Wizard."
    Maya "You're supposed to be all-powerful and reality bending or whatever, right?"
    Char " If by 'all-powerful' you mean-"
    Maya "Just answer the question."
    Char "More or less, yeah."
    Maya" Alright. And Kyousuke here is like your wizard apprentice or something, right?"
    Char "He is my wizlet, correct."
    Maya "Shouldn't you teach him something?"
    Maya "Isn't the mark of a knowledgeable person, their ability to teach others?"
    Kyou "I want to learn magic! That sounds awesome!"
    Kyou "Do you know any other magic tricks Charlotte?"
    Char "The better question, Kyousuke, would be are there any magic tricks I don't know."
    Char "And the answer is, only the forbidden ones my masters told me to never ever study."
    Char "I studied them anyway but I'd never admit that."
    Kyou "Wow, what kind of forbidden magic did you study?"
    Char "No idea what you’re talking about."
    Maya "Let’s move onto this lesson, shall we?"
    Char "We shall!"
    Char "And this time, let’s up the ante a bit."
    Char "I will teach you any spell or power you can dream of Kyousuke! Anything at all."
    Kyou "Woah, really?"
    Kan "Uh, really any power? Because I was thinking maybe something lik-"
    Char "Any power at all!"
    Kyou "Wicked!"
    Char "What would you like to learn, delicate and humble Kyousuke?"
    Char "And you, walking-cliche Kanna, pay attention! Your slapstick hijinks will not get in the way of what you're about to see."
    Kan "I said I was sorry!"

    #Cut back to Ringo and Youko in Kyousuke's bag".

    # ART The usual VN choice GUI
    "Two more choices appear in front of Kyousuke."
    "Super Strength."
    "Two sodas."

    Youk "..."
    Rin "..."
    Youk "What does he mean by two sodas?"
    Rin "I have no idea."
    Rin "You’re not seriously considering giving this kid super strength, are you?"
    Rin "He’s gonna end up hurting himself."
    Youk "Of course not. At least not long enough for him to do any damage."
    Youk "But I don’t have the faintest clue what he means by thinking of two sodas."
    Youk"Is he that thirsty?"
    Rin "Man this is getting stupid."
    Youk "You just now realized  that?"
    Youk "Regardless, I believe you're up first this time."
    Rin "Aww, you’re actually playing by the rules?"
    Youk "Some of us have honor, Mr. Fortune."
    Rin "Oh really, and you’re so honorable for always tampering with everything?"
    Youk "I am not a halfwit. You just want the upper hand in this situation so you’re trying to appeal to my sense of pride."
    Rin "Is it working?"
    Youk "Yes. And I will strike a deal with you for this choice and only this choice, Mr. Fortune."
    Youk "I won’t mettle in any way as long as you don’t change the choices. Only highlight them."
    Youk "Let’s see if things really go your way for super strength or whatever the heck ‘two sodas’ means."
    Rin "How do I know you’ll keep your end of the bargain?"
    Youk "Is my word not good enough?"
    Rin "Nope."
    Youk "Then you’ll just have to trust me. You could learn a thing about honor."
    Youk "You would be surprised how much further you’d get in life with it."
    Rin "I think I’ve gotten plenty far in life without it, thank you very much."
    Youk "I’m sure you think that."

    Rin "(We need to get the ball rolling on the fortune telling. But Charlotte needs to be the one to do it, not Kyousuke.)"
    Rin "(We didn’t plan at all for a trick like this one.)"
    Rin "(But this may be a chance to make Charlotte look even worse.)"
    Rin "(Or a chance for Kanna to look good.)"
    Rin "(Whatever I do or pick, even if Youko said he won’t do anything, who knows how that’s going to go.)"
    Rin "(Not show why, but I got a feeling seeing whatever happens with super strength will turn out alright.)"
    Rin "(But I know Youko is just as confused as I am about the soda thing. Maybe letting Kyousuke be Kyousuke will be chaotic enough to make Charlotte mess up.)"

    # CODE
    #Menu: Choices for Kyousuke.
    #"Highlight: Supers strength"
    #"Highlight: Two sodas."

    #Choice 2.A "Super Strength"

    #NOTES - Kyousuke wants to be strong. Charlotte shows him a technique to increase his strength just a little bit. He does indeed feel a little bit stronger.
    #Charlotte recommends crushing the Micolash rock to gain it’s insight to look into the other world.
    #But when he tries to crush the Micolash rock that Charlotte gives him, he can’t do it. Kanna gives it a try and she crushes Micolash with ease.
    #Charlotte and Maya are speechless while Kyousuke is extremely impressed.
    Kyou "I want to be strong!"
    Kyou "Super strong!"
    Kan "That’s not really a spell."
    Char "But it is a power! How strong do you desire to be?"
    Kyou "The strongest guy in the school!"
    Char "Just in the school?"
    Kyou "The strongest guy in the city?"
    Char "Just in the city?"
    Kyou "THE STRONGEST GUY IN THE WORLD!"
    Char "JUST IN THE WORLD KYOUSUKE?"
    Maya "Stop. Stop. Stop."
    Maya "Let's pump the breaks here guys."
    Char "She’s right. Becoming the strongest being in the cosmos takes time. Mars wasn’t built in a day after all."
    Maya "The expression is `Rome wasn’t built in a day."
    Char "That’s not correct. I was there when it was built and it only took a few hours."
    Kan "Kyousuke, you’re already super strong aren’t you?"
    Kan "Why do you want to be stronger?"
    Kyou "I don’t know. It just sounds like it would be cool."
    Kan "I guess it would be cool."
    Maya "It would be."
    Char "It would be cool indeed."
    Char "But I can’t just make you super strong all of a sudden."
    Char "Well I mean of course I can, but this is about your training, not about my magical ability."
    Char "So I will show you a technique to begin your journey of strength training!"
    Kan "Is it proper diet and exercise?"
    Char " Nope. Don’t be ridiculous."
    Maya "It’s going to be some over exaggerated over the top ritual, isn’t it?"
    Char "Exactly!"
    Char "Now Kyousuke. This incantation is a simple one."
    Char "And because you have a wizard learner's permit, you are free to practice incantations and sorceries like this one."
    Char "No hexes or pyromancies though, don’t want to get a head of ourselves after all."
    Char "But if you two try to learn this incantation without a learner's permit, then you’ll be pulled into the pancake dimension by the weight lifting Shinbou monks."
    Maya "Why are the weightlifters in the pancake dimension? That’s a lot of carbs isn’t it?"
    Kan "Is everything made out of pancakes there? Do they use the pancakes as weights?"
    Maya "If their monks, what do they believe in? The maple syrup God?"
    Char "My point is only Kyousuke can attempt this technique. So don’t try it!"
    Char "Now Kyousuke, do you still have the mana capacitor I gave you earlier?"
    Kyou "Uh..."
    Maya "Do you mean the rock you glued googly eyes on?"
    Char "Do not take the eyes of Micolash lightly!"
    Char "We must be thankful to be granted those eyes so we may see the true reality around us."
    Char "But yes, do you still have it Kyousuke?"
    Kyou "I do! Got it right here."
    Char "Excellent! Hand to me."
    Kyou "Alright."
    #Charlotte spits on the rock.
    Char "*Ptooe.*"
    Maya "Eww, what the heck are you doing?"
    Char "Trust me, this is the easiest way to do the incantation."
    Char "Your turn Kyousuke! Let ‘er rip!"
    Kyou "Uh, alright."
    #Kyousuke spits on the rock.
    Kyou "*Ptooe.*"
    Char "Now that we’ve moistened the eyes of Micolash, it’s time for the durability test."
    Char "Squeeze the mana capacitor as hard as you can!"
    Maya "That’s disgusting!"
    Maya "Kyousuke, you don’t have to do what this sicko says."
    Kyou "But I want to get stronger..."
    Char "And you shall! Just squeeze the mana capacitor!"
    Kyou "Well, O.K."
    "Kyousuke wraps his fist around the rock and squeezes."
    "The spit squishes between his fingers and makes the ink from the sharpie run off."
    #*Small cracking noise*
    Kyou "Woah!"
    Kyou "I think it broke!"
    Maya "What? No way let me see."
    Kyou "It’s still intact, but there’s a crack in the middle of it."
    Kyou "Does this mean I’ve gotten stronger?"
    Char "Precisely!"
    Char "And you’ve absorbed .001% of my power."
    Char "If we do this every day and you absorb my power bit by bit, you’ll soon be the strongest being in all of the cosmos!"
    Char "Well second strongest after me, but I’ll allow you to have the credit of being the strongest."
    Kan "N-now hold on! How do we know you didn’t do something with the rock?"
    Kan "How do we even know it’s a rock? You and Kyousuke were the only ones who touched it."
    Maya "Hey yeah! It could be made of papier-mâché or something. We make fake decorations all the time in arts and crafts club. How do we know you didn’t do the same?"
    Char "Again, the mana capacitor that has been bestowed with the eyes of Micolash is not something to be taken lightly I assure you."
    Char "While calling it a mere ‘rock’ is a stretch; I will admit it has similar qualities to a rock. But I did not tamper with it in any way."
    Maya "What’s it going to take for you to admit it’s just a stupid rock?"
    Char "I’ll be drawing my last breath in the fields of combat before I ever say such a thing."
    Char "If you do not believe me, then maybe you should hold the mana capacitor."
    Char "Not like you could even charge any mana to it, that’s only something magical beings such as myself and Kyousuke can do."
    Maya "Fine, give me that."
    "Maya wraps her fist around the rock and squeezes."
    "The spit slides underneath her fingers and the wet ink stains her fingers."
    Maya "Ewwwwww."
    Maya "Yeah it’s a rock."
    Char "Mana capacitor."
    Maya "I know what I said."
    Maya "And I wasn’t able to crack it or anything. It’s as sturdy as it looks."
    Char "So the rock cracked due to Kyousuke’s new level of strength!"
    Kan "Wait just a minute!"
    Kan "I’d like to hold the rock too."
    Char "Mana capacitor."
    Maya "She knows what she said."
    Kan "I feel like there’s something fishy going on that’s all."
    Char "Are you saying Kyousuke and I’s incantation was some sort of trick?"
    Char "It’s a classic Shinbou-technique power transformation. It’s not like I did anything crazy."
    Kan "Either way I just want to see the rock for myself."
    Maya "I already said it is just a rock! You just want to touch Kyousuke’s spit, you creep."
    Kan "I do not!"
    Maya "Are you saying you wouldn’t touch Kyousuke’s lovely spit? That’s pretty rude to Kyousuke isn’t it?"
    Kan "Whose side are you on?"
    Maya "Kyousuke’s of course. Are you saying that you’re not on Kyousuke’s side?"
    Kan "JUST GIVE ME THE ROCK!"
    Maya "Fine, geez."
    "Kan wraps her fist around the rock."
    Maya "Are you blushing?"
    Kan "JUST LET ME LOOK AT IT O.K?"
    "She starts squeezing the rock."
    "The spit coats her entire hand and the ink on the rock is completely faded."
    #"*Loud cracking noise*"
    #The rock crumbles.
    Kan "Huh."
    Kan "See I knew something was up with it! It’s completely destroyed."
    Kyou "WOAH!"
    Kyou "That’s amazing Kanna! You pulverized it. It’s like sand now!"
    Kan "Nice try Charlotte! I knew this was some sort of fake!"
    Char "..."
    Maya "..."
    Maya "I think uh...I think that was an actual rock."
    Char "I uh..."
    Char "K-Kyousuke must have weakened it for you! His new strength must have damaged the structural integrity of the mana capacitor."
    Maya " But it was really solid. There was just a small crack in it, but it felt sturdy."
    Maya "She just turned it into dust like it was nothing."
    Kan "Make as many fake rocks or props as you want, we’re not falling for it!"
    Kyou "Wait, the rock was fake?"
    Char "Nonono I can assure you it was a genuine stone mana capacitor."
    Kyou "That was kinda a fun trick Charlotte, but I wanted to actually get stronger, not just pretend like I am."
    Char "But you are! You are stronger than you were before!"
    Maya "Uh...yeah Charlotte! Kyousuke’s perception of the world is far above even the likes of whatever you claim to be."
    Maya "He played along for your sake, but he knew deep down it was fake."
    Char "Wha? You were just as confused as I about what she did to my mana capacitor!"
    Maya "N-no. I was just caught off guard. I knew it was fake."
    Maya "T-there’s no way someone like Kanna here could do something like that."
    Kan "Hey!"
    Kyou "How did you get so strong, Kanna?"
    Kan "O-oh I’m not that strong. You weakened it for me Kyousuke."
    # End of Choice 2.A

    # CODE
    #Choice 2.A
    #  Charlotte 0 points
    #Maya 0 points
    #Kanna +1 points
    $game_player.increaseRelationship("Kanna",1)
    $game_player.increaseRelationship("Charlotte",0)


    #Choice2.B "Two Sodas"

    #NOTES - Kyousuke explains that he is thirsty but he only has one soda in his backpack. He wants to duplicate it to get another soda! When Charlotte attempts to duplicate the soda, she ends up duplicating the wrong brand by mistake. (This is because Youko grabs a soda for Charlotte but it’s the wrong one.) So Maya takes Kyousuke’s soda and duplicates it for him. Because she knows how to do that. She just does. And when pressed about how / why Maya can do this, she just says she can and there’s no elaboration.


    #Choice 2.B "Two Sodas"

    #Cut to Ringo and Youko

    Youk "Did you seriously make him choose that?"
    Rin "Two sodas."
    Youk "Two sodas?"
    Rin "Two sodas!"
    Youk "Well what on earth happens now?"
    Rin "I guess we’ll find ou-WOAH."

    "Kyousuke begins to take off his backpack."

    Rin "What does he think he’s doing?"
    Rin "We gotta move if we don’t want to get spotted."
    Youk "I’m just going to blend into the shadows inside the backpack. Maybe he won’t notice you?"
    Youk "Just pretend to be a cute little teddy bear in his backpack."
    Rin "Shut up! Make me blend too!"
    Youk "No, I don’t think I will."
    Rin "Then I’m coming with you!"
    Youk "What are yo-ahh  get off of me!"

    "Kyousuke removes his backpack, unzips the main pocket, and starts going through it."

    #Cut back to the group

    Kyou "I got it! I know exactly what you could teach me Charlotte!"
    "Kyousuke pulls out a can of soda from his backpack."
    Kyou "Check it out!"
    Kyou "You can teach me this!"
    "..."
    Char "Er...teach you what exactly?"
    Maya "Of course you wouldn’t know, it’s behind your power Charlotte."
    Char "I beg pardon? What are you talking about?"
    Maya "I know exactly what Kyousuke is asking."
    Maya "Right, Kanna?"
    Kan "Uh...o-of course, it’s simple what he’s asking for."
    Kan "Do you really not know Charlotte?"
    Char "While I have spent a few years working as a jester for the King of the Moon-Dew mountains."
    Char "Do not treat me like a fool!"
    Char "Kyousuke, pray tell, can you be specific about what you would like to learn?"
    Kyou "Two sodas!"
    Char "..."
    Char "Two sodas?"
    Kan "Two sodas?"
    Maya "Two sodas."
    Kan "Uh...I don’t get it."
    Char "You would like to learn to create soda?"
    Maya "Duplication, you brainlets."
    Maya "Kyousuke wants to learn the art of duplication."
    Maya "I’m the only one who truly understands his intelligence. It’s no wonder you guys couldn’t comprehend his desires."
    Maya "Let me help Kyousuke, I can teach you how to duplicate anything."
    Kyou "Sure! I’m just really thirsty and I know one soda isn’t going to be enough."
    Kan "What? Why would you know how to duplicate anything?"
    Char "I agree with head-in-the-clouds Kanna, where did you learn any duplication spells?"
    Maya "It’s easy. Anyone can do it."
    Char "No. We’re not going to waste any time with a feeble human’s attempt at the art of replication."
    Char "Kyousuke! You desire a second tonic, yes?"
    Kyou "Right! I only have one can of  Dr. Amigo’s Jalapeno Desert Splash Blast. I think I need at least two, maybe three to quench this thirst."
    Char "Really? But Dr. Amigo’s Jalapeno Desert Splash Blast is known to be the perfect drink for any occasion."
    Char "I know I drink it in winter, fall, spring, and summer. Day or night. Work days, off days. Lazy afternoons or date nights. There’s never a time where the splash of Dr. Amigo's Jalapeno flavor isn't perfect!"
    Char "Dr. Amigo’s Jalapeno Desert Splash Blast. Bring the heat of the desert and the splash of the ocean, wherever you go."
    Char "Now with extra chunks of jalapeno gunk!"
    Kan "..."
    Maya "..."
    Maya "So...are you gonna make another soda or..."
    Char "Yes of course."
    Char "Kyousuke! Hand me the can of Dr. Amigo’s Jalapeno Desert Splash Blast, if you will."
    Kyou "Here’s the can of Dr. Amigo’s Jalapeno Desert Splash Blast, Charlotte!"
    Kan "Can we...can we please just call it soda?"
    Char "But calling it just soda would be an insult! Dr. Amigo’s Jalapeno De-"
    Kan "NOW YOU HAVE THE SODA. WHAT HAPPENS NEXT?"
    Char "I’m not sure why you felt the need to raise your voice at me. But the next step would be this."
    Char "Kyousuke! Think incredibly hard about this can of...soda."
    Char "The aerodynamic shape of the can. The colorful collage of the logo. The sixty-four flavors hitting your tongue at the same time when you take a drink."
    Char "Every empirical detail. Every sensual sensation. This drink in your brain, so perfectly imagined, you can taste it."
    Kyou "I see it, I see it."
    Kyou "The smell, the taste, the color, the sound of the can opening."
    Char "Good Kyousuke! Now open your backpack and I will place the can within."
    Char "The combination of the mana I’ve transported into the can while I held it and the mental projection you gave of the can should mix together to create not one, not three, but two cans of soda."
    Char "We’re training your metal projection. If we do this often enough, you’ll be able to duplicate objects much bigger than a mere can of soda!"
    Kyou "Awesome! What should I do now? Do I pull the soda out?"
    Char "First shake your bag! As hard as you can!"
    Maya "Wouldn’t that make the soda explode when he opens it?"
    Char "If it were a normal soda yes. But thanks to Dr. Amigo’s patented anti-fizz electric splash juice, we don’t need to worry about any carbonated explosions."
    Char "Now give it a good shake!"
    "Kyousuke shakes the bag."
    "The tinging of multiple pens, and pencils slamming into an aluminum can is heard."
    Char "And now open the bag!"
    Kyou "Woah!"
    Kyou "There’s two cans of soda!"
    Char "Exactly I thought as much."
    Char "And what do the can’s say long-tan-and handsome Kyousuke?"
    Kan "Please don’t make him say it."
    Kyou "Dr. Amigo’s Jalapeno Desert Splash Blast!"
    Char "And the other one Kyousuke?"
    Kan "Please, no more..."
    Kyou "Dr. Amigo’s Jalapeno Dessert Splash Blast!"
    Char "Precisely! See how easy it was to-"
    Char "Wait, what did you say?"
    Kyou "Dr. Amigo’s Jalapeno Dessert Splash Blast."
    Kyou "It’s the wrong flavor..."
    Maya "So you’re telling me. That sweet innocent Kyousuke, who only wanted the refreshingly cool yet crisp taste of the desert."
    Maya "Was given the sweet yet deceptively brisk taste of a dessert?"
    Maya "Have you no shame, Charlotte?"
    Kyou "Charlotte, how could you do this to me?"
    Char "I...but...come on it’s one letter off!"
    Char "Are you not mystified that I made a can appear from thin air?"
    Kyou "But you didn’t duplicate it. It’s just a different can."
    Char "How do we even know that Kyousuke didn’t have another can in his bag?"
    Maya "Are you calling Kyousuke a liar?"
    Char "No! Of course not! I just feel that-"
    Maya "Don’t listen to her, Kyousuke. Here let me help you with the soda you wanted."
    "Kyousuke hands the can of Dr. Amigo’s Jalapeno Desert Splash Blast to Maya."
    Kan "What exactly are you going to do Maya?"
    Maya "Don’t worry about it."
    Maya "I figured this would happen anyway."
    "Maya turns her back from the group. A ruffling sound can be heard."
    Maya "Here you go Kyousuke."
    Kyou "Wow! Two cans of Dr. Amigo’s Jalapeno Desert Splash Blast you did that so fast!"
    Maya "It’s easy. I do it all the time."
    Char "WHAT!?"
    Kan "How did you do that?"
    Maya "I know how to duplicate."
    Char "What do you mean you know how to duplicate?"
    Maya "I just told you, I know how to duplicate."
    Char "Yes, I do too. I just did it."
    Maya "If you just did it why are the cans different?"
    Char "Well I don’t...they’re basically the same thing."
    Maya "But they’re not."
    Kan "Maya, how did you do that?"
    Maya "Are you people not listening? I can duplicate things. It’s easy."
    Kan "But HOW?"
    Char "AND WITHOUT MAGIC NO LESS?"
    Maya "You guys could do it too if you tried."
    Char "I DID TRY. AND I SUCCEEDED."
    Kan "Are you in some ‘duplication club’ or something?"
    Maya "You guys are making a big deal over nothing. Anyone can do it."
    Maya "Do you want another one, Kyousuke?"
    Kyou "No thanks Maya!"
    Kyou "I really thought you could help teach me something Charlotte. Maybe next time I guess."
    Char "But I...Kyousuke you used your mental projection to-"
    Maya "Can we move on now?"
    "Kanna and Charlotte" "NO!"
    Maya "Let’s move on."

    #Back to Ringo and Youko
    Rin "Whew that was a close one! He almost saw me."
    Youk "If you even think about ever touching me again, I’ll turn you into something much worse than a cute little teddy bear."
    Rin "And from the looks of it, Charlotte isn’t looking that impressive to Kyousuke."
    Youk "No matter. A few minor setbacks is nothing to me."

    # CODE
    #Choice 2.B
    #  Charlotte - 1 points
    #Maya 0 points
    #Kanna 0 points
    $game_player.increaseRelationship("Kanna",0)
    $game_player.increaseRelationship("Charlotte",-1)



    Char "Alright, that's it. Everyone, gather around, for I, Charlotte Von Vega, will allow one and all to view a spectacle of magic no one can comprehend!"

    "A small crowd of other students begin to gather."

    #Cut back to Ringo and Youko in Kyousuke's bag".

    Rin "Oh boy, here we go."
    Youk "You may think you have gotten the upper hand today."
    Youk "But, rest assured, this next trick will set things straight."

    #Back to the group.

    Maya "What, are you finally going to do something cool like fortune telling?"
    Char "Yes, as a matter of fact, I am."
    Kan "Today’s been kinda crazy and I feel bad your magic hasn’t gone the way you planned, Charlotte."
    Kan "C-can I make fortune telling a bit easier for you? To prove how great you are?"
    Char "Why, sweet Kanna, of course."
    Kan "Tell us what kind of food I packed into my lunch box."
    Kyou "Isn't that kinda like mind reading? We did something like that already, didn't we?"
    Kan "Not if she doesn’t read my mind! It’s more like clairvoyance."
    Maya "That's kind of boring. What if you already told her?"
    Char "Wha?"
    Kan "What do you mean, Maya?"
    Maya "You could have easily told her what's in the lunchbox, shown her even! We need some sort of middleman to figure out what's in the lunchbox."
    Maya "Like, someone to say what Charlotte's thinking maybe."
    Char "That's it! Astral projection!"

    "Murmurs among the small crowd that gathered."

    Char "I, of course, already know what's in the lunchbox. But Kyousuke does not!"
    Char "Using the powers of astral projection, I will communicate to Kyousuke what's in the box. And he will reveal the contents inside!"
    Char "Kyousuke, can you confirm you have yet to see Kanna today, before she WWE tackled me?"
    Kyou "Yes, I didn't see her before that."
    Maya "I also attest that I didn't see Kanna before that, nor see Kyousuke talk to her."
    Char "Alright, I will now begin the thought transfer."
    Char "I will remain standing right here, so you can all see. I am now interacting with him purely through metaphysical cognitions."

    "Charlotte places her fingers upon her forehead, and begins humming."

    # CODE Show previous CG where Ringo and Youko talk on Kyousuke's backpack
    #Cut back to Ringo and Youko.

    Youk "I must congratulate you on your first few attempts. Made me look like a fool. But it won't happen again."
    Youk "Care to go first?"
    Rin "Does it matter? You're just gonna overwrite him, aren't you?"
    Youk "Oh, most surely."
    Rin "Just get it over with already."

    "Youko places one single purple choice in front of Kyousuke. "

    Youk "A banana, yogurt, rice balls, and sushi."
    Youk "Is this true? Quite the peculiar lunch box."
    Rin "Might be."
    Youk "Accept your defeat with some dignity, Mr. Fortune."

    #Cut back to the group.

    Char "Alright! Kyousuke, did you feel my thoughts cascading into your mind?"
    Kyou "Umm, yes, I think so."
    Char "Everyone, please hold your breath and applause, for I am about to place just a small slice of my galaxy-sized brain, into this normal mortal boy."
    Char "Alright, Kyousuke, tell us."
    Char "WHAT'S"
    Char "IN"
    Char "THE"
    Char "BOX?"

    "A silence fills the crowd."

    Kyou "Um, for some reason, I feel as though I know what's in the lunchbox."
    Kyou "A banana, a cup of yogurt, rice balls, and I think some sushi?"
    Char "Well? Will you oblige us and open the lunchbox in question, Kanna?"

    "Kanna silently opens the lunchbox, and shows it to the crowd of people."
    "The contents appear to be a banana, yogurt, rice balls, and sushi, just how it was predicted."

    # ART Charlotta sprite grinning.
    "Charlotte breaks out into a massive grin."

    Char "WAHAHAHA!"

    #SFX Crowd walla (murmurs, surprised gasps and excited voice), maybe some applause.
    "The crowd murmurs. Small cheers and gasps can be heard quietly from around the room."

    Char "Is the audience satisfied? They sure sound like it to me. Need I do anything more to prove just how limitless my power and influence can be?"
    Char "The great and powerful Charlotte Von Vega proves herself again!"
    Char "WAHAHAHA!"
    Kan "Actually, Charlotte, hold that thought."

    #ART Maybe a CG, if you guys want.
    "Kanna pulls out the contents of the lunchbox, to reveal a blanket. In the center of the blanket, is the picture of an ordinary lunch consisting of a banana, a cup of yogurt, rice ball, and sushi."
    "All around the center however, were small red and gold hearts, layered above the green fabric."
    "It appears the blanket was folded in a way, so the picture of the lunch would be on top."
    "If one were to peek into the lunchbox, they could probably tell it was a blanket."
    "But if one were a small shadow, quickly peeking in and then looking away, they could easily mistake the picture on the blanket for real lunch items."

    Kan "I made this for you, Kyousuke. I didn't have anything else to put it in, so I skipped lunch today to bring it to you!"
    Maya "What? A present for Kyousuke?  Kanna, that's not fair!"
    Char "Wa?"
    Char "Waha?"
    Char "Waha... ha?"
    Kan "It's amazing you guessed the picture on the blanket, Charlotte! I wonder how you did that?"
    Kan "But it looks like you're wrong this time."

    Char "I..."
    Char "But..."
    Char "..."

    #SFX light laughter
    "Snickers and suppressed laughter can be heard from the kids watching."
    "Charlotte holds her head up, and without saying a word, walks away from the staring group."

    # CODE or ART
    #Charlotte points -1
    #Kanna points +1
    #Show the player this.
    $game_player.increaseRelationship("Kanna",1)
    $game_player.increaseRelationship("Charlotte",-1)

    # CODE Show the usual CG of Ringo and Youko on Kyousuke's backpack
    #Cut to Ringo and Youko in Kyousuke's bag one last time.

    Youk "You... you!"
    Rin "Me, that's right."
    Youk "In front of everyone, how dare you!?"
    Rin " She's the one to blame. We were just planning on making her look dumb in front of Kyousuke and, maybe, Maya."
    Rin " But little Miss Showoff wanted everyone to watch her perform your stupid, cheating trick."
    Rin "This is how us, little guys, beat the big corporate boys."
    Youk "...Very well Mr. Fortune, I’ll cut you a deal"
    Youk "I won't override Kyousuke's mind, so long as you don't crush Charlotte's spirit like that ever again."
    Rin "I'm telling you. She did it to herself. But, alright, deal."
    Rin "A healthy dose of social embarrassment never hurt anyone."
    Youk "Just remember we're here to bring these kids together, not apart."
    Rin "Ha! What’s a corporate slave like you know about bringing people together?"
    Rin "Remember, we do have a conflict of interest. And if you're gonna cheat, I'll do what I can to prevent that."
    Youk "True. Nevertheless, proper etiquette shouldn't be disregarded. See you later, Mr. Fortune"
    Rin "Unfortunately, yes, you will."

    #Cut back to the group.

    Maya "She didn't put up much of a fight, huh? I thought she would have like, laughed and stuff, given a massive soliloquy on how cool she is, and denied her loss."
    Kyou "Thanks for the blanket, Kanna! That's so nice of you!"
    Kan "Y-yeah, of course. I wasn't sure about your favorite color. I hope you like it."
    Maya "Alright, how did you know all this? How'd she know the picture on the blanket? What's the deal?"
    Kan "A good magician never reveals her secrets."

    #Day 6     Kanna's room.
    scene room night
    Kan "Ringo, what if we're doing the wrong thing?"
    Kan "Are we manipulating Kyousuke like the other two girls are?"
    Rin "Yea, I guess we are. But this is what you wanted, ain't it?"
    Rin "Besides, there doesn't seem to be a lot of harm in it, is there?"
    Kan "Tomorrow, maybe just let me talk to Kyousuke."
    Kan "Even if the other two show up and get feisty.  I just want to talk to him, without you affecting him."
    Rin "Kid, we made a deal. You made a wish, and I need to grant it. I really, really can’t stand being a bear anymore."
    Kan "Please, Ringo, just tomorrow! We'll go back to normal after that."
    Rin "{i}Sigh. {/i}"
    Rin "Alright, kid, if it'll make you feel better."
    Kan "You think Charlotte's alright?"
    Rin "She was cheating, remember? I'm surprised our plan worked out so well. "
    Kan "Same. See you tomorrow, Ringo."
    Rin "Night, kid."

    #Everyone's scores with Kyousuke so far.

    #Possible scores increases day 6 .
    #Choice 1.A :     -2 Charlotte
        #    0 Maya
        #    +2 Kanna

    #Choice 1.B:     -2 Charlotte
        #    +1 Maya
        #    +1 Kanna

    "SHOW SCORE"

    $Kanna = game_player.getRelationship('Kanna')
    $Maya = game_player.getRelationship('Maya')
    $Charlotte = game_player.getRelationship('Charlotte')
    "We Kanna has [Kanna] , Maya has [Maya] and Charlotte [Charlotte]"


    #Add/remove points from total accordingly.
    #Show total scores so far.
    #Day 6 end:
