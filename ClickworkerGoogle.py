from splinter import Browser
import time
import re

regex = " (\S.+?[a-z][.!?])(?=\s+|$)"

googleSite = None
query = None
pageURL = None
websiteToFind = None
foundWebsite = None
workItem = None
imcompleteText = None
completeText = None
page = None

def login():
    browser.visit("http://www.clickworker.com/")
    browser.fill("username", "user")
    browser.fill("password", "pw")
    browser.find_by_name("commit").click()

def startWork():
    while True:
        if browser.find_link_by_href("/en/clickworker/jobs/82746/edit"):
            print("Found link")
            break
        else:
            print("Sleeping")
            time.sleep(2)
    browser.click_link_by_href("/en/clickworker/jobs/82746/edit")
    print("Clicked the button")

def resetVars():
    googleSite = None
    query = None
    pageURL = None
    websiteToFind = None
    foundWebsite = None
    workItem = None
    imcompleteText = None
    completeText = None
    page = None

def doTask():
    resetVars()
    page = 1

    #find the workitem
    workItemLabel = browser.find_by_css("#things-for-current-job > div:nth-child(1) > span:nth-child(2)")
    workItem = workItemLabel[0].text
    workItem = workItem.replace("#", "")

    #find the google site
    googleSiteLabel = browser.find_by_css("#task_one_1 > div:nth-child(1) > label:nth-child(1) > u:nth-child(2)")
    if "google.com" in googleSiteLabel[0].text:
        googleSite = "http://google.com"
    elif "google.co" in googleSiteLabel[0].text:
        googleSite = "http://google.co"

    #find the query
    queryLabel = browser.find_by_css("#task_one_1 > div:nth-child(1) > div:nth-child(2) > font:nth-child(1)")
    query = queryLabel[0].text

    #visit google and search for query
    googleBrowser.visit(googleSite)
    googleBrowser.find_by_css("a._Gs:nth-child(4)").click()
    googleBrowser.fill('q', query)
    googleBrowser.find_by_name('btnG').click()
    pageURL = googleBrowser.url

    #feed the pageURL to the form
    script = "$('#google_url_1').append('" + pageURL + "');" + "$('#google_url_1').keyup();"
    browser.execute_script(script)

    #asign the website to find
    websiteToFindLabel = browser.find_by_css("#task_two_1 > div:nth-child(1) > div:nth-child(3) > font:nth-child(1)")
    websiteToFind = websiteToFindLabel[0].text

    #find the website on google
    while True:
        found = googleBrowser.find_link_by_partial_href(websiteToFind)
        if found.is_empty():
            googleBrowser.find_by_id("pnnext").click()
            page += 1
        else:
            googleBrowser.find_link_by_partial_href(websiteToFind).click()
            foundWebsite = googleBrowser.url
            break

    #feed page number and url to form
    script = "$('#output_" + str(workItem) + "__google_page1').val('" + str(page) + "');"
    browser.execute_script(script)
    script = "$('#research_url_1').val('" + foundWebsite + "');" + "$('#research_url_1').keyup();"
    browser.execute_script(script)

    #find the incomplete text
    incompleteTextLabel = browser.find_by_css("div.fourcols:nth-child(2) > div:nth-child(2) > label:nth-child(2) > font:nth-child(1)")
    incompleteText = incompleteTextLabel[0].text.replace("…", "")

    #find the complete text on website
    completeText = re.search(incompleteText + regex, googleBrowser.html).group(0)
    print("Found text:", completeText)

    #feed the complete text into the form
    script = "$('#research_code_1').append('" + completeText + "');" + "$('#research_code_1').keyup();"
    browser.execute_script(script)

    #click save
    browser.find_by_css(".button_right").click()


browser = Browser()
googleBrowser = Browser()
login()
startWork()
while True:
    doTask()


# browser.quit()
# googleBrowser.quit()

