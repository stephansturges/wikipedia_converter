import os
import json
import re

def cut_string_before_substring(input_string, substring):
    # Find the index of the first occurrence of the substring
    index = input_string.find(substring)

    # If the substring is not found, return the original string
    if index == -1:
        return input_string

    # Otherwise, return the substring of the input string up to the index
    return input_string[:index]

# Define the input and output file paths
input_dir = './wikiplaintext/'
output_file = 'requests_for_openai_embeddings.jsonl'

# Create an empty list to store the JSON objects
json_objects = []

# Loop over each file in the input directory
for filename in os.listdir(input_dir):

    # Load the JSON file
    with open(os.path.join(input_dir, filename), 'r') as f:
        json_data = json.load(f)

    # Extract the title and text fields from the JSON data
    title = json_data['title']
    text = json_data['text']

    # Clear the text field
    string = "".join(str(x) for x in text)
    head, sep, tail = string.partition('==References')
    string = head.replace("{| |}", "").replace("()", "")
    string = re.sub('{[^>]+}', '', string)

    head, sep, tail = string.partition('{|')
    string = head

#    string = cut_string_before_substring('==Refere')

    head, sep, tail = string.partition('==Refere')
    string = head
    head, sep, tail = string.partition('== Refernces')
    string = head
    head, sep, tail = string.partition('== REfe')
    string = head
    head, sep, tail = string.partition('== refere')
    string = head
    head, sep, tail = string.partition('== Refe')
    string = head
    head, sep, tail = string.partition('== Refere')
    string = head
    head, sep, tail = string.partition('== Refrence')
    string = head
    # head, sep, tail = string.partition('== Other')
    # string = head
    # head, sep, tail = string.partition('==Other')
    # string = head
    head, sep, tail = string.partition('== Other web')
    string = head
    head, sep, tail = string.partition('==Other web')
    string = head
    head, sep, tail = string.partition('==Other wbes')
    string = head
    head, sep, tail = string.partition('== Notes')
    string = head
    head, sep, tail = string.partition('==Notes')
    string = head
    head, sep, tail = string.partition('== Sources')
    string = head
    head, sep, tail = string.partition('==Sources')
    string = head
    head, sep, tail = string.partition('== sources')
    string = head
    head, sep, tail = string.partition('== Source')
    string = head
    head, sep, tail = string.partition('==Source')
    string = head
    head, sep, tail = string.partition('== source')
    string = head
    # Create the input string for the JSON object
    input_str = f'Title: {title} Content: {string}'

    # Create the JSON object and append it to the list
    json_obj = {
        'model': 'text-embedding-ada-002',
        'input': input_str
    }
    json_objects.append(json_obj)

# Write the list of JSON objects to a JSONL file
with open(output_file, 'w') as f:
    for json_obj in json_objects:
        f.write(json.dumps(json_obj) + '\n')
