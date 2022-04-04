### Styles


## Thought screen ###############################################################
##
## This screen is used to display the thoughts of a character. The one parameter
## is a list of thoughts (please use only up to 2 for now)
##
init python:
    thought_button_transform_duration = 0.3
    thought_button_transform_strength = 0.5
transform thought_button_shiver_transform(target_offset=(0,0), target_zoom=1.0, start_delay=0.0):
    anchor (0.5, 0.5) transform_anchor True
    pause start_delay
    parallel:
        easein 0.3 zoom target_zoom alpha 1
    parallel:
        block:
            ease thought_button_transform_duration offset (target_offset[0] - 5*thought_button_transform_strength, target_offset[0] - 5*thought_button_transform_strength)
            ease thought_button_transform_duration offset (target_offset[0] + 5*thought_button_transform_strength, target_offset[0] + 5*thought_button_transform_strength)
            ease thought_button_transform_duration offset (target_offset[0] + 0, target_offset[0] - 3*thought_button_transform_strength)
            ease thought_button_transform_duration offset (target_offset[0] - 3*thought_button_transform_strength, target_offset[0] + 0)
            ease thought_button_transform_duration offset (target_offset[0] + 5*thought_button_transform_strength, target_offset[0] - 5*thought_button_transform_strength)
            ease thought_button_transform_duration offset (target_offset[0] - 5*thought_button_transform_strength, target_offset[0] + 5*thought_button_transform_strength)
            ease thought_button_transform_duration offset (target_offset[0] + 3*thought_button_transform_strength, target_offset[0] + 0)
            repeat
transform thought_button_normal_transform(target_offset=(0,0), target_zoom=1.0, start_delay=0.0):
    anchor (0.5, 0.5) transform_anchor True
    pause start_delay
    ease 0.2 offset target_offset zoom target_zoom
transform thought_button_hide_transform:
    linear 0.3 alpha 0 zoom 0

image thought_bubble_idle:
    "gui/thought/thought_bubble_default.png"
    alpha 0.8
image thought_bubble_choice:
    "gui/thought/thought_bubble_default.png"
    matrixcolor TintMatrix("#F9CFA8")
    alpha 0.8
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

screen thought(items, expanded=[], block_progress=True, choice_mode=False):
    default hovered_index = None
    fixed:
        if block_progress and expanded is not None and len(expanded) == len(items):
            add "flash_white"
        align (0.5, 0.1)
        for i in range(len(items)):
            button:
                if choice_mode:
                    pos (600 + i*700, 150)
                else:
                    pos (800 + i*300, 150)
                if choice_mode:
                    background "thought_bubble_choice"
                else:
                    background "thought_bubble_idle"
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
                elif i in expanded or choice_mode:
                    if choice_mode:
                        at thought_button_normal_transform
                    elif i == 0:
                        at thought_button_normal_transform(target_offset=(-200, 0))
                    elif i == 1:
                        at thought_button_normal_transform(target_offset=(200, 0))
                    text items[i]:
                        text_align 0.5
                        align (0.5, 0.5)
                        color "#000"
                        size 32
                else:
                    if i == hovered_index:
                        at thought_button_shiver_transform(target_zoom=0.3)
                    else:
                        at thought_button_shiver_transform(target_zoom=0.2)
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
    if expanded is None and not choice_mode:
        if not block_progress:
            timer 0.3 action Hide("thought")
        else:
            timer 0.3 action Return()
    elif len(expanded) == len(items) and not choice_mode:
        ## play juice SFX for finishing minigame
        #timer 0.1 action Play('juicy_sfx.ogg')
        timer 2.0 action Show("thought", None, items, expanded=None, block_progress=block_progress)
        if block_progress:
            key config.keymap['dismiss'] action Show("thought", None, items, expanded=None, block_progress=block_progress)
