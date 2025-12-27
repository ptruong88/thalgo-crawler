from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By

def _get_element(container_div, orders):
    temp_div = container_div
    for order in orders:
        elements = order.split(':')
        print(f"elements: {elements}")
        element_type = elements[0]
        element_name = elements[1]
        if element_type == 'CLASS_NAME':
            temp_div = temp_div.find_element(By.CLASS_NAME, element_name)
        elif element_type == 'ID':
            temp_div = temp_div.find_element(By.ID, element_name)
        elif element_type == 'TAG_NAME':
            temp_div = temp_div.find_element(By.TAG_NAME, element_name)
    return temp_div

def get_element_text(container_div, orders, isElementHidden = False):
    temp_div = _get_element(container_div, orders)        
    return temp_div.get_attribute("textContent") if isElementHidden else temp_div.text

def get_element_attribute(container_div, orders, attribute_name):
    return _get_element(container_div, orders).get_attribute(attribute_name)

def get_elements(container_div, orders):    
    result = []
    temp_element = _get_element(container_div, orders[:-1])
    elements = orders[-1].split(':')
    # print(f"elements: {elements}")
    element_type = elements[0]
    element_name = elements[1]
    if element_type == 'CLASS_NAME':
        result = temp_element.find_elements(By.CLASS_NAME, element_name)

    return result