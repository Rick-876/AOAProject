import re
import nltk

class ChatAnalyzer:
    def __init__(self):
        # Download necessary NLTK resources 
        try:
            nltk.download('punkt')
            nltk.download('averaged_perceptron_tagger')
            nltk.download('stopwords')
        except Exception as e:
            print("An error occurred while downloading NLTK resources:", e)

    def is_valid_message(self, message):
        try:
            # Check if message length is greater than a threshold and contains alphabetic characters
            return len(message) > 3 and any(c.isalpha() for c in message)
        except Exception as e:
            print("An error occurred while validating the message:", e)
            return False

    def is_sensible_response(self, message):
        try:
            # Tokenize the message using NLTK
            tokens = nltk.word_tokenize(message)

            # Filter out stop words and punctuation
            filtered_tokens = [token for token in tokens if token.isalpha() and token not in nltk.corpus.stopwords.words('english')]

            # Check for presence of content-bearing words (nouns, verbs, adjectives, adverbs)
            content_words = [token for token, tag in nltk.pos_tag(filtered_tokens)
                              if tag.startswith('NN') or tag.startswith('VB') or tag.startswith('JJ') or tag.startswith('RB')]

            return len(content_words) > 0
        except Exception as e:
            print("An error occurred while analyzing the response:", e)
            return False

    def analyze_chat(self, chat_lines, teacher):
        try:
            # Regular expression patterns for extracting relevant information
            pattern = re.compile(r'(\d{2}:\d{2}:\d{2}) From (.*?): (.*)')

            # Dictionary to store participation data
            participation = {}

            # Count of questions asked (by teacher)
            total_questions = 0

            # Iterate through each line in the chat
            for line in chat_lines:
                match = pattern.match(line)
                if match:
                    timestamp = match.group(1)
                    speaker = match.group(2)
                    message = match.group(3)

                    # Exclude the teacher's data
                    if message.endswith("?"):
                        total_questions += 1
                    else:
                        if self.is_valid_message(message):
                            # Check if the response makes sense
                            if self.is_sensible_response(message):
                                if speaker != teacher:  # Exclude the teacher
                                    if speaker in participation:
                                        participation[speaker]["count"] += 1
                                    else:
                                        participation[speaker] = {"count": 1}

            # Compute participation grades
            for speaker, data in participation.items():
                # Calculate the participation grade based on the ratio of questions asked by the participant
                # to the total count of questions asked, rounded to 1 decimal place
                participation[speaker]["grade"] = round((data["count"] / total_questions) * 100, 1) if total_questions != 0 else 0

            return participation
        except Exception as e:
            print("An error occurred while analyzing the chat:", e)
            return {}
