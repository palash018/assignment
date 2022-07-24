import streamlit as st

st.title('Multiplication of 2 numbers')
a = st.number_input('Enter a number')
b = st.number_input('Enter another number')
c= st.number_input('Enter another number')
l=[a,b,c]
result = max(l)
st.write(result)