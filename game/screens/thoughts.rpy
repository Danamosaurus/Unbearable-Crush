### Styles


## Thought screen ###############################################################
##
## This screen is used to display the thoughts of a character. The one parameter
## is a list of thoughts (please use only up to 2 for now)
##
init python:
    thought_button_transform_duration = 0.3
    thought_button_transform_strenth = 0.5
transform thought_button_minimised_transform(target_zoom=0.2):
    anchor (0.5, 0.5) transform_anchor True
    parallel:
        easein 0.3 zoom target_zoom alpha 1
    parallel:
        block:
            ease thought_button_transform_duration offset (-5*thought_button_transform_strenth, -5*thought_button_transform_strenth)
            ease thought_button_transform_duration offset (5*thought_button_transform_strenth, 5*thought_button_transform_strenth)
            ease thought_button_transform_duration offset (0, -3*thought_button_transform_strenth)
            ease thought_button_transform_duration offset (-3*thought_button_transform_strenth, 0)
            ease thought_button_transform_duration offset (5*thought_button_transform_strenth, -5*thought_button_transform_strenth)
            ease thought_button_transform_duration offset (-5*thought_button_transform_strenth, 5*thought_button_transform_strenth)
            ease thought_button_transform_duration offset (3*thought_button_transform_strenth, 0)
            repeat
transform thought_button_expanded_transform(target_offset=(0,0), target_zoom=1.0):
    ease 0.2 offset target_offset zoom target_zoom
transform thought_button_hide_transform:
    linear 0.3 alpha 0 zoom 0

image flash_white:
    "#fff"
    alpha 0
    linear 0.3 alpha 0.5
    linear 1.0 alpha 0.0
init python:
    def thought_button_add_expanded_index(val, index):
        if val is None:
            return [index]
        return val + [index]
screen thought(items, expanded=[], block_progress=True):
    default hovered_index = None
    fixed:
        if block_progress and expanded is not None and len(expanded) == len(items):
            add "flash_white"
        align (0.5, 0.1)
        for i in range(len(items)):
            button:
                pos (1100 + (i-1) * 300, 150)
                background "gui/thought/thought_bubble_default.png"
                xsize 480
                ysize 270
                padding (80, 40)
                if expanded is None:
                    at thought_button_hide_transform
                    text items[i]:
                        text_align 0.5
                        align (0.5, 0.5)
                        color "#000"
                        size 32
                elif i in expanded:
                    if i == 0:
                        at thought_button_expanded_transform((-200, 0))
                    elif i == 1:
                        at thought_button_expanded_transform((200, 0))
                    text items[i]:
                        text_align 0.5
                        align (0.5, 0.5)
                        color "#000"
                        size 32
                else:
                    if i == hovered_index:
                        at thought_button_minimised_transform(0.3)
                    else:
                        at thought_button_minimised_transform(0.2)
                    text "...":
                        text_align 0.5
                        align (0.5, 0.5)
                        yoffset -30
                        color "#000"
                        size 150
                    hovered SetScreenVariable("hovered_index", i)
                    unhovered SetScreenVariable("hovered_index", None)
                if expanded is None or i in expanded:
                    action None
                else:
                    action [SetScreenVariable("hovered_index", None),
                            Show("thought", None, items, expanded=thought_button_add_expanded_index(expanded, i), block_progress=block_progress)]
    if expanded is None:
        if not block_progress:
            timer 0.3 action Hide("thought")
        else:
            timer 0.3 action Return()
    elif len(expanded) == len(items):
        ## play juice SFX for finishing minigame
        #timer 0.1 action Play('juicy_sfx.ogg')
        timer 2.0 action Show("thought", None, items, expanded=None, block_progress=block_progress)
        if block_progress:
            key config.keymap['dismiss'] action Show("thought", None, items, expanded=None, block_progress=block_progress)
