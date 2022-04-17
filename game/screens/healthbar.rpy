### Styles


## Healthbar screen ###############################################################
##
## This screen is used to display and animate the healthbar
##
## EXAMPLE 1, show screen healthbar(name, from_health, to_health, duration_to_stay_on_screen):
## show screen healthbar("Kanna", 0, 1, 2.5)
##
## EXAMPLE 2, show screen healthbar_multiple(list_of_healthbar_values, duration_to_stay_on_screen):
## show screen healthbar_multiple([
##         ("Kanna", 0, 1),
##         ("Maya", 5, 4),
##         ("Charlotte", 2, 4),
##     ], 2.5
## )
default healthbar_max = 5

transform healthbar_transform(align=(0.95, 0.03), yoffset=-100):
    on show:
        align align yoffset yoffset
        easein 0.6 yoffset 0
    on hide:
        easeout 0.6 yoffset yoffset

transform healthbar_inner_transform(from_val, to_val):
    xsize from_val
    0.6
    ease 1.0 xsize to_val

screen healthbar(name, from_health, to_health, duration=2.5, align=(0.95, 0.03), yoffset=-100):
    fixed:
        at healthbar_transform(align=(0.95, 0.03), yoffset=-100)
        xsize 600
        ysize 50
        hbox:
            spacing 20
            fixed:
                xsize 180
                text name:
                    size 40
                    text_align 1.0
                    xalign 1.0
                    outlines [ (2, "#000") ]
            fixed:
                xsize 400
                ysize 50
                frame:
                    background Frame('gui/healthbar/healthbar_frame.png', 6, 6, 6, 6)
                    xalign 0.0
                    xsize 400
                    ysize 50
                frame:
                    background Frame('gui/healthbar/healthbar_fill.png', 6, 6, 6, 6)
                    at healthbar_inner_transform(int(1.0 * from_health / healthbar_max * 400), int(1.0 * to_health / healthbar_max * 400))
                    xalign 0.0
                    ysize 50
                frame:
                    background Tile('gui/healthbar/healthbar_overlay.png')
                    margin (6, 6)
                    xalign 0.0
                    xsize 400
                    ysize 50
    if duration is not None:
        timer duration action Hide("healthbar")

screen healthbar_multiple(name_health, duration=2.5):
    for i in range(len(name_health)):
        $ name, from_health, to_health = name_health[i]
        fixed:
            at healthbar_transform(align=(0.95, 0.03+0.08*i), yoffset=-100-100*i)
            xsize 600
            ysize 200
            xalign 0.95
            use healthbar(name, from_health, to_health, None)
    if duration is not None:
        timer duration action Hide("healthbar_multiple")
