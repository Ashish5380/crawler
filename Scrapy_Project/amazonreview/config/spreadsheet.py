from Scrapy_Project.amazonreview.utils.logger import logger

import gspread


class AmazonLinks:

    def __init__(self):
        self.client = gspread.service_account('../../amazonreview/AmazonLink-e2dbc198a2b4.json')
        self.data = self.get_all_values_from_sheet()

    """ gets all data from all spread sheet and puts it in a dictionary"""
    def get_all_values_from_sheet(self):
        logger.info("Opening connection to Google sheets")
        spreadsheets = self.client.open('AmazonLinks')
        # get list of all spreadsheet
        titles_list = []
        for spreadsheet in spreadsheets:
            titles_list.append(spreadsheet.title)
        logger.info("Brands to be processed: {}".format(titles_list))
        # fetch data from all the spreadsheet
        rows = []
        for brand in titles_list:
            sheet = spreadsheets.worksheet(brand)
            values_from_sheet = sheet.get_all_values()[1:]
            rows.extend(values_from_sheet)
        return rows
