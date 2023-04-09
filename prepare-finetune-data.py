import os
import json
import re

src_dir = 'completions'
prompt_dir = 'prompts'

def open_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as infile:
        return infile.read()

def find_matching_file(file_name, directory):
    file_pattern = re.compile(re.escape(file_name) + r'_\d+\.\d+\.txt')
    for file in os.listdir(directory):
        if file_pattern.match(file):
            return file
    return None

if __name__ == '__main__':
    src_path = os.path.join(os.getcwd(), src_dir)
    prompt_path = os.path.join(os.getcwd(), prompt_dir)

    files = os.listdir(src_path)
    data = list()
    for file in files:
        file_name = os.path.splitext(file)[0].rsplit('_', 1)[0]
        matching_prompt_file = find_matching_file(file_name, prompt_path)

        if matching_prompt_file:
            completion = open_file(os.path.join(src_path, file))
            prompt = open_file(os.path.join(prompt_path, matching_prompt_file))
            info = {'prompt': prompt, 'completion': completion}
            data.append(info)

    with open('Sentiment.jsonl', 'w') as outfile:
        for i in data:
            json.dump(i, outfile)
            outfile.write('\n')
