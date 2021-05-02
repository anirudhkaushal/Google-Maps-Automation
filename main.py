from selenium import webdriver
from time import sleep

driver = webdriver.Chrome("D:\Downloads\chromedriver_win\chromedriver")
driver.get("https://www.google.com/maps/@22.1725814,81.7803918,4.84z")

sleep(2)

def destinationPoint():
    destinationPlace = driver.find_element_by_class_name("tactile-searchbox-input")
    destinationPlace.send_keys("Bengaluru")
    submit = driver.find_element_by_xpath("/html/body/jsl/div[3]/div[9]/div[3]/div[1]/div[1]/div[1]/div[2]/div[1]/button")
    submit.click()

destinationPoint()

def directions():
    sleep(5)
    directions = driver.find_element_by_xpath("/html/body/jsl/div[3]/div[9]/div[8]/div/div[1]/div/div/div[4]/div[1]/div/button")
    directions.click()

directions()

def startingPoint():
    sleep(5)
    startingPlace = driver.find_element_by_xpath("/html/body/jsl/div[3]/div[9]/div[3]/div[1]/div[2]/div/div[3]/div[1]/div[1]/div[2]/div/div/input")
    startingPlace.send_keys("Mumbai")
    sleep(5)
    submit = driver.find_element_by_xpath("/html/body/jsl/div[3]/div[9]/div[3]/div[1]/div[2]/div/div[3]/div[1]/div[1]/div[2]/button[1]")
    submit.click()

startingPoint()

def getDistance():
    sleep(2)
    totalDistance = driver.find_element_by_xpath("/html/body/jsl/div[3]/div[9]/div[8]/div/div[1]/div/div/div[5]/div[2]/div/div[1]/div[1]/div[2]/div")
    print("Total distance (in km) : ", totalDistance.text)
    totalTravellingTimeViaCar = driver.find_element_by_xpath("/html/body/jsl/div[3]/div[9]/div[8]/div/div[1]/div/div/div[5]/div[2]/div/div[1]/div[1]/div[1]/span[1]")
    print("Total travelling time via car : ", totalTravellingTimeViaCar.text)
    totalTravellingTimeViaAeroplane = driver.find_element_by_xpath("/html/body/jsl/div[3]/div[9]/div[8]/div/div[1]/div/div/div[5]/div[3]/div/div[4]/div[1]/div/div[1]")
    print("Total travelling time via aeroplane : ", totalTravellingTimeViaAeroplane.text)

getDistance()


