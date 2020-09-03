# Automated-newsletter
This is a copy of the automated newsletter I built for TheCovidSolutionsGuide website

It is currently an on going process as many parts of the program are still being changed. 

To run it first install the requirements with 

pip install -r requirements.txt

Credentials have to be created, see google sheets api https://developers.google.com/sheets/api/quickstart/python

repeat the same steps for google docs and gmail

install wkhtmltopdf, this processes differs on different operating systems.

Now run makeNewsletter.py will generated the newsletter with banner, blogs from the website, and links that are sent to the company email. 

and gSheets.py will return the emails of the subscribers of newsletter on the website.