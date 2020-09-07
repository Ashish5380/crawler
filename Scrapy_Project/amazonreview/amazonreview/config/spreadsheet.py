import gspread


class AmazonLinks:

    def __init__(self):
        self.client = self.create_client()
        self.values = self.get_all_values_from_sheet()
        self.data = self.construct_dict_from_values()

    def create_client(self):
        return gspread.service_account('/Users/ashishbhatt/Downloads/AmazonLink-e2dbc198a2b4.json')

    def get_all_values_from_sheet(self):
        sheet = self.client.open('AmazonLinks').sheet1
        value = sheet.get_all_values()
        return value

    def construct_dict_from_values(self):
        dict_data = {}
        headers = self.values.pop(0)
        print(self.values)
        data = []
        for index in range(len(headers)):
            for val in self.values:
                data.append(val[index])
            dict_data.setdefault(headers[index], data)
            data = []
        return dict_data


if __name__ == '__main__':
    AmazonLinks()
