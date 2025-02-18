from bs4 import BeautifulSoup
import os
import re

folder_path = "/mnt/c/Users/jaquij/Dropbox/PC/Desktop/Spring 2025 Crowdsourcing Research/Spring-2025-Research/Data"

for filename in os.listdir(folder_path):
    file_path = os.path.join(folder_path, filename)
    # print(filename)
    with open(file_path, "r", encoding="utf-8") as file:
        content = file.read()
        soup = BeautifulSoup(content, "html.parser")  # Parse HTML
        
        title = soup.title.text.strip()
        UncleanName, Title = title.split(":", 1)
        Title = Title.strip()
        CleanName = UncleanName.split("by")[1].strip()
        print("GoFundMe Source:", filename)
        print("GoFundMe Name:", CleanName)
        print("GoFundMe CleanTitle:", Title)

        donation_elements = soup.find_all(class_=re.compile("progress-meter_progressMeterHeading"))

        for elem in donation_elements:
            # Check if the element contains a donation amount or goal (check for specific keywords in text)
            if "raised of" in elem.text.lower():
                donation_amount = elem.text.strip()
                raised = donation_amount.split("raised of")[0]
                rest = donation_amount.split("raised of")[1]
                goal,num_donations = rest.split("goal")
                goal = goal.strip("raised")
                raised = raised.strip("raised")
                num_donations = re.sub(r"\D","", num_donations)


                
            else:
                donation_amount = elem.text.strip()
                raised = donation_amount.split("raised of")[0]
                rest, num_donations, goal = ["NA","NA","NA"]
                raised = raised.strip("raised")
                
                

        print("Donation Amount:", raised)
        print("Goal Amount:", goal)
        print("# of Donations:", num_donations)


        print("")
        

        # print("Full Title:", title)