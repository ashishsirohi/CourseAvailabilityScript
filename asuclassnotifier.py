from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from bs4 import BeautifulSoup as bs
import re
import os
import getpass
import sys
import yagmail
#from twilio.rest import TwilioRestClient

#Twilio AUTH creds for SMS verification
account_sid = "YOUR_SID"
auth_token  = "YOUR_AUTH"
#client = TwilioRestClient(account_sid, auth_token)


#Availability function (CRON compatible, uses SYSARG)
def class_availability():
    if len(sys.argv) > 1:

        #Yag library to utilize SMTP connection to google server
        #yag = yagmail.SMTP("your_gmail_email@gmail.com", "your_password")

        #Leave these blank, used to concatenate availability and send
        email_to_send = ''
        sms_to_send = ''


        print "Searching...."

        #Sysargs parsed and appended to classes array
        classes = []
        for x in sys.argv:
            classes.append(x)
        classes = classes[1:]

        #Driver INIT
        url_page = "https://webapp4.asu.edu/catalog/classlist?k=91334&t=2177&e=all&hon=F"
        driver = webdriver.PhantomJS(service_args=['--ignore-ssl-errors=true', '--ssl-protocol=any', '--load-images=no'])

        #Mobile workaround
        driver.set_window_size(1400,1000)
        # driver = webdriver.Chrome()
        driver.get(url_page)

        #Avoid cookie issue with JS rendering
        time.sleep(1)

        #Locate radio
        x = driver.find_element_by_id('searchTypeAllClass')

        x.click()
        time.sleep(.5)

        #Loop through sysarg avail class list
        for your_classes in classes:
            url_page = "https://webapp4.asu.edu/catalog/classlist?k=91334&t=2177&e=all&hon=F"
            driver.get(url_page)

            driver.save_screenshot('test_google.png')

            source = driver.page_source

            soup = bs(source, "lxml")

            #print source

            professors = []
            classes = []

            for td in soup.findAll("td", { "class":"instructorListColumnValue" }):
                professors.append(td)

            for td in soup.findAll("td", { "class":"titleColumnValue" }):
                classes.append(td)

            counter = 0
            for td in soup.findAll("td", { "class":"availableSeatsColumnValue" }):
                temp = str(td)
                prof = str(professors[counter])


                prof = prof.strip(' \t\n\r')
                prof = prof.replace(' ', '')
                prof = prof.replace('\n', '')
                prof = prof.replace('\t', '')

                #parse the html patterns
                professor = re.findall(r'\">(?:(.|\n)*)<span>((.|\n)*?)(</span>)', prof)
                class_count = re.findall(r'\">(\d+)(?:(.|\n)*)(of)(?:(.|\n)*>)(\d+)', temp)
                if your_classes in str(td):

                    if (int(class_count[0][0]) > 0):

                        x = '''
****************************************************************************************************************************

Professor %s has open seats available! Hurry now because there are only %s seats left!!

<a href="https://webapp4.asu.edu/catalog/classlist?k=%s&t=2161&e=open&hon=F">Click Here to Register!</a>

****************************************************************************************************************************\n
'''%(professor[0][1], class_count[0][0], your_classes)

                        email_to_send += x
                        sms_to_send += 'https://webapp4.asu.edu/catalog/classlist?k=%s&t=2161&e=open&hon=F - Professor %s\n'%(your_classes, professor[0][1])

                else:
                    print "No Seat avaialble!!"
                counter+=1
        print email_to_send
        """contents = [email_to_send]
        yag.send("WHERE TO SEND", 'Schachte Open Seat Finder!', contents)
        message = client.messages.create(body=sms_to_send,
        to="+",    # Replace with your phone number
        from_="+") # Replace with your Twilio number"""



if __name__ == "__main__":
    class_availability()
