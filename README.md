# Regex Onboarding Hackathon
## Data Extraction & Secure Validation Assignment

In this project, the main emphasis was to apply regex patterns in Python, so as to extract key information from the input text.

In the `input/raw-text.txt`, there's a random AI-generated text containing valid or invalid texts.

In the `src/main.py`, the first job was to open the `raw-text.txt` file, and ensure to only process it when there's no malicious (or invalid) data formats. When there are such invalid data or text formats, the system notifies the user that input is unsafe. If the input is safe, the processing continues, and the system looks for valid email addresses, valid ALU specific email addresses, valid credit cards, and valid URLs. Later, these data are written in the `output/sample-output.json` file.

## How to Run

1. Clone the repository
2. In the terminal, move to `alu-regex-data-extraction_JRene4460011/src` and run:

```bash
Python main.py
```

3. The system will run, but immediately inform that the input is unsafe, given that the `raw-text.txt` file currently has some dangerous, unwanted texts. However, one can make changes in the file and run `Python main.py` again, which will update the `sample-output.json` file (this file currently contains old outputs that got stored before the system started checking whether the input text has dangerous texts or not. So, `sample-output.json` might contain some dangerous text, given that it is storing old results data).