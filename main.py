import spacy
from spacy.tokens import DocBin
import json
from tika import parser

def resume_parser(resume_file):
    # Load the pre-trained spacy model
    nlp = spacy.load("en_core_web_trf")
    
    # Extract text from the resume PDF using Tika
    resume_text = parser.from_file(resume_file)['content']
    
    # Process the resume text with the spacy model
    doc = nlp(resume_text)
    
    # Extract named entities
    entities = [(ent.text, ent.label_) for ent in doc.ents]
    
    # Return the extracted entities
    return entities

def train_ner(training_data):
    # Create a blank spacy model
    nlp = spacy.blank("en")
    
    # Create a DocBin object to store the training data
    doc_bin = DocBin()
    
    # Convert training data to spacy format
    for text, annotations in training_data:
        doc = nlp.make_doc(text)
        ents = []
        for start, end, label in annotations:
            span = doc.char_span(start, end, label=label)
            if span is None:
                continue
            ents.append(span)
        doc.ents = ents
        doc_bin.add(doc)
    
    # Train the NER model
    ner = nlp.create_pipe("ner")
    nlp.add_pipe(ner)
    ner.add_label("PERSON")
    ner.add_label("ORG")
    nlp.begin_training()
    for itn in range(10):
        nlp.update(doc_bin.get_docs(nlp.vocab), sgd=optimizer)
    
    return nlp

# Load the training data
with open("training_data.json", "r") as file:
    training_data = json.load(file)

# Train the NER model
ner_model = train_ner(training_data)

# Save the trained model
ner_model.to_disk("ner_model")

# Use the trained model to parse a new resume
entities = resume_parser("resume.pdf")
print(entities)
