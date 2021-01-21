class Lead:
    def __init__(self, tc_brand, tc_number, driver, garage_number):
        self.tc_brand = tc_brand
        self.tc_number = tc_number
        self.driver = driver
        self.garage_number = garage_number

    def change_tc(self, new_tc_brand, new_tc_number):
        old_tc_brand = self.tc_brand
        old_tc_number = self.tc_number
        self.tc_brand = new_tc_brand
        self.tc_number = new_tc_number
        return 'Марка ТС изменен с ' + str(old_tc_brand) + ' на ' + str(self.tc_brand) + "\n" + \
               'Номер ТС изменен с ' + str(old_tc_number) + ' на ' + str(self.tc_number)

    def change_driver(self, new_driver_name):
        old_driver = self.driver
        self.driver = new_driver_name
        return 'Имя водителя изменена с ' + old_driver + ' на ' + self.driver

    def change_garage_number(self, new_garage_number):
        old_garage_number = self.garage_number
        self.garage_number = new_garage_number
        return 'Гаражный номер изменен с ' + str(old_garage_number) + ' на ' + str(self.garage_number)


a = Lead(12345, 67890, 'Андрей', 321)

print(a.change_tc(131516, 12131415))
print(a.change_driver("Алексей"))
print(a.change_garage_number(12345))
