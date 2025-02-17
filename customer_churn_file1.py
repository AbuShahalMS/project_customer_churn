import pandas as pd

data = pd.read_csv("project_customer_churn/customer_churn.csv")

def customer_churn():
    # print(data)


    # missing values and handle them appropriately
    data1 = data.isnull().sum()
    print("missing values and handle ",data1)


    # Total Charges column to a numerical format
    data["Total Charges (INR)"] = pd.to_numeric(data["Total Charges (INR)"])
    print(data.head())

    # average subscription length of churned vs. non-churned customers
    data3 = data.groupby("Churn")["Subscription Length (months)"].mean()
    print(data3)

    # region has the highest churn rate
    data4 = (data[data["Churn"] == "Yes"].groupby("Region").size())
   # sort = data4.nlargest(1)
    print(data4)

    # average monthly charges for churned and non-churned customers
    data5 = data.groupby("Churn")["Monthly Charges (INR)"].mean().sort_values(ascending=False)
    print(data5)

    ## payment method is most common among churned customers
    data6 = (data[data["Churn"] == "Yes"].groupby("Payment Method").size())
    largest = data6.nlargest(1)
    print(largest)








customer_churn()
