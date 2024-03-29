### Styles
init python:
    import math
    Rin_sprite_transform_distance = 30.0
    Rin_sprite_transform_strength = 0.6
    Rin_sprite_transform_current_going_up = True
    Rin_sprite_transform_current_offset = 0.0
    def Rin_sprite_transform_function(trans, st, at):
        global Rin_sprite_transform_strength, Rin_sprite_transform_current_going_up, Rin_sprite_transform_distance, Rin_sprite_transform_current_offset
        trans.yoffset = Rin_sprite_transform_current_offset
        if Rin_sprite_transform_current_going_up:
            trans.yoffset += Rin_sprite_transform_strength * math.sqrt(abs(1.0 - trans.yoffset / Rin_sprite_transform_distance))
            if abs(Rin_sprite_transform_distance - trans.yoffset) < 0.1:
                Rin_sprite_transform_current_going_up = False
        else:
            trans.yoffset -= Rin_sprite_transform_strength * math.sqrt(abs(trans.yoffset / Rin_sprite_transform_distance))
            if abs(trans.yoffset) < 0.1:
                Rin_sprite_transform_current_going_up = True
        Rin_sprite_transform_current_offset = trans.yoffset
        return 0

transform Rin_sprite_transform:
    function Rin_sprite_transform_function
    repeat
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
init python:
    def say_window1_transform(trans, st, at):
        global say_window1_show_transform

        if not "say_window1_show_transform" in globals():
            say_window1_show_transform = False

        trans.alpha = 0.8
        trans.anchor = (0.5, 0.5)
        trans.transform_anchor = True
        if say_window1_show_transform == False:
            trans.yoffset = 320
            trans.rotate = -3
            say_window1_show_transform = True

        if say_window1_show_transform == True:
            if st > 0.3:
                trans.yoffset = 0
                trans.rotate = 0
                return None
            else:
                trans.yoffset -= trans.yoffset * st
                if trans.rotate is not None:
                    trans.rotate -= trans.rotate * st
                return 0
    def say_window2_transform(trans, st, at):
        global say_window2_show_transform

        if not "say_window2_show_transform" in globals():
            say_window2_show_transform = False

        if say_window2_show_transform == False:
            trans.yoffset = 500
            say_window2_show_transform = True

        if st < 0.1:
            return 0
        if say_window2_show_transform == True:
            if st > 0.4:
                trans.yoffset = 0
                return None
            else:
                trans.yoffset -= trans.yoffset * (st - 0.1)
                return 0
    def say_window1_transform_reset(trans, st, at):
        global say_window1_show_transform
        say_window1_show_transform = False
    def say_window2_transform_reset(trans, st, at):
        global say_window2_show_transform
        say_window2_show_transform = False

transform say_window1_animation:
    on show:
        function say_window1_transform
    on hide:
        pause 0.1
        easeout 0.3 yoffset 320 rotate -3
        function say_window1_transform_reset
transform say_window2_animation:
    on show:
        function say_window2_transform
    on hide:
        easeout 0.3 yoffset 500
        function say_window2_transform_reset

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

    ### Textbox background
    frame at say_window1_animation:

        pos (283+702, 739+170)
        xysize (1405, 341)

        margin (0,0)
        padding (0,0)

        background "gui/textbox/textbox1.png"

    ### Textbox
    fixed at say_window2_animation:
        frame:

            pos (283, 739)
            xysize (1405, 341)

            margin (0,0)
            padding (0,0)

            background "gui/textbox/textbox2.png"

        window:
            id "window"

            if who is not None:

                window:

                    id "namebox"

                    text who:

                        pos (510, 713)

                        id "who"

                        font "fonts/Inter-Regular-slnt=0.ttf"
                        size 60
                        bold True
                        color "#fff"

                        outlines [ (absolute(3), "#e13b86", absolute(0), absolute(0)) ]

            text what id "what":

                xysize (1050, 400)

                xpos 500
                ypos 829

                line_spacing 20

                font "fonts/Rubik-VariableFont_wght.ttf"

                color "#000"

                outlines []


            ## If there's a side image, display it above the text. Do not display on the
            ## phone variant - there's no room.
            if not renpy.variant("small"):
                #Define positioning of side images here for each character
                #If 'who' is speaking, and is NOT currently listed in hide_sides, add their side image at the defined position.
                if who == 'Kanna' and not who in hide_sides:
                    add SideImage() xalign -0.1 yalign .5 yanchor 0
                elif who == 'Kyousuke' and not who in hide_sides:
                    add SideImage() xalign -0.1 yalign .5 yanchor 0
                elif who == 'Maya' and not who in hide_sides:
                    add SideImage() xalign -0.1 yalign .5 yanchor 0
                elif who == 'Charlotte' and not who in hide_sides:
                    add SideImage() xalign -0.1 yalign .5 yanchor 0
                elif who == 'Ringo' and not who in hide_sides:
                    add SideImage() xalign 0.0 yalign .5 yanchor 0 at Rin_sprite_transform
                elif who == 'Youko' and not who in hide_sides:
                    add SideImage() xalign -0.1 yalign .5 yanchor 0
                #If the speaking character doesn't have a defined position above, use this default position
                elif not who in hide_sides:
                    add SideImage() xalign -.1 yalign .5 yanchor 0

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
