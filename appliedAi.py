import streamlit as st
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer
import language_tool_python

st.title("Text Summarizer with Grammar Checker")

st.header("Enter Text")
input_text = st.text_area("Paste your text here:", height=200)

if st.button("Summarize Text"):
    if input_text:
        parser = PlaintextParser.from_string(input_text, Tokenizer("english"))
        summarizer = LsaSummarizer()
        summary = summarizer(parser.document, sentences_count=2)
        summarized_text = " ".join([str(sentence) for sentence in summary])
        st.success(summarized_text)
    else:
        st.warning("Please enter text to summarize.")

if st.button("Check Grammar"):
    if input_text:
        tool = language_tool_python.LanguageTool('en-US')
        matches = tool.check(input_text)
        corrected_text = language_tool_python.utils.correct(input_text, matches)
        st.success(corrected_text)
    else:
        st.warning("Please enter text to check grammar.")

st.header("Output")
st.write("Here you will see the summarized and/or grammar-checked text based on your actions above.")

if st.checkbox("Show Summarized and Corrected Text"):
    if input_text:
        parser = PlaintextParser.from_string(input_text, Tokenizer("english"))
        summarizer = LsaSummarizer()
        summary = summarizer(parser.document, sentences_count=2)
        summarized_text = " ".join([str(sentence) for sentence in summary])
        
        tool = language_tool_python.LanguageTool('en-US')
        matches = tool.check(summarized_text)
        combined_text = language_tool_python.utils.correct(summarized_text, matches)
        
        st.info(combined_text)
    else:
        st.warning("Please enter text to summarize and check grammar.")

# Footer
st.write("This application provides both text summarization and grammar checking functionalities. Enter your text above to get started.")
