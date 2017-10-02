# Wikipedia Web Crawl Case Study
# By clicking the first link of each Wikipedia article, how long will it take to get to the "Philosophy" article?

import time
import urllib
import requests
import bs4

"""
Steps: (a few mins of planning can save hours of wasted time)
1. Try it out
2. Learn
3. Design
4. Write code
5. Test
6. Repeat
"""

# Define the starting article
# start_url = "https://en.wikipedia.org/wiki/Special:Random"
start_url = "https://en.wikipedia.org/wiki/Class_(biology)"
# Define the target article ("Philosophy")
target_url = "https://en.wikipedia.org/wiki/Philosophy"
target_url2 = "https://en.wikipedia.org/wiki/Philosophical" # re-directs to "Philosophy"

# Function to find the first link in an article
def find_first_link(url):
    # Requests library, extracts HTML
    response = requests.get(url)
    html = response.text
    # BeautifulSoup library, parses HTML
    soup = bs4.BeautifulSoup(html, "html.parser")
    # Find the <div> that contains the article's body
    content_div = soup.find(id='mw-content-text').find(class_="mw-parser-output")

    # If the article contains no links, this value will remain None
    article_link = None

    if not content_div:
        return
    # Find all direct children of content_div that are paragraphs
    for element in content_div.find_all("p", recursive=False):

        # Finds links that are italicized
        if element.find("i", recursive=False):
            if element.find("i", recursive=False).find("a", recursive=False):
                article_link = element.find("i", recursive=False).find("a", recursive=False).get('href')
                break

        # Find the first anchor tag that's a DIRECT CHILD of a paragraph
        # This will ignore other links, i.e. footnotes and pronunciation
        if element.find("a", recursive=False):
            article_link = element.find("a", recursive=False).get('href')
            break
    # Return None if article_link still doesn't have a value
    if not article_link:
        return

    # TODO: avoid articles starting with "Help:"
    # while article_link[:11] == "/wiki/Help:":

    # If not none, build a full url from the article_link url
    first_link = urllib.parse.urljoin('https://en.wikipedia.org/', article_link)

    # USE TO AVOID CYCLES!
    if first_link in article_chain[:-1]:
        for element in content_div.find_all("p", recursive=False):
            # Finds the second link
            if element.findAll("a", recursive=False)[1]:
                article_link = element.findAll("a", recursive=False)[1].get('href')
                break
        if not article_link:
            return
        first_link = urllib.parse.urljoin('https://en.wikipedia.org/', article_link)

    return first_link

# Function to define when the crawler should stop
def continue_crawl(search_history, target_url, target_url2, max_steps=25):
    # Print each article as it's found
    print(article_chain[-1])
    # If the target has been found
    if search_history[-1]==target_url or search_history[-1]==target_url2:
        # Check if first article is random, if so search_history will be +1
        if start_url == "https://en.wikipedia.org/wiki/Special:Random":
            first_article = search_history[1]
            philosophy_score = len(search_history)-2
        else:
            first_article = search_history[0]
            philosophy_score = len(search_history)-1
        print("VOILA! The target article has been found. {} has a philosophy score of {}! :O".format(first_article[30:], philosophy_score))
        # Stop the function and resulting loop
        return False
    # If the list is too long
    elif len(search_history)>max_steps:
        print("Daaang, we couldn't find it. That list is too long!")
        return False
    # If the list has a cycle
    elif search_history[-1] in search_history[:-1]:
        print("Woah, list has a cycle, dude!")
        return False
    # Otherwise continue the crawler
    else:
        return True

# Initialize the article_chain list with the first article
article_chain = [start_url]

# CRAWL! Can add an argument to change max_steps
while continue_crawl(article_chain, target_url, target_url2, 100):
    # Call the find_first_link function to get that first link in an article
    first_link = find_first_link(article_chain[-1])
    # If there are no links, first_link will have a returned value of None
    if not first_link:
        print("ABORT! ABORT! This article has no links.")
        break
    # As long as first_link has a value, it will be added to the article list
    article_chain.append(first_link)
    # Delay for about two seconds to avoid flooding Wikipedia
    time.sleep(2)
