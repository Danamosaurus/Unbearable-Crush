### Messages

define DELETE_SAVE = _("Are you sure you want to delete this save?")
define OVERWRITE_SAVE = _("Are you sure you want to overwrite your save?")
define LOADING = _("Loading will lose unsaved progress.\nAre you sure you want to do this?")
define QUIT = _("Are you sure you want to quit?")
define MAIN_MENU = _("Are you sure you want to return to the main menu?\nThis will lose unsaved progress.")

### Animations

transform confirm_screen_flower_slide_animation:

    xoffset 0

    linear 60.0 xoffset -1920

    repeat

### Styles

style confirm_screen_message_style:

    font "fonts/Inter-Regular-slnt=0.ttf"
    size 55
    bold True
    color "#fff"

    text_align 0.5

    line_spacing -12

    outlines [ (absolute(3), "#e26da0", absolute(0), absolute(0)) ]

style confirm_screen_message_shadow_style:

    font "fonts/Inter-Regular-slnt=0.ttf"
    size 55
    bold True
    color "#0000004D"

    text_align 0.5

    line_spacing -12

    outlines [ (absolute(3), "#0000004D", 7, 8) ]

## Confirm screen ##############################################################
##
## The confirm screen is called when Ren'Py wants to ask the player a yes or no
## question.
##
## https://www.renpy.org/doc/html/screen_special.html#confirm

screen confirm(message, yes_action, no_action):

    ## Ensure other screens do not get input while this screen is displayed.
    modal True

    zorder 200

    frame:

        pos (0,0)
        xysize (1920, 1080)

        margin (0,0)
        padding (0,0)

        background None

        ### Flower slide
        fixed:

            pos(0,0)

            at confirm_screen_flower_slide_animation

            add "gui/confirm/flower_slide.png":
                pos(0,0)

            add "gui/confirm/flower_slide.png":
                pos(1920,0)

        ### Box
        add "gui/confirm/background.png":
            pos(0,0)

        ### Title
        if message == DELETE_SAVE:

            add "gui/confirm/delete_title.png":
                pos (625, 460)

        elif message == OVERWRITE_SAVE:

            add "gui/confirm/overwrite_title.png":
                pos (578, 460)

        elif message == LOADING:

            add "gui/confirm/load_title.png":
                pos (648, 410)

        elif message == QUIT:

            add "gui/confirm/quit_title.png":
                pos (751, 460)

        elif message == MAIN_MENU:

            add "gui/confirm/return_menu_title.png":
                pos (609, 460)

        else:

            ### Message
            fixed:

                pos (609, 403)
                xysize (707, 200)

                # Message shadow
                text message:
                    xysize (707, 200)

                    style "confirm_screen_message_shadow_style"

                # Message
                text message:
                    xysize (707, 200)

                    style "confirm_screen_message_style"

        ### Buttons

        ## Yes button
        imagebutton:

            pos (761, 640)
            xysize (107, 53)

            idle "gui/confirm/yes_idle.png"
            hover "gui/confirm/yes_hover.png"

            action yes_action

        ## No button
        imagebutton:

            pos (1083, 640)
            xysize (81, 53)

            idle "gui/confirm/no_idle.png"
            hover "gui/confirm/no_hover.png"

            action no_action
