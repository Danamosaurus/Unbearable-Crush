### RenPy variables. Do not mess with.

define gui.history_allow_tags = set()

### Animations

transform history_screen_animation:

    on show, replace:

        yoffset 100
        alpha 0.0

        parallel:
            ease 0.5 alpha 1.0

        parallel:
            easein 0.5 yoffset 0.0

    on hide:

        alpha 1.0

        parallel:
            ease 0.5 alpha 0.0

        parallel:
            easein 0.5 yoffset 100.0

### Styles

style history_screen_name:

    font "fonts/Inter-Regular-slnt=0.ttf"
    size 60
    bold True
    color "#fff"

    outlines [ (absolute(3), "#e13b86", absolute(0), absolute(0)) ]


style history_screen_dialogue:

    line_spacing 20

    font "fonts/Inter-Regular-slnt=0.ttf"
    color "#000"
    size 30

    outlines []


## History screen ##############################################################
##
## This is a screen that displays the dialogue history to the player. While
## there isn't anything special about this screen, it does have to access the
## dialogue history stored in _history_list.
##
## https://www.renpy.org/doc/html/history.html

screen history():

    tag menu

    modal True

    ## Avoid predicting this screen, as it can be very large.
    predict False

    frame:

        pos (0,0)
        xysize (1,1)

        margin (0,0)
        padding (0,0)

        background "gui/history/background.png"

        at history_screen_animation

        vpgrid:

            id "history_vpgrid"

            pos (370, 160)
            xysize (1164, 748)

            child_size (1164, 250)

            xinitial 0
            yinitial 0

            scrollbars None

            cols 1
            rows len( _history_list )

            mousewheel True
            draggable True
            edgescroll None
            arrowkeys True
            pagekeys True

            for h in _history_list:

                use history_entry( h.who, h.what )

        ### Scroll bar
        # Only show the scrollbar when there are more than 4 entries in the logbook.
        if len( _history_list ) > 3:

            # An invisible bar with a thumb.
            vbar:
                value YScrollValue("history_vpgrid")

                pos (1555, 161)
                xysize (39, 746)

                base_bar "gui/history/scroll_bar.png"

                thumb "gui/history/scroll_thumb.png"
                thumb_offset 20

                top_gutter 19
                bottom_gutter 15

        ### Back button
        imagebutton:

            pos (286,916)
            xysize (302, 74)

            idle "gui/save_load/back_idle.png"
            hover "gui/save_load/back_hover.png"

            action Hide("history")

    # Key input processing.
    key "game_menu_alt" action Hide("history")


screen history_entry( who, what ):

    frame:

        xpadding 10
        xsize 1144

        yminimum 250

        background None

        vbox:

            if not who == None:

                text who:

                    style "history_screen_name"

            text what:

                style "history_screen_dialogue"
