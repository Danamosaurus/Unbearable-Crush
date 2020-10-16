##FLOWER MENU

### Auxiliar functions

init python:
    import math
    right_click_pos = (0, 0)
    tap_mode = False

    flower_menu_actions = [
        ('save', ShowMenu('save')),
        ('load', ShowMenu('load')),
        ('pref', ShowMenu('preferences')),
        ('menu', MainMenu()),
        ('quit', Quit(confirm=not main_menu)),

        ### DEBUG BUTTONS
        ('sprite', Show('dynamicspritespreview')),
    ]

    def polygon_point_offset(ind, distance=75, points=5):
        if points == 1:
            ind += 0.5
        elif points > 1:
            ind += (points - 1) * 0.5
        ang = -2.0 * math.pi / points
        x = math.sin(ang * ind) * distance
        y = math.cos(ang * ind) * distance
        return (x, y)

    class HoverFlowerButton:
        def __call__(self):
            global right_click_pos, tap_mode
            dim = (115, 110)
            right_click_pos = (config.screen_width - dim[0], dim[1])
            tap_mode = False

    class TapFlowerButton:
        def __call__(self):
            global right_click_pos, tap_mode
            dim = (115, 110)
            right_click_pos = (config.screen_width - dim[0], dim[1])
            tap_mode = True

    class RightClickFlower:
        def __call__(self):
            global right_click_pos, tap_mode
            dim = (115, 110)
            right_click_pos = list(renpy.get_mouse_pos())
            if config.screen_width - right_click_pos[0] < dim[0]:
                right_click_pos[0] = config.screen_width - dim[0]
            elif right_click_pos[0] < dim[0]:
                right_click_pos[0] = dim[0]
            if right_click_pos[1] < dim[1]:
                right_click_pos[1] = dim[1]
            elif config.screen_height - right_click_pos[1] < dim[1]:
                right_click_pos[1] = config.screen_height - dim[1]
            right_click_pos = tuple(right_click_pos)
            tap_mode = False


### Animations

transform flower_menu_transform:

    anchor (0.5, 0.5)

    on show:
        zoom 0.0
        easein_cubic 0.15 zoom 1.02
        ease 0.05 zoom 1.0
    on hide:
        easein 0.2 zoom 0.0

transform flower_button_transform:
    on idle:
        linear 0.2 alpha 0.5
    on hover:
        linear 0.2 alpha 1

transform flower_moon_transform:
    anchor (0.5, 0.5)
    on show:
        parallel:
            rotate 0
            linear 5.0 rotate 180
            repeat
        parallel:
            zoom 0.0
            easein 0.2 zoom 1.02
            ease 0.3 zoom 1.0
    on hide:
        easein 0.2 zoom 0.0

### Transparent button used to call the flower menu

screen flower_menu_button():

    key "mouseup_3" action [
            # RightClickFlower(),
            # Hide('flower_menu_button'),
            Show('circle_menu', transition=dissolve ),
    ]
#
#
# screen flower_menu_moon():
#     if quick_menu:
#         frame at flower_moon_transform:
#             background None
#             padding (0, 0)
#             margin (0, 0)
#             pos right_click_pos
#
#             add im.FactorScale('gui/sagi/roundbutton-hover.png', 0.15):
#                 align (0.5, 0.5)
#                 xoffset -25
#             add im.FactorScale('gui/sagi/roundbutton-hover.png', 0.15):
#                 align (0.5, 0.5)
#                 xoffset 25

# screen flower_menu():
#     if quick_menu:
#         button:
#             background None
#             padding (0, 0)
#             margin (0, 0)
#             xysize (1.0, 1.0)
#             key "mouseup_3" action [
#                 Hide('flower_menu'),
#                 Show('flower_menu_button'),
#                 Hide('flower_menu_moon'),
#             ]
#             action [
#                 Hide('flower_menu'),
#                 Show('flower_menu_button'),
#                 Hide('flower_menu_moon'),
#             ]
#
#         button at flower_menu_transform:
#             background None
#             padding (0, 0)
#             margin (0, 0)
#             xysize (800, 800)
#             pos right_click_pos
#             #THIS IS THE SMALL CIRCLE IN THE MIDDLE OF THE MENU FOR MOON TO ORBIT
#             #add im.FactorScale('gui/sagi/roundbutton-hover.png', 0.4):
#                 #align (0.5, 0.5)
#             for i in range(0, len(flower_menu_actions)):
#                 frame:
#                     background None
#                     padding (0, 0)
#                     margin (0, 0)
#                     offset polygon_point_offset(i, points=len(flower_menu_actions))
#                     imagebutton:
#                         align (0.5, 0.5)
#                         idle 'gui/sagi/roundbutton-idle.png'
#                         hover 'gui/sagi/roundbutton-hover.png'
#                         action [
#                             Hide('flower_menu'),
#                             Show('flower_menu_button'),
#                             Hide('flower_menu_moon'),
#                             flower_menu_actions[i][1],
#                         ]
#                     text flower_menu_actions[i][0]:
#                         align (0.5, 0.5)
#                         yoffset 0
#                         text_align 0.5
#                         size 15
#                         color '#000'
#             action []
#             if not tap_mode:
#                 mousearea:
#                     unhovered [
#                         Hide('flower_menu'),
#                         Show('flower_menu_button'),
#                         Hide('flower_menu_moon'),
#                     ]

screen circle_menu:

    modal True

    tag menu

    frame:

        anchor (0.5, 0.5)
        align (0.5, 0.5)
        xysize (1.0, 1.0)

        margin (0,0)
        padding (0,0)

        background None

        at transform:

            on show:

                alpha 0.0
                zoom 0.0

                parallel:
                    ease 0.5 alpha 1.0

                parallel:
                    ease 0.5 zoom 1.0


        ### Sliding background
        fixed:

            pos(0,0)

            at confirm_screen_flower_slide_animation

            add "gui/circle_menu/background.png":
                pos(0,0)

            add "gui/circle_menu/background.png":
                pos(1920,0)

        ### Invisible button that closes this screen.
        button:

            xysize (1.0, 1.0)

            key "mouseup_3" action [ Hide('circle_menu'), Show('flower_menu_button') ]

            action Hide('circle_menu')

        ### Buttons

        ## Save button
        imagebutton:

            pos (708, 209)
            xysize( 228, 227 )

            idle "gui/circle_menu/save_idle.png"
            hover "gui/circle_menu/save_hover.png"

            action [ Hide('circle_menu'), ShowMenu("save") ]

        ## Load button
        imagebutton:

            pos (1003, 209)
            xysize( 228, 227 )

            idle "gui/circle_menu/load_idle.png"
            hover "gui/circle_menu/load_hover.png"

            action [ Hide('circle_menu'), ShowMenu("load") ]

        ## Skip button
        imagebutton:

            pos (623, 484)
            xysize( 228, 227 )

            idle "gui/circle_menu/skip_idle.png"
            hover "gui/circle_menu/skip_hover.png"

            action [ Hide('circle_menu'), Skip() ] # alternate Skip(fast=True, confirm=True)

        ## Config button
        imagebutton:

            pos (1083, 484)
            xysize( 228, 227 )

            idle "gui/circle_menu/config_idle.png"
            hover "gui/circle_menu/config_hover.png"

            action [ Hide('circle_menu'), ShowMenu("preferences") ]

        ## Quit button
        imagebutton:

            pos (853, 659)
            xysize( 228, 227 )

            idle "gui/circle_menu/quit_idle.png"
            hover "gui/circle_menu/quit_hover.png"

            action [ Hide('circle_menu'), MainMenu(confirm=True) ]
