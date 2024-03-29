init python:
    musicbox_content = [
        ( "Music/A Future Together.ogg", "A Future Together", "Paul Robins"),
        ( "Music/Aster.ogg", "Aster", "Paul Robins"),

    ]
# I still don't know who did each of these songs
    musicbox_currently_playing = None
screen Jukebox():
    tag menu
    style_prefix "journal"
    #add gui.main_menu_background at fade_transform
    add "backgrounds/space.png" at main_menu_bg_transform
    frame:
            pos (40, 120)
            background None
            padding (0,0,0,0)
            xsize 790
            ysize 770
            vpgrid xoffset -10:
                cols 1
                mousewheel True
                draggable True
                scrollbars "vertical"
                side_xalign 0.5
                yinitial 0.0
                yspacing 20

                for i in range(len(musicbox_content)):
                    $ clip, title, artist = musicbox_content[i]
                    frame:
                        background None
                        xsize 750
                        ysize 135
                        padding (0,0,0,0)
                        right_margin 20
                        xalign 0
                        imagebutton:
                            idle Frame("gui\sagi\smallbutton-idle.png", Borders(30,30,30,30))
                            hover Frame("gui\sagi\smallbutton-highlighted.png", Borders(30,30,30,30))
                            if i == musicbox_currently_playing:
                                action [ SetVariable("musicbox_currently_playing", None), Play("music", "music/main menu.ogg") ]
                            else:
                                action [ SetVariable("musicbox_currently_playing", i), Play("music", clip) ]
                        frame:
                            background None
                            xsize 750
                            ysize 135
                            padding (30,15,30,15)
                            right_margin 20
                            xalign 0

                            text title pos (0, 0):
                                size 50
                                color "#36428A"
                                outlines []
                            text "by " + artist pos (0, 50):
                                # font "BebasNeue-Regular.otf"
                                size 50
                                color "#36428A"
                                outlines []

    fixed pos (700, 910):
        imagebutton:
            idle "gui\sagi\smallbutton-idle.png"
            hover "gui\sagi\smallbutton-highlighted.png"
            action Return()
        text "Back":
            size 30
            outlines []
