import google.generativeai as genai
def desc_keywords(text):
    model = genai.GenerativeModel("gemini-1.5-flash")
    response=model.generate_content([f"This text description: {text} is uploaded to rail madad platform which is used for raising complaints or grievances in Indian railways. Analyze this description in depth and find the main problems that are related to railways and are effected by people the most( so not the small ones but the big ones that has more impact, if there are no big impacts are there then give the smaller ones) and categorize them into these categrories. the categories are: 1.delay, 2. cancellation, 3.refund, 4.sanitation, 5.injury, 6.food, 7.staff, 8.security, 9.others. Just give the category names only and don't describe the probelem and give the categories in a comma seperated values and don't number them"])
    return response.text

def img_keywords(image_path):
    img=PIL.Image.open(image_path)
    model = genai.GenerativeModel("gemini-1.5-flash")
    response=model.generate_content([f"This image is uploaded to rail madad platform which is used for raising complaints or grievances in Indian railways. Analyze this image in depth and find the main problems that are related to railways and are effected by people the most( so not the small ones but the big ones that has more impact, if there are no big impacts are there then give the smaller ones) and categorize them into these categrories. the categories are: 1.delay, 2. cancellation, 3.refund, 4.sanitation, 5.injury, 6.food, 7.staff, 8.security, 9.others. Just give the category names only and don't describe the probelem and give the categories in a comma seperated values and don't number them",image_path])
    return response.text

def mapping(keys):
    dictionary={
        "delay": "railwayStation",
        "ticket cancellation": "railwayStattion",
        "refund": "railwayStation",
        "sanitation": "railwayStation",
        "injury": "medical",
        "food": "railwayStation",
        "staff": "railwayStation",
        "security": "police",
        "others": "railwayStation",
        "train damages": "railwayStation",
        "rail track damages": "railwayStation",
    }
    return dictionary[keys[0]]