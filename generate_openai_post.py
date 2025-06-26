from openai import OpenAI
from dotenv import load_dotenv
import os

# .env laden
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=api_key)

def generate_post(news_title) -> str:
    prompt = f"""
    Erstelle einen hochwertigen LinkedIn-Beitrag auf Englisch, Hier ist ein aktueller Nachrichtenartikel-Titel zum Thema IT:

    Titel: {news_title}

    Er soll:

    - mit einem aufmerksamkeitsstarken Satz beginnen
    - den Kern der Nachricht prägnant und anregend zusammenfassen
    - mit einer Frage oder Meinung abschließen
    - sachlich-professionell, aber persönlich geschrieben sein
    - 2 Absätze lang sein
    - gerne mit sinnvollen Emojis
    - auf Hashtags verzichten
    Antworte nur mit dem fertigen Beitragstext, ohne Vorbemerkung oder Erklärung.
    """

    response = client.chat.completions.create(
        model="gpt-4",  
        messages=[
            {"role": "system", "content": "Du bist ein professioneller LinkedIn-Texter, der kurze, anregende Beiträge für ein englischsprachiges Fachpublikum im Bereich IT verfasst. Du kennst die gängigen Formate, Tonalität und Plattform-Erwartungen."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7,
        max_tokens=400
    )


    return response.choices[0].message.content


