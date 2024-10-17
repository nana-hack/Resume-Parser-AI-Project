Here's a basic README.txt for the resume parser project:

```
Resume Parser
=============

This project aims to build a resume parser using the spaCy library in Python. The parser will extract relevant information from a resume, such as personal details, work experience, education, and skills.

Prerequisites
-------------
- Python 3.x
- spaCy library
- Tika library
- Training data in JSON format

Installation
------------
1. Install Python 3.x from the official website.
2. Install spaCy library using the command: `pip install spacy`
3. Install Tika library using the command: `pip install tika`
4. Download the pre-trained English model for spaCy using the command: `python -m spacy download en_core_web_trf`

Usage
-----
1. Prepare your training data in JSON format with the following structure:
```json
[
    {
        "text": "John Doe is a software engineer at Google.",
        "annotations": [
            [0, 8, "PERSON"],
            [22, 28, "ORG"]
        ]
    },
    {
        "text": "Jane Smith works at Amazon as a data scientist.",
        "annotations": [
            [0, 10, "PERSON"],
            [21, 27, "ORG"]
        ]
    }
]
```

2. Save the training data as `training_data.json` in the same directory as the project files.

3. Run the `train_ner` function to train the NER model on the training data.

4. Use the `resume_parser` function to parse a new resume PDF file. It will return the extracted entities along with their labels.

Customization
-------------
- You can add more entity labels to the NER model by modifying the `train_ner` function.
- You can fine-tune the NER model by adjusting the training parameters and data.
- The project can be extended to handle different file formats for resumes.

Contribution
------------
If you find any issues or have suggestions for improvements, feel free to open an issue or submit a pull request.

License
-------
This project is licensed under the MIT License.
```

This README provides an overview of the project, installation instructions, usage guidelines, and customization options. You can further enhance the README based on your specific project requirements.
