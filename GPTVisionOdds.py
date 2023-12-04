# from pip._internal import main as pipmain
""" 
pipmain(['install', "pytesseract"]) 
pipmain(['install', "Pillow"])  """

import subprocess
import pytesseract
from PIL import Image

import base64
import requests
import openai
import json

# OpenAI API Key
api_key = "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"


#remember to uncomment the subprocess to run the node screenshot.js to read in to the tesseract OCR as GPT Vision was bad
# subprocess.run(['node', 'screenshot.js'])
# Function to encode the image
""" def encode_image(image_path):
  with open(image_path, "rb") as image_file:
    return base64.b64encode(image_file.read()).decode('utf-8')

# Path to your image
image_path = "screeenshot.png"

# Getting the base64 string
base64_image = encode_image(image_path)

headers = {
  "Content-Type": "application/json",
  "Authorization": f"Bearer {api_key}"
}

payload = {
  "model": "gpt-4-vision-preview",
  "messages": [
    {
      "role": "user",
      "content": [
        {
          "type": "text",
          "text": "put the data in this picture in to a csv table"
        },
        {
          "type": "image_url",
          "image_url": {
            "url": f"data:image/jpeg;base64,{base64_image}"
          }
        }
      ]
    }
  ],
  "max_tokens": 1024
}

response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload)
print ("/n/n")

print ("Json Response")
print(response.json())
print ("/n/n")


# Parse the JSON string to a dictionary
data = response.json()

# Accessing the content field
# Assuming there's only one choice and one message in the response
content = data['choices'][0]['message']['content'] """



# Path to tesseract executable
# On Windows, it might be something like 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

# Load your image
image_path = "screeenshot.png"
img = Image.open(image_path)

# Use Tesseract to do OCR on the image
text = pytesseract.image_to_string(img)

print(text)


# Set your API key here. Do NOT expose it publicly.
openai.api_key = api_key

prompt=("suggest who might do well based on the ladder and odds only from this :"+text)

response = openai.ChatCompletion.create(
  model="gpt-4",  # Replace with your chat model name
  messages=[
      {"role": "system", "content": "You are a helpful assistant."},
      {"role": "user", "content": prompt}
      # Add more messages as needed
  ]
)

print(response.choices[0].message)

