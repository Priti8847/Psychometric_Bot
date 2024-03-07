import chatterbot
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import streamlit as st


# Set page config and custom theme
st.set_page_config(
    page_title="Psychometric Bot",
    page_icon="🧠",  # Replace with a brain icon
    layout="wide",  # Use a wider layout for better organization
    initial_sidebar_state="expanded",  # Optionally expand the sidebar
    
)
hide_default_format = """
       <style>
       #MainMenu {visibility: hidden; }
       footer {visibility: hidden;}
       </style>
       """
st.markdown(hide_default_format, unsafe_allow_html=True)
# Load HTML and CSS files
def load_css(file_path):
    with open(file_path) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

def load_html(file_path):
    with open(file_path) as f:
        st.markdown(f.read(), unsafe_allow_html=True)

def main():
    load_css("style.css")
    load_html("style.html")

# Create and train the chatbot
bot = ChatBot("Psychometric Bot", read_only=False, logic_adapters=["chatterbot.logic.BestMatch"])

# Define categories for each question
neuroticism_questions = [
    "Do you often expect to be encouraged by your friends?",
    "Does the answer ’no’ given by someone seems to you disagreeable?",
    "Does your mind often change?",
    "Do you sometimes experience unreasonable distress?",
    "Do you feel embarrassed while wanting to talk to an attractive stranger?",
    "Do you often get worried about things that you don't say or do?",
    "Does your feelings easily hurt?",
    "Do you experience excessive power and sometimes also excessive weakness?",
    "Whenever someone scolds you, do you, in turn, scold them?",
    "Do you experience yourself sometimes guilty?",
    "Do you consider yourself a person in a stressful situation?",
    "After completing an important task, do you worry that you could’ve done better?",
    "Do a series of thoughts interrupt you in your sleep?",
    "Does your heartbeat often increase and you feel nervous?",
    "Do you feel trembling or falter sometimes?",
    "Are you an easy person to be excited?",
    "Are you concerned with the possibilities of sad things that may happen in the future?",
    "you have very terrible dreams at night?",
    "Do you feel sad about physical suffering and hardships?",
    "Do you consider yourself a quick rubbing person?",
    "Do you feel hurt when people point out mistakes in you or in your work?",
    "Do you suffer from inferior emotion?",
    "Do you worry about your health?",
    "Do you suffer from drowsiness?"
]

extroversion_questions = [
    "Do you become frequently submerged with excitation?",
    "Do you mostly keep yourself free from worries?",
    "Do you re-think by stopping for the inclusion of a task before you begin a task?",
    "Do you often say and do things without consideration?",
    "Are you ready to do anything for adventure?",
    "Are you often a practitioner to make immediate decisions and make immediate assignments on it?",
    "Do you mostly like studying more than meeting people?",
    "Do you like to travel?",
    "Do you want to keep a few but close friends?",
    "Do you mostly practice wandering in your fantasy world?",
    "Do you mostly let yourself enjoy in opportunities of fun and enjoyment?",
    "Do people think you’re a lively person?",
    "Do most remain calm when you’re with others?",
    "If you have to gain information regarding a particular topic, do you prefer consulting books rather that people?",
    "Do you like the type of work in which excessive concentration is expected?",
    "Do you hate the mass group who joke each other among themselves?",
    "Do you like to do tasks where you need to work quickly?",
    "Are you slow in your work and do not rush?",
    "Do you like to talk so much that you'd not miss a chance to brat-chat even from a stranger?",
    "Will you be sad if you don’t often meet many people?",
    "Will you say that you have enough self-confidence?",
    "Do you feel yourself capable on an amnesty occasion to enjoy your full pleasure?",
    "Can you make damp opportunities and parties live?",
    "Do you like blowing fun of others?"
]

lie_questions = [
    "Do you decide to do a piece of work without worrying about inconveniences?",
    "Do you sometimes find it difficult to control yourself in a state of aggression?",
    "Do you sometimes have thoughts and emotions in mind that you want to hide from others?",
    "Are all your habits best and desirable?",
    "Do you gossip or chit-chat?",
    "Will you give correct information about all the items to the taxman when you are sure that the taxman can never catch you?",
    "Have you ever given a set time or the work to meet someone and reached punctually?",
    "From the people you know, are there some that you definitely do not like?",
    "Do you also discuss topics that do not have any specific information to you?"
]



# Train the chatbot
neuroticism_answers = ["Yes", "Yes", "Yes", "Yes", "Yes", "Yes", "Yes", "Yes", "Yes", "Yes", "Yes", "Yes", "Yes", "Yes", "Yes", "Yes", "Yes", "Yes", "Yes", "Yes", "Yes", "Yes", "Yes", "Yes"]
extroversion_answers = ["Yes", "Yes", "No", "Yes", "Yes", "Yes", "No", "Yes", "No", "Yes", "Yes", "Yes", "No", "No", "No", "No", "Yes", "No", "Yes", "Yes", "Yes", "No", "Yes", "Yes"]
lie_answers = ["Yes", "No", "No", "Yes", "No", "Yes", "No", "No", "NO"]

list_to_train = [
    # Neuroticism category
    "Bot: " + neuroticism_questions[0] + "\nUser: Yes",
    "Bot: " + neuroticism_questions[1] + "\nUser: Yes",
    "Bot: " + neuroticism_questions[2] + "\nUser: Yes",
    "Bot: " + neuroticism_questions[3] + "\nUser: Yes",
    "Bot: " + neuroticism_questions[4] + "\nUser: Yes",
    "Bot: " + neuroticism_questions[5] + "\nUser: Yes",
    "Bot: " + neuroticism_questions[6] + "\nUser: Yes",
    "Bot: " + neuroticism_questions[7] + "\nUser: Yes",
    "Bot: " + neuroticism_questions[8] + "\nUser: Yes",
    "Bot: " + neuroticism_questions[9] + "\nUser: Yes",
    "Bot: " + neuroticism_questions[10] + "\nUser: Yes",
    "Bot: " + neuroticism_questions[11] + "\nUser: Yes",
    "Bot: " + neuroticism_questions[12] + "\nUser: Yes",
    "Bot: " + neuroticism_questions[13] + "\nUser: Yes",
    "Bot: " + neuroticism_questions[14] + "\nUser: Yes",
    "Bot: " + neuroticism_questions[15] + "\nUser: Yes",
    "Bot: " + neuroticism_questions[16] + "\nUser: Yes",
    "Bot: " + neuroticism_questions[17] + "\nUser: Yes",
    "Bot: " + neuroticism_questions[18] + "\nUser: Yes",
    "Bot: " + neuroticism_questions[19] + "\nUser: Yes",
    "Bot: " + neuroticism_questions[20] + "\nUser: Yes",
    "Bot: " + neuroticism_questions[21] + "\nUser: Yes",
    "Bot: " + neuroticism_questions[22] + "\nUser: Yes",
    "Bot: " + neuroticism_questions[23] + "\nUser: Yes",

    

    # Extroversion category
    "Bot: " + extroversion_questions[0] + "\nUser: Yes",
    "Bot: " + extroversion_questions[1] + "\nUser: Yes",
    "Bot: " + extroversion_questions[2] + "\nUser: No",
    "Bot: " + extroversion_questions[3] + "\nUser: Yes",
    "Bot: " + extroversion_questions[4] + "\nUser: Yes",
    "Bot: " + extroversion_questions[5] + "\nUser: Yes",
    "Bot: " + extroversion_questions[6] + "\nUser: No",
    "Bot: " + extroversion_questions[7] + "\nUser: Yes",
    "Bot: " + extroversion_questions[8] + "\nUser: No",
    "Bot: " + extroversion_questions[9] + "\nUser: Yes",
    "Bot: " + extroversion_questions[10] + "\nUser: Yes",
    "Bot: " + extroversion_questions[11] + "\nUser: Yes",
    "Bot: " + extroversion_questions[12] + "\nUser: No",
    "Bot: " + extroversion_questions[13] + "\nUser: No",
    "Bot: " + extroversion_questions[14] + "\nUser: No",
    "Bot: " + extroversion_questions[15] + "\nUser: No",
    "Bot: " + extroversion_questions[16] + "\nUser: Yes",
    "Bot: " + extroversion_questions[17] + "\nUser: No",
    "Bot: " + extroversion_questions[18] + "\nUser: Yes",
    "Bot: " + extroversion_questions[19] + "\nUser: Yes",
    "Bot: " + extroversion_questions[20] + "\nUser: Yes",
    "Bot: " + extroversion_questions[21] + "\nUser: No",
    "Bot: " + extroversion_questions[22] + "\nUser: Yes",
    "Bot: " + extroversion_questions[23] + "\nUser: Yes",

    # Lie category
    "Bot: " + lie_questions[0] + "\nUser: Yes",
    "Bot: " + lie_questions[1] + "\nUser: No",
    "Bot: " + lie_questions[2] + "\nUser: No",
    "Bot: " + lie_questions[3] + "\nUser: Yes",
    "Bot: " + lie_questions[4] + "\nUser: No",
    "Bot: " + lie_questions[5] + "\nUser: Yes",
    "Bot: " + lie_questions[6] + "\nUser: No",
    "Bot: " + lie_questions[7] + "\nUser: No",
    "Bot: " + lie_questions[8] + "\nUser: No",
    
]

# Train the chatbot
list_trainer = ListTrainer(bot)
list_trainer.train(list_to_train)

# Streamlit UI
st.title("Psychometric Bot")
user_responses = {}

for conversation in list_to_train:
    bot_message, user_message = conversation.split('\n')
    question = bot_message.split(': ')[1]
    options = ["Yes", "No"]
    selected_option = st.radio(f"Bot: {question}", options, key=question)
    user_responses[question.lower()] = selected_option.lower()  # Convert to lowercase for consistency
   
analysis_button = st.button("Analyze Responses")

def analyze_responses(responses):
    neuroticism_score = sum(1 for question, answer in zip(neuroticism_questions, neuroticism_answers) if responses.get(question.lower()) == answer.lower())
    extroversion_score = sum(1 for question, answer in zip(extroversion_questions, extroversion_answers) if responses.get(question.lower()) == answer.lower())
    lie_score = sum(1 for question, answer in zip(lie_questions, lie_answers) if responses.get(question.lower()) == answer.lower())

    neuroticism_total = len(neuroticism_questions)
    extroversion_total = len(extroversion_questions)
    lie_total = len(lie_questions)

    result = f"Neuroticism Score: {neuroticism_score}/{neuroticism_total}, Extroversion Score: {extroversion_score}/{extroversion_total}, Lie Score: {lie_score}/{lie_total}"

    return result

if analysis_button:
    analysis_result = analyze_responses(user_responses)
    st.markdown(f"**Analysis Result:** {analysis_result}")

if analysis_button:
    analysis_result = analyze_responses(user_responses)

    # Extract neuroticism score
    neuroticism_score = int(analysis_result.split(':')[1].split('/')[0])

    # Neuroticism level declaration
    if 1 <= neuroticism_score <= 11:
        neuroticism_level = "Low Neuroticism"
    elif 12 <= neuroticism_score <= 18:
        neuroticism_level = "Moderate Neuroticism"
    elif 19 <= neuroticism_score <= 24:
        neuroticism_level = "High Neuroticism"
    else:
        neuroticism_level = "Invalid Score"

    st.markdown(f"**Neuroticism Level:** {neuroticism_level}")

    # Explanations based on neuroticism score
    if neuroticism_level == "High Neuroticism":
        neuroticism_explanation = """
        Based on the assessment,it appears that you exhibit higher levels of neuroticism,
        Individuals with this trait often demonstrate heightened sensitivity, apprehension, and 
        a tendency to worry. Impulsivity, pessimism, and difficulties in coping with stress may 
        be areas of concern. Emotions are likely felt intensely, leading to a tendency to get 
        upset easily. Social discomfort and susceptibility to having feelings hurt are common 
        experiences for those high in neuroticism. Additionally, struggles with resisting 
        distractions or temptations may be apparent.
        """
    elif neuroticism_level == "Low Neuroticism":
        neuroticism_explanation = """
        Upon evaluation, it appears that you have lower levels of neuroticism. Individuals with 
        this trait often exhibit a calm demeanor under pressure. They tend to be slow to anger,
        unaffected by others' opinions, and are less prone to stress over minor issues. Even-
        tempered and possessing good emotional control, those low in neuroticism generally
        navigate challenges with composure.
        """
    else:
        neuroticism_explanation = "Explanation not available for this score range."

    st.markdown("**Neuroticism Explanation:**")
    st.markdown(neuroticism_explanation)

if analysis_button:
    analysis_result = analyze_responses(user_responses)

    # Extract extroversion score
    extroversion_score = int(analysis_result.split(':')[2].split('/')[0])

    # Extroversion level declaration
    if 1 <= extroversion_score <= 11:
        extroversion_level = "Low Extroversion"
    elif 12 <= extroversion_score <= 18:
        extroversion_level = "Moderate Extroversion"
    elif 19 <= extroversion_score <= 24:
        extroversion_level = "High Extroversion"
    else:
        extroversion_level = "Invalid Score"

    st.markdown(f"**Extroversion Level:** {extroversion_level}")

    # Explanations based on extroversion score
    if extroversion_level == "High Extroversion":
        extroversion_explanation = """
        Following the assessment, it seems that you exhibit higher levels of extraversion.
        Individuals with this trait are often characterized as 'the life of the party.' They are 
        outgoing, friendly, easy to connect with, and tend to be talkative. High extraversion 
        individuals are typically popular, energetic, and optimistic. Enjoying social interactions, 
        they thrive on being around others and often find themselves in the spotlight. Their 
        assertive and outgoing nature often positions them as leaders in social situations and group projects. 
        """
    elif extroversion_level == "Low Extroversion":
        extroversion_explanation = """
        Upon evaluation, it appears that you have lower levels of extraversion. Individuals with 
        this trait tend to be more reserved, maintaining a small, close-knit circle of friends and 
        preferring not to be the center of attention. It may take some time for individuals low on 
        extraversion to open up to new people, and they often lean towards low-key activities, 
        such as movie nights rather than big parties. Being introspective, self-aware, and 
        valuing privacy are common characteristics among those with lower extraversion.
        """
    else:
        extroversion_explanation = "Explanation not available for this score range."

    st.markdown("**Extroversion Explanation:**")
    st.markdown(extroversion_explanation)

