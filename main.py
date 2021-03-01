import eel
eel.init('web')

@eel.expose
def uppercase_convert_python(text):
    eel.change_text_area(text.upper())
    return None

@eel.expose
def lowercase_convert_python(text):
    eel.change_text_area(text.lower())
    return None


eel.start('index.html', size=(600, 300))