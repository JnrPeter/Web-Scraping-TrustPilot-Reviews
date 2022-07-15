# We first begin by importing the necessary libraries to be used for scraping
from bs4 import BeautifulSoup
import requests

# An input command that allows user to type in the url of the site page to be scraped
print("Welcome!!!!")
input = input("Paste or enter the url of the site that you want to scrape here>>> ")

#connecting to the site page that we want to scrape and getting html back in text.
scrape = requests.get(input).text

#passing the html we got from the page into the beautiful soup parser to clean the html and assign it to an object called "soup".
soup = BeautifulSoup(scrape,'html.parser')

# This is to print out the title of the site page we are scraping, just to make sure that we have the page we want.
print(soup.title.text)

## We find all the article and class tags in the soup object which contains the information we want to scrape
maintags = soup.find_all('article',class_= "paper_paper__1PY90 paper_square__lJX8a card_card__lQWDv styles_reviewCard__hcAvl")

#A for loop to run through the main tags and find the subtags that contain the information we want.
for i in maintags:
    re = i.find('p', {"data-service-review-text-typography": "true"})
    num = i.find('div', {"data-consumer-reviews-count": "1"})

    #A check to ensure that the reviews and the number of reviews is not None, without doing this we won't get any attribute (text or integer) from those tags.

    if re is not None and num is not None:

       #Looking for the tags that contain the name of the consumer and returning the text that it contains.
       name = i.find('div', {"data-consumer-name-typography": "true"}).text

       #Looking for the tags that contain the number of reviews and returning the text that it contains.
       num_review = i.find('div', {"data-consumer-reviews-count": "1"}).text

       # Looking for the tags that contain rating score and returning the text that it contains
       score = i.find('div', class_="star-rating_starRating__4rrcf star-rating_medium__iN6Ty").img.get("alt")

       # Looking for the tags that contain date the review was posted and returning the text that it contains
       time = i.find('div',class_="typography_typography__QgicV typography_bodysmall__irytL typography_color-gray-6__TogX2 typography_weight-regular__TWEnf typography_fontstyle-normal__kHyN3 styles_datesWrapper__RCEKH").text

       # Looking for the tags that contain the title of the review and returning the text that it contains
       Review_Title = i.find('h2', class_="typography_typography__QgicV typography_h4__E971J typography_color-black__5LYEn typography_weight-regular__TWEnf typography_fontstyle-normal__kHyN3 styles_reviewTitle__04VGJ").text

       # Looking for the tags that contain the review comments and returning the text that it contains
       review = i.find('p', {"data-service-review-text-typography": "true"}).text

       # We create a new directory called Trustpilot_reviews and a text file called Customer_reviews.txt. We then write the output of of our code(Name,num_review etc.) into that file
       with open("Trustpilot_reviews/Customer_reviews.txt", "a") as f:
           f.write(f"Name:{name.strip()} \n")
           f.write(f"num_review:{num_review.strip()} \n")
           f.write(f"score:{score.strip()} \n")
           f.write(f"time:{time.strip()} \n")
           f.write(f"Review_Title:{Review_Title.strip()} \n")
           f.write(f"reviews:{review.strip()} \n")
           f.write ("\n")
           f.write("\n")


    print("Done")