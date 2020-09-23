import gspread
from ecommerce_crawler.onedirect_common.utils.logger import logger
import os
cwd = os.getcwd()
spreadsheet_json_file = os.path.join(cwd, "onedirect_common/config/config_files/spreadsheet.json")


class AmazonLinks:

    def __init__(self):
        self.client = gspread.service_account(spreadsheet_json_file)
        self.data = self.get_all_values_from_sheet()

    """ gets all data from all spread sheet and puts it in a dictionary"""

    def get_all_values_from_sheet(self):
        logger.info("Opening connection to Google sheets")
        spreadsheets = self.client.open('AmazonLinks')
        # get list of all spreadsheet
        titles_list = []
        for spreadsheet in spreadsheets:
            titles_list.append(spreadsheet.title)
        # fetch data from all the spreadsheet
        logger.info("Brands to be processed: {}".format(titles_list))
        rows = []
        for brand in titles_list:
            sheet = spreadsheets.worksheet(brand)
            values_from_sheet = sheet.get_all_values()[1:]
            rows.extend(values_from_sheet)
        logger.info("Number of rows fetched from spreadsheet :: {0}".format(len(rows)))
        return rows
