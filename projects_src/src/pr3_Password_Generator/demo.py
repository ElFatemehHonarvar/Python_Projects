
import streamlit as st
from password_generator import PinCodeGenerator, RandomPasswordGenerator, MemorablePasswordGenerator

col1, col2 = st.columns(2)

with col2:
    # link for emoji : https://github.com/ikatyang/emoji-cheat-sheet
    st.title(":wave: Welcome to our Password Generator Site ")
    st.markdown("### 👌 Here you find a lot of recommendations for creating a secure password")


with col1:
    st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT_Xe04J96BjUzU839NbDWAGqL9sONJ65TjFQ&s", width=250,)

    password_type = st.radio("what is you method?",
                ["PinCodeGenerator", "RandomPasswordGenerator", "MemorablePasswordGenerator"])

    if password_type == "PinCodeGenerator":
        length = st.slider("Select the Length of Password", min_value=4, max_value=20)

        generator = PinCodeGenerator(length)
        if st.button("show", type="primary"):
            st.info(f"{generator.generate()}")

    elif password_type == "RandomPasswordGenerator":
        length = st.slider("Select the Length of Password", min_value=4, max_value=20)
        include_numbers = st.toggle("Select Numbers:yes/no")
        include_symbols = st.toggle("Select Symbols:yes/no")

        generator = RandomPasswordGenerator(length, include_numbers, include_symbols)
        if st.button("show", type="primary"):
            st.write(f"your password is : ```{generator.generate()}```")

    elif password_type == "MemorablePasswordGenerator":
        num_of_words = st.slider("Select the Num of Words", min_value=2, max_value=5)
        random_captalize = st.toggle("Captalization")
        separator = st.text_input("Select your separator unless - is selected", value="-")

        generator = MemorablePasswordGenerator(num_of_words, random_captalize, separator, vocabulary=None)
        if st.button("show", type="primary"):
            st.badge(f"your password is : {generator.generate()}")




