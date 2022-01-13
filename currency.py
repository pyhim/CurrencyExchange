from requestdata import request_currency


class Currency:

    def __init__(self):
        func_call = request_currency()
        self._currencies = func_call[0]
        self._currencies.pop([0][0])
        self._status_code = func_call[1]

    def status(self):
        status = "OK"

        if self._status_code >= 400:
            status = "Error"

        return self._status_code, status

    def sale(self, sale_currency_name, sale_value):
        result = float()

        for element in self._currencies:
            if element['currency'] == sale_currency_name:
                result = sale_value * element['saleRateNB']

        return result

    def purchase(self, purchase_currency_name, purchase_value):
        result = float()

        for element in self._currencies:
            if element['currency'] == purchase_currency_name:
                result = purchase_value / element['purchaseRateNB']

        return result

    def show_currency(self, currency_name):
        result = None

        for element in self._currencies:
            if element['currency'] == currency_name:
                result = {
                    'Sale': element['saleRateNB'],
                    'Purchase': element['purchaseRateNB']
                }

        return result
