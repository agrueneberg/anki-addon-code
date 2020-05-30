import os
from aqt import gui_hooks

ADDON_PATH = os.path.dirname(__file__)

def insert_code(editor):
    editor.web.eval("wrap('<code>', '</code>');")

def add_code_button(buttons, editor):
    buttons.insert(
        len(buttons) - 1, # add before hamburger menu
        editor.addButton(
            os.path.join(ADDON_PATH, "code.png"), # icon,
            "code", # cmd,
            insert_code, # func
            "Wrap in selection in <code> elements (Ctrl+])", # tip
            keys = "Ctrl+]"
        )
    )

gui_hooks.editor_did_init_buttons.append(add_code_button)
