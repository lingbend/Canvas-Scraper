from bs4 import BeautifulSoup
import requests
from canvasapi import Canvas
import time
import webbrowser
from CanvasKeys import keys, base_urls
import sys



def main():
    if (len(sys.argv) < 5):
        print("""Too few arguments, give arguments in the form of
               python CanvasScraper.py domain_index(int) course_number output_file_name mode""")
        exit()
    domain = int(sys.argv[1] - 1)
    current_api_key = keys[domain]
    root = base_urls[1]
    course_num = sys.argv[2]
    outfile_name = sys.argv[3]
    mode = sys.argv[4]

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
    important_pages = []

    for j in new_page_list: # printing the url of each page
        print(j)
        html_page = course.get_page(j).body
        if (mode == "-h"):
            h5p_mode(html_page, important_pages, j, root, course_num)

    print(important_pages)

def h5p_mode(page_body, important_pages, j, root, course_num):
    if '.h5p.com' in page_body or (course_num + '/external_tools/retrieve?') in page_body or 'h5p-iframe' in page_body:
        important_pages.append(root + '/courses/' + course_num + '/pages/' + j)





if __name__ == "__main__":
    main()