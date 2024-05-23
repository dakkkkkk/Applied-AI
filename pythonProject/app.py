import tkinter as tk
from tkinter import scrolledtext
from rake_nltk import Rake
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer

def summarize_text():
    input_text = text_area.get("1.0", "end-1c")

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

    # Clear previous result
    result_text.config(state=tk.NORMAL)
    result_text.delete(1.0, tk.END)

    # Output the summary and extracted keywords
    result_text.insert(tk.END, "Summary:\n")
    for sentence in summary:
        result_text.insert(tk.END, str(sentence) + "\n")

    result_text.insert(tk.END, "\nExtracted Keywords:\n")
    for score, phrase in extracted_keywords:
        result_text.insert(tk.END, f"{phrase} (Score: {score})\n")

    result_text.config(state=tk.DISABLED)

# Create the main window
root = tk.Tk()
root.title("Text Summarizer")

# Create a text area for input
text_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=40, height=10)
text_area.pack(padx=10, pady=10)

# Create a button to trigger summarization
summarize_button = tk.Button(root, text="Summarize", command=summarize_text)
summarize_button.pack(pady=5)

# Create a text area for displaying results
result_text = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=40, height=10, state=tk.DISABLED)
result_text.pack(padx=10, pady=10)

# Start the GUI main loop
root.mainloop()
