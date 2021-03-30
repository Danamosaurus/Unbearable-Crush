### Styles

style textbox_day_style:

    font "fonts/Inter-Regular-slnt=0.ttf"
    size 60
    bold True
    color "#fff"

    outlines [ (absolute(3), "#e13b86", absolute(0), absolute(0)) ]


## Say screen ##################################################################
##
## The say screen is used to display dialogue to the player. It takes two
## parameters, who and what, which are the name of the speaking character and
## the text to be displayed, respectively. (The who parameter can be None if no
## name is given.)
##
## This screen must create a text displayable with id "what", as Ren'Py uses
## this to manage text display. It can also create displayables with id "who"
## and id "window" to apply style properties.
##
## https://www.renpy.org/doc/html/screen_special.html#say

screen say(who, what):

    ### Day at top
    if not game_day == "":

        frame:

            pos (0,39)
            xysize (378, 75)

            margin (0,0)
            padding (0,0)

            background "gui/textbox/day_bar.png"

            text "[game_day]":

                pos (15, -8)

                style "textbox_day_style"

    ### Textbox
    frame:

        pos (283, 739)
        xysize (1405, 341)

        margin (0,0)
        padding (0,0)

        background "gui/textbox/textbox.png"


    window:
        id "window"

        if who is not None:

            window:

                id "namebox"

                text who:

                    pos (410, 713)

                    id "who"

                    font "fonts/Inter-Regular-slnt=0.ttf"
                    size 60
                    bold True
                    color "#fff"

                    outlines [ (absolute(3), "#e13b86", absolute(0), absolute(0)) ]

        text what id "what":

            xysize (1203, 400)

            xpos 400
            ypos 829

            line_spacing 20

            font "fonts/Inter-Regular-slnt=0.ttf"

            color "#000"

            outlines []


        ## If there's a side image, display it above the text. Do not display on the
        ## phone variant - there's no room.
        if not renpy.variant("small"):
            if not who in hide_sides:
                add SideImage() xalign -.1 yalign .5 yanchor 0
            #elif who == 'Kanna':
            #    add SideImage() xalign -0.1 yalign .5 yanchor 0
            #elif who == 'Kyousuke':
            #    add SideImage() xalign -0.1 yalign .5 yanchor 0
            #elif who == 'Maya':
            #    add SideImage() xalign -0.1 yalign .5 yanchor 0
            #elif who == 'Charlotte':
            #    add SideImage() xalign -0.1 yalign .5 yanchor 0
            #elif who == 'Ringo':
            #    add SideImage() xalign -0.1 yalign .5 yanchor 0
            #elif who == 'Youko':
            #    add SideImage() xalign -0.1 yalign .5 yanchor 0

    ### Icons
    fixed:

        pos(1190, 988)

        ## Rollback button
        imagebutton:

            pos (0,51)
            xysize (37, 39)

            idle "gui/textbox/rollback_idle.png"
            hover "gui/textbox/rollback_hover.png"
            selected_idle "gui/textbox/rollback_selected.png"
            selected_hover "gui/textbox/rollback_selected.png"

            action Rollback()

        ## Quick save button
        imagebutton:

            pos (74, 40)
            xysize (42,42)

            idle "gui/textbox/qs_idle.png"
            hover "gui/textbox/qs_hover.png"
            selected_idle "gui/textbox/qs_selected.png"
            selected_hover "gui/textbox/qs_selected.png"

            action QuickSave()

        ## Quick load button
        imagebutton:

            pos (155, 30)
            xysize (43, 43)

            idle "gui/textbox/square_idle.png"
            hover "gui/textbox/square_hover.png"
            selected_idle "gui/textbox/square_selected.png"
            selected_hover "gui/textbox/square_selected.png"

            action QuickLoad()

        ## Skip button
        imagebutton:

            pos (232, 21)
            xysize (42, 41)

            idle "gui/textbox/skip_idle.png"
            hover "gui/textbox/skip_hover.png"
            selected_idle "gui/textbox/skip_selected.png"
            selected_hover "gui/textbox/skip_selected.png"

            action Skip() alternate Skip(fast=True, confirm=True)

        ## History button
        imagebutton:

            pos (312, 10)
            xysize (39, 40)

            idle "gui/textbox/history_idle.png"
            hover "gui/textbox/history_hover.png"
            selected_idle "gui/textbox/history_selected.png"
            selected_hover "gui/textbox/history_selected.png"

            action Show('history')

        ## Heart Button
        imagebutton:

            pos (389, 0)
            xysize (39, 39)

            idle "gui/textbox/heart_idle.png"
            hover "gui/textbox/heart_hover.png"
            selected_idle "gui/textbox/heart_hover.png"
            selected_hover "gui/textbox/heart_hover.png"
            action [ FileTakeScreenshot(), ShowMenu("circle_menu") ]

