import streamlit as st
import requests
from streamlit_lottie import st_lottie
from PIL import Image
from flask import Flask
#streamlit run website.py

def website():
  return
st.set_page_config(page_title="My Web Page", page_icon=":tada:", layout="wide")

def load_lottieur(url):
  r=requests.get(url)
  if r.status_code !=200:
    return None
  return r.json()


#use local CSS
def local_css(file_name):
  with open(file_name) as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style.css")

#load assests
lottie_coding=load_lottieur("https://lottie.host/d54f8819-3b40-40cd-a007-f66c51b9e1a9/HJtPPEs7qI.json")
Walking_Dog = Image.open("Chance.jpg")
resized_WD = Walking_Dog.resize((350, 350))
Sleeping_dog = Image.open("PXL_20231005_205004791~3.jpg")
resized_SD = Sleeping_dog.resize((350, 350))

#Header section
with st.container ():
  st.subheader("Hi, I am Zach 🙋‍♂️")
  st.title("A sales expert in Austin Texas")
  st.markdown(
    """
    **About me:**  \nThe Sales Whiz with a Tech-Loving Heart (and an Awesome Amstaff!)

    \nA results-driven sales professional with a proven track record of consistently achieving 90% of my sales goals over 6 years, generating \$70k - \$100k thousand in monthly revenue. I'm not afraid to roll up my sleeves, and am a cold-calling machine, averaging 80-100 calls daily while maintaining a 5% conversion rate.

    \nI'm not just your average salesperson. I'm genuinely passionate about how technology shapes our lives. I'm fascinated by phones and their potential to revolutionize how we interact with the world.

    \nWhile I may not have a grand story of tech problem-solving on a global scale, I'm the go-to tech guy for my family and friends. Whether it's migrating phones, learning and managing new software, or troubleshooting glitches, I'm always happy to lend a hand.

    \nLastly, of course, my life wouldn't be complete without Chance, my loyal Amstaff companion. He's the perfect blend of energy and chill, always there to offer support during challenging tasks or provide a much-needed cuddle during frustrating moments. 
    Our daily 4-mile walks help me clear my head and return to work refreshed and focused.

    \nWhen I'm not busy closing deals or geeking out over the latest tech, you can find me cooking and watching ancient marvels on youtube.

    \nLet's connect and discuss how my passion for sales and technology can help your business thrive!
    
    """
    )
  st.write("[Check Out My Favorite Tech Podcast >](https://www.youtube.com/@TheVerge)")

# What I Do
with st.container():
  st.write("----")
  left_column, right_column = st.columns(2)
  with left_column:
    st.header ("What I do")
    st.write("##")
    st.write(
        """
        - Consistently exceed sales targets, and strive to educate customers in technology and its ability to solve their problem.
        - Build strong client relationships, expanding market through strategic sales methodology.
        - Develop and implement effective training programs, improving new hire productivity and onboarding time.
        - Lead and mentor high-performing teams, consistently exceeding sales targets and encouraging collaboration.
        - Proficient in various CRM software, including Salesforce, Dynamics, and Zoho. Currently working on Salesforce admin modules

        """
    )
  with right_column:
    st_lottie(lottie_coding, height=400, key="coding")   

#project 1
with st.container():
  st.write("---")
  st.subheader("Key Competencies / Concepts That Make Me Amazing")
  st.write("##")
  image_column, text_column = st.columns((1,5))
  #insert image
  with image_column:
    st.image(resized_SD)
  with text_column:
    st.subheader("How I rely on a routine to maximise my week")
    st.write( 
      """
      **Let me talk about routines!!**
      \nI thrive on structure and believe a well-defined routine is essential for maximizing productivity. 
      However, I also recognize the importance of adaptability in a fast-paced, technology-driven environment. My routine is designed to balance both focus and flexibility.

      \n**Some Examples:**\n
      Early Start and Strategic Planning:
      My day begins at 5 a.m. with three hours dedicated to reflection, goal setting, and creating a prioritized action plan. 
      This practice ensures I enter the workday at 8 a.m. with clarity and purpose.

      Morning Outreach and Physical Activity:
      I promptly initiate outreach to new leads, establishing initial contact through voicemail and personalized text messages. 
      This is followed by a brisk walk, combining physical activity with mental refresh.

      Client Engagement and Relationship Building:
      Midday is focused on nurturing leads through follow-up calls, addressing inquiries, and scheduling consultations. 
      Another walk in the afternoon provides a brief respite and allows me to prepare for the afternoon/evening appointments.

      Dedicated Client Time and Future Planning:
      Late afternoons are reserved for client meetings and consultations, where I address their needs and guide them through the decision-making process.
      I conclude each workday by reviewing outcomes and preparing for the next day's activities.

      Professional Development and Strategic Networking:
      Evenings are allocated to continuous learning through industry publications, podcasts, and occasional networking events.
      I often incorporate physical activity into this time, engaging in walks or visiting the local dog park.
      During football season, I may choose to combine professional development with social interaction at a local establishment while supporting my team (Go Cowboys!).

      Rest and Recharge:
      I disconnect from most technology by 9 p.m., ensuring adequate time for relaxation and personal pursuits.  
      """
    )
    st.write("[Some Wisdom >](https://www.youtube.com/watch?v=6_kVEz0HQPg)")  

#project 2
with st.container():
  image_column, text_column = st.columns((1,5))
  with image_column:
    st.image(resized_WD)
  with text_column:
    st.subheader("The Value of a Network and an always learning Mentality")
    st.write(
      """
      As Jack Welch famously said, "If you're the smartest person in the room, you're in the wrong room."
      
      I embrace this philosophy by actively seeking environments where I can learn and grow. 
      Engaging with diverse perspectives not only expands my knowledge but also provides valuable insights and solutions. 
      
      Recognizing that expertise is domain-specific, I cultivate a strong network of professionals who can offer guidance and understanding in areas where I am less experienced. 
      
      This 'always learning' mentality, combined with a robust network, reduces the risk of being misled and opens doors to new opportunities and personal development.
      """
    )
    st.write("[Networking Awesomeness >](https://www.youtube.com/watch?v=63Ku_oo6tW8)")
# Contact
with st.container():
  st.write("----")
  st.header(" Connect with me!")
  st.write("##")


#documnetaion: https://formsubmit.com/ !!!! Change Email!!!!
  contact_form = """
  <form action="https://formsubmit.co/zackary.lantz@gmail.com" method="POST">
     <input type="hidden" name="captcha" value="false">  
     <input type="text" name="name" placeholder="Your Name" required>
     <input type="email" name="email" placeholder="Your Email" required>
     <textarea name="message" placeholder="Your message here:" required></textarea>
     <button type="submit">Send</button>
</form>
"""

left_column, right_column= st.columns(2)
with left_column:
  st.markdown(contact_form, unsafe_allow_html=True)
with right_column:
  st.empty()
