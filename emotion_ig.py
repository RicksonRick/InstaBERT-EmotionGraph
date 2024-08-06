import streamlit as st
import instaloader
import pandas as pd
import re
import csv
from transformers import BertTokenizer, BertForSequenceClassification, pipeline
import plotly.express as px

# Função para salvar comentários do Instagram
def salvar_comentarios_instagram(username, password, url):
    L = instaloader.Instaloader()
    L.login(username, password)
    match = re.search(r'/p/([^/?]+)', url)
    if not match:
        raise ValueError("Não foi possível extrair o shortcode da URL fornecida.")
    shortcode = match.group(1)
    post = instaloader.Post.from_shortcode(L.context, shortcode)
    nome_arquivo = f'comentarios_instagram_{username}.csv'
    with open(nome_arquivo, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Usuário', 'Comentário', 'ID', 'Data do Comentário UTC'])
        for comment in post.get_comments():
            writer.writerow([comment.owner.username, comment.text, comment.id, comment.created_at_utc])
    return nome_arquivo

# Função para classificar emoções nos comentários
def classificar_emocoes_no_csv(caminho_csv):
    caminho_modelo = './BERT_emotions_portuguese'
    model = BertForSequenceClassification.from_pretrained(caminho_modelo)
    tokenizer = BertTokenizer.from_pretrained(caminho_modelo)
    classifier = pipeline('text-classification', model=model, tokenizer=tokenizer, top_k=1)
    df = pd.read_csv(caminho_csv)
    def classify_emotion(text):
        try:
            result = classifier(text)
            if result and len(result) > 0 and 'label' in result[0][0]:
                return result[0][0]['label']
            else:
                return "N/A"
        except Exception as e:
            print(f"Erro ao classificar o texto: {text}. Erro: {e}")
            return "Erro"
    df['Emoção'] = df['Comentário'].apply(classify_emotion)
    nome_arquivo_saida = caminho_csv.replace('.csv', '_com_emocoes.csv')
    df.to_csv(nome_arquivo_saida, index=False)
    return nome_arquivo_saida, df

# Streamlit interface
st.title('Instagram Comment Emotion Classifier')
username = st.text_input("Username")
password = st.text_input("Password", type="password")
url = st.text_input("Instagram Post URL")

if st.button('Classify Emotions'):
    if username and password and url:
        try:
            csv_file = salvar_comentarios_instagram(username, password, url)
            resultado_arquivo, df = classificar_emocoes_no_csv(csv_file)
            st.success(f"Emotions classified and saved to {resultado_arquivo}")
            st.write("Preview of the classified comments:")
            st.dataframe(df[['Comentário', 'Emoção']])  # Display only Comment and Emotion columns

            # Plotting the pie chart of emotions using Plotly
            emotion_counts = df['Emoção'].value_counts().reset_index()
            emotion_counts.columns = ['Emoção', 'Quantidade']
            fig = px.pie(emotion_counts, names='Emoção', values='Quantidade', title='Distribuição das Emoções', hole=0.4)
            st.plotly_chart(fig)

        except Exception as e:
            st.error(f"Error: {str(e)}")
    else:
        st.error("Please fill in all the fields.")