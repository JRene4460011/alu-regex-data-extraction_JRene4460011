# In the following two lines of code, I'm importing the 're' module and 'json' module. 're' is used for regular expression operations in Python, and 'json' is used for working with JSON data.
import re
import json

def verify_input(text):
    dangerous_patterns = [
        r"<script.*?>.*?</script>",   # XSS
        r"(DROP|DELETE|INSERT|SELECT|UPDATE)\s+\w+",  # SQL injection
        r"\.\./",                      # Trying to escape directories or access parent directories.
        r"(__import__|eval|exec)\s*\(", # Python code injection
    ]
    for pattern in dangerous_patterns:
        if re.search(pattern, text, re.IGNORECASE | re.DOTALL):
            print(f"[WARNING] Potentially unsafe input detected. Pattern: {pattern}")
    return text

# Below, I'm opening the raw-text.txt file, which contains the sample text for testing. Moreover, I'm reading and storing the content in that file into the content variable. I can therefore print the complete text in the terminal, or use it for anything (including applying regex patterns)
with open("../input/raw-text.txt", "r") as file:
    content = file.read()

content = verify_input(content)

# Here, I'm applying regex patterns, which I tested on rubular.com, to extract all valid email addresses (and ALU specific ones), credit cards, URLs, and phone numbers from the content variable, given that I used it to store our text from the raw-text.txt file.
pattern = r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"
alu_pattern = r"[A-Za-z0-9._%+-]+@(?:alueducation\.com|alumni\.alueducation\.com|si\.alueducation\.com)(?!\S)"
credit_card_pattern = r"(?:\d[ -]*?){13,16}"
url_pattern = r"https?:\/\/[^\s'\"<>]+"
phone_pattern = r"(?:\+\d{1,3}[ -]?)?(?:07\d{8}|07\d{2}[ -]\d{3}[ -]\d{3})"

# Here, I'm applying my regex patterns on the content variable, and ensuring that no duplicate email or credit card will be included in the final list of valid emails.
# emails = list(set(re.findall(pattern, content)))  ====> I'm commenting this out because I want to exclude the ALU specific emails from the list of other emails. 

emails = list(set(re.findall(pattern, content)) - set(re.findall(alu_pattern, content)))
alu_emails = list(set(re.findall(alu_pattern, content)))

# credit_cards = list(set(re.findall(credit_card_pattern, content)))
# This new way of credit_cards extraction will help me to hide the last 6 digits of the credit card numbers, thus improving the security.
credit_cards = [
    card[:-6] + "******"
    for card in set(re.findall(credit_card_pattern, content))
]

# Here, I'm applying the regex pattern for URLs and Phone numbers, but ensuring that phone numbers are displayed in a more secretive way.
urls = list(set(re.findall(url_pattern, content)))

phone_numbers = [
    pnumber[:-5] + "*****"
    for pnumber in set(re.findall(phone_pattern, content))
]

# Then here, I created a dictionary "data" to store the list of valid emails, specific ALU emails, and valid credit card under the key "All valid emails" and "ALU valid emails" respectively.
data = {
    "All valid emails": emails,
    "ALU valid emails": alu_emails,
    "Valid credit cards": credit_cards,
    "Valid URLs": urls,
    "Valid phone numbers": phone_numbers
}

# Finally, I'm writing the "data" dictionary into our JSON output file named 'sample-output.json'!!!!
with open("../output/sample-output.json", "w") as file:
    json.dump(data, file, indent=4)