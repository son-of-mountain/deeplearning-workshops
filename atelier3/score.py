import pandas as pd
import nltk
from nltk.tokenize import word_tokenize

nltk.download('stopwords')

# Define your lists of keywords for internal and external news
internal_keywords = ['الملك', 'الحكومة', 'الاستقلال', 'الرباط', 'العلمي', 'الراشدي', 'الأغلبية', 'النواب', 'جامعات']
external_keywords = ['إسرائيل', 'البحرين', 'باريس', 'الأممي', 'البوليساريو', 'رواندا']

# Your input string

# Arabic stop words list
stop_words = set(nltk.corpus.stopwords.words('arabic'))

# Load the CSV file into a DataFrame
df = pd.read_csv('titles.csv')

# Iterate over the DataFrame
for i in range(len(df)):
    # Get the title
    title = df.loc[i, 'title']

    # Tokenize the text
    words = word_tokenize(title)

    # Remove stop words and punctuation
    keywords = [word for word in words if word not in stop_words and word.isalpha()]

    df.loc[i, 'keywords'] = ' '.join(keywords)

    # Initialize the score
    score = 0

    # Check if the title is related to external or local news
    for keyword in external_keywords:
        if keyword in title:
            score += 1
    for keyword in internal_keywords:
        if keyword in title:
            score -= 1
    score = max(0, min(10, score))  # Ensure the score is between 0 and 10

    # Update the score in the DataFrame
    df.loc[i, 'score'] = score

# Write the DataFrame back to the CSV file
df.to_csv('titles-scored.csv', index=False)

# the score
# if the title is for external news , the score is close to 10
# if the title is for local news , the score is close to 0
