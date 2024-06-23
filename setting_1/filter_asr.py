file_name = './conformer/generate-test_asr.txt'  # Update with your file name
output_file = "./conformer/asr_generated_preds_sorted.txt" # update with your output file name

with open(file_name, 'r') as file:
    lines_with_d = [line.strip() for line in file if line.strip().startswith('D')]

numbers_and_lines = []
for line in lines_with_d:
    start_index = line.find('-') + 1
    end_index = line.find('\t', start_index)
    number = int(line[start_index:end_index])
    numbers_and_lines.append((number, line))


numbers_and_lines.sort(key=lambda x: x[0])
sorted_lines = [line for _, line in numbers_and_lines]    
modified_list=[]

for i in range(len(sorted_lines)):
    parts = sorted_lines[i].split("\t")
    modified_list.append(parts[2])

with open(output_file, 'w') as file:
    for item in modified_list:
        file.write(item + '\n')

print(f"Modified list has been written to {output_file}")   
