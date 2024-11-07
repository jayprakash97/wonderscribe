import streamlit as st

validation_query_response = {
  0: {"query": "friendships between boy and girl",
      "gold_response": "story about etc "},
  1: {"query": "Brushing the tooth",
      "gold_response": " "}
}

# Function to evaluate RAG system using ROUGE
def rouge_scores(predicated_response, gold_response):
  import evaluate
  rouge = evaluate.load('rouge')
  rouge_scores = rouge.compute(predictions=predicated_response, references=gold_response)
  return rouge_scores

def bleu_scores(predicated_response, gold_response):
  import evaluate
  bleu = evaluate.load('bleu')
  bleu_scores = bleu.compute(predictions=predicated_response, references=gold_response)
  return bleu_scores

def bert_scores(predicated_response, gold_response):
  import evaluate
  bertscore = evaluate.load('bertscore')
  bert_scores = bertscore.compute(predictions=predicated_response, references=gold_response, lang= 'en')
  bert_scores['precision'] = sum(bert_scores['precision']) / len(bert_scores['precision'])
  bert_scores['recall'] = sum(bert_scores['recall']) / len(bert_scores['recall'])
  bert_scores['f1'] = sum(bert_scores['f1']) / len(bert_scores['f1'])
  return bert_scores

import streamlit as st
import requests
import json
import base64 
import re
from io import BytesIO 
from PIL import Image
#import pip
# Install googletrans library using pip
# pip.install('googletrans')
#pip install googletrans
#from googletrans import Translator

# st.set_page_config(page_title="Multiple App", page_icon="👌")
# st.write(print(st.__version__))
col1, col2  = st.columns(2, vertical_alignment="center")
# col1, col2 = st.columns(2, horizontal_alignment="left")
with col1:
    st.image("pages/WS_Logo.png", width=200)
with col2:
    st.write("")
   
# Streamlit app title
# st.title("Welcome to WonderScribe Page", font_size="20px")
st.title("Welcome to WonderScribe Page")
 
# # Create input fields to collect data for the POST request body
# name = st.text_input("Enter your name")
# age = st.number_input("Enter your age", min_value=0)

#========== Function for evaluating RAG application ===========
validation_query_response_list = {
  0: {'query': 'Female Srila children Magical Kingdoms Fantacy Brushing the tooth Develop hygiene habbits 300',
      'gold_response': 'In the enchanting Magical Kingdoms, where unicorns roamed and fairies danced, lived a young girl named Srila. Srilas days were filled with wonder and adventure, but there was one task she often neglected - brushing her teeth. One morning, as Srila was exploring the enchanted forest, she stumbled upon a curious creature. It was a tiny tooth fairy, with delicate wings and a sparkling wand. The tooth fairy fluttered around Srila, sprinkling a magical dust on her teeth. "What is this?" Srila asked, feeling a tingle in her mouth. "This is a special tooth-cleaning dust," the fairy explained. "It will keep your teeth strong and shiny, but you must remember to brush them every day."Srila promised to be more diligent about her dental hygiene. The tooth fairy smiled and vanished in a shower of glitter. From that day on, Srila made brushing her teeth a daily ritual. She used a soft-bristled brush and sweet-tasting toothpaste infused with fairy magic. Srila would sing songs and dance as she brushed, making it a fun and enjoyable activity. As Srilas teeth grew healthier and brighter, she noticed other changes too. Her breath stayed fresh, and she could enjoy all her favorite foods without any discomfort. The tooth fairy would visit occasionally, praising Srilas dedication and rewarding her with small treasures. '},
  1: {'query': 'Mike 400',
      'gold_response': ' '}
}
st.write("1")
st.write(f"validation_query_response.: {validation_query_response_list[0]}")
# Function to evaluate RAG system using ROUGE
def rouge_scores(predicated_response, gold_response):
  import evaluate
  rouge = evaluate.load('rouge')
  rouge_scores = rouge.compute(predictions=predicated_response, references=gold_response)
  return rouge_scores

def bleu_scores(predicated_response, gold_response):
  import evaluate
  bleu = evaluate.load('bleu')
  bleu_scores = bleu.compute(predictions=predicated_response, references=gold_response)
  return bleu_scores

def bert_scores(predicated_response, gold_response):
  import evaluate
  bertscore = evaluate.load('bertscore')
  bert_scores = bertscore.compute(predictions=predicated_response, references=gold_response, lang= 'en')
  bert_scores['precision'] = sum(bert_scores['precision']) / len(bert_scores['precision'])
  bert_scores['recall'] = sum(bert_scores['recall']) / len(bert_scores['recall'])
  bert_scores['f1'] = sum(bert_scores['f1']) / len(bert_scores['f1'])
  return bert_scores


def image_decode(image_data_decode):
    image_data = base64.b64decode(image_data_decode)
    return image.open(BytesIO(image_data))



with st.form("form_key"):
    st.write("Craft personalized stories that bring adventure to life and ignite imagination and creativity")
    gender = st.selectbox("Your Gender", options=["Male", "Female", "Don't want to share"])
    main_character = st.text_input("What will be the name of the main character?", placeholder="Who will star in your story?")
    audience = st.selectbox("Audience", options=["children", "young adult", "adult", "senior"])
    story_setting = st.selectbox("Story Setthing", options=["Magical Kingdoms", "Underwater Kingdoms", "Pirate ships", "Exotic locations", "Imaginary world", "Digital words", "Others"])
    story_type = st.selectbox("Story Type", options=["Fantacy", "Fairy Tales", "Mythology", "Bedtime stories", "Adventure", "Mystery", "Love", "Horror", ])
    story_theme = st.text_input("What would be topic of the story?", placeholder="Leave brief idea of a story")
    moral_lesson = st.text_input("What would be the moral of this story?", placeholder="Enter moral lesson from this story")
    story_length = st.selectbox("Story Length (in words) ", options=["300", "400", "500"])
    
    submit_btn = st.form_submit_button("Submit")

# st.write(f"""Your story summary:\n
# Audience: {audience} \n
# Main Character: {main_character} \n
# Story Setting: {story_setting} \n
# Story Type: {story_type} \n
# Story Theme: {story_theme} \n
# Moral Lesson: {moral_lesson} \n
# Story Size (in words) : {story_length}
# """)

# story_theme_value = st.text_input( value=story_theme)

# AWS API URL for POST request
AWS_API_URL = "https://wacnqhon34.execute-api.us-east-1.amazonaws.com/dev/"
 
# Optional: Set up headers (if using an API key or authentication)
headers = {
 #   "x-api-key": "your-api-key",  # Remove if your API doesn't require a key
    "Content-Type": "application/json",  # Specify the content type for the POST request
}
 
# Create a button that triggers the POST request
if submit_btn:  # st.button("Submit"):
    payload = {
       "story_type" : story_type,
       "main_character" : main_character,
       "story_theme" : story_theme, # 'Brushing the tooth',
       "moral_lesson" : moral_lesson,
       "setting" : story_setting, 
       "word_count" : story_length
      }
    # Create the payload (data) to be sent in the POST request

      
    try:
        json_data = payload
        # Make a POST request to the AWS API
        response = requests.post(AWS_API_URL, headers=headers, json=json_data)
    
        # Check if the request was successful (status code 200-299)
        if response.status_code == 200:
            data = response.json()  # Parse JSON response
            st.success("POST request successful!")
            st.write('debug1')
            
            # Extract the body content, which is a JSON string itself
            body_content = json.loads(data["body"])
            st.write('debug2')
         
            #st.write("Response from API:", body_content)
            # Extract the story text
            story_text = body_content["text"]
          
            st.title("Children's Story")
            st.write(story_text)

            # translator = Translator()
            # english_tax_term = story_text
            # target_language = "french"  # Replace with your desired target language

            # translated_tax_term = translator.translate(english_tax_term, dest=target_language).text
            # st.write(translated_tax_term)
         
            # Base64 encoded image string
            # image1 = image_decode(body_content["image_data_decode"])
            # st.image(image1, caption='Decoded Image', use_column_width=True)
             
            # Alternatively, you can directly pass the binary image data
            # st.image(BytesIO(image_data), caption='Decoded Image', use_column_width=True)

            # image2 = image_decode(body_content["image_data_decode2"])
            # st.image(image2, caption='Decoded Image', use_column_width=True)

            # image3 = image_decode(body_content["image_data_decode3"])
            # st.image(image3, caption='Decoded Image', use_column_width=True)

            # image4 = image_decode(body_content["image_data_decode4"])
            # st.image(image4, caption='Decoded Image', use_column_width=True)

            # image1 = image_decode(body_content["image_data_decode"])
            # st.image(image1, caption='Decoded Image', use_column_width=True)

      #       for 1 in validation_query_response_list.keys():
      #           references_answer.append(validation_questions_answers[i]['gold_answer'])
      #           if validation_questions_answers[i]['gold_answer'] =        "story_type" : story_type,
      #  "main_character" : main_character,
      #  "story_theme" : story_theme, # 'Brushing the tooth',
      #  "moral_lesson" : moral_lesson,
      #  "setting" : story_setting, 
      #  "word_count" : story_length
      #           model_output = 
      #           0: {'query': 'Female Srila children Magical Kingdoms Fantacy Brushing the tooth Develop hygiene habbits 300',
      # 'gold_response': 'In the enchanting Magical Kingdoms, where unicorns roamed and fairies danced, lived a young girl named Srila. Srila's days were filled with wonder and adventure, but there was one task she often neglected - brushing her teeth. One morning, as Srila was exploring the enchanted forest, she stumbled upon a curious creature. It was a tiny tooth fairy, with delicate wings and a sparkling wand. The tooth fairy fluttered around Srila, sprinkling a magical dust on her teeth. "What's this?" Srila asked, feeling a tingle in her mouth. "This is a special tooth-cleaning dust," the fairy explained. "It will keep your teeth strong and shiny, but you must remember to brush them every day."Srila promised to be more diligent about her dental hygiene. The tooth fairy smiled and vanished in a shower of glitter. From that day on, Srila made brushing her teeth a daily ritual. She used a soft-bristled brush and sweet-tasting toothpaste infused with fairy magic. Srila would sing songs and dance as she brushed, making it a fun and enjoyable activity. As Srila's teeth grew healthier and brighter, she noticed other changes too. Her breath stayed fresh, and she could enjoy all her favorite foods without any discomfort. The tooth fairy would visit occasionally, praising Srila's dedication and rewarding her with small treasures. '},
  
            model_input = gender + main_character + audience + story_setting + story_type + story_theme + moral_lession + story_length
            st.text(f"model_input: {model_input}")
            #       base64_string1 = body_content["image_data_decode1"]
            image_data1 = base64.b64decode(base64_string1)
            image1 = Image.open(BytesIO(image_data1))
            st.image(image1, caption='Decoded Image1', use_column_width=True)

            base64_string2 = body_content["image_data_decode2"]
            image_data2 = base64.b64decode(base64_string2)
            image2 = Image.open(BytesIO(image_data2))
            st.image(image2, caption='Decoded Image2', use_column_width=True)

            # base64_string3 = body_content["image_data_decode3"]
            # image_data3 = base64.b64decode(base64_string3)
            # image3 = Image.open(BytesIO(image_data3))
            # st.image(image3, caption='Decoded Image', use_column_width=True)
        
        else:
            st.error(f"Failed with status code: {response.status_code}")
            st.write(response.text)  # Display the error message from API
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")

st.sidebar.success("Select a page above.")
st.sidebar.text("Made with 💕 by WonderScribe")


