import streamlit as st
import requests
import json
import evaluate

# Function to evaluate RAG system using ROUGE
# def rouge_scores(predicated_response, gold_response):
#     rouge = evaluate.load('rouge')
#     rouge_scores = rouge.compute(predictions=predicated_response, references=gold_response, use_stemmer=True)
#     return rouge_scores

# def bleu_scores(predicated_response, gold_response):
#     bleu = evaluate.load('bleu')
#     bleu_scores = bleu.compute(predictions=predicated_response, references=gold_response)
#     return bleu_scores

# def bert_scores(predicated_response, gold_response):
#     bertscore = evaluate.load('bertscore')
#     bert_scores = bertscore.compute(predictions=predicated_response, references=gold_response, lang= 'en')
#     bert_scores['precision'] = sum(bert_scores['precision']) / len(bert_scores['precision'])
#     bert_scores['recall'] = sum(bert_scores['recall']) / len(bert_scores['recall'])
#     bert_scores['f1'] = sum(bert_scores['f1']) / len(bert_scores['f1'])
#     return bert_scores

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
    validation_query_response_list = {
        0: {'query': 'Female,Srila,children,Magical Kingdoms,Fantacy,Brushing the tooth,Develop hygiene habbits,300',
            'gold_response': 'In the enchanting Magical Kingdoms, where unicorns roamed and fairies danced, lived a young girl named Srila. Srilas days were filled with wonder and adventure, but there was one task she often neglected - brushing her teeth. One morning, as Srila was exploring the enchanted forest, she stumbled upon a curious creature. It was a tiny tooth fairy, with delicate wings and a sparkling wand. The tooth fairy fluttered around Srila, sprinkling a magical dust on her teeth. "What is this?" Srila asked, feeling a tingle in her mouth. "This is a special tooth-cleaning dust," the fairy explained. "It will keep your teeth strong and shiny, but you must remember to brush them every day."Srila promised to be more diligent about her dental hygiene. The tooth fairy smiled and vanished in a shower of glitter. From that day on, Srila made brushing her teeth a daily ritual. She used a soft-bristled brush and sweet-tasting toothpaste infused with fairy magic. Srila would sing songs and dance as she brushed, making it a fun and enjoyable activity. As Srilas teeth grew healthier and brighter, she noticed other changes too. Her breath stayed fresh, and she could enjoy all her favorite foods without any discomfort. The tooth fairy would visit occasionally, praising Srilas dedication and rewarding her with small treasures. '
        }
    }

    query_string = validation_query_response_list[0]['query']
    gold_response = validation_query_response_list[0]['gold_response']
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
    
    st.write("### Evaluation Scores ###")
    #st.write(f"gold_response - {gold_response}")

    gold_response = "In the enchanting Magical Kingdoms, where unicorns roamed and fairies danced, lived a young girl named Srila. Srilas days were filled with wonder and adventure, but there was one task she often neglected - brushing her teeth. One morning, as Srila was exploring the enchanted forest, she stumbled upon a curious creature. It was a tiny tooth fairy, with delicate wings and a sparkling wand. The tooth fairy fluttered around Srila, sprinkling a magical dust on her teeth. What is this? Srila asked, feeling a tingle in her mouth. This is a special tooth-cleaning dust, the fairy explained. It will keep your teeth strong and shiny, but you must remember to brush them every day. Srila promised to be more diligent about her dental hygiene. The tooth fairy smiled and vanished in a shower of glitter. From that day on, Srila made brushing her teeth a daily ritual. She used a soft-bristled brush and sweet-tasting toothpaste infused with fairy magic. Srila would sing songs and dance as she brushed, making it a fun and enjoyable activity. As Srilas teeth grew healthier and brighter, she noticed other changes too. Her breath stayed fresh, and she could enjoy all her favorite foods without any discomfort. The tooth fairy would visit occasionally, praising Srilas dedication and rewarding her with small treasures."
    st.write(f"gold_response - {gold_response}")
    # cal_rouge_scores= rouge_scores(predicated_response, gold_response)
    # st.write(f"Calculated Rouge Scores - {cal_rouge_scores}")

    st.write("##### Rouge Scores #####")
    st.write(rouge_scores(predicated_response, gold_response))
        
    st.write("##### Bleu Scores #####")
    st.write(bleu_scores(predicated_response, gold_response) )
    
    st.write("### Bert Scores ###")
    st.write(bert_scores(predicated_response, gold_response))
    
    # cal_bert_scores = bert_scores(predicated_response, gold_response)
    # st.write(f"Calculated Bert  Scores - {bert_scores}")

if __name__ == "__main__":
    main()
