import streamlit as st
score=0
st.write("1. Who is the Prime Minister of India?")
st.write("A) Narendra Modi")
st.write("B) Rahul Gandhi")
st.write("C) Amit Shah")
st.write("D) Arvind Kejriwal")
ans=text_input("ente your answer")
if ans.lower()=="a":
  score+=5
st.write("-----------------------------")  
  
st.write("2. What is the capital of India?")
st.write(A) Mumbai")
st.write("B) New Delhi")
st.write("C) Kolkata")
st.write("D) Chennai")
if ans.lower()=="b":
  score+=5
st.write("-----------------------------")  

st.write("3. Which planet is known as the Red Planet?")
st.write("A) Earth")
st.write("B) Venus")
st.write("C) Mars")
st.write("D) Jupiter")
if ans.lower()=="d":
  score+=5
st.write("-----------------------------")  

st.write("4. Which is the largest ocean in the world?")
st.write("A) Atlantic Ocean")
st.write("B) Indian Ocean")
st.write("C) Pacific Ocean")
st.write("D) Arctic Ocean")
if ans.lower()=="c":
  score+=5
st.write("-----------------------------")  

st.write("5. Who invented the light bulb?")
st.write("A) Alexander Graham Bell")
st.write("B) Thomas Edison")
st.write("C) Isaac Newton")
st.write("D) Albert Einstein")
if ans.lower()=="a":
  score+=5
st.write("-----------------------------")
st.write(score)
if score==5:
    st.write("congratulation you are 1st position")
    st.balloons()
if score==4:
    st.write("congratulation you are 2st position")
    st.snow()
else:
  st.write("better luck next time ")
  
  
