## In First Setting we do ASR -> Summarisation -> Machine Translation


## Training:- 

### 1. ASR training as on MuST-C

As given on fairseq.

### 2. Train the summariser:

Clone the S2T2 repository

```bash
!git clone https://github.com/balaramas/S2T2.git

#cd into the repository
cd S2T2  
```

- Run this command to start training process. Mention the model name and train_file path for training. Change the number of epochs and batch according to needs. 
```bash
python3 examples/pytorch/summarization/run_summarization.py \
    --model_name_or_path balaramas/bart-large-summariser-finetune \ # specify the model name
    --do_train \
    --train_file {path_to_the_csv_file} \ #specify the csv file which has the text and summary in different columns
    --output_dir {out_dir_for_storing_checkpoints} \  #specify the output directory
    --overwrite_output_dir \
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

### 3. Train the Mt Model

- Run this code to start training the mt model. In this setting we're performing english to hindi, so we follow the lang_ids for mbart model. We have to use different lang_ids supported by different models.

```bash
python3 examples/pytorch/translation/run_translation.py \
    --model_name_or_path balaramas/hindi-mbart-finetune \ # specify the MT model name
    --do_train \
    --source_lang en_XX \
    --forced_bos_token hi_IN \
    --train_file {path_to_the_JSON_file} \ #specify the JSON file which has the en and hi in different dictionaries
    --output_dir {out_dir_for_storing_checkpoints} \  #specify the output directory
    --per_device_train_batch_size= 16 \
    --per_device_eval_batch_size= 16 \
    --num_train_epochs 5 \
    --predict_with_generate

```
- Use these extra lines with the train command if you want to push to Huggingface id 🤗
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


### 2. Summarisation Inference



- Process the ASR generated text file to create a csv file which will have the groundtruth summaries to be fed to the summariser model.
- Change the directories inside the .py file accordingly

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
    --model_name_or_path balaramas/bart-large-summariser-finetune \
    --do_predict \
    --test_file {test_split_CSV_file} \
    --per_device_train_batch_size=16 \
    --per_device_eval_batch_size=16 \
    --predict_with_generate

```

### 3. MT Inference

- Process the Summarisation model generated text file to create a JSON file which will have the groundtruth hindi to be fed to the machine translator model.
- Change the directories inside the .py file accordingly

 ```bash
python mt_format_json.py
```
- Inference/Generation with the MT model.

```bash
!git clone https://github.com/balaramas/S2T2.git

cd S2T2 
```

```bash
python3 examples/pytorch/translation/run_translation.py \
    --model_name_or_path balaramas/hindi-mbart-finetune \
    --do_predict \
    --source_lang en_XX \
    --forced_bos_token hi_IN \
    --test_file {test_split_JSON_file} \
    --per_device_train_batch_size=16 \
    --per_device_eval_batch_size=16 \
    --predict_with_generate

```

