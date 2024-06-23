import csv

input_file_path = "./summary_result/generated_predictions.txt" #predictions generated nby the summariser
output_csv_path = "./summary_result/generated_summary.csv"
json_name = "./summary_result/mt_test_en_hi.json" #file where json file will be created to be fed to the MT model



with open(input_file_path, 'r') as input_file, open(output_csv_path, 'w', newline='') as output_csv:
    csv_writer = csv.writer(output_csv)

    for line in input_file:
        # Assuming each line in the text file should be treated as a single column in the CSV file
        row_data = [line.strip()]

        # Write the row to the CSV file
        csv_writer.writerow(row_data)

# print(f'Text file converted to CSV. Output saved to {output_csv_path}')

import json

def read_csv(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        sentences = [row[0] for row in reader]
    return sentences

def merge_to_json(english_file, hindi_file, output_file):
    english_sentences = read_csv(english_file)
    hindi_sentences = read_csv(hindi_file)

    if len(english_sentences) != len(hindi_sentences):
        raise ValueError("Number of sentences in English and Hindi files do not match.")

    data = []
    for en, hi in zip(english_sentences, hindi_sentences):
        data.append({"translation": {"en": en, "hi": hi}})

    with open(output_file, 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    english_csv = output_csv_path #english
    hindi_csv = "./groundtruths/summaries_test_hi.csv" #hindi
    output_json = json_name

    merge_to_json(english_csv, hindi_csv, output_json)
