import gspread


class AmazonLinks:

    def __init__(self):
        self.client = self.create_client()
        self.data = self.get_all_values_from_sheet()
        print(self.values)

    def create_client(self):
        return gspread.service_account('../../AmazonLink-e2dbc198a2b4.json')

    """ gets all data from all spread sheet and puts it in a dictionary"""
    def get_all_values_from_sheet(self):
        value = []
        titles_list = []
        data_dict = {}
        spreadsheets = self.client.open('AmazonLinks')
        # get list of all spreadsheet
        for spreadsheet in spreadsheets:
            titles_list.append(spreadsheet.title)
        # fetch data from all the spreadsheed
        for brand in titles_list:
            sheet = spreadsheets.worksheet(brand)
            value.extend(sheet.get_all_values()[:])
            data_dict = self.construct_dict_from_values(value, data_dict)
            value = []
        return data_dict

    """Inputs value list from a spread sheet and appends to the dictionary passed"""
    def construct_dict_from_values(self, values, dict):
        headers = values.pop(0)
        for value in values:
            for index in range(len(headers)):
                if headers[index] not in dict.keys():
                    dict[headers[index]] = [value[index]]
                else:
                    dict[headers[index]].append(value[index])
        return dict


if __name__ == '__main__':
    AmazonLinks()
