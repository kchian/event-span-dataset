import json
import re

total_counter = 0

counter_map = {}

with open('./train.jsonl', 'r') as file:

    data_list = list(file)

    for json_str in data_list:

        entry = json.loads(json_str)
        total_counter += 1

        if(total_counter%1000 == 0):
            print(total_counter)
        
        full_sentence = entry["context_left"] + entry["mention"] + entry["context_right"]
        context_lang = entry["context_lang"]

        if context_lang not in counter_map:
            counter_map[context_lang] = {}

        if full_sentence not in counter_map[context_lang]:
            counter_map[context_lang][full_sentence] = []

        counter_map[context_lang][full_sentence].append(entry["mention"])


with open('./test.jsonl', 'r') as file:

    data_list = list(file)

    for json_str in data_list:

        entry = json.loads(json_str)
        total_counter += 1

        if(total_counter%1000 == 0):
            print(total_counter)
        
        full_sentence = entry["context_left"] + entry["mention"] + entry["context_right"]
        context_lang = entry["context_lang"]

        if context_lang not in counter_map:
            counter_map[context_lang] = {}

        if full_sentence not in counter_map[context_lang]:
            counter_map[context_lang][full_sentence] = []

        counter_map[context_lang][full_sentence].append(entry["mention"])

with open('./dev.jsonl', 'r') as file:

    data_list = list(file)

    for json_str in data_list:

        entry = json.loads(json_str)
        total_counter += 1

        if(total_counter%1000 == 0):
            print(total_counter)
        
        full_sentence = entry["context_left"] + entry["mention"] + entry["context_right"]
        context_lang = entry["context_lang"]

        if context_lang not in counter_map:
            counter_map[context_lang] = {}

        if full_sentence not in counter_map[context_lang]:
            counter_map[context_lang][full_sentence] = []

        counter_map[context_lang][full_sentence].append(entry["mention"])

print(total_counter)

# sentence_list = []

# total_counter = 0

# for language in counter_map.keys():
#     for sentence in counter_map[language].keys():
#         text = str(sentence)
#         total_counter += 1
#         if(total_counter%1000 == 0):
#             print(total_counter)

#         for span in counter_map[language][sentence]:
#             text = text.replace(span,'<a>' + span + '</a>')
#             #re.sub(span, '<a>' + span + '</a>', text)
#         result = {}
#         result["language"] = language
#         result["text"] = text
#         sentence_list.append(result)

# print(total_counter)

# jsonString = json.dumps(sentence_list, ensure_ascii=False, indent=2)

# with open('list.jsonl', 'w', encoding='utf-8') as f:
#   f.write(jsonString)
#   f.close()

language_label_dict = {}

with open('./label_dict.jsonl', 'r') as label_file:

    label_list = list(label_file)

    for json_str in label_list:

        entry = json.loads(json_str)

        lan = entry["label_lang"]
        label = entry["label_title"]

        if(lan not in language_label_dict):
            language_label_dict[lan] = set()

        language_label_dict[lan].add(label)

sentence_list = []

total_counter = 0

for language in counter_map.keys():
    for sentence in counter_map[language].keys():
        text = str(sentence)

        total_counter += 1
        if(total_counter%1000 == 0):
            print(total_counter)

        spans = set(counter_map[language][sentence])

        for span in span:
            text = text.replace(span,'<a>' + span + '</a>')
        for label in language_label_dict[language]:
            if(label not in spans):
                text = text.replace(label,'<a>' + label + '</a>')

        result = {}
        result["language"] = language
        result["text"] = text

        if("<a><a>" not in text) and ("<a></a>" not in text):
            sentence_list.append(result)

print(total_counter)

jsonString = json.dumps(sentence_list, ensure_ascii=False, indent=2)

with open('list_enhanced_3.jsonl', 'w', encoding='utf-8') as f:
  f.write(jsonString)
  f.close()
