import pandas as pd
import numpy as np
from duckduckgo_search import DDGS
import requests
from bs4 import BeautifulSoup
import os
import time
import torch
torch.classes.__path__ = [os.path.join(torch.__path__[0], torch.classes.__file__)]
from transformers import pipeline
from main import pipe

def list_generator(df):
  lst=[]
  for row in range(len(df)):
    if df.loc[row, 'Website'] != None or df.loc[row, 'Website'] != 'N/A':
      name=df.loc[row, 'Website']
      lst.append(name.replace('https://', ''))
    else:
      name=df.loc[row, 'Company']
      lst.append(f"{name}.com")
  return lst

def link_generator(lst):
  links=[]
  body_lst=[]
  for query in lst:
    results=DDGS().text(query, max_results=1,)
    time.sleep(2)  # To avoid hitting the API too quickly
    link=results[0]['href']
    body = results[0]['body']
    links.append(link)
    body_lst.append(body)
    print(link)
  return links, body_lst

def info_generator(links,body):
  info=[]
  count=0
  for url in links:
    if url != '':
      response = requests.get(url)
      soup = BeautifulSoup(response.text, "html.parser")
      articles = [para.get_text() for para in soup.find_all("p")]
      text=' '.join(articles)
      info.append(body[count]+text)
      count+=1
    else:
      info.append(None)
      print(info)
  return info

def preprocessor(info):
  information=[]
  for i in info:
    if i != None:
      i=i.lower()
      lst= i.split('\n')
      lst=[word for word in lst if len(word) >= 10]
      information.append(lst)
    else:
      information.append(None)
  return information

def classifier(lst):
  scs=[]
  for i in lst:
    if i != None:
      results=pipe(i,candidate_labels=['buy', 'sales','prospect', 'other'])
      scores=[]
      for result in results:
        
        buy = result["scores"][result["labels"].index("buy")]
        prospect = result["scores"][result["labels"].index("prospect")]
    
        total_score = buy + prospect
        scores.append(total_score)
      scs.append(scores)
    else:
      scs.append(None)
  return scs

def score_calculator(lst):
  lead_intent_score=[]
  for i in lst:
    if i != None:
      if len(i) > 0:
        lead_intent_score.append(round(float(np.mean(i)),2))
      else:
        lead_intent_score.append(None)
    else:
      lead_intent_score.append(None)
  return lead_intent_score
