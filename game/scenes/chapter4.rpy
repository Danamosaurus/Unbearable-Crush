label chapter4:

    $ game_day = "Day 4"

    scene hallway onlayer master with squares:
        subpixel True xpos 0.5 ypos 2.2 xanchor 0.5 yanchor 1.0 rotate None
        parallel:
            xpos -0.02
            ease_cubic 3.17 xpos 0.45

    Kan smile happy ec "{i}Hm mm mm mm hmmm.{/i}"
    Kan smile happy ec "{i}Hm mmmm, hmm mm hmmmmmmmm.{/i}"
    Kan smile happy ec "{i}HMMM, HM HM HMMM, MMM, HM MMMMM.{/i}"

    Rin "If you're going to hum can you do it, I don't know, QUIETLY?"
    Kan "Well aren't you just a stuffed little bundle of sunshine this morning?"
    Rin "Believe it or not, not everyone likes to hear aggressive grunting in their ears."
    Rin "And I can hear {i}everything{/i} in this backpack. Crystal clear, surround sound, caveman sounds from Kanna."
    Kan "Well {i}excuse me{/i} for being in a good mood. But we got the perfect plan for today!"

    Kan speaking "Maya's put up some real competition, but she's no match for my ultimate ability."

    Rin "Yeah, who knew you'd be SO good at baking! I'm honestly shocked."
    Rin "I really thought you bought those brownies we ate from the store or something."

    Kan eo "They were homemade from scratch, thank you very much."
    Kan eo "And I’ve been practicing. Our class recipe contest is coming up, and when my turn comes, I’m going to make a cake so good that they’ll have to make me next year's student chef!"

    Rin "I'll say. I haven't tasted chocolates like these in decades."

    Kan "...Huh?"

    Kan speaking confident "Aaaaa! Don't eat them! Those are for Kyousuke! What are you doing in there?"

    Rin "Delicious!"

    Kan sleeping "Just don't eat all of them..."
    Kan sleeping "When I give Kyousuke these extra special chocolates, he'll just have to fall for me."

    Kan drooling happy ec "Ehehe~"

    show Kyou normal at center with Dissolve(.5)

    Rin "Oh, look, there he is!"

    Kan speaking excited crazy blush "{i}Ah.{/i}!"

    Rin "Just remember! Trust the fancy chocolate!"

    "I hand her the box, snugging one last one for the road."

    Kan speaking excited crazy blush "Right. Fancy chocolate. Let's do this!"

    Rin "Loving the confidence kid. Go! Go! Go!"

    Kan speaking surprised crazy "Hey, Kyou-"

    Maya "Oh Kyousuke! I have an extra special surprise for you!"

    Kan angry crazy "Hmm!?"
    $ hide_sides = ['Kyousuke']
    Kyou surprised "Oh, Maya, good morning!"

    Maya speaking normal "I was thinking about how much you loved the rice balls I made for you a few days ago, so I thought that I could do something to brighten your day!"
    Maya speaking normal "So I made you more of them!"
    Kyou "Wow uh, thanks Maya! I thnk."

    Maya flirting eo "Your welcome! And wouldn't it be great if you had these kind of surprises everyday?"
    Maya flirting eo "From now on, I'll be making your lunch daily."

    Kyou "Woah Maya, are you sure? That sounds like a ton of work!"
    Maya flirting eo "Oh it's just what I do Kyousuke. What are such good friends for?"

    Kan "{i}Nng!{/i}"

    Rin "Relax, kiddo. Let your boy Ringo handle this."

    "Don't have to make this complicated, just got to get Kyousuke here to think about sweets."
    "And then coincidentally: {i}Oh would you look at that? I'm in the mood for some sweet chocolaty goodness and Kanna here just happens to have some?{/i}"
    "{i}Looks like I'm falling in love with her now!{/i}"
    "Oh to be young again. They think love is so simple."
    "Let's see what Kyousuke's thinking here."

    "Wait..."

    "...That smell again."

    "But I took a shower last night, am I still this stinky?"
    "Hold on, what's happening? What's with the kids crowding around the windows"

    "Girl 1 " "What's with that weird girl outside?"
    "Girl 2" "Let's go see! Looks like some kind of magic show!"

    Kan "Magic show? Is the school doing some kind of event?"
    Maya "Event? Oh thanks for remind me {i}Kanna{/i}. Kyousuke, about the festival this weekend~"
    Kan "W-wait! What don't we see what's happening outside!"
    Kan "It looks like all the other kids are heading out there, why don't we go take a look?"
    Kyou "Sure! Sounds like fun. I do wonder what all the commotion is."

    "NOTE FOR TEAM: If we're still using the front of the school yard background for this scene, we'd use it here before cutting the CG in."


    #Background Front of school
    "Not as many kids out here as I thought they'd be."
    "There's still a small group forming in the courtyard, watching something."

    "Boy" "Is this authorized by the student council, Pres?"
    "President" "No it's not. If this takes too long we'll put a stop to it."
    "President" "But let's see how this plays out."

    Kan "What's going on?"
    Maya "Did she really have to come with us, Kyousuke?"
    Maya "I don't want her to think hanging around us is going to be a regular thing."
    Kan "And what would be so wrong with that?"
    Maya "You'll get your boring person germs on everything."
    Kan "That shouldn't be a problem. Just use your hair to clean everything!"
    Kan "What's in it exactly? Is it that blue liquid soap used for cleaning toilets?"
    Maya "If one more word comes out of your flappy fat lipped mouth, I'm going to put you in the ground."
    Kyou "Guys look! Some sort of magic act is starting!"


    "???" "Come one, come all. Come and witness feats and wonders beyond the gates of human understanding."
    "???" "Watch as I break the limits of human capability, defying God and peforming the very same act as he did."


    #ART Charlotte appears CG
    scene cgs charlotte_intro with dissolve:
        xanchor .5
        yanchor .5
        xpos .5
        ypos .5
        zoom .35


    "???" "Only I, Charlotte Von Vega, the celestial witch of the stars, monk of the cosmos, and warlock of time, can perform such raw magical talents. "
    "???" "Behold mortals, the act of CREATION!"
    "???" "WAHAHAHAHA!"
    #Poof sound effect
    "Woah!"
    #Bird, Dove noises
    "There's birds everywhere!"
    #Students cheering / voices murming with the birs falling everywhere
    Char "Fly my feathered minions, fly!"
    Char "Grace the universe with the presence of my creation, spread the word and love of Charlotte Von Vega to all!"
    Char "WAHAHAHAHA!"

    Kan "How'd she do that? There's so many of them!"
    Kyou "It's amazing!"
    Maya "It's a simple magic trick. She must of had them under her sleeves."

    "President" "Alright that's enough, that's enough. We've had our fun. Everyone go back inside!"


    scene hallway onlayer master with squares:
        subpixel True xpos 0.45 ypos 2.2 xanchor 0.5 yanchor 1.0 rotate None

    Kyou "That was so cool! How do you guys think she did it?"
    Maya "Sleeves, Kyousuke, her sleeves."
    Kan "That is a LOT of birds to hide in her sleeve."
    Maya "Now Kyousuke, do you want your maple rice ball now or later?"
    Kan "W-wait! Kyousuke, I have a surprise for you too!"
    Kyou "Oh my gosh, you guys are so nice!"
    "Alright, distractions over. Now let's take a peak at his thougts-"
    #ART Show Kanna & Maya popins

    Char "Prepare yourself, Kyousuke! For the rulers of this world have declared our sacred introduction!"
    Maya sad speaking "This lunatic again?"
    Char "By my authority as the master of the dark gateways between realms, I declare this man to be my eternal servant..."

    Char "...In this life and the next, An eternal contract between you, Kyousuke, and the dark wizard Charlotte Von Vega!"

    Kyou frown "I uh, don't know what that means."

    Char "Don't be alarmed. In this mortal form, I can manifest only one-tenth of my true power. When I present to you my gift, all of your questions will be answered."

    Char "Now eat! Taste the magical sensation of my strawberry cake of astral knowledge and be my companion for all eternity!"
    Kyou "Huh, funny enough, I was really craving some sweets!"

    Kan frown pout ec "{i}...{/i}"
    Kan "K-kyousuke! I made you these chocolates! Do you want to try one?"
    Kyou "Sure, Kanna! But first, I want to try the strawberry cake first."
    Maya "What about my rice balls!?"

    "I-I can't read his thoughts."
    "I don't know what this is, but it's no match for my power of suggestion."


    #CG kyousuke choice

    #Rin "See? He's already made up his mind!"

    #CG Ringo's golden choice poofs away and is replaced by Charlotte's purple choice.

    # CG Surprised pikachu face popin
    #Rin "{i}Eh-{/i}"

    #Kan speaking confident "It's gone!"

    Maya annoyed eo "Kyousuke?"

    # CG Simulate "Eat Charlotte's delicious strawberry cake" being picked
    Kyou "I - I think I..."
    Kyou "Love the strawberry cake! Yum yum yum, delicioso!"
    Maya "You didn't even try mine!?"
    Kan "Or mine!? Kyousuke, what about the chocolates?"
    Kyou "Let me, mmmm, finish this cake up first."

    show Char cheeky smile at center with dissolve:
        zoom 1.25

    Char cheeky smile "Well, Kyousuke, how does it feel? Do you suddenly find me...irresistable?"
    #Code XP bar goes up up up +++++ 
    Char smile ec "Do you feel compelled to bow down at my feet and succumb to my every request?"
    Kyou "{i}Mmm{/i}, so good~"


    Char frustrated eo "It's not working... why isn't it working!?"

    # CG Suddenly Maya comes back to her senses.

    Maya "Hey! What's the big idea? Stop eating that!"

    #SFX slap the cake out of his hands, plate falls to the ground, rolls around a little bit.

    Maya "I've got to get you away from this loon so you can enjoy my company properly! Come on, Kyousuke!"

    "She grabs his hand and pulls him away."

    Char "Wait! Come back. I command you to!"

    Char disgusted "Why didn't my spell work?"

    hide Char with dissolve

    "Kanna backs away and we duck behind a corner."

    show hallway onlayer master:
        ease_cubic 3.17 xpos 1.35

    Kan "Ringooo! What do we do? That banshee is trying to steal him away from me! Why didn’t you stop Kyousuke from eating her dumb cake?"

    Rin "Something interfered with my suggestion magic. Normally I take a look at what he’s thinking and push him in your direction, but it’s like someone else did it first."

    Kan speaking excited crazy blush "{i}Gasp!{/i} The other spirit you were talking about? Is Charlotte a spirit?"

    Rin "Nope. She's not a spirit."

    Kan speaking curious "Really?"

    Rin "Yup, she's completely human."

    Kan "But what about all that magic stuff? Those words she was saying?"

    Rin "Nope. Totally human. Not one lick of magic in her."

    Kan smile concerned ec "So all those things..."

    Rin "There's no '{i}Master of the Dark Gateway{/i}' or whatever. Totally delusional! Ha!"

    #SFX Bell rings

    Kan speaking curious "But how did she change your persuasion magic? What was Kyousuke so obsessed with her cake?"

    Rin "Yeah, about that...I'll handle it, don't worry. You head off to class. I've got some investigating to do."

    Kan smile worried eo "Alright, Ringo."
    Kan smile happy speaking ec "I'll leave it in your capable paws, I guess."

    "That smell again, way stronger now."
    "Wait a minute, I know this smell."

    Rin "{i}*Sniff, sniff*{/i} Alright. Now where are you..."

    # CODE Scene hallway with squares

    Rin "We both know theres no way that girl did all those things on her own. Come on out."

    # Fox appears

    "???" "Ah, I thought I had caught the scent of a spirit in the area. Although, I must confess, I wasn't expecting a cute little teddy bear."

    Rin "Show yourself, spirit!"
    $ hide_sides = ['Youko']
    show Youk  onlayer master:
        xpos 931 ypos 1079 xanchor 0.5 yanchor 1.0 alpha 0
        parallel:
            additive 1
            easeout 1 additive 0
        parallel:
            easein 1.5 alpha 1
        parallel:
            easein 1 zpos -50

    Youk speaking "Ringo Fortune? Is that really you? I almost mistook you for a clearance sale toy."

    Rin "Youko! So it was you who's been screwing up my magic! Can't you see I'm trying to grant a wish here?"

    Youk smile "Oh fierce and powerful servant of luck, I see you've lost a bet."
    Youk smile "Was it a curse from a fellow spirit? A hex from an unhappy wish maker?"
    Youk smile "Perhaps you just have some perverted wish to be a teddy bear that you won't admit?"
    Rin "Can it, you demon! I ain't telling you squat!"

    Youk speaking "Your ridiculous form aside, as a fellow spirit, I'm sure you can understand that I'm merely acting in accordance to my master's will."

    Rin "Yeah, about that... How did the demon spirit Youko end up serving a delusional high schooler?"

    Rin "Did {i}you{/i} lose a bet?"

    Youk neutral "Wow, truly a clever retort. Genius, really...I suppose it happens we find ourselves in similar situations."
    Youk neutral "But it's simple Mr. Fortune. Someone made a wish on my shrine, so I must fulfill it. It's the first rule of any transaction."
    Youk "And business is the real force of this world, not luck, love, or anything in between."
    Rin "Oh brother, just stop! No one wants to hear that boring nonsense."
    Youk speaking "That aside, I must ask that you don't interfere with my work. The lady Charlotte has requested a human companion, and it seems Kyousuke is the only boy who is acceptable."

    Rin "Sounds a lot like my wish maker. Under normal circumstances, I'd be just fine letting you have him. I'm not so rude to interfere with the work of another spirit."

    Rin "But, this time, you can't have him!"

    Youk neutral "Beg pardon?"

    Rin "I need him! I'm trying to make that boy go on a date with my delusional teenager. You're messing that up, so, begone demon! Lest I smite thee, with the magic of heaven's door, or whatever."

    Youk speaking "Oh, I'm absolutely trembling."
    Youk speaking "Then it shall be some sort of competition then? For the boy, Kyousuke?"
    Rin "You're on!"
    Youk smile "Oh, Mr. Fortune, always one to charge boldly ahead without thinking."
    Youk smile "It will be fun tearing you down."
    Rin "Likewise you pretencious jerk!"
    Youk neutral "If you excuse me, the lady Charlotte is requesting me."
    Youk smile "Looks like we'll be seeing more of each other, til next time Mr. Fortune."


    scene room with squares

    Kan "SHE SUMMONED A SPIRIT? HOW IS THAT FAIR?"
    Rin "Aren't you being a bit hypothetical?"
    Kan "NO I'LL NEVER GET KYOUSUKE TO NOTICE ME!"
    Kan "ARRGGHHHH."
    "And back to screaming into her pillow she goes."
    Kan "Is that even...right?"
    Rin "It's no left or right kid, we'll deal with her and her spirit as we go."
    Kan "No, I mean, this Charlotte girl summoned a spirit to help her get Kyousuke too."
    Kan "That doesn't seem...good. Like she's just using some magical powers to get Kyousuke to like her."
    Kan "That's not true love..."
    Kan "And aren't we doing the same thing?"
    Rin "We're not like them! We're just...{i}suggesting{/i} Kyousuke to make some differnet choices."
    Rin "Choices that will end up with him and you together!"
    Kan "But that's not...real."
    Rin "It's real enough, isn't it? Besides, you really think Kyousuke wants to end up with that wackjob? Or even Maya for that matter?"
    Kan "No...maybe...I don't know. It's his feelings, it's not up to any of us."
    Kan "Relationships are about two people together, not one person just following what the other person wants."
    Kan "Right?"
    Rin "I think, you're thinking too hard. Just let me handle this, alright?"
    Kan "I don't know, I need time to think."
    Rin "Tell you what, let me survey the situation tomorrow. See how this Charlotte girl and her spirit operate."
    Kan "Well...I did promise the Home Ec club I'd help them with sewing and baking tomorrow..."
    Rin "Go! Bake a scarf or knit a cake or whatever, let ole Ringo handle it."
    Kan "Well...okay. I trust you."
    Rin "Great! Now get some sleep, I gotta get my thougts together about all this."
    Kan "Good night, Ringo."
    "All of this just got a lot more messy."
    "Of course it did, it always does."
    "And I'm stuck in this stupid bear form until we get it figured out."
    "Go figure."

    scene white with Dissolve(1.0)

    jump chapter5
