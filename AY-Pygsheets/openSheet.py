def openSpreadSheet(spreadSheetUrl , sheetName):
    import pygsheets
    gc = pygsheets.authorize(service_file = r"C:\Users\csc26\Desktop\Google\sheet-access-250701-f43fa8915df5.json")    #Google憑證
    spreadSheet = gc.open_by_url(spreadSheetUrl)    #透過url打開指定google sheet
    sheet = spreadSheet.worksheet_by_title(sheetName)   #透過表單名稱打開對應表單
    return sheet
