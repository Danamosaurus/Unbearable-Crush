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
    choice_box_style = 'default'
    choice_button_animation_suggestion_transform_duration = 0.3
    choice_button_animation_suggestion_transform_strength = 0.5
transform choice_button_animation_default_transform(start_delay=0.0):
    xoffset -1000 alpha 0
    pause start_delay
    easein 0.6 xoffset 0 alpha 1
transform choice_button_animation_hide_default_transform(start_delay=0.0, target_xoffset=0):
    pause start_delay
    linear 0.3 xoffset target_xoffset alpha 0
transform choice_button_animation_suggestion_transform(start_delay=0.0):
    xoffset 0 alpha 0 anchor (0.5, 0.5) xalign 0.5 ypos 200 transform_anchor True
    pause start_delay
    parallel:
        easein 0.3 alpha 1
    parallel:
        block:
            ease choice_button_animation_suggestion_transform_duration offset (-5*choice_button_animation_suggestion_transform_strength, -5*choice_button_animation_suggestion_transform_strength)
            ease choice_button_animation_suggestion_transform_duration offset (5*choice_button_animation_suggestion_transform_strength, 5*choice_button_animation_suggestion_transform_strength)
            ease choice_button_animation_suggestion_transform_duration offset (0, -3*choice_button_animation_suggestion_transform_strength)
            ease choice_button_animation_suggestion_transform_duration offset (-3*choice_button_animation_suggestion_transform_strength, 0)
            ease choice_button_animation_suggestion_transform_duration offset (5*choice_button_animation_suggestion_transform_strength, -5*choice_button_animation_suggestion_transform_strength)
            ease choice_button_animation_suggestion_transform_duration offset (-5*choice_button_animation_suggestion_transform_strength, 5*choice_button_animation_suggestion_transform_strength)
            ease choice_button_animation_suggestion_transform_duration offset (3*choice_button_animation_suggestion_transform_strength, 0)
            repeat
transform choice_button_animation_hide_suggestion_transform(start_delay=0.0, target_offset=(0,0), target_zoom=1.0):
    pause start_delay
    parallel:
        linear 0.3 alpha 0
    parallel:
        ease 0.3 offset target_offset zoom target_zoom

screen choice(items, tohide=None):
    style_prefix "choice"

    vbox:
        style "choice_vbox"
        for i in range(len(items)):
            button:
                style "choice_bar_style"
                text items[i].caption:
                    style "choice_bar_text"
                if choice_box_style == 'suggestion':
                    if tohide is None:
                        at choice_button_animation_suggestion_transform((i-1) * 0.1)
                    elif i == tohide:
                        at choice_button_animation_hide_suggestion_transform(0, (0, -250 - 100*i), 0.3)
                    else:
                        at choice_button_animation_hide_suggestion_transform((i-1) * 0.05)
                else:
                    if tohide is None:
                        at choice_button_animation_default_transform((i-1) * 0.1)
                    elif i == tohide:
                        at choice_button_animation_hide_default_transform(0, 1000)
                    else:
                        at choice_button_animation_hide_default_transform((i-1) * 0.05)
                if tohide is None:
                    action Show("choice", None, items, tohide=i)
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
