import requests
import json

def readFile(fileName):  # 讀檔案
    with open(fileName, "r") as file:
        return file.read().strip()

def fetchData(endPoint):    #打API
    response = requests.get(endPoint)
    if response.status_code == 200:
        return response.text
    else:
        print(f"Error {response.status_code}")

def main():
    dateFile = readFile("date.txt")
    endPoint = f"https://agtbooking.hoshinoresorts.com/api/agent/rooms/vacancies/weekly?adult=2&endDate=2024%2F08%2F06&hotelId=0000000201&lang=EN&startDate=2024%2F07%2F31&stayLength=1&underFour=0&underSeven=0&underTwelve=0"
    result  = fetchData(endPoint = endPoint)
    jsonParseResult = json.loads(result)
    
    vacancyList = jsonParseResult["vacancyList"]

    for detail in vacancyList:
        date = detail["date"]
        if date == dateFile:
            print(detail)
            break

        
if __name__ == "__main__":
    main()