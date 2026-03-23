from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.orm import declarative_base, sessionmaker

# Naudojame naujesne deklaravimo vieta, kad isvengtume ispejimu
Base = declarative_base()

# Lentele spalvu paletems saugoti
class ColorPalette(Base):
    __tablename__ = 'color_palettes'
    id = Column(Integer, primary_key=True)
    emotion = Column(String)  # Pvz., 'Luxury', 'Playful'
    hex_1 = Column(String)    # Spalva 1
    hex_2 = Column(String)    # Spalva 2
    hex_3 = Column(String)    # Spalva 3
    brightness = Column(Float) 

# Lentele sriftams saugoti
class FontPair(Base):
    __tablename__ = 'font_pairs'
    id = Column(Integer, primary_key=True)
    emotion = Column(String)
    headline_font = Column(String) # Pagrindinis sriftas
    body_font = Column(String)     # Teksto sriftas
    category = Column(String)      # Serif, Sans-Serif ir t.t.

# DB nustatymai - sukuria SQLite faila jusu projekto aplanke
engine = create_engine('sqlite:///design_helper.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

# Komentaras: Si dalis atsakinga už komunikacija tarp Python ir SQL