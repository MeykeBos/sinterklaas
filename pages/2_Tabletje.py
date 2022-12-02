import streamlit as st
import string
import time
import dataclasses
import random
from PIL import Image
from demos import persist

st.set_page_config(page_title="surprise", page_icon=":gift:", layout="centered", initial_sidebar_state="auto", menu_items=None)

persist.load_widget_state()

if "name_input" not in st.session_state:
    st.session_state["name_input"] = ""

st.write(
        """# 📸 Tijd om te shinen""")
st.write(""" """)
st.write(""" """)
st.write("""Aan het begin,""")
st.write("""Vul je eerst je naam in.""")
st.write(""" """)
st.write("""Vervolgens laat je zien - van jezelf - de beste versie,""")
st.write("""En neem dan snel een selfie.""")
st.markdown("""---""")

# [start] [persistent states]__________________________________________
@dataclasses.dataclass
class gameState:
    # HangMan
    hm_word: str = ""
    # get a dict with each letter in hm_word
    hm_word_letters = set(hm_word)
    # get all letters of the alfabet in capitals
    hm_alphabet = set(string.ascii_uppercase)
    hm_used_letters = set()
    hm_word_list = []
    hm_n_lifes: int = 6
    hm_idxml_key: int = 0
    hm_picture: str = ""



@st.cache(allow_output_mutation=True)
def _gameState() -> gameState:
    return gameState()


hm = _gameState()


# [start] [HangMan]____________________________________________________


def HangMan():
    word = st.text_input(
        f"Vul eerst je naam in 👇",
        type="default",
        placeholder="naam",
        key=f"word_{hm.hm_idxml_key}"
    )
    #st.write(hm.hm_word)
    if hm.hm_word == "":
        if word == "":
            st.warning("**Oeps, je hebt je naam nog niet ingevuld.**")
        else:
            hm.hm_word = word.upper()
            st.experimental_rerun()
    elif hm.hm_word != "":
        st.success("**Gelukt... Nu is het selfie tijd!**")

        st.markdown("___")

        with st.spinner('...'):
            time.sleep(random.randint(1, 2))
        #with st.spinner(list_waiting_lines[random.randint(0, 4)]):
        #    time.sleep(random.randint(1, 4))

        holder1, holder2, holder3 = st.empty(), st.empty(), st.empty()
        hm_picture = holder1.camera_input("Selfie tijd...", key=str(hm.hm_idxml_key + 1))

        time.sleep(1)

        if hm_picture:

            list_waiting_lines = ["Hmmm... lastig met zo'n knappe kop...",
                                  "Poeh... wat geef je me nou om mee te werken?",
                                  "Is dit alles wat de Haanen te bieden hebben?",
                                  "Knap, ja... zeker heel knap...",
                                  "Selfies, waar zijn de ouderwetse spiegels eigenlijk nog goed voor?"]

            dj = ["DJ", "DIRK", "DIRK JAN", "D-J", "DIRK-JAN", "D JAN", "D-JAN"]
            annet = ["ANNET"]
            sander = ["SANDER"]
            sabine = ["SABINE", "SABIEN", "SABIENE", "SABIENTJE"]
            ida = ["IDA"]
            hanneke = ["HANNEKE"]
            ciska = ["CISKA", "CIS"]
            jasper = ["JASPER", "JAP", "JAPPIE"]
            fret = ["FRET", "FRED", "FREDDY"]
            jolanda = ["JOLANDA"]
            jelle = ["JELLE", "PAPA"]
            meyke = ["MEYKE", "MAMA"]
            lode = ["LODE"]
            julie = ["JULIE"]

            if hm.hm_word in julie:
                st.success("Spiegeltje Spiegeltje aan de wand, Julie is de ijdelste EN mooiste Haan van Nederland!")
                time.sleep(1)
                st.snow()
                st.session_state["name_input"] = hm.hm_word
                col1, col2, col3 = st.columns(3)

                with col1:
                    image1 = Image.open("/images/Julie.jpeg")
                    st.image(image1)

                with col2:
                    image2 = Image.open("/images/Julie2.jpg")
                    st.image(image2)

                with col3:
                    image3 = Image.open("/images/Julie3.jpg")
                    st.image(image3)
                b_reset = st.button("🛑 Ga snel naar 'Kado'")

            elif hm.hm_word in dj:
                st.warning("Potentie... zeker... Maar je haar heeft duidelijk de zout-water look nodig... ", icon="⚠️")
                image_dj = Image.open('2016-03-08_FSOR__Rod_Stewart__DSC6183_CREDIT_Farm_Sanctuary-1-1187x1600.jpg')
                st.image(image_dj)
                st.session_state["name_input"] = hm.hm_word
                b_reset = st.button("🛑 Laat een Haan met een good hair day het proberen...")

            elif hm.hm_word in annet:
                st.warning("Prachtig mooi! Wonderbaarlijk zelfs... Maar niet de Haan die we zoeken... ", icon="⚠️")
                image_annet = Image.open(
                    'fc794943954423e0a6a21e58ea8a11f4.jpg')
                st.image(image_annet)
                st.session_state["name_input"] = hm.hm_word
                b_reset = st.button("🛑 Laat een andere Haan het proberen...")

            elif hm.hm_word in sander:
                st.warning("Jong, stoer, sterk, ogenschijnlijk een echte zeebonk... Maar vandaag zoeken we een 'bovenwater Haan'", icon="⚠️")
                image_sander = Image.open(
                    '/images/nat.jpg')
                st.image(image_sander)
                st.session_state["name_input"] = hm.hm_word
                b_reset = st.button("🛑 Laat een landrot exemplaar het proberen...")

            elif hm.hm_word in sabine:
                st.warning("Een duidelijke Haanen-neus en een ietwat serieuze 'look', zeer fraai. "
                           "Maar we zoeken een Haan die zichzelf zeer graag bewondert.", icon="⚠️")
                image_sabine = Image.open(
                    'HensandRoosters-AlextenNapel-NEDERLANDSE.BAARDKUIFHOEN.-ROOSTER32017.jpg')
                st.image(image_sabine)
                st.session_state["name_input"] = hm.hm_word
                b_reset = st.button("🛑 Laat een andere Haan het proberen...")

            elif hm.hm_word in ida:
                st.warning("Juist, juist... gefocust, recht door zee. Superbe, voortreffelijk! Maar we zoeken toch nog net iets anders...", icon="⚠️")
                image_ida = Image.open(
                    '0eb959958fee025e868bbdc05973fd9a.jpg')
                st.image(image_ida)
                st.session_state["name_input"] = hm.hm_word
                b_reset = st.button("🛑 Laat ander gevogelte het nu proberen...")

            elif hm.hm_word in hanneke:
                st.warning("Wat een fraaie Opper-Haan! Maar op deze leeftijd doe je mee voor andere prijzen :)", icon="⚠️")
                image_hanneke = Image.open(
                    'rooster.webp')
                st.image(image_hanneke)
                st.session_state["name_input"] = hm.hm_word
                b_reset = st.button("🛑 Laat een andere Haan het proberen... Wellicht een iets jeugdiger exemplaar..?")

            elif hm.hm_word in ciska:
                st.warning("Ja, duidelijk ook een echte zeevrouw! Twee zeilvakanties doen een Haan duidelijk goed! Maar helaas...", icon="⚠️")
                image_ciska = Image.open(
                    'rooster-edited.webp')
                st.image(image_ciska)
                st.session_state["name_input"] = hm.hm_word
                b_reset = st.button("🛑 Laat een andere Haan het proberen... Heeft je broertje al geprobeerd?")

            elif hm.hm_word in jasper:
                st.warning("De echte geconcentreerde studenten-look! Maar wel eentje die thuis woont en niet elke avond peperkoek met corned beef eet.", icon="⚠️")
                image_jasper = Image.open(
                    'tough-looking-red-rooster-boss-chicken.jpg')
                st.image(image_jasper)
                st.session_state["name_input"] = hm.hm_word
                b_reset = st.button("🛑 Laat een andere Haan het proberen...")

            elif hm.hm_word in fret:
                st.warning("Ja, hier hebben we duidelijk te maken met een vooraanstaande Haan! "
                           "Nog maar even en ook jij hoeft niet meer voor het geld te kraaien.", icon="⚠️")
                image_fred = Image.open(
                    'header_essay-this-one-gettyimages-764854961_high.jpg')
                st.image(image_fred)
                st.session_state["name_input"] = hm.hm_word
                b_reset = st.button("🛑 Laat een andere -jongere- Haan het proberen... ")

            elif hm.hm_word in jolanda:
                st.warning("Ja, ja, ja... een echte ware Haan. Prachtige neus, wonderschone kin... "
                           "Maar helaas zoeken we een surprise-knutselende Haan vandaag.", icon="⚠️")
                image_jolanda = Image.open(
                    '7LGATJPHINGLRHRD2B7RZOLEV4.jpg')
                st.image(image_jolanda)
                st.session_state["name_input"] = hm.hm_word
                b_reset = st.button("🛑 Jammer dat je kinderen er niet zijn, die hadden zeker hoge ogen gegooid in dit tournament... "
                                    "Laat een andere Haan het proberen...")

            elif hm.hm_word in jelle:
                st.warning("Oei-joei-joei Jelle! Een verse Haan... Zeker knap, maar niet de Haan die ik zoek. "
                           "Misschien moet je de volgende keer proberen, een andere camerahoek...", icon="⚠️")
                image_jelle = Image.open(
                    'scale.webp')
                st.image(image_jelle)
                st.session_state["name_input"] = hm.hm_word
                b_reset = st.button("🛑 Laat een andere Haan het proberen...")

            elif hm.hm_word in meyke:
                st.warning("Juist... zeer fraai, wel een look ietwat overspannen. Komt dat door de kinderen.. kun je ze af en toe niet naar Spanje verbannen? ", icon="⚠️")
                image_meyke = Image.open(
                    'rooster-1.webp')
                st.image(image_meyke)
                st.session_state["name_input"] = hm.hm_word
                b_reset = st.button("🛑 Laat anderen het toch maar proberen... ")

            elif hm.hm_word in lode:
                st.warning("Ohhhh, zo knap en scheetig! En wat een prachtig haar! Zonder twijfel de mooiste kleuter uit deze familie... echt waar!", icon="⚠️")
                image_lode = Image.open(
                    'lode.webp')
                st.image(image_lode)
                st.session_state["name_input"] = hm.hm_word
                b_reset = st.button("🛑 Laat een andere Haan het proberen... Heeft je vader al een poging gewaagd..?")

            else:
                st.warning("Jij bent denk ik geen Haan, je mist de typische verfijnde Haanen-look! En komt niet voor in mijn grote boek!")
                image_non = Image.open(
                    'andere_haan.jpeg')
                st.image(image_non)
                st.session_state["name_input"] = hm.hm_word
                b_reset = st.button("🛑 Laat een ECHTE Haan het proberen...")


            # b_reset = st.button("🛑 Laat een andere Haan het proberen")
            if b_reset:
                hm.hm_word = ""
                hm.hm_word_letters = set(hm.hm_word)
                hm.hm_used_letters = set()
                hm.hm_word_list = []
                hm.hm_n_lifes = 6
                hm.hm_idxml_key += 1
                hm.hm_picture: str = ""
                st.experimental_rerun()

            st.markdown("""___""")


if __name__ == "__main__":
    HangMan()
