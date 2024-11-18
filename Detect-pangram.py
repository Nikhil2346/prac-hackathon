def is_pangram(st):
    return True if len(set(i for i in st.lower() if i.isalpha()))>=26 else False