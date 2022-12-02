import streamlit as st
from demos import orchestrator
from demos import persist
from PIL import Image
import dataclasses
import string
import time

st.set_page_config(page_title="surprise", page_icon=":gift:", layout="centered", initial_sidebar_state="auto", menu_items=None)

persist.load_widget_state()

if "name_input" not in st.session_state:
    st.session_state["name_input"] = ""

if not st.session_state["name_input"] == "JULIE":
    st.warning("# Hey! Het lijkt erop dat dit kado niet voor jou is. Zoek eerst uit Wie de knapste Haan van het land is! En kom daarna hier terug.")
    st.stop()  # App won't run anything after this line

st.write(
        f"""
        # Surprise 2022! 👋
        """
    )

st.write(''' ''')
st.write('''
            # Lieve Julie,
            Elke mogelijkheid die jouw ouders je geven,''')
st.write('''
            Grijp jij je kans, je bent zo bedreven.''')
st.write(''' ''')
st.write('''
            Letten ze even niet op,''')
st.write('''
            Dan sta jij weer op de foto met je knappe "kop".''')
st.write(''' ''')
st.write('''
            Selfie hier en selfie daar,''')
st.write('''
            Soms met een schattig of grappig gebaar!''')
st.write(''' ''')
st.write('''
            Soms met konijn, vaak met je broer,''')
st.write('''
            Soms erg lief maar vaak ook erg stoer!''')
st.write(''' ''')
st.write('''
            In een zelfgemaakte video vertel je soms hele verhalen,''')
st.write('''
            Maar op de foto's zien we je schitteren en stralen!''')
st.write(''' ''')
st.write('''
            Wat jammer dat je je niet dagelijks versieren mag,''')
st.write('''
            Maar lippenstift is volgens je moeder echt alleen voor een feestdag.''')
st.write(''' ''')
st.write('''
            Deze sint gaat je daarom helpen met een kado,''')
st.write('''
            Maar heeft wel eerst een challenge voor je in-petto.''')
st.write(''' ''')
st.write('''
            Zoals je weet zijn er dit jaar grote problemen met de kado's,''')
st.write('''
            Sommige zijn zelfs geheel spoorloos! ''')
st.write(''' ''')
st.write('''
            Kijk snel de video om te zien hoe het er met jouw kado voorstaat''')
st.write('''
            Hopelijk is die van jou gewoon netjes hier in huis, of anders in de straat... ''')
st.write(''' ''')
st.write(''' ''')
st.write(''' ''')

st.write("## Bekijk de video \U0001F3AC ")
video_file = open('/images/video_julie.mp4', 'rb')
video_bytes = video_file.read()
st.video(video_bytes)

with st.expander("\U0001F575	 Hoe nu verder? "):
    st.write("Helaas, ook bij jou is het dus niet goed gegaan...")
    st.write("dus is het voor jou nu tijd om op te staan.")
    st.write(''' ''')
    st.write("Zoek de plekken op de plaatjes,")
    st.write("en vul met de aanwijzingen de gaatjes.")
    st.write(''' ''')
    st.write(''' ''')
    st.write('''Succes lieve Julie ''')
    st.write(''' ''')
    st.write(''' ''')
    st.write('''### Plek 1''')
    plek1 = Image.open('/images/plek1.jpeg')
    st.image(plek1, width=300)
    st.write('''### Plek 2''')
    plek2 = Image.open('/images/plek2.jpeg')
    st.image(plek2, width=300)
    st.write('''### Plek 3''')
    plek3 = Image.open('/images/plek3.jpeg')
    st.image(plek3, width=300)
    st.write('''### Plek 4''')
    plek4 = Image.open('/images/plek4.jpeg')
    st.image(plek4)


    # [start] [persistent states]__________________________________________
    @dataclasses.dataclass
    class gameState2:
        # HangMan
        hm_word2: str = "JAS-VAN-PAPA"
        hm_word_letters2 = set(hm_word2)
        hm_alphabet2 = set(string.ascii_uppercase)
        hm_used_letters2 = set()
        hm_word_list2 = []
        hm_n_lifes2: int = 6
        hm_idxml_key2: int = 0


    @st.cache(allow_output_mutation=True)
    def _gameState2() -> gameState2:
        return gameState2()


    hm2 = _gameState2()


    # [start] [HangMan]____________________________________________________

    def HangMan2():
        word2 = "KAPSTOK"
        hm2.hm_word2 = word2.upper()
        hm2.hm_word_letters2 = set(hm2.hm_word2)
        #st.experimental_rerun()



        word_list2 = [letter if letter in hm2.hm_used_letters2 else "-" for letter in hm2.hm_word2]


        st.markdown(
            f"""
            <br>
                Deze letters heb je al ingevuld: {" ".join(hm2.hm_used_letters2)} <br>
                <br>
                Hier mag je je kado zoeken: {"".join(word_list2)}
            <br>
            """,
            unsafe_allow_html=True,
        )
        holder1, holder2, holder3 = st.empty(), st.empty(), st.empty()
        user_letter2 = holder1.text_input(
            "Vul 1 letter in (een voor een):", max_chars=1, key=str(hm2.hm_idxml_key2 + 1)
        ).upper()

        paswoord = st.text_input(
            f"Dringend hulp nodig? Vraag Sinterklaas...",
            type="password",
            placeholder="password",
            key="paswoord"
        )
        if paswoord == "meyke":
            show_answer = st.button("🔍 Reset 🔭")
            if show_answer:
                hm2.hm_word2 = "KAPSTOK"
                hm2.hm_word_letters2 = set(hm2.hm_word2)
                hm2.hm_used_letters2 = set()
                hm2.hm_word_list2 = []
                hm2.hm_n_lifes2 = 6
                hm2.hm_idxml_key2 += 1
                st.experimental_rerun()


        if (
                len(hm2.hm_word_letters2) > 0 and hm2.hm_n_lifes2 > 0 and user_letter2 != ""
        ) and hm2.hm_word2:

            if user_letter2 in hm2.hm_alphabet2 - hm2.hm_used_letters2:
                hm2.hm_used_letters2.add(user_letter2)
                if user_letter2 in hm2.hm_word_letters2:
                    hm2.hm_word_letters2.remove(user_letter2)
                    holder2.success("Goed gedaan!")
                else:
                    holder2.error("Deze letter is niet goed. Probeer het nog een keer!")
                    hm2.hm_n_lifes2 -= 1

            elif user_letter2 in hm2.hm_used_letters2:
                holder2.info("Deze letter had je al ingevuld. Probeer een andere!")

            elif user_letter2 not in hm2.hm_alphabet2 and user_letter2 != "":
                holder2.error("Dit is geen letter!")

        elif (
                len(list(set([letter for letter in hm2.hm_word2 if letter in hm2.hm_used_letters2]))) == len(hm2.hm_word_letters2) or hm2.hm_n_lifes2 == 0
        ) and hm2.hm_word2:
            holder1.empty()

            if "".join(word_list2) == hm2.hm_word2:
                holder1.success(
                    f"\nGefeliciteerd! Ga snel je kado zoeken bij de {hm2.hm_word2} !!"
                )
                st.balloons()
            else:
                holder2.info(f"Ga maar snel je kado zoeken bij de {hm2.hm_word2}")
                holder3.error("")
                time.sleep(1)

        #st.write(len([letter for letter in hm2.hm_word2 if letter in hm2.hm_used_letters2]),list(set([letter for letter in hm2.hm_word2 if letter in hm2.hm_used_letters2])), len(hm2.hm_word_letters2), hm2.hm_word_letters2)
        time.sleep(1)


        if user_letter2 != "":
            hm2.hm_idxml_key2 += 1
            st.experimental_rerun()


        st.markdown("""___""")


    if __name__ == "__main__":
        HangMan2()



