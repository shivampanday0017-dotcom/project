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
  
st.write("2. What is the capital of India?
A) Mumbai
B) New Delhi
C) Kolkata
D) Chennai")
if ans.lower()=="b":
  score+=5
st.write("-----------------------------")  

st.write("3. Which planet is known as the Red Planet?
A) Earth
B) Venus
C) Mars
D) Jupiter")
if ans.lower()=="d":
  score+=5
st.write("-----------------------------")  

st.write("4. Which is the largest ocean in the world?
A) Atlantic Ocean
B) Indian Ocean
C) Pacific Ocean
D) Arctic Ocean")
if ans.lower()=="c":
  score+=5
st.write("-----------------------------")  

st.write("5. Who invented the light bulb?
A) Alexander Graham Bell
B) Thomas Edison
C) Isaac Newton
D) Albert Einstein")
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
  
  
