import streamlit as st
import requests
import json
import evaluate
import pandas as pd

validation_query_response = {
  0: {"query": "friendships between boy and girl",
      "gold_response": "story about etc "},
  1: {"query": "Brushing the tooth",
      "gold_response": " "}
}

# Function to evaluate RAG system using ROUGE

# def rouge_scores(predicated_response, gold_response):
#   import evaluate
#   rouge = evaluate.load('rouge')
#   rouge_scores = rouge.compute(predictions=predicated_response, references=gold_response)
#   return rouge_scores

# def bleu_scores(predicated_response, gold_response):
#   import evaluate
#   bleu = evaluate.load('bleu')
#   bleu_scores = bleu.compute(predictions=predicated_response, references=gold_response)
#   return bleu_scores

# def bert_scores(predicated_response, gold_response):
#   import evaluate
#   bertscore = evaluate.load('bertscore')
#   bert_scores = bertscore.compute(predictions=predicated_response, references=gold_response, lang= 'en')
#   bert_scores['precision'] = sum(bert_scores['precision']) / len(bert_scores['precision'])
#   bert_scores['recall'] = sum(bert_scores['recall']) / len(bert_scores['recall'])
#   bert_scores['f1'] = sum(bert_scores['f1']) / len(bert_scores['f1'])
#   return bert_scores


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

    st.title("Display Excel File in Streamlit")
    file = "pages/images/file.xlsx"
    df = pd.read_excel(file)
    st.dataframe(df) 

if __name__ == "__main__":
    main()

