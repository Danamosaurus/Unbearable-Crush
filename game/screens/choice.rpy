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

screen choice(items):
    style_prefix "choice"

    vbox:

        style "choice_vbox"

        for i in items:

            button:

                style "choice_bar_style"

                text i.caption:

                    style "choice_bar_text"

                action i.action



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
