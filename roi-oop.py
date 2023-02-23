class RoiCalc():
    def __init__(self, income, expenses, cashflow, investment, roi):
        self.income = income
        self.expenses = expenses
        self.cashflow = cashflow
        self.investment = investment
        self.roi = roi

        print("The ROI for your investment property is " +
              str(roi) + "%" + " annually")


income = int(input(
    "What is the monthly rent? If unit is vacant what is the average rent in the area? "))*12
expenses = int(
    input("What are your yearly expenses to maintain the rental property? "))
investment = int(
    input("How much capital was used to secure this investment? "))
cashflow = income - expenses
roi = (cashflow/investment)*100

RoiCalc(income, expenses, cashflow, investment, roi)