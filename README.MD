# Japanese PDF Translator

A quick Japanese to English PDF translator. It uses the DeepL API to translate each sentence in the PDF, then outputs the results to a CSV file.

## Requirements
- Python 3.10
- deepl
- PyPDF2

Install all dependencies:

```cmd
pip install -r requirements.txt
```

## API Key
You must have an API key to use DeepL. Create an account [here](https://www.deepl.com/pro-api?cta=menu-pro-api). Once created, you can configure a `config.py` file. Create a variable called `auth_key` and assign you api key to it. 

```python
# Import config file
import config

# Use auth_key varible
auth_key = config.auth_key
```