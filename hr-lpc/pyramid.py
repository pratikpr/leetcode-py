class Employee:
    def __init__(self, name, boss, bonus):
        self.name = name
        self.boss = boss
        self.bonus = bonus/100

def count(nEmployess, hier, nSales, sales):
    jude = Employee("Jude", None, 100)
    emps_meta = {"Jude": ("Jude", None, 100)}
    sales_dict = {}

    for emp in nEmployess:
        emps_meta[emp[0]] = (emp[0], emp[1], int(emp[2]))
        sales[emp[0]] = 0

    for sale in sales:
        empl = sales[0]
        boss = sales[1]
        total = int(sales[2])

        empl_sale = sales_dict[empl]
        e = emps_meta[empl]
        b = emps_meta[boss]
        es = total
        bs = total
        while boss:
            es = es * e[2]/100
            bs = bs * (100-e[2]/100)
            es = 