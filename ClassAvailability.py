from selenium import webdriver
from bs4 import BeautifulSoup as bs
import time

#function to check the current status of the class
def check_status(course, term):
    # driver inititalizaiton
    print "Checking status for %s..." %course
    url = "https://webapp4.asu.edu/catalog/classlist?k=%s&t=%s&e=all&hon=F" % (course, term)
    driver = webdriver.PhantomJS(service_args=['--ignore-ssl-errors=true', '--ssl-protocol=any'])

    driver.set_window_size(1024, 768)
    driver.get(url)
    time.sleep(0.5)

    #Selecting All class option
    x = driver.find_element_by_id('searchTypeAllClass')
    x.click()

    url = "https://webapp4.asu.edu/catalog/classlist?k=%s&t=%s&e=all&hon=F" % (course, term)
    driver.get(url)
    driver.save_screenshot("class.png") #Testing purpose

    #getting page source
    source = driver.page_source
    soup = bs(source, "lxml")

    #print source
    #print "Current Status:"
    status = []

    instructor = soup.find("td", {"class": "instructorListColumnValue"})
    #status.append(str(instructor).strip('\t\n'))
    if instructor is not None:
        instructor = instructor.text
        status.append(str(instructor).strip('\t\n'))

    course = soup.find("td", {"class": "titleColumnValue"})
    #status.append(str(course).strip('\t\n'))
    if course is not None:
        course = course.text
        status.append(str(course).strip('\t\n'))

    seats = soup.find("td", { "class":"availableSeatsColumnValue" })
    #s = str(seats).strip('\t\n')
    #status.append(str(s.strip('\n').split('of')[0]).strip('\n'))
    if seats is not None:
        seats = seats.text
        s = str(seats).strip('\t\n')
        status.append(str(s.strip('\n').split('of')[0]).strip('\n'))

    #print status

    return status

    #instructor = str(instructor)
    #instructor_out = re.findall(r'\">(?:(.|\n)*)<span>((.|\n)*?)(</span>)', instructor)

    #print seats
    #seats = str(seats)
    #seats_count = re.findall(r'\">(\d+)(?:(.|\n)*)(of)(?:(.|\n)*>)(\d+)', seats)

    #print course
    #course = str(course)
    #course_name = re.findall(r'\">(\d+)(?:(.|\n)*)', course)

    #print str(instructor_out[0][1]).strip(r'\t\n')
    #print course_name
    #print seats_count[0][0]

    pass