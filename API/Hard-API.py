import requests
import json

class StatusCodeException(Exception):   #建立class是為了更好處理和辨識錯誤
    pass

def readFile(fileName):  # 讀檔案
    try:
        with open(fileName, "r") as file:
            return file.read().strip()
    except FileNotFoundError:
        raise Exception(f"File {fileName} not found")
    except Exception as e:
        raise Exception(f"Error reading file {fileName}: {e}")

def fetchData(endPoint):    #打API
    try:
        response = requests.get(endPoint)
        response.raise_for_status() # 這會為錯誤的回應拋出一個HTTPError
        return response.text
    
    except requests.exceptions.HTTPError as http_error: 
        raise StatusCodeException(f"HTTP error occurred: {http_error}")
    
    except Exception as error:
        raise StatusCodeException(f"Other error occurred: {error}")

def main():
    dateFile = readFile("date.txt")
    endPoint = f"https://agtbooking.hoshinoresorts.com/api/agent/rooms/vacancies/weekly?adult=2&endDate=2024%2F08%2F06&hotelId=0000000201&lang=EN&startDate=2024%2F07%2F31&stayLength=1&underFour=0&underSeven=0&underTwelve=0"
    result  = fetchData(endPoint = endPoint)
    jsonParseResult = json.loads(result)
    
    vacancyList = jsonParseResult.get("vacancyList", [])
    if not vacancyList:
        print("No vacancyList found in the response")
        return

    for detail in vacancyList:
        date = detail["date"]
        if date == dateFile:
            print(detail)
            break
    else:
        print(f"No vacancy found for the date {dateFile}")
        
if __name__ == "__main__":
    main()