# os module handig voor het ophalen van de directories
# Het gebruikt de os-module om de huidige werkmap op te halen 
import os

current_folder = globals()['_dh'][0]
data_location = os.path.join(current_folder,'data.csv')

# nltk punkt voor zinnen en leestekens
import nltk
nltk.download('punkt')
from nltk.tokenize import sent_tokenize

#deze zou weg kunnen als de code runt
#import string
#import collections as ct
