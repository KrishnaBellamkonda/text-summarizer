# This program holds all the methods and functions required for 
# the preprocessing step
import json 
import os 
import numpy as np

# Main program Globals
from nltk.tokenize import  RegexpTokenizer
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import nltk.data

def initialize_tokenizer(to_lower_case = True):
    import tokenization 
    path = os.path.join(os.getcwd(),
                       "models/ExtractiveSummarizer_v1_40_words/assets/vocab.txt")
    FullTokenizer = tokenization.FullTokenizer
    tokenizer = FullTokenizer(path, to_lower_case)
    return tokenizer

stop_words = set(stopwords.words('english'))
regex_tokenizer = RegexpTokenizer(r"\w+")
tokenizer = initialize_tokenizer()

def padding(text_, max_length = 40):
    tokenized_string = tokenize_text(text_)
    padded_string = tokenized_string + [0]*(max_length - len(tokenized_string))
    segments_array = np.zeros((max_length, ), dtype = np.int32)
    mask_array = [1]*(len(tokenized_string)) + [0] * (max_length - len(tokenized_string))
    return padded_string, segments_array, mask_array

def tokenize_text(text_):
    return tokenizer.convert_tokens_to_ids(["[CLS]"] + tokenizer.tokenize(text_) + ["[SEP]"])


def preprocessing(text_):
    sentences_dict_path = "./input_data/sentences_list.json"
    text_ = text_.lower().strip()
    sentence_tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
    text_ = sentence_tokenizer.tokenize(text_)
    senteces_dict = {"sentences":text_}
    with open(sentences_dict_path, "w", encoding = "utf-8") as fp:
        fp.write(json.dumps(senteces_dict))
    for index, line in enumerate(text_):
        cleaned_line = regex_tokenizer.tokenize(line.strip("\n").strip())
        text_[index] = " ".join(cleaned_line)
    return text_

def stop_words_processing(text_, stop_words = stop_words):
    data = preprocessing(text_)
    cleaned_lines = []
    for line in data:
        tokenized_line = word_tokenize(line)
        cleaned_line = []
        for word in tokenized_line:
            if word not in stop_words:
                cleaned_line.append(word)
        cleaned_line = " ".join(cleaned_line)
        
        cleaned_lines.append(cleaned_line)
    return cleaned_lines

def final_preprocessing(filtered_sentences_list):
    all_ids, all_segs, all_masks = [], [], []
    for sentence in filtered_sentences_list:
        padd, segs, masks = padding(sentence)
        all_ids.append(padd)
        all_segs.append(segs.tolist())
        all_masks.append(masks)
        # print("All ids", all_ids)
        # print("All segs", all_segs)
        # print("All masks", all_masks)
        return_tuple = (np.array(list(all_ids), dtype =np.int32), np.array(list(all_segs), dtype =np.int32), np.array(list(all_masks), dtype =np.int32))
    return return_tuple
        
def complete_preprocessing(data_string):
    """
    This function takes care of the entire preprocessing of the data
    
    """
    
    stopwords_cleaned_strings = stop_words_processing(data_string)
    all_ids, all_segs, all_masks = final_preprocessing(stopwords_cleaned_strings) 
    return all_ids, all_segs, all_masks
