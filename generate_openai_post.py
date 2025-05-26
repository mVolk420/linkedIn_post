from openai import OpenAI
from dotenv import load_dotenv
import os

# .env laden
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=api_key)

def generate_post(news_list) -> str:
    prompt = f"""
    Erstelle einen hochwertigen LinkedIn-Beitrag auf Englisch, Hier sind aktuelle Nachrichtenartikel-Titel zum Thema IT:

    Titel: {news_list}

    Suche dir den deiner Meinung nach den wichtigsten raus und erstelle ein Beitrag. Der Beitrag richtet sich an ein englischsprachiges, beruflich interessiertes LinkedIn-Publikum Dabei sollen News zu Aktienbewertungen ignoriert werden.
    Er soll:

    - mit einem aufmerksamkeitsstarken Satz beginnen
    - den Kern der Nachricht prägnant und anregend zusammenfassen
    - mit einer Frage oder Meinung abschließen
    - sachlich-professionell, aber persönlich geschrieben sein
    - 4 - 5 Absätze lang sein
    - auf Emojis und Hashtags verzichten (außer sie sind sinnvoll und dezent)

    Antworte nur mit dem fertigen Beitragstext, ohne Vorbemerkung oder Erklärung.
    """

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",  # für alle verfügbar
        messages=[
            {"role": "system", "content": "Du bist ein professioneller LinkedIn-Texter, der kurze, anregende Beiträge für ein englischsprachiges Fachpublikum im Bereich IT verfasst. Du kennst die gängigen Formate, Tonalität und Plattform-Erwartungen."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7,
        max_tokens=400
    )


    return response.choices[0].message.content


