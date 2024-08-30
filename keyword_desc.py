import google.generativeai as genai
import os
from dotenv import load_dotenv, dotenv_values 
load_dotenv()
from desc import desc_keywords
from image_desc import img_keywords
from departments import mapping

genai.configure(api_key=os.getenv("gemini_api"))

import PIL.Image

model = genai.GenerativeModel("gemini-1.5-flash")

def keys_to_list(keys):
    l=keys.split(", ")
    return l

def img_desc_keywords(image_path,text):

    if image_path=="" and text=="":
        return "Did not give any inputs"

    if image_path!="" and text!="":
        #cats=desc_keywords(text)
        keys=model.generate_content([f"This image is uploaded to rail madad platform which is used for raising complaints or grievances in Indian railways. The {text} is the description of the probelem. Analyze this image and text in depth and find the main problems that are related to railways and are effected by people the most( so not the small ones but the big ones that has more impact, if there are no big impacts are there then give the smaller ones) and categorize them into these categrories. the categories are: 1.delay, 2.ticket cancellation, 3.refund, 4.sanitation, 5.injury, 6.food, 7.staff, 8.security, 9.train damages, 10.rail track damages 11.others. Just give the category names only and don't describe the probelem and give the categories in a comma seperated values and don't number them",image_path])
        keywords=keys_to_list(keys.text)
        return keywords

    if image_path!="":
        keys=img_keywords(image_path)
        keywords=keys_to_list(keys.text)
        return keywords

    if text!="":
        text_keys=desc_keywords(text)
        text_keywords=keys_to_list(text_keys.text)
        return text_keywords
    
def departments(image_path,text):
    keys=img_desc_keywords(image_path,text)
    dept=mapping(keys)
    return dept
