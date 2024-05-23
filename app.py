from rake_nltk import Rake
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer

# Input text to be summarized
input_text = """
In a recent article on the transformative potential of artificial intelligence in healthcare, experts highlighted the significant strides AI is making in diagnostics and treatment personalization. Advanced machine learning algorithms are now capable of analyzing vast datasets from medical records, imaging studies, and genetic information to identify patterns and predict disease outcomes with unprecedented accuracy. This technological leap not only enhances early detection of conditions like cancer and heart disease but also tailors treatment plans to individual patients, improving efficacy and reducing adverse effects. As AI continues to evolve, its integration into healthcare promises to revolutionize patient care and streamline clinical workflows, ultimately leading to better health outcomes and more efficient medical practices.
"""

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

# Output the summary and extracted keywords
print("Original Text:")
print(input_text)
print("\nSummary:")
for sentence in summary:
    print(sentence)

print("\nExtracted Keywords:")
for score, phrase in extracted_keywords:
    print(f"{phrase} (Score: {score})")
