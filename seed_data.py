from database import session, ColorPalette, FontPair

# Funkcija spalvu pridejimui
def seed_colors():
    # Sukuriame keleta pavyzdziu su emocijomis
    palettes = [
        ColorPalette(emotion='Luxury', hex_1='#1A1A1A', hex_2='#D4AF37', hex_3='#FFFFFF', brightness=0.5),
        ColorPalette(emotion='Playful', hex_1='#FF4081', hex_2='#FFD54F', hex_3='#4FC3F7', brightness=0.8),
        ColorPalette(emotion='Professional', hex_1='#2C3E50', hex_2='#BDC3C7', hex_3='#2980B9', brightness=0.4),
        ColorPalette(emotion='Nature', hex_1='#2D5A27', hex_2='#8B4513', hex_3='#F5F5DC', brightness=0.6)
    ]
    # Irasome i duomenu baze
    session.add_all(palettes)
    session.commit()
    print("Spalvos sekmingai pridetos!")

# Funkcija sriftu pridejimui
def seed_fonts():
    # Google Fonts poros (Headline ir Body)
    fonts = [
        FontPair(emotion='Luxury', headline_font='Playfair Display', body_font='Lato', category='Serif'),
        FontPair(emotion='Playful', headline_font='Fredoka One', body_font='Quicksand', category='Display'),
        FontPair(emotion='Professional', headline_font='Roboto', body_font='Open Sans', category='Sans-Serif'),
        FontPair(emotion='Nature', headline_font='Montserrat', body_font='Lora', category='Mix')
    ]
    session.add_all(fonts)
    session.commit()
    print("Sriftai sekmingai prideti!")

# Paleidziame pildyma
if __name__ == "__main__":
    seed_colors()
    seed_fonts()