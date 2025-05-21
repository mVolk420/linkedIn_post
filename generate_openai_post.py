from openai import OpenAI
from dotenv import load_dotenv
import os

# .env laden
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=api_key)

def create_linkedin_post(news_title: str, news_summary: str) -> str:
    prompt = f"""
    Erstelle einen hochwertigen LinkedIn-Beitrag auf Deutsch zur folgenden KI-News:

    Titel: {news_title}
    Zusammenfassung: {news_summary}

    Der Beitrag richtet sich an ein deutschsprachiges, beruflich interessiertes LinkedIn-Publikum.
    Er soll:

    - mit einem aufmerksamkeitsstarken Satz beginnen
    - den Kern der Nachricht prägnant und anregend zusammenfassen
    - mit einer Frage oder Meinung abschließen
    - sachlich-professionell, aber persönlich geschrieben sein
    - maximal 4 Absätze lang sein
    - auf Emojis und Hashtags verzichten (außer sie sind sinnvoll und dezent)

    Antworte nur mit dem fertigen Beitragstext, ohne Vorbemerkung oder Erklärung.
    """

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",  # für alle verfügbar
        messages=[
            {"role": "system", "content": "Du bist ein professioneller LinkedIn-Autor."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7,
        max_tokens=400
    )


    return response.choices[0].message.content

