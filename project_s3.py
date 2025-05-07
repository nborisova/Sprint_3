import datetime

class OnlineSalesRegisterCollector:

    def __init__(self):
        self.__name_items = []
        self.__number_items = 0
        self.__item_price = {'чипсы': 50, 'кола': 100, 'печенье': 45, 'молоко': 55, 'кефир': 70}
        self.__tax_rate = {'чипсы': 20, 'кола': 20, 'печенье': 20, 'молоко': 10, 'кефир': 10}

    @property
    def name_items(self):
        return self.__name_items
    
    @property
    def number_items(self):
        return self.__number_items
    
    def add_item_to_cheque(self, name):
        if len(name) == 0 or len(name) > 40:
            raise ValueError('Нельзя добавить товар, если в его названии нет символов или их больше 40')
        elif name not in self.__item_price:
            raise NameError('Позиция отсутствует в товарном справочнике')
        else:
            self.__name_items.append(name)
            self.__number_items += 1

    def delete_item_from_check(self, name):
        if name not in self.__name_items:
            raise NameError('Позиция отсутствует в чеке')
        else:
            self.__name_items.remove(name)
            self.__number_items -= 1

    def check_amount(self):
        total = []
        for i in self.__name_items:
            total.append(self.__item_price[i])
        if len(total) > 10:
            return sum(total) - (sum(total) * 0.1)
        else:
            return sum(total)
        
    def twenty_percent_tax_calculation(self):
        twenty_percent_tax = []   
        for i in self.__name_items:
            if self.__tax_rate[i] == 20:
                twenty_percent_tax.append(i)

        total = []
        for i in twenty_percent_tax:
            if self.__item_price[i]:
                total.append(self.__item_price[i])

        taxes = 0
        for i in total:
           taxes += i * 0.2

        if len(self.__name_items) > 10:
            return taxes - (taxes * 0.1)
        else:
            return taxes 

    def ten_percent_tax_calculation(self):
        ten_percent_tax = []
        for i in self.__name_items:
            if self.__tax_rate[i] == 10:
                ten_percent_tax.append(i)

        total = []
        for i in ten_percent_tax:
            if self.__item_price[i]:
                total.append(self.__item_price[i]) 

        taxes = 0
        for i in total:
           taxes += i * 0.1 

        if len(self.__name_items) > 10:
            return taxes - (taxes * 0.1)
        else:
            return taxes                        
  
    def total_tax(self):
        return self.twenty_percent_tax_calculation() + self.ten_percent_tax_calculation()

check = OnlineSalesRegisterCollector()
check.add_item_to_cheque('кефир')
check.add_item_to_cheque('кефир')
check.add_item_to_cheque('кола')
print(check.name_items)
print(check.check_amount())
print(check.ten_percent_tax_calculation())
print(check.total_tax())