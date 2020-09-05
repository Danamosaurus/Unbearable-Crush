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

    on hide:

        alpha 1.0

        parallel:
            ease 0.5 alpha 0.0

        parallel:
            easein 0.5 yoffset 100.0

    on show:

        yoffset 100
        alpha 0.0

        parallel:
            ease 0.5 alpha 1.0

        parallel:
            easein 0.5 yoffset 0.0

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

                        #
                        #                         text FileTime(slot, format=_("{#file_time}%A, %B %d %Y, %H:%M"), empty=_("empty slot")):
                        #                             style "slot_time_text"
                        #
                        #                         text FileSaveName(slot):
                        #                             style "slot_name_text"
                        #
                        #                         key "save_delete" action FileDelete(slot)

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


#     default page_name_value = FilePageNameInputValue(pattern=_("Page {}"), auto=_("Automatic saves"), quick=_("Quick saves"))
#
#     use game_menu(title):
#
#         fixed:
#
#             ## This ensures the input will get the enter event before any of the
#             ## buttons do.
#             order_reverse True
#
#             ## The page name, which can be edited by clicking on a button.
#             button:
#                 style "page_label"
#
#                 key_events True
#                 xalign 0.5
#                 action page_name_value.Toggle()
#
#                 input:
#                     style "page_label_text"
#                     value page_name_value
#
#             ## The grid of file slots.
#             grid gui.file_slot_cols gui.file_slot_rows:
#                 style_prefix "slot"
#
#                 xalign 0.5
#                 yalign 0.5
#
#                 spacing gui.slot_spacing
#
#                 for i in range(gui.file_slot_cols * gui.file_slot_rows):
#
#                     $ slot = i + 1
#
#                     button:
#                         action FileAction(slot)
#
#                         has vbox
#
#                         add FileScreenshot(slot) xalign 0.5
#
#                         text FileTime(slot, format=_("{#file_time}%A, %B %d %Y, %H:%M"), empty=_("empty slot")):
#                             style "slot_time_text"
#
#                         text FileSaveName(slot):
#                             style "slot_name_text"
#
#                         key "save_delete" action FileDelete(slot)
#
#             ## Buttons to access other pages.
#             hbox:
#                 style_prefix "page"
#
#                 xalign 0.5
#                 yalign 1.0
#
#                 spacing gui.page_spacing
#
#                 textbutton _("<") action FilePagePrevious()
#
#                 if config.has_autosave:
#                     textbutton _("{#auto_page}A") action FilePage("auto")
#
#                 if config.has_quicksave:
#                     textbutton _("{#quick_page}Q") action FilePage("quick")
#
#                 ## range(1, 10) gives the numbers from 1 to 9.
#                 for page in range(1, 10):
#                     textbutton "[page]" action FilePage(page)
#
#                 textbutton _(">") action FilePageNext()
#
#
# style page_label is gui_label
# style page_label_text is gui_label_text
# style page_button is gui_button
# style page_button_text is gui_button_text
#
# style slot_button is gui_button
# style slot_button_text is gui_button_text
# style slot_time_text is slot_button_text
# style slot_name_text is slot_button_text
#
# style page_label:
#     xpadding 75
#     ypadding 5
#
# style page_label_text:
#     text_align 0.5
#     layout "subtitle"
#     hover_color gui.hover_color
#
# style page_button:
#     properties gui.button_properties("page_button")
#
# style page_button_text:
#     properties gui.button_text_properties("page_button")
#
# style slot_button:
#     properties gui.button_properties("slot_button")
#
# style slot_button_text:
#     properties gui.button_text_properties("slot_button")
