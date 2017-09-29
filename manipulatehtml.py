# Python with HTML (HyperText Markup Language)

# Chrome > View > Developer > View Source
# Developer > Developer Tools (organized view) > RC link > inspect
"""
HTML ex:
<html>
  <body>
    <p>
    Paragraph!
    </p>
    <p>
    Move!
      <img src = "cat.jpg">
    </p>
  </body>
</html>
"""

# All Wikipedia pages lead to 'Philosophy'? (philosophy_count)

# Search: "python request web page from a url" = Requests (3rd party)
"""
pip3 install requests
python3
"""
import requests
response = requests.get("https://en.wikipedia.org/wiki/Super_NES_Classic_Edition") # Wikipedia article
print("HERE IS FULL HTML")
print(response.text) # lotsa HTML
print("HERE IS HTML TYPE")
print(type(response.text)) # hint: string

# Search: "python parse HTML" = BeautifulSoup (3rd party)
"""
pip3 install beautifulsoup4
python3
"""
from bs4 import BeautifulSoup
# import requests
# response = requests.get("https://en.wikipedia.org/wiki/Super_NES_Classic_Edition")
html = response.text
print("HERE IS FULL HTML")
print(html)
soup = BeautifulSoup(html, 'html.parser')
print("HERE IS TITLE")
print(soup.title)
print("HERE IS 1ST PARAGRAPH")
print(soup.p)
print("HERE IS FRIST LINK")
print(soup.p.a)
print("HERE IS ALL ANCHOR TAGS IN 1ST PARAGRAPH")
print(soup.p.find_all('a'))
print("HERE IS DIV ELEMENT WITH THIS ID")
print(soup.find(id="image-gallery"))
