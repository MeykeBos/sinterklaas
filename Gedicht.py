import sys
from pathlib import Path
import streamlit as st
from PIL import Image

st.set_page_config(page_title="surprise", page_icon=":gift:", layout="centered", initial_sidebar_state="auto", menu_items=None)

file = Path(__file__).resolve()
parent, root = file.parent, file.parents[1]
sys.path.append(str(root))

try:
    sys.path.remove(str(parent))
except ValueError:  # Already removed
    pass


# Create opening page
def draw_main_page():
    st.write(''' ''')
    st.write('''
            # Beste Dirk, Lieve Haan,
            Daar stond je dan, met de wind in de haren en de handen aan het roer,''')
    st.write('''
            Zo sta ik daar ook altijd aan de vooravond van mijn jaarlijkse najaars tour.''')
    st.write(''' ''')
    st.write('''
            De warmte van de zon op de huid en de geur van het water, oh wat een genot,''')
    st.write('''
            Dat alles maakt dat ik mij elk jaar wederom voel als een volmaakte jonge god.''')
    st.write(''' ''')
    st.write('''
            Ik kan mij zo voorstellen dat jij -als Haan-, ondanks het missen van mijn mooie baard haren,''')
    st.write('''
            Eenzelfde "Adonis" gevoel ervaart als jij gaat varen!''')
    st.write(''' ''')
    st.write('''
            Maar ook tijdens de bruiloft van je nicht zagen wij je schitteren in een prachtig pak,''')
    st.write('''
            Echter was je niet de enige Haan die deze dag verscheen in vol ornaat en met uitziend gemak...''')
    st.write(''' ''')
    st.write('''
            Zowel de warme als de koude kant van de familie, opgedofd en wondermooi, ''')
    st.write('''
            Alsof alle Haanen toen al op de hoogte waren van dit waanzinigge familie toernooi.''')
    st.write(''' ''')
    st.write('''
            Vandaag gaan we namelijk, beste Dirk Jan,''')
    st.write('''
            Op zoek naar de allermooitste en ijdelste Haanen vrouw of man.''')
    st.write(''' ''')
    st.write('''
            Om deze wedstrijd eerlijk te jureren,''')
    st.write('''
            Kunnen we natuurlijk niet zomaar afgaan op wat eeniemand mag of zou beweren.''')
    st.write(''' ''')
    st.write('''
            Om die reden hebben mijn pieten onder het stof vandaan gehaald, een waar sprookjes object,''')
    st.write('''
            Het gaat om een spiegel die eerlijk en oprecht, een oordeel kan vellen Correct.''')
    st.write(''' ''')
    st.write('''
            Wie o wie is op dit moment de ijdelste en allerknapste Haan?''')
    st.write('''
            En wie in deze familie is het meeste met zijn spiegelbeeld begaan..?''')
    st.write(''' ''')
    st.write('''
            Doe een gooi doen naar deze fel begeerde titel en klik links op "Tabletje"''')
    st.write('''
            En geef 'm van Jetje!!!''')
    st.write(''' ''')
    st.write(''' ''')
    st.write(''' ''')
    st.write('''_Tabletje, Tabletje in mijn hand_ ''')
    st.write('''_Wie is de ijdelste en mooiste Haan van Nederland?_ ''')

    st.write(''' ''')
    st.write(''' ''')
    st.write(''' ''')
    st.write('''Wij wensen een iedere Haan een hoop succes!''')
    st.write('''Hartelijke groeten, ook namens mijn Pieten, de Sint''')

    image = Image.open('group_pic.jpeg')
    st.image(image, caption='Bewijslast: Haanen in volle glorie...')
draw_main_page()
