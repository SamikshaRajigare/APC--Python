import re
def extract_hashtags(text):
    hashtags = re.findall(r'#\w+', text)
    return hashtags

post = """
Loving the new features in Python! #Python #Coding #AI_Projects
Stay updated with #MachineLearning and #DataScience.
"""
print(extract_hashtags(post))