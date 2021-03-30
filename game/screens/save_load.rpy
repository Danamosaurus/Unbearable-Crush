### RenPy variables. DO NOT DELETE

define config.thumbnail_width = 374
define config.thumbnail_height = 210

### Auxiliar variables

define SAVE_SCREEN = 0
define LOAD_SCREEN = 1

define load_save_screen_slot_pos = [(0,0), (0, 312), (428, 0), (428, 312), (866, 0), (866, 312), (1295, 0), (1295, 312)]
define load_save_screen_number_width = [26, 34, 36, 38, 35, 37, 34, 36, 36]

### Animations

transform save_load_screen_animation:

    on show, replace:

        yoffset 100
        alpha 0.0

        parallel:
            ease 0.5 alpha 1.0

        parallel:
            easein 0.5 yoffset 0.0
    #
    # on hide:
    #
    #     alpha 1.0
    #
    #     parallel:
    #         ease 0.5 alpha 0.0
    #
    #     parallel:
    #         easein 0.5 yoffset 100.0

## Load and Save screens #######################################################
##
## These screens are responsible for letting the player save the game and load
## it again. Since they share nearly everything in common, both are implemented
## in terms of a third screen, file_slots.
##
## https://www.renpy.org/doc/html/screen_special.html#save https://
## www.renpy.org/doc/html/screen_special.html#load

screen save():

    tag menu

    use file_slots( SAVE_SCREEN )


screen load():

    tag menu

    use file_slots( LOAD_SCREEN )


screen file_slots( load_or_save ):

    frame:

        pos (61, 95)
        xysize (1803, 987)

        margin (0,0)
        padding (0,0)

        background "gui/save_load/background.png"

        at save_load_screen_animation

        ### Screen title

        if load_or_save == SAVE_SCREEN:

            add "gui/save_load/save_title.png":
                pos (33, -4)

        else:

            add "gui/save_load/load_title.png":
                pos (35, -4)

        ### File slots tabs
        fixed:

            pos(50, 95)

            for i in range (1, 9):

                if FileLoadable(i) or load_or_save == SAVE_SCREEN:

                    button:

                        pos load_save_screen_slot_pos[ i - 1 ]
                        xysize (406, 306)

                        idle_background "gui/save_load/slot" + str(i) + "_idle.png"
                        hover_background "gui/save_load/slot" + str(i) + "_hover.png"

                        # Screenshot
                        add FileScreenshot(i, empty="gui/save_load/no_data_image.png"):
                            pos(10, 22)

                        # Time info.
                        text FileTime(i, format=_("%a, %b %d %y, %H:%M"), empty=_("")):

                            align (0.5, 0.975)

                            text_align 0.5

                            size 23

                            color "#fff"

                            outlines [ (absolute(3), "#e13b86", absolute(0), absolute(0)) ]


                        action FileAction(i)

                        key "save_delete" action FileDelete(i)

        ### Back button
        imagebutton:

            pos (3,744)
            xysize (302, 74)

            idle "gui/save_load/back_idle.png"
            hover "gui/save_load/back_hover.png"

            action Return()


        ## Save or load screen buttons.
        if load_or_save == SAVE_SCREEN:

            # Load screen button
            imagebutton:

                pos (868, 744)
                xysize (112, 45)

                idle "gui/save_load/load_idle.png"
                hover "gui/save_load/load_hover.png"
                selected "gui/save_load/load_selected.png"

                action ShowMenu("load")

        elif not main_menu:

            # Save screen button
            imagebutton:

                pos (866, 744)
                xysize (115, 45)

                idle "gui/save_load/save_idle.png"
                hover "gui/save_load/save_hover.png"
                selected "gui/save_load/save_selected.png"

                action ShowMenu("save")

        ## Q button
        imagebutton:

            pos (1016 , 744)
            xysize (41, 47)

            idle "gui/save_load/q_idle.png"
            hover "gui/save_load/q_hover.png"
            selected_idle "gui/save_load/q_selected.png"
            selected_hover "gui/save_load/q_selected.png"

            action FilePage("quick")

        ## A button
        imagebutton:

            pos (1091, 744)
            xysize (42, 44)

            idle "gui/save_load/a_idle.png"
            hover "gui/save_load/a_hover.png"
            selected_idle "gui/save_load/a_selected.png"
            selected_hover "gui/save_load/a_selected.png"

            action FilePage("auto")

        ## Numbered pages
        for i in range(1, 10):

            imagebutton:

                pos (1167 + 69 * (i-1) , 744)
                xysize (load_save_screen_number_width[i-1], 44)

                idle "gui/save_load/" + str(i) + "_idle.png"
                hover "gui/save_load/" + str(i) + "_hover.png"
                selected_idle "gui/save_load/" + str(i) + "_selected.png"
                selected_hover "gui/save_load/" + str(i) + "_selected.png"

                action FilePage(i)

    ### Key input
    key "game_menu_alt" action Return()
