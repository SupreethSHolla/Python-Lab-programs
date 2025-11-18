# Q: What does findall() return here?
import re


def extractDate(url):
    return re.findall(r'/(\d{4})/(\d{1,2})/(\d{1,2})/', url)


url1 = "https://www.washingtonpost.com/nation/2023/03/04/pandemic-food-stamps-ending/"
print(extractDate(url1))

url2 = input("Enter new url: ")
print(extractDate(url2))
