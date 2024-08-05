from openSheet import openSpreadSheet

def main():
    spreadSheetUrl = f"https://docs.google.com/spreadsheets/d/1AtAyqgkAUv3uWQwmerDLGPaw_BpR6WVe-C1ny7GqJqM/edit?gid=0#gid=0"    #google sheet url
    sheetName = "gsheets"   #google sheet table name
    sheet = openSpreadSheet(spreadSheetUrl , sheetName) #call openSpreadSheet funciton
    dataFrame = sheet.get_all_records() #拿到表單中的全部資料
    for data in dataFrame:  #for in 迴圈取資料
        print(f"AY_order_ID : {data["AY_order_id"]}, AY_order_host_id : {data["AY_order_host_id"]}, AY_order_room_id : {data["AY_order_room_id"]}")  #輸出對應資料

if __name__ == "__main__":
    main()