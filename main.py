import csv
import time

import tkinter as tk
from tkinter import ttk

from selenium import webdriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

type_of_business = "Restaurant"
name_of_city = "New York"
number_of_listing = 10
output_file = "business_listings.csv"
is_started = None


def get_inputs():
    global type_of_business
    global name_of_city
    global number_of_listing
    global output_file

    root = tk.Tk()
    root.title("Business Listing Search")
    root.geometry("450x300")
    root.resizable(False, False)

    # Use existing variables as defaults
    type_of_business_var = tk.StringVar(value=type_of_business)
    name_of_city_var = tk.StringVar(value=name_of_city)
    number_of_listing_var = tk.StringVar(value=str(number_of_listing))
    output_file_var = tk.StringVar(value=output_file)

    ttk.Label(root, text="Business type:").pack(anchor="w", padx=20, pady=(20, 5))
    ttk.Entry(root, textvariable=type_of_business_var, width=45).pack(padx=20)

    ttk.Label(root, text="City name:").pack(anchor="w", padx=20, pady=(15, 5))
    ttk.Entry(root, textvariable=name_of_city_var, width=45).pack(padx=20)

    ttk.Label(root, text="Minimum number of listings:").pack(
        anchor="w", padx=20, pady=(15, 5)
    )
    ttk.Entry(root, textvariable=number_of_listing_var, width=45).pack(padx=20)

    ttk.Label(root, text="Output CSV file name:").pack(
        anchor="w", padx=20, pady=(15, 5)
    )
    ttk.Entry(root, textvariable=output_file_var, width=45).pack(padx=20)

    def submit():
        global type_of_business
        global name_of_city
        global number_of_listing
        global output_file
        global is_started
        is_started = 1
        type_of_business = type_of_business_var.get()
        name_of_city = name_of_city_var.get()
        number_of_listing = int(number_of_listing_var.get())
        output_file = output_file_var.get()

        root.destroy()

    ttk.Button(root, text="Start", command=submit).pack(pady=5)

    root.mainloop()

def scroll_and_wait(wait_time=5) :
    driver.execute_script(
    '''
       element = document.querySelector('.m6QErb.DxyBCb.kA9KIf.dS8AEf.XiKgde.ecceSd[role="feed"]');
       element.scrollTo(0,element.scrollHeight);
       element.scrollTo(0,element.scrollHeight);
    '''
    )
    time.sleep(wait_time)

def find_and_get(parent_element, child_element_css_selector) :
    result="-"
    try :
        element =  parent_element.find_elements(By.CSS_SELECTOR, child_element_css_selector)[-1]
        result = element.text
    except :
        pass
    return result



get_inputs()


main_url = f"https://www.google.com/maps/search/{type_of_business}+in+{name_of_city}/"


options= Options()
options.add_argument('--incognito')
if not is_started :
    exit() 
driver = uc.Chrome(options=options)
driver.get(main_url)
time.sleep(3)
try :
    element = driver.find_element(By.CSS_SELECTOR, '.m6QErb.DxyBCb.kA9KIf.dS8AEf.XiKgde.ecceSd[role="feed"]')
except :
    print("Failed")
    time.sleep(300)
if not element  :
    exit()
all_nodes = driver.find_elements(By.CSS_SELECTOR, '[class="hfpxzc"]')
while len(all_nodes ) < number_of_listing  :
    number_of_listing_before_scroll=len(all_nodes)
    scroll_and_wait()
    all_nodes = driver.find_elements(By.CSS_SELECTOR, '[class="hfpxzc"]')
    if len(all_nodes) == number_of_listing_before_scroll :
        break

all_links = [element.get_attribute('href') for element in all_nodes]

all_data = []

for link in all_links :
    driver.get(link)
    time.sleep(1)
    element = ""
    try:
        element = driver.find_element(By.CSS_SELECTOR,'.m6QErb.XiKgde[role="region"]:has([ve-visible])')
    except :
       pass
    if not element :
        continue

    name  = "-"
    phone = "-"
    website = "-"
    name = find_and_get( driver, ".DUwDvf.lfPIob")
    phone = find_and_get(driver,'button .AeaXub:has(.google-symbols.NhBTye.PHazN)  .rogA2c')
#    print(phone)
 #   print(not phone.replace('+','').replace('-','').isnumeric() )
    if not phone.replace('+','').replace('-','').replace(' ','').isnumeric() :
        phone= '-'
    website = find_and_get(driver,'.AeaXub:has(.google-symbols.PHazN) .ITvuef')
    all_data.append([name,phone,website])
driver.quit()
with open(output_file, "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)

    writer.writerow(["Name", "Phone", "Website"])
    writer.writerows(all_data)


