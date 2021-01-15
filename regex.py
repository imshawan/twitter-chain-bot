import re

url_pattern = re.compile(r"http\S+", re.DOTALL)

example_tweet = "Check this out. https://linkedin.com"
text_without_url = url_pattern.sub(r"", example_tweet)