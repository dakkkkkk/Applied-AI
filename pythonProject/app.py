import streamlit as st
from rake_nltk import Rake
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer

def summarize_text(input_text):
    # Extract keywords using RAKE
    r = Rake()
    r.extract_keywords_from_text(input_text)
    extracted_keywords = r.get_ranked_phrases_with_scores()[:5]  # Get top 5 ranked phrases

    # Parse the input text
    parser = PlaintextParser.from_string(input_text, Tokenizer("english"))

    # Create an LSA summarizer
    summarizer = LsaSummarizer()

    # Generate the summary
    summary = summarizer(parser.document, sentences_count=2)  # You can adjust the number of sentences in the summary

    return summary, extracted_keywords

# Create the Streamlit app
st.title("Text Summarizer")

# Input text area
input_text = st.text_area("Enter your text here:")

# Summarize button
if st.button("Summarize"):
    if input_text:
        summary, extracted_keywords = summarize_text(input_text)

        # Display summary
        st.subheader("Summary:")
        for sentence in summary:
            st.write(sentence)

        # Display extracted keywords
        st.subheader("Extracted Keywords:")
        for score, phrase in extracted_keywords:
            st.write(f"{phrase} (Score: {score})")
    else:
        st.warning("Please enter some text to summarize.")
