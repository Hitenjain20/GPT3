#!/usr/bin/env python
# coding: utf-8

# In[1]:


import openai
import os 


# In[2]:


openai_key = os.environ.get("Openai_APi_key")


# In[3]:


openai.File.create(file=open("output.jsonl"), purpose='answers')


# In[7]:


myPrompt = """
What is your banks interest rate offer on housing loans?
"""


# In[10]:


response = openai.Answer.create(
    search_model="ada", 
    model="davinci", 
    question=myPrompt, 
    file="file-HJv6zXAwxGXffp4FA0vJBOOl", 
    examples_context="Anyone can open a account in this bank for just 1000 Rupees .", 
    examples=[["In how much it cost ot open my account?", "1000 Rupees."]], 
    max_rerank=10,
    max_tokens=50,
    stop=["\n", "<|endoftext|>"]
)


# In[11]:


print(response)


# In[ ]:




