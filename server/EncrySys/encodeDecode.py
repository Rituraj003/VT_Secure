
import random
import pandas as pd
import dataprofiler as dp
import os

def reource_path(relative_path):
    return os.path.join(
        os.environ.get(
            "_MEIPASS2",
            os.path.abspath(".")
        ),
        relative_path
    )
    
f = open(reource_path("EncrySys/1-1000.txt"), "r")
words = f.read().splitlines()

data_labeler = dp.DataLabeler(labeler_type = "unstructured")
data_labeler.set_params(
    {'postprocessor': {'output_format':'ner', 'use_word_level_argmax':True}} 
)

def encryptor(input_message):
    ret_string = ""
    for num, i in enumerate(input_message):
        ret_string += hex(ord(i))[2]
        ret_string += chr(random.randint(47, 126))
        ret_string += hex(ord(i))[3]
        ret_string += chr(random.randint(47, 126))
        ret_string += words[random.randint(0, 999)]
        if num != (len(input_message) - 1):
            ret_string += "*"
    list_string = []
    for num2, i2 in enumerate(ret_string):
        shifter = (num2 % 3) * ((-1) ** (num2 % 2))
        list_string.append(chr(ord(i2)+shifter))
    return "".join(list_string)

def EncryptedState(stringText):
    data = pd.Series([stringText])
    predictions = data_labeler.predict(data)
    predictions = predictions['pred'][0]
    if (len(predictions) > 0):
        encodedStr = data[0][:predictions[0][0]]
        for i in range(len(predictions)):
            encodedStr += encryptor(data[0][predictions[i][0]:predictions[i][1]])
            if (i < len(predictions) - 1):
                encodedStr += data[0][predictions[i][1]:predictions[i+1][0]]
    else:
        encodedStr = encryptor(stringText)
    return encodedStr



def decrypter(def_hash):
    decrypt = []
    ret_dec = ""
    for num2, i2 in enumerate(def_hash):
        shifter = (num2 % 3) * ((-1) ** (num2 % 2))
        decrypt.append(chr(ord(i2) - shifter))
    dec_string = "".join(decrypt)
    alpha = dec_string.split("*")
    for i in alpha:
        ret_dec += chr(int(i[0]+i[2], base = 16))
    return ret_dec

def DecodedState(EncrpytString):
    SplitStr = EncrpytString.split(" ")
    DecodedStr = ""
    for i in range(len(SplitStr)):
        try:
            DecodedStr += decrypter(SplitStr[i]) 
        except:
            DecodedStr += SplitStr[i] 
        if (i < len(SplitStr) - 1):
            DecodedStr += " "
    return DecodedStr

