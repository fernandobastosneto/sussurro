import streamlit as st
import whisper
from pytube import YouTube
import validators
import tiktoken
import openai

# Load whisper model
model = whisper.load_model("base")

def transcribe(file):
    transcription = model.transcribe(file)
    return transcription["text"]

# @st.cache_data
def download_youtube_audio(url):
    yt = YouTube(url)
    yt.streams.get_audio_only().download(filename="yt.mp4")

def num_tokens_from_string(string: str, encoding_name: str) -> int:
    """Returns the number of tokens in a text string."""
    encoding = tiktoken.get_encoding(encoding_name)
    num_tokens = len(encoding.encode(string))
    return num_tokens

def traduzir(transcription):
    openai.api_key = api_key  # Set the API key
    response = openai.ChatCompletion.create(
        model="gpt-4",
        temperature=0,
        messages=[
            {
                "role": "system",
                "content": "You are a highly skilled AI trained in language comprehension. Please translate the following text from its native language to Portuguese. Ensure that the translation captures the essence and nuances of the original text as much as possible. Observe that the text might be informal and might have colloquialisms and be a transcription of someone speaking."
            },
            {
                "role": "user",
                "content": transcription
            }
        ]
    )
    return response['choices'][0]['message']['content']

# Streamlit UI

with st.sidebar:
    api_key = st.text_input("OpenAI API Key", key="chatbot_api_key", type="password")
    "[Como pegar uma API key da OpenAI](https://platform.openai.com/account/api-keys)"
    "[View the source code](https://github.com/fernandobastosneto/sussurro/)"
    "Criado por Fernando Bastos (fernando.bastos@itamaraty.gov.br)"

st.title("📚 Tradutor de Vídeos do YouTube")
st.caption("🌍 Um bot que transcreve vídeos e os traduz para a língua portuguesa. Utiliza o Whisper e o GPT-4, ambos da OpenAI")

with st.form('my_form'):
  url = st.text_input("URL do YouTube:")
  submitted = st.form_submit_button('Submit')
  if not api_key.startswith('sk-'):
    st.warning('Não esqueça da API key da OpenAI!', icon='⚠')
  if submitted and api_key.startswith('sk-'):
    if url:
        if validators.url(url):
            st.write("A URL é válida.")
            download_youtube_audio(url)
            with st.spinner('Passo 1 de 2 - Transcrevendo para a língua original...'):
                transcricao = transcribe("yt.mp4")
            st.write("Transcription:", transcricao)
            token_count = num_tokens_from_string(transcricao, "cl100k_base")
            st.write("Token Count:", token_count)

            with st.spinner('Passo 2 de 2 - Traduzindo para o português...'):
                traducao = traduzir(transcricao)
            st.write(traducao)
            
        else:
            st.write("A URL não é válida.")



