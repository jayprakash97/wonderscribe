import streamlit as st
import requests
import json
import re
from io import BytesIO 
from PIL import Image
import evaluate

# Function to evaluate RAG system using ROUGE
def rouge_scores(predicated_response, gold_response):
  rouge = evaluate.load('rouge')
  rouge_scores = rouge.compute(predictions=predicated_response, references=gold_response)
  return rouge_scores

def bleu_scores(predicated_response, gold_response):
  bleu = evaluate.load('bleu')
  bleu_scores = bleu.compute(predictions=predicated_response, references=gold_response)
  return bleu_scores

def bert_scores(predicated_response, gold_response):
  bertscore = evaluate.load('bertscore')
  bert_scores = bertscore.compute(predictions=predicated_response, references=gold_response, lang= 'en')
  bert_scores['precision'] = sum(bert_scores['precision']) / len(bert_scores['precision'])
  bert_scores['recall'] = sum(bert_scores['recall']) / len(bert_scores['recall'])
  bert_scores['f1'] = sum(bert_scores['f1']) / len(bert_scores['f1'])
  return bert_scores

@st.cache_data 
def fetch_story_data(payload, _force_refresh=False):
    if _force_refresh:
        st.cache_data.clear()
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
    validation_query_response_list = {
        0: {'query': 'Female,Srila,children,Magical Kingdoms,Fantacy,Brushing the tooth,Develop hygiene habbits,300',
            'gold_response': 'In the enchanting Magical Kingdoms, where unicorns roamed and fairies danced, lived a young girl named Srila. Srilas days were filled with wonder and adventure, but there was one task she often neglected - brushing her teeth. One morning, as Srila was exploring the enchanted forest, she stumbled upon a curious creature. It was a tiny tooth fairy, with delicate wings and a sparkling wand. The tooth fairy fluttered around Srila, sprinkling a magical dust on her teeth. "What is this?" Srila asked, feeling a tingle in her mouth. "This is a special tooth-cleaning dust," the fairy explained. "It will keep your teeth strong and shiny, but you must remember to brush them every day."Srila promised to be more diligent about her dental hygiene. The tooth fairy smiled and vanished in a shower of glitter. From that day on, Srila made brushing her teeth a daily ritual. She used a soft-bristled brush and sweet-tasting toothpaste infused with fairy magic. Srila would sing songs and dance as she brushed, making it a fun and enjoyable activity. As Srilas teeth grew healthier and brighter, she noticed other changes too. Her breath stayed fresh, and she could enjoy all her favorite foods without any discomfort. The tooth fairy would visit occasionally, praising Srilas dedication and rewarding her with small treasures. '}
    }

    query_string = validation_query_response_list[0]['query']
    gold_response = validation_query_response_list[0]['gold_response']
    gender, name, audience, setting, genre, topic, moral, word_count = query_string.split(',')

    payload = {
        "audience" : audience,
        "story_type" : '',
        "main_character" : name,
        "story_theme" : genre, 
        "moral_lesson" : moral,
        "setting" : setting, 
        "word_count" : word_count,
        "story_lang" : '',
        "api_Path" : "getStory"
    }

    story_texts = fetch_story_data(payload)

    predicated_response = ' '.join(story_texts)

    st.write("### Evaluation Scores ###")
    st.write("Rouge Scores - ", rouge_scores(predicated_response, gold_response))
    st.write("Bleu  Scores - ", bleu_scores(predicated_response, gold_response))
    st.write("Bert  Scores - ", bert_scores(predicated_response, gold_response))

if __name__ == "__main__":
    main()
