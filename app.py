import streamlit as st
from model.bert_model import BertSimilarity

st.title('Text Similarity Application')

text1 = st.text_area("Text 1")
text2 = st.text_area("Text 2")

if st.button('Calculate Similarity'):
    model = BertSimilarity()
    similarity_score = model.compute_similarity(text1, text2)
    st.write('Similarity Score:', similarity_score)