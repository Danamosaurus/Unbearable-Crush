### Styles

style choice_vbox:
    xalign 0.5
    ypos 405
    yanchor 0.5

    spacing gui.choice_spacing

style choice_bar_style:

    background Frame("gui/choice/choice_bar.png", 35, 30, 19, 84)

    padding (30, 30, 19, 40)

    xsize 1223
    yminimum 120

style choice_bar_text:

    xfill True
    yfill True

    text_align 0.5

    align (0.5, 0.8 )

    color "#000"

    idle_color "#000"
    idle_outlines [ (absolute(2), "#fff", absolute(0), absolute(0)) ]

    hover_color "#fff"
    hover_outlines [ (absolute(2), "#d06e99", absolute(0), absolute(0)) ]

    insensitive_color "#000"
    insensitive_outlines [ (absolute(2), "#fff", absolute(0), absolute(0)) ]

    font "fonts/Inter-Regular-slnt=0.ttf"


## Choice screen ###############################################################
##
## This screen is used to display the in-game choices presented by the menu
## statement. The one parameter, items, is a list of objects, each with caption
## and action fields.
##
## https://www.renpy.org/doc/html/screen_special.html#choice
init python:
    choice_button_animation_suggestion_transform_duration = 0.3
    choice_button_animation_suggestion_transform_strength = 0.5
transform choice_button_animation_default_transform(start_delay=0.0):
    xoffset -1000 alpha 0
    pause start_delay
    easein 0.6 xoffset 0 alpha 1
transform choice_button_animation_hide_default_transform(start_delay=0.0, target_xoffset=0):
    pause start_delay
    linear 0.3 xoffset target_xoffset alpha 0

transform choice_button_animation_hide_suggestion_transform(start_delay=0.0, target_pos=(0,0), target_zoom=1.0, target_alpha=0):
    pause start_delay
    parallel:
        linear 0.3 alpha target_alpha
    parallel:
        ease 0.3 pos target_pos zoom target_zoom offset (0, 0)
image thought_bubble_choice_hover:
    "gui/thought/thought_bubble_default.png"
    # matrixcolor TintMatrix("#F9CFA8")
    alpha 1.0
screen choice(items, tohide=None, choice_type="default", image_to_show="Rin normal", original_thought=None, state=None):
    if choice_type == "thought":
        if original_thought is not None:
            if state == "done":
                use thought(original_thought[0:1], choice_mode=True)
            else:
                use thought(original_thought, choice_mode=True)
        fixed:
            if state == "done":
                add "flash_white"
            window:
                add image_to_show
                align (0.5, 1.3)
            for i in range(len(items)):
                button:
                    pos (540 + i*800, 900)
                    background "thought_bubble_idle"
                    xsize 480
                    ysize 270
                    padding (80, 40)
                    text items[i].caption:
                        text_align 0.5
                        align (0.5, 0.5)
                        color "#000"
                        size 32
                    if tohide is None:
                        at thought_button_shiver_transform(start_delay=i*0.1)
                        hover_background "thought_bubble_choice_hover"
                    elif i == tohide:
                        at choice_button_animation_hide_suggestion_transform(target_pos=(1300, 150), target_alpha=1)
                    else:
                        at choice_button_animation_hide_suggestion_transform(target_pos=(540 + i*800, 900))
                    if tohide is None:
                        action Show("choice", None, items, tohide=i, choice_type=choice_type, image_to_show=image_to_show, original_thought=original_thought)
                    else:
                        action None
        if tohide is not None:
            if state is None:
                timer 0.3 action Show("choice", None, items, tohide=tohide, choice_type=choice_type, image_to_show=image_to_show, original_thought=original_thought, state="done")
            elif state == "done":
                timer 2.0 action items[tohide].action
                key config.keymap['dismiss'] action items[tohide].action
    else:
        style_prefix "choice"
        vbox:
            style "choice_vbox"
            for i in range(len(items)):
                button:
                    style "choice_bar_style"
                    text items[i].caption:
                        style "choice_bar_text"
                    if tohide is None:
                        at choice_button_animation_default_transform((i-1) * 0.1)
                    elif i == tohide:
                        at choice_button_animation_hide_default_transform(0, 1000)
                    else:
                        at choice_button_animation_hide_default_transform((i-1) * 0.05)
                    if tohide is None:
                        action Show("choice", None, items, tohide=i, choice_type=choice_type, image_to_show=image_to_show, original_thought=original_thought)
                    else:
                        action None
        if tohide is not None:
            timer 0.5 action items[tohide].action

## When this is true, menu captions will be spoken by the narrator. When false,
## menu captions will be displayed as empty buttons.
define config.narrator_menu = True

style choice_vbox is vbox
style choice_button is button
style choice_button_text is button_text

style choice_button is default:
    properties gui.button_properties("choice_button")

style choice_button_text is default:
    properties gui.button_text_properties("choice_button")
