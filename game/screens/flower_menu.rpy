### Animations

transform circle_menu_intro_exit_animation:

    alpha 0.0
    crop ( 0, 0, 1920, 1080)

    on show:
        ease 0.5 alpha 1.0

    on hide:
        ease 0.5 alpha 0.0

transform circle_menu_buttons_animation:

    on show:

        alpha 0.0
        zoom 0.0
        crop ( 0, 0, 1920, 1080)

        parallel:
            ease 0.5 alpha 1.0

        parallel:
            ease 0.5 zoom 1.0

    on hide:

        alpha 1.0
        zoom 1.0

        parallel:
            ease 0.5 alpha 0.0

        parallel:
            ease 0.5 zoom 0.0


### Transparent button used to call the flower menu

screen flower_menu_button():

    key "mouseup_3" action [
            # RightClickFlower(),
            # Hide('flower_menu_button'),
            FileTakeScreenshot(),
            ShowMenu("circle_menu"),

    ]

screen circle_menu:

    modal True

    tag menu

    # Sliding background.
    frame:

        pos (0,0)
        xysize (1.0, 1.0)

        margin (0,0)
        padding (0,0)

        background None

        at circle_menu_intro_exit_animation

        ### Sliding background
        fixed:

            pos(0,0)

            at confirm_screen_flower_slide_animation

            add "gui/circle_menu/background.png":
                pos(0,0)

            add "gui/circle_menu/background.png":
                pos(1920,0)

    # Menu
    frame:

        anchor (0.5, 0.5)
        align (0.5, 0.5)
        xysize (1.0, 1.0)

        margin (0,0)
        padding (0,0)

        background None

        at circle_menu_buttons_animation

        ### Invisible button that closes this screen.
        button:

            xysize (1.0, 1.0)

            key "mouseup_3" action [ Hide('circle_menu'), Show('flower_menu_closing') ]

            action [ Hide('circle_menu'), Show('flower_menu_closing') ]

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

            action [ MainMenu(confirm=True) ]


screen flower_menu_closing():

    modal True

    timer 0.45 action [ Return(), Show('flower_menu_button') ]
