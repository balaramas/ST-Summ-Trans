import csv
import pandas as pd

def process_lines(lines):
    sentence = ' '.join(lines)
    return sentence

input_file_path = './asr_result/conformer/asr_generated_preds_sorted.txt' 

output_file_path = './asr_result/conformer/eighteen_lines_asr.csv'  # combined 18 lines

ground_truth_path = "./groundtruths/summaries_test_en.csv"  # summary_file as ground truth


with open(input_file_path, 'r') as input_file:
    lines = input_file.readlines()

sentences = [process_lines(lines[i:i+18]) for i in range(0, len(lines), 18)]

with open(output_file_path, 'w', newline='') as output_file:
    csv_writer = csv.writer(output_file)
    csv_writer.writerow(['Sentence']) 
    csv_writer.writerows([(sentence,) for sentence in sentences])

# print(f'Successfully created CSV file: {output_file_path}')



file_with_header_path = output_file_path
file_without_header_path = ground_truth_path
df_with_header = pd.read_csv(file_with_header_path)
df_without_header = pd.read_csv(file_without_header_path, header=None)

df_with_header.rename(columns={"Sentence": "text"}, inplace=True)
df_without_header.rename(columns={0: "summary"}, inplace=True)

merged_df = pd.concat([df_with_header, df_without_header], axis=1)

merged_file_path = "./asr_result/conformer/test_summ_en-en.csv"  # save the csv file which will be fed to the summariser 

merged_df.to_csv(merged_file_path, index=False)

print("Merged file for summariser created:", merged_file_path)
