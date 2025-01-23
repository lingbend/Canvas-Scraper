from bs4 import BeautifulSoup
import requests
from canvasapi import Canvas
import time
import webbrowser
from CanvasKeys import keys, base_urls
import sys



def main():
    domain = sys.argv[1] # Gets domain number from keyfile
    current_api_key = keys[domain]
    root = base_urls[1]
    course_num = sys.argv[2]

    canvas = Canvas(root, current_api_key) # Creates a Canvas object
    course = canvas.get_course(course_num) # Creates a course object using the course number
    page_list = course.get_pages() # Gets a list of all the course's regular pages as an object

    new_page_list = []
    for i in page_list: # getting each page's URL and checking if valid
        url = root + '/courses/' + course_num + '/pages/' + i.url
        print(url) # displaying URL
        if requests.get(url).status_code != 200: # checking if website doesn't give an error code
            print('error')
        else:
            new_page_list.append(i.url) # adding the unique part of the URL to a list
        time.sleep(1)
    h5p_pages = []

    for j in new_page_list: # printing the url of each page
        print(j)
        html_page = course.get_page(j).body
        if 'byu.h5p.com' in html_page or '585/external_tools/retrieve?' in html_page or 'h5p-iframe' in html_page:
            h5p_pages.append('https://byuis.instructure.com/courses/585/pages/' + j)

    print(h5p_pages)