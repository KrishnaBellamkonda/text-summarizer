# This is the preprocessing main function 
import json 
import os 
import numpy as np
from nltk.tokenize import  RegexpTokenizer
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from preprocessing_fns import initialize_tokenizer, complete_preprocessing, padding, tokenize_text, preprocessing,stop_words_processing, final_preprocessing

if __name__ == "__main__":
    stop_words = set(stopwords.words('english'))
    regex_tokenizer = RegexpTokenizer(r"\w+")
    tokenizer = initialize_tokenizer()
    string_path = "./input_data/string.json"
    with open(string_path, "r", encoding = "utf-8") as fp:
        string_file= json.load(fp)
    string = string_file["string"]
    all_ids, all_segs, all_masks = complete_preprocessing(string)
    request_dict =  json.dumps({
                "signature_def":"serving_default",
                "inputs":{"tag":"Examples",
                "input_segments":all_segs.tolist(), 
                "input_masks":all_masks.tolist(),
                "input_ids":all_ids.tolist(),
                },
             })
    with open("./input_data/preprocessed_string.json", "w", encoding="utf-8") as fp:
        fp.write(request_dict)