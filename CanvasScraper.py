import requests
from canvasapi import Canvas
from CanvasKeys import keys, base_urls
import sys



def main():
    if (len(sys.argv) < 5):
        print("""Too few arguments, give arguments in the form of
               python CanvasScraper.py domain_index(int) course_number output_file_name mode""")
        exit()
    domain = int(sys.argv[1]) - 1
    current_api_key = keys[domain]
    root = base_urls[domain]
    course_num = sys.argv[2]
    outfile_name = sys.argv[3]
    mode = sys.argv[4]
    search = ""
    if mode == "-s":
        if len(sys.argv) < 6:
            print("""Too few arguments, give arguments in the form of
            python CanvasScraper.py domain_index(int) course_number output_file_name mode""")
            exit()
        search = sys.argv[5]

    canvas = Canvas(root, current_api_key) # Creates a Canvas object
    course = canvas.get_course(course_num) # Creates a course object using the course number
    page_list = course.get_pages() # Gets a list of all the course's regular pages as an object

    new_page_list = []
    print('Retrieving page urls:')
    for i in page_list: # getting each page's URL and checking if valid
        url = root + '/courses/' + course_num + '/pages/' + i.url
        # print(url) # displaying URL
        code = requests.get(url).status_code
        if code != 200: # checking if website doesn't give an error code
            print('\nBad status code,' + code + ', continuing...')
        else:
            new_page_list.append(i.url) # adding the unique part of the URL to a list
        print('.', end="")
    important_pages = []
    print('\nFiltering urls:')
    for j in new_page_list: # printing the url of each page
        # print(j)
        html_page = course.get_page(j).body
        if (html_page is None):
            continue
        elif (mode == "-h"):
            h5p_mode(html_page, important_pages, j, root, course_num)
            print('.', end="")
        elif (mode == "-s"):
            search_mode(html_page, important_pages, j, root, course_num, search)
            print('.', end="")


    print('\nAdding urls to html file:')
    output_file = open(outfile_name, "w")
    output_file.write('<!DOCTYPE html>\n<html>\n<body>')
    for k in important_pages:
        output_file.write('<p><a href="' + k + '">' + k + '</a></p>' + "\n")
        print('.', end="")
    output_file.write('</body>\n</html>\n')
    output_file.close()
    print('\nFinished')

def h5p_mode(page_body, important_pages, j, root, course_num):
    if '.h5p.com' in page_body or (course_num + '/external_tools/retrieve?') in page_body or 'h5p-iframe' in page_body:
        important_pages.append(root + '/courses/' + course_num + '/pages/' + j)

def search_mode(page_body, important_pages, j, root, course_num, key_word):
    if key_word in page_body:
        important_pages.append(root + '/courses/' + course_num + '/pages/' + j)






if __name__ == "__main__":
    main()