# -*- coding: utf-8 -*-
"""Pre-Processing.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1pCf8IKvbGDeoA__JWw7bI-3fTlLNMasX
"""

pip install tweet-preprocessor

import preprocessor as p
import json

f = open('data.json')
data = json.load(f)

# Option Name	Option Short Code
# URL	p.OPT.URL
# Mention	p.OPT.MENTION
# Hashtag	p.OPT.HASHTAG
# Reserved Words	p.OPT.RESERVED
# Emoji	p.OPT.EMOJI
# Smiley	p.OPT.SMILEY
# Number	p.OPT.NUMBER
p.set_options(p.OPT.URL, p.OPT.EMOJI, p.OPT.MENTION)

for i in data['dataset']:
  var=p.clean(i['corpus'])
  i['corpus']=var

for i in data['dataset']:
  print(i)