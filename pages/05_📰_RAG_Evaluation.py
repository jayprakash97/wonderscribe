import streamlit as st
import requests
import json
import evaluate
import pandas as pd
import base64

# Set page configuration
st.set_page_config(page_title="RAG Model Evaluation", page_icon="📰", layout="wide")

# Background image URL
background_image_url = "https://raw.githubusercontent.com/Natsnet/WS_Back_img/main/WonderScribe_bk_blue_page_1.jpg"

# CSS for background image, custom box, and sidebar
background_css = f"""
<style>
[data-testid="stAppViewContainer"] {{
    background-image: url("{background_image_url}");
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
    background-attachment: fixed;
}}

.custom-box {{
    background-color: rgba(255, 255, 255, 0.8);
    border-radius: 10px;
    padding: 20px;
    margin: 20px auto;
    max-width: 800px;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
    font-family: Arial, sans-serif;
    color: #5481c4;
    line-height: 1.6;
}}
.custom-box h3 {{
    text-align: center;
    margin-top: 20px;
}}
.custom-box ul {{
    padding-left: 20px;
}}
/* Sidebar customization */
[data-testid="stSidebar"] {{
    background-color: #f0f4ff; /* Light blue */
    color: #5481c4; /* Match the main page color */
    font-family: Arial, sans-serif;
    font-size: 18px; /* Adjust font size */
}}
[data-testid="stSidebar"] * {{
    color: #5481c4; /* Sidebar text color */
}}
[data-testid="stSidebar"] .stMarkdown {{
    text-align: center; /* Center text inside sidebar */
}}
</style>
"""

# Apply CSS styles
st.markdown(background_css, unsafe_allow_html=True)

# Function to add the WonderScribe logo to the top of the sidebar
def add_logo_to_sidebar_top(logo_path, width="250px"):
    with open(logo_path, "rb") as f:
        encoded_logo = base64.b64encode(f.read()).decode("utf-8")
    st.sidebar.markdown(
        f"""
        <style>
            [data-testid="stSidebar"]::before {{
                content: '';
                display: block;
                background-image: url("data:image/png;base64,{encoded_logo}");
                background-size: contain; /* Ensure the logo scales proportionally */
                background-repeat: no-repeat;
                background-position: top center;
                height: 250px; /* Increase height to fit the full logo */
                padding-top: 20px; /* Add space above the logo */
                margin-bottom: 20px; /* Add space below the logo */
            }}
        </style>
        """,
        unsafe_allow_html=True,
    )

# Add the WonderScribe logo to the sidebar
add_logo_to_sidebar_top("pages/images/Updated_WonderS_logo.png", width="250px")

# Title for the page
st.markdown(
    "<h1 style='color: #5481c4; text-align: center; font-size: 3em;'>RAG Model Evaluation</h1>",
    unsafe_allow_html=True,
)

validation_query_response = {
  0: {"query": "friendships between boy and girl",
      "gold_response": "story about etc "},
  1: {"query": "Brushing the tooth",
      "gold_response": " "}
}

def rouge_scores(predicted_response, gold_response):
    try:
        rouge = evaluate.load('rouge')
        scores = rouge.compute(
            predictions=[predicted_response],
            references=[gold_response],
            use_aggregator=True
        )
        return scores
    except Exception as e:
        return f"Error computing ROUGE score: {str(e)}"

def bleu_scores(predicted_response, gold_response):
    try:
        bleu = evaluate.load('bleu')
        bleu_scores = bleu.compute(
            predictions=[predicted_response], 
            references=[[gold_response]]
        )
        return bleu_scores
    except Exception as e:
        return f"Error computing BLEU score: {str(e)}"

def bert_scores(predicted_response, gold_response):
    try:
        bertscore = evaluate.load('bertscore')
        bert_scores = bertscore.compute(
            predictions=[predicted_response], 
            references=[gold_response], 
            lang='en'
        )
        # Average the scores
        bert_scores['precision'] = sum(bert_scores['precision']) / len(bert_scores['precision'])
        bert_scores['recall'] = sum(bert_scores['recall']) / len(bert_scores['recall'])
        bert_scores['f1'] = sum(bert_scores['f1']) / len(bert_scores['f1'])
        return bert_scores
    except Exception as e:
        return f"Error computing BERT score: {str(e)}"
 
def fetch_story_data(payload):
    AWS_API_URL = "https://wacnqhon34.execute-api.us-east-1.amazonaws.com/dev/"
    headers = {
        "Content-Type": "application/json"
    }
   
    json_data = payload

    response = requests.post(AWS_API_URL, headers=headers, json=json_data)
    if response.status_code == 200:
        data = response.json() 
        return data["story_texts"]
    else:
        return []

def main():
    validation_query_response_list = '''
    [
        {"query": "Female,Srila,children,Magical Kingdoms,Fantacy,Brushing the tooth,Develop hygiene habbits,300",
         "gold_response": "In the Magical Kingdoms, there lived a young girl named Srila, whose adventures were the stuff of legends. Srila was a curious and imaginative child, always eager to explore the wonders that surrounded her. One day, as she wandered through the enchanted forest, she stumbled upon a hidden path that led her to a magnificent castle. As Srila approached the castle, she was greeted by a friendly group of talking animals, who welcomed her with open arms. They marveled at her bravery and invited her to join them on a grand adventure through the kingdom. Together, Srila and her new animal friends explored the winding corridors of the castle, discovering hidden rooms filled with ancient magic and mystical artifacts. They encountered a wise old wizard who shared with them the importance of maintaining good hygiene habits, explaining how cleanliness and self-care were essential for staying healthy and strong. Srila listened intently, her eyes wide with fascination. She had never thought much about the importance of hygiene, but the wizard's words resonated with her. She realized that by keeping herself and her surroundings clean, she could not only stay healthy but also feel more confident and empowered. Inspired by the wizards teachings, Srila and her animal friends set out to explore the kingdom, putting their newfound knowledge into practice. They washed their hands regularly, brushed their teeth, and kept their living spaces tidy. As they traveled, they encountered other residents of the Magical Kingdoms, sharing their lessons on the importance of hygiene. Over time, Srila and her friends noticed a remarkable difference in their overall well-being. They felt healthier, happier, and more confident. The residents of the Magical Kingdoms were also inspired by their example, and soon, the entire kingdom was filled with the joyful sounds of laughter and the sweet scent of cleanliness. As Srila and her friends prepared to return home, they knew that they had not only discovered the power of good hygiene but also the importance of sharing their knowledge with others. With a renewed sense of purpose, they bid farewell to the Magical Kingdoms, their hearts filled with the promise of a future where everyone could enjoy the benefits of a clean and healthy lifestyle. And so, Srila's adventure in the Magical Kingdoms came to a close, but the lessons she had learned would stay with her forever. From that day on, she made sure to maintain her hygiene habits, and she even started a campaign to teach others the importance of cleanliness and self-care. Srila's story became a shining example of how a little bit of effort can go a long way in creating a healthier and happier world." 
        },
        {"query": "Male,John,children,Magical Kingdoms,Fantacy,Friendship between two boys,build trust,300",
         "gold_response": " In the Magical Kingdoms, there lived a young man named John. He was not like the other residents - John possessed a unique gift, a deep connection to the mystical forces that permeated the land. While others marveled at the wonders around them, John could sense the underlying currents of magic, feeling its pulse through his veins. One day, as John wandered the winding paths, he stumbled upon a hidden grove. There, he encountered a wise old wizard, who recognized the spark of potential within the young man. The wizard offered to teach John the ways of the Magical Kingdoms, sharing ancient secrets and guiding him on a journey of self-discovery. Eager to learn, John accepted the wizard's offer, and together they delved into the mysteries of the land. John mastered spells, communed with the elements, and even befriended the elusive creatures that roamed the Magical Kingdoms. As his skills grew, so did his sense of wonder and responsibility. However, John's journey was not without its challenges. He encountered those who sought to misuse the power of the Magical Kingdoms for their own gain, sowing discord and mistrust among the people. John knew he had to act, to protect the delicate balance of the land he had grown to love. Guided by the wizard's wisdom and his own growing understanding, John set out to confront the forces of darkness. Through acts of bravery, compassion, and unwavering trust, he slowly won over the skeptics and forged alliances with the diverse inhabitants of the Magical Kingdoms. In the end, John's journey taught him a valuable lesson: that true power lies not in domination, but in the strength of one's character and the bonds of trust forged with others. By embracing this lesson, John became a beacon of hope, inspiring the people of the Magical Kingdoms to work together and build a future of peace and prosperity. And so, John's story became a testament to the power of trust, a reminder that even in the most fantastical of realms, the greatest magic lies in the connections we forge with one another. The Magical Kingdoms flourished under his guidance, a testament to the transformative power of a single individual who dared to believe in the goodness of others."
        },
        {"query": "Male, Mike,children,Pirate Ship,Fantacy,A kid astronaut explores different planets,kindness,300",
         "gold_response": "In the Magical Kingdoms, there lived a young girl named Srila, whose adventures were the stuff of legends. Srila was a curious and imaginative child, always eager to explore the wonders that surrounded her. One day, as she wandered through the enchanted forest, she stumbled upon a hidden path that led her to a magnificent castle. As Srila approached the castle, she was greeted by a friendly group of talking animals, who welcomed her with open arms. They marveled at her bravery and invited her to join them on a grand adventure through the kingdom. Together, Srila and her new animal friends explored the winding corridors of the castle, discovering hidden rooms filled with ancient magic and mystical artifacts. They encountered a wise old wizard who shared with them the importance of maintaining good hygiene habits, explaining how cleanliness and self-care were essential for staying healthy and strong. Srila listened intently, her eyes wide with fascination. She had never thought much about the importance of hygiene, but the wizard's words resonated with her. She realized that by keeping herself and her surroundings clean, she could not only stay healthy but also feel more confident and empowered. Inspired by the wizards teachings, Srila and her animal friends set out to explore the kingdom, putting their newfound knowledge into practice. They washed their hands regularly, brushed their teeth, and kept their living spaces tidy. As they traveled, they encountered other residents of the Magical Kingdoms, sharing their lessons on the importance of hygiene. Over time, Srila and her friends noticed a remarkable difference in their overall well-being. They felt healthier, happier, and more confident. The residents of the Magical Kingdoms were also inspired by their example, and soon, the entire kingdom was filled with the joyful sounds of laughter and the sweet scent of cleanliness. As Srila and her friends prepared to return home, they knew that they had not only discovered the power of good hygiene but also the importance of sharing their knowledge with others. With a renewed sense of purpose, they bid farewell to the Magical Kingdoms, their hearts filled with the promise of a future where everyone could enjoy the benefits of a clean and healthy lifestyle. And so, Srila's adventure in the Magical Kingdoms came to a close, but the lessons she had learned would stay with her forever. From that day on, she made sure to maintain her hygiene habits, and she even started a campaign to teach others the importance of cleanliness and self-care. Srila's story became a shining example of how a little bit of effort can go a long way in creating a healthier and happier world." 
        }
    ] 
    '''

    json_data = json.loads(validation_query_response_list)
 
    for item in json_data:
        query_string = item.get("query")
        gold_response = item.get("gold_response")
    
        gender, name, audience, setting, genre, topic, moral, word_count = query_string.split(',')
    
        st.write(f"{audience} {genre} {name} {moral} {setting} {word_count} ")
    
        payload = {
            "audience" : audience,
            "story_type" : genre,
            "main_character" : name,
            "story_theme" : genre, 
            "moral_lesson" : moral,
            "setting" : setting, 
            "word_count" : word_count,
            "story_lang" : "English",
            "api_Path" : "getStory"
        }
        
        story_texts = fetch_story_data(payload)
        # st.write(story_texts)
        predicated_response = ' '.join(story_texts)
    
        st.write(f"predicated_response - {predicated_response}")
        
        st.write("##### Evaluation Scores #####")
        #st.write(f"gold_response - {gold_response}")
    
        st.write(f"gold_response - {gold_response}")
      
        cal_rouge_scores= rouge_scores(predicated_response, gold_response)
        # st.write(f"Calculated Rouge Scores - {cal_rouge_scores}")
    
        st.write("##### Rouge Scores #####")
        st.write(rouge_scores(predicated_response, gold_response))
            
        st.write("##### Bleu Scores #####")
        st.write(bleu_scores(predicated_response, gold_response) )
        
        st.write("##### Bert Scores #####")
        st.write(bert_scores(predicated_response, gold_response))
        
        # cal_bert_scores = bert_scores(predicated_response, gold_response)
        # st.write(f"Calculated Bert  Scores - {bert_scores}")

def file_display():
    st.write("#### RAG Model Evaluation Results :")
    file_path = "pages/file.xlsx"
    try:
      df = pd.read_excel(file_path)
      st.dataframe(df) 
    except FileNotFoundError:
      st.error(f"File was not found at path")

if __name__ == "__main__":
    # main()
    file_display()

