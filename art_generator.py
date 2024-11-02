from ascii_templates import build_template_art

def generate_ascii_art(text, symbol_set, width, height):
    ascii_art = build_template_art(text, symbol_set[0])
    return ascii_art
