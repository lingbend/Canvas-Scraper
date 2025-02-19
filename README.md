# Canvas-Scraper

## Instructions
This is webscraper for the LMS Canvas using the canvasapi library.

This code requires you to have a CanvasKeys.py file with 2 lists stored inside: keys and base_urls. base_urls should store the roots of the canvas domains you wish to scrape as strings, ending in the TLD with no "/" at the end. The keys need to be generated within your Canvas account and only have the access you do. The keys should be stored as strings at the same index of the corresponding base_url.

## Input Format
python CanvasScraper.py domain_index(int starting at 1) course_number output_file_name.html mode

## Current modes:
- h5p activity finder: "-h"
- search mode: "-s" (add the keyword as the last parameter)

## Disclaimer
This code is provided for educational purposes only. Ensure you comply with the terms of service of any website you scrape and refer to their robots.txt file. Do not scrape Canvas without permission.

## Author
- lingbend
