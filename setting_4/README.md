## In Fourth Setting we do ASR ->  Direct Summarisation & Translation


## Training:- 

### 1. ASR training as on MuST-C

As given on fairseq.


### 2. Train the summariser (end-to-end English to Hindi):

Clone the S2T2 repository

```bash
!git clone https://github.com/balaramas/S2T2.git

#cd into the repository
cd S2T2  
```

- Run this command to start training process. Mention the model name and train_file path for training. Change the number of epochs and batch size according to needs. 
```bash
python3 examples/pytorch/summarization/run_summarization.py \
    --model_name_or_path balaramas/mbart-enhiriser \ # specify the model name
    --do_train \
    --source_lang en_XX \
    --forced_bos_token hi_IN \
    --train_file {path_to_the_csv_file} \ #specify the csv file which has the text and summary in different columns
    --output_dir {out_dir_for_storing_checkpoints} \  #specify the output directory
    --per_device_train_batch_size= 16 \
    --per_device_eval_batch_size= 16 \
    --num_train_epochs 5 \
    --predict_with_generate

```

- Use these extra lines with the run_summarization file if you want to push to Huggingface id 🤗
```bash
--push_to_hub true \
--push_to_hub_model_id {name_of_model} \
--push_to_hub_token {Access_Token_for_huggingface} \
```




## Test :-
### 1. ASR Inference

- Perform ASR inference
- Get the predictions generated
- Sort the lines in the generated_predictions of asr using the code as follows:

 ```bash
python filter_asr.py generated_asr.txt
```
where "generated_asr.txt" is the command line argument to the generated transcriptions file.


### 2. Summarisation Inference (end-to-end English to Hindi)

- Process the MT model generated text file to create a csv file which will have the groundtruth summaries to be fed to the summariser model.
- Change the directories inside the .py file accordingly
- The csv file should be having column of 18 lines in english as text, and 1 line of hindi summary as summary

 ```bash
python summary_format_csv.py
```

- Inference/Generation with the summarisation model.

```bash
!git clone https://github.com/balaramas/S2T2.git

cd S2T2 
```

```bash
python3 examples/pytorch/summarization/run_summarization.py \
    --model_name_or_path balaramas/mbart-enhiriser \
    --do_predict \
    --source_lang en_XX \
    --forced_bos_token hi_IN \
    --test_file {test_split_CSV_file} \ #text column in english and summary column in hindi
    --per_device_train_batch_size=16 \
    --per_device_eval_batch_size=16 \
    --predict_with_generate

```


