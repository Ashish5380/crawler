import gspread

class AmazonLinks:

    def __init__(self):
        self.client = gspread.service_account('../AmazonLink-e2dbc198a2b4.json')
        self.data = self.get_all_values_from_sheet()
        print(self.data)

    """ gets all data from all spread sheet and puts it in a dictionary"""
    def get_all_values_from_sheet(self):
        spreadsheets = self.client.open('AmazonLinks')
        # get list of all spreadsheet
        titles_list = []
        for spreadsheet in spreadsheets:
            titles_list.append(spreadsheet.title)
        # fetch data from all the spreadsheet
        rows = []
        for brand in titles_list:
            sheet = spreadsheets.worksheet(brand)
            values_from_sheet = sheet.get_all_values()[1:]
            rows.extend(values_from_sheet)
        return rows
