from django.shortcuts import render
from django.views import generic
import dataprofiler as dp
import json
import pandas as pd

# Create your views here.

class EncryptView(generic.TemplateView):
    template_name = "encrypt.html"
    

data = "HEllo this is Rituraj, you can contact me at rituraj@vt.edu"
data = pd.Series([data])
data_labeler = dp.DataLabeler(labeler_type = "unstructured")
# predictions = data_labeler.predict(data)
# print(predictions['pred'])
# convert prediction to word format and ner format
# Set the output to the NER format (start position, end position, label)
# print("\n\n\n\n\n\n\n\n\n")

data_labeler.set_params(
    {'postprocessor': {'output_format':'ner', 'use_word_level_argmax':True}} 
)
predictions = data_labeler.predict(data)

# display results
print(predictions, "\n\n\n\n")
print(predictions['pred'],"\n\n\n\n\n")