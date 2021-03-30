
### Changes to RenPy's default keymaps happen here.

init python:

    # Su+press RenPy's "game menu" button, the cause of many woes.
    config.keymap['game_menu'] = []

    # And create an alternative one.
    config.keymap['game_menu_alt'] = [ 'K_ESCAPE', 'K_MENU', 'K_PAUSE', 'mouseup_3' ],
