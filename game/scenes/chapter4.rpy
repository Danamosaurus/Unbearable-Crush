label chapter4:

    $ game_day = "Day 4"

    scene hallway onlayer master with squares:
        subpixel True xpos 0.5 ypos 2.2 xanchor 0.5 yanchor 1.0 rotate None 
        parallel:
            xpos -0.02
            ease_cubic 3.17 xpos 0.45

    Kan smile happy ec "Hm mm mm mm hmmm."

    "Kanna hums along as we enter the school. I'm riding in her backpack again, this time with a very special box in here with me."

    Kan speaking "That Maya's put up some real competition, but she's no match for my ultimate ability."

    Rin "Yeah, who knew you'd be good at baking! I'm honestly shocked."

    Kan eo "I’ve been practicing. Our class recipe contest is coming up, and when my turn comes, I’m going to make a cake so good that they’ll have to make me next year's student chef."

    Rin "I'll say. I haven't tasted chocolates like these in decades."

    Kan "...Huh?"
    
    Kan speaking confident "Aaaaa! Don't eat them! Those are for Kyousuke! What are you doing in there?"

    Rin "Delicious!"

    Kan sleeping"{i}pout{/i} When I give Kyousuke these extra special chocolates, he'll just have to fall for me."

    Kan drooling happy ec "Ehehe..."

    show Kyou normal at center with Dissolve(.5)

    Rin "Oh, look, there he is!"

    Kan speaking excited crazy blush "{i}Ah.{/i}!"

    Rin "Just remember! Trust in the fancy chocolate!"

    "I hand her the box. She holds it with newfound confidence."

    Kan sad "Right. Fancy chocolate. Let's do this!"

    Rin "Ready? Go!"

    "She steps forward to Kyousuke."

    Kan speaking surprised crazy "Hey, Kyou-"

    Maya "Oh Kyousuke, darling! I have an extra special surprise for you!"

    Kan angry crazy "Hmm!"
    $ hide_sides = ['Kyousuke']
    Kyou surprised "Oh, Maya, hey."

    Maya speaking normal "I was thinking about how much you loved the rice balls I made for you yesterday, and I thought that I could do something to brighten your day!"

    Maya flirting eo "So I'm going to make your lunch every day."

    Kan "{i}Nng!{/i}"

    Rin "Relax, kiddo. Let your boy Ringo handle this."

    "I poke my head out of Kanna's backpack."

    Rin "Ahem..."

    # Art The usual CG?
    "Choice appears : 'What I'd really love right now is some extra special chocolates.'"

    "Perfect."

    Rin "Alright Kanna, here comes your cue."

    "Wait..."

    "...That smell."

    "But where-"

    "???"  "WAHAHAHAHA!"

    #ART Charlotte appears CG
    scene cgs charlotte_intro with dissolve:
        xanchor .5
        yanchor .5
        xpos .5
        ypos .5
        zoom .35
    "???" "Prepare yourself, Kyousuke! For the rulers of this world have declared our sacred introduction!"

    #ART Show Kanna & Maya popins

    Maya sad speaking "Who is this chick?"

    "???" "By my authority as the master of the dark gateways between realms, I declare this man to be my eternal servant..."

    "???" "...In this life and the next, An eternal contract between you, Kyousuke, and the dark wizard Charlotte Von Vega!"

    $ hide_sides = ['Charlotte']
    Kyou frown "I uh, don't know what that means. I'd really like to eat some extra special chocolates right now though."

    Char "Don't be alarmed. In this mortal form, I can manifest only one-tenth of my true power. When I present to you my gift, all of your questions will be answered."

    Char "Now eat! Taste the magical sensation of my strawberry cake of astral knowledge and be my companion for all eternity!"

    scene hallway onlayer master with squares:
        subpixel True xpos 0.45 ypos 2.2 xanchor 0.5 yanchor 1.0 rotate None 

    Kan frown pout ec "{i}...{/i}"

    Rin "I don't know what this is, but it's no match for my power of suggestion."

    #CG kyousuke choice

    Rin "See? He's already made up his mind!"

    #CG Ringo's golden choice poofs away and is replaced by Charlotte's purple choice.

    # CG Surprised pikachu face popin
    Rin "{i}Eh-{/i}"

    Kan speaking confident "It's gone!"

    Maya annoyed eo "Kyousuke?"

    # CG Simulate "Eat Charlotte's delicious strawberry cake" being picked

    Kyou "I - I think I..."

    Kyou happy "prefer...strawberry...cake..."

    show Char cheeky smile at center with dissolve:
        zoom 1.25

    Char cheeky smile "Well, Kyousuke, how does it feel? Do you suddenly find me...irresistable?"
    #Code XP bar goes up up up +++++ 
    Char smile ec "Do you feel compelled to bow down at my feet and succumb to my every request?"

    Kyou "{i}Mmm{/i}, really good cake."
    #XP bar starts falling back down, settling on +3 for Charlotte
    $game_player.increaseRelationship("Charlotte",3)
    Char frustrated eo "It's not working... why isn't it working!?"

    # CG Suddenly Maya comes back to her senses.

    Maya "Hey! What's the big idea? Don't eat that!"

    #SFX slap the cake out of his hands, plate falls to the ground, rolls around a little bit.

    Maya "I've got to get you away from this loon so you can enjoy my company properly! Come on, Kyousuke!"

    "She grabs his hand and pulls him away."

    Char "Wait! Come back. I command you to!"

    Char disgusted " Why didn't my spell work?"

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

    Rin "There's no 'Master of the Dark Gateway' or whatever. Totally delusional! Aha!"

    #SFX Bell rings

    Kan speaking curious "But how did she change your persuasion magic? I totally saw it."

    Rin "Yeah, about that...I'll handle it, don't worry. You head off to class. I've got some investigating to do."

    Kan smile worried eo "Alright, Ringo."
    Kan smile happy speaking ec "I'll leave it in your capable paws."

    "She puts me down and goes off to class."

    Rin "{i}Sniff{/i} Alright. Now where are you..."

    # CODE Scene hallway with squares

    Rin "We both know theres no way that girl did all those things on her own..."

    # Fox appears

    "???" "Ah, I thought I had caught the scent of a spirit in the area. Although, I must confess,  I wasn't expecting a cute little teddy bear."
    
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

    Youk speaking "Your ridiculous form aside, as a fellow spirit, I'm sure you can understand that I'm merely acting in accordance to my master's will."

    Rin "Yeah, about that... How did the demon spirit Youko end up serving a delusional high schooler?"

    Rin "Did {i}you{/i} lose a bet?"

    Youk neutral "Wow, truly a clever retort. Genius, really...I suppose it happens we find ourselves in similar situations."

    Youk speaking "That aside, I must ask that you don't interfere with my work. The lady Charlotte has requested a human companion, and it seems Kyousuke is the only boy who is acceptable."

    Rin "I've heard that somewhere before. Under normal circumstances, I'd be just fine letting you have him. I'm not so rude to interfere with the work of another spirit."

    Rin "But, this time, you can't have him!"

    Youk neutral "Beg pardon?"

    Rin "I need him! I'm trying to make that boy go on a date with my delusional teenager. You're messing that up, so, begone demon! Lest I smite thee, with the magic of heaven's door, or whatever."

    Youk speaking "Oh, I'm absolutely trembling."

    scene white with Dissolve(1.0)

    jump chapter5
