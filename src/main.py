# In the following two lines of code, I'm importing the 're' module and 'json' module. 're' is used for regular expression operations in Python, and 'json' is used for working with JSON data.
import re
import json

# Below, I'm opening the raw-text.txt file, which contains the sample text for testing. Moreover, I'm reading and storing the content in that file into the content variable. I can therefore print the complete text in the terminal, or use it for anything (including applying regex patterns)
with open("../input/raw-text.txt", "r") as file:
    content = file.read()

# Here, I'm applying regex patterns, which I tested on rubular.com, to extract all valid email addresses (and ALU specific ones) and credit cards from the content variable, given that I used it to store our text from the raw-text.txt file.
pattern = r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"
alu_pattern = r"[A-Za-z0-9._%+-]+@(?:alueducation\.com|alumni\.alueducation\.com|si\.alueducation\.com)"
credit_card_pattern = r"(?:\d[ -]*?){13,16}"

# Here, I'm applying my regex patterns on the content variable, and ensuring that no duplicate email or credit card will be included in the final list of valid emails.
emails = list(set(re.findall(pattern, content)))
alu_emails = list(set(re.findall(alu_pattern, content)))

# credit_cards = list(set(re.findall(credit_card_pattern, content)))
# This new way of credit_cards extraction will help me to hide the last 6 digits of the credit card numbers, thus improving the security.
credit_cards = [
    card[:-6] + "******"
    for card in set(re.findall(credit_card_pattern, content))
]

# Then here, I created a dictionary "data" to store the list of valid emails, specific ALU emails, and valid credit card under the key "All valid emails" and "ALU valid emails" respectively.
data = {
    "All valid emails": emails,
    "ALU valid emails": alu_emails,
    "Valid credit cards": credit_cards
}

# Finally, I'm writing the "data" dictionary into our JSON output file named 'sample-output.json'!!!!
with open("../output/sample-output.json", "w") as file:
    json.dump(data, file, indent=4)