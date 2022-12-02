import streamlit as st
from demos import examples


def show_examples():
    st.write(
        """# 📸 Tijd om te shinen""")
    st.write(""" """)
    st.write(""" """)
    st.write("""Aan het begin,""")
    st.write("""Vul je eerst je naam in.""")
    st.write(""" """)
    st.write("""Vervolgens laat je zien van jezelf de beste versie,""")
    st.write("""En neem dan snel een selfie.""")
    st.markdown("""---""")

    examples.show()


if __name__ == "__main__":
    pass