
import spacy
nlp = spacy.load("en_core_web_sm")

def extract_entities(text):
    doc = nlp(text[:1000])
    ents = [(ent.text, ent.label_) for ent in doc.ents]
    return str(ents)

def enrich_data(df):
    df['entities'] = df['clean_message'].apply(extract_entities)
    return df
