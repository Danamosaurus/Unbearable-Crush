### Styles

style preferences_bars_style:

    xysize (453, 40)

    left_bar "gui/preferences/bar_left.png"
    right_bar "gui/preferences/bar_right.png"

    thumb "gui/preferences/thumb_idle.png"

    thumb_offset 20
    left_gutter 15
    right_gutter 15

## Preferences screen ##########################################################
##
## The preferences screen allows the player to configure the game to better suit
## themselves.
##
## https://www.renpy.org/doc/html/screen_special.html#preferences

screen preferences():

    tag menu

    frame:

        pos (61, 89)
        xysize (1803, 903)

        margin (0,0)
        padding (0,0)

        background "gui/preferences/background.png"

        at save_load_screen_animation

        ### Display window section
        fixed:

            xpos 177

            # Windowed
            imagebutton:

                ypos 176
                xysize (392, 50)

                idle "gui/preferences/windowed_idle.png"
                hover "gui/preferences/windowed_hover.png"
                selected_idle "gui/preferences/windowed_selected.png"
                selected_hover "gui/preferences/windowed_selected.png"

                selected (preferences.fullscreen == False)

                action Preference("display", "window")

            # Fullscreen
            imagebutton:

                ypos 231
                xysize (392, 50)

                idle "gui/preferences/fullscreen_idle.png"
                hover "gui/preferences/fullscreen_hover.png"
                selected_idle "gui/preferences/fullscreen_selected.png"
                selected_hover "gui/preferences/fullscreen_selected.png"

                action Preference("display", "fullscreen")

        ### Rollback side section
        fixed:

            xpos 728

            # Disabled
            imagebutton:

                ypos 176
                xysize (393, 50)

                idle "gui/preferences/disabled_idle.png"
                hover "gui/preferences/disabled_hover.png"
                selected_idle "gui/preferences/disabled_selected.png"
                selected_hover "gui/preferences/disabled_selected.png"

                action Preference("rollback side", "disable")

            # Left
            imagebutton:

                ypos 231
                xysize (393, 50)

                idle "gui/preferences/left_idle.png"
                hover "gui/preferences/left_hover.png"
                selected_idle "gui/preferences/left_selected.png"
                selected_hover "gui/preferences/left_selected.png"

                action Preference("rollback side", "left")

            # Right
            imagebutton:

                ypos 286
                xysize (393, 50)

                idle "gui/preferences/right_idle.png"
                hover "gui/preferences/right_hover.png"
                selected_idle "gui/preferences/right_selected.png"
                selected_hover "gui/preferences/right_selected.png"

                action Preference("rollback side", "right")


        ### Skip settings
        fixed:

            xpos 1285

            # Unseen text
            imagebutton:

                ypos 176
                xysize (393, 50)

                idle "gui/preferences/utext_idle.png"
                hover "gui/preferences/utext_hover.png"
                selected_idle "gui/preferences/utext_selected.png"
                selected_hover "gui/preferences/utext_selected.png"

                action Preference("skip", "toggle")

            # After choices
            imagebutton:

                ypos 231
                xysize (393, 50)

                idle "gui/preferences/afchoices_idle.png"
                hover "gui/preferences/afchoices_hover.png"
                selected_idle "gui/preferences/afchoices_selected.png"
                selected_hover "gui/preferences/afchoices_selected.png"

                action Preference("after choices", "toggle")

            # Transitions
            imagebutton:

                ypos 286
                xysize (393, 50)

                idle "gui/preferences/transitions_idle.png"
                hover "gui/preferences/transitions_hover.png"
                selected_idle "gui/preferences/transitions_selected.png"
                selected_hover "gui/preferences/transitions_selected.png"

                action InvertSelected(Preference("transitions", "toggle"))

        ### Text speed & Auto-forward time
        fixed:

            xpos 143

            # Text speed
            bar:

                ypos 447

                style "preferences_bars_style"

                value Preference("text speed")

            # Auto-forward speed
            bar:

                ypos 550

                style "preferences_bars_style"

                value Preference("auto-forward time")

        ### Volumes
        fixed:

            xpos 696

            # Music
            bar:

                ypos 448

                style "preferences_bars_style"

                value Preference("music volume")

            # Sound
            bar:

                ypos 551

                style "preferences_bars_style"

                # hovered Play("sound", config.sample_sound)

                value Preference("sound volume")

            # Voice
            bar:

                ypos 666

                style "preferences_bars_style"

                # hovered Play("voice", config.sample_voice)

                value Preference("voice volume")

        ### Mute all button
        imagebutton:

            pos (728, 726)
            xysize (392, 50)

            idle "gui/preferences/mute_all_idle.png"
            hover "gui/preferences/mute_all_hover.png"
            selected_idle "gui/preferences/mute_all_selected.png"
            selected_hover "gui/preferences/mute_all_selected.png"

            action Preference("all mute", "toggle")

        ### Back button
        imagebutton:

            pos (4,737)

            xysize (302, 74)

            idle "gui/save_load/back_idle.png"
            hover "gui/save_load/back_hover.png"

            action Return()
