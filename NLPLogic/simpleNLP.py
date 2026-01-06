from textblob import TextBlob
import nltk

nltk.download("brown")
nltk.download("punkt")
nltk.download("punkt_tab")
import wikipedia


def search_wikipedia(query):
    try:
        text = wikipedia.search(query)
        return text
    except wikipedia.exceptions.DisambiguationError as e:
        return f"Disambiguation error: {e.options}"
    except wikipedia.exceptions.PageError:
        return "Page not found."


def summarize_wikipedia(title):
    try:
        summary = wikipedia.summary(title)
        return summary
    except wikipedia.exceptions.DisambiguationError as e:
        return f"Disambiguation error: {e.options}"
    except wikipedia.exceptions.PageError:
        return "Page not found."


def get_text_blob(text):
    blob = TextBlob(text)
    return blob


def get_phrases(name):
    text = summarize_wikipedia(name)
    blob = get_text_blob(text)
    return blob.noun_phrases
