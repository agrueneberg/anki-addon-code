from aqt import gui_hooks

def insert_code(editor):
    editor.web.eval("wrap('<code>', '</code>');")

def add_code_button(buttons, editor):
    buttons.append(
        editor.addButton(
            "", # icon,
            "code", # cmd,
            insert_code, # func
            "Wrap in selection in <code> elements (Ctrl+])", # tip
            "Code", # label
            keys = "Ctrl+]"
        )
    )

gui_hooks.editor_did_init_buttons.append(add_code_button)
