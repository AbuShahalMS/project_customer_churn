import pandas as pd
import numpy as np
import matplotlib.pylab as plt


data = pd.read_csv("/home/cybacor/Desktop/shahal/projects/project_customer_churn/customer_churn.csv")

def customer_churn():
    print(data)


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

    # bar chart comparing average subscription lengths of churned vs. non-churned customers
    data7 = data.groupby("Churn")["Subscription Length (months)"].mean()
    xpoint = data7.index
    ypoint = data7.values
    plt.bar(xpoint,ypoint)
    plt.xlabel("churned vs unchurned customers")
    plt.ylabel("average subscription")
    plt.title("bar chart")
    plt.plot()
    plt.show()

    ## pie chart to show the distribution of churned customers across different regions
    plt.pie(data4,labels = data4.index,autopct='%1.2f%%')
    plt.show()

    # histogram distribution of total charges among customers
    data8 = data.groupby("Customer ID")["Total Charges (INR)"].sum()
    plt.hist(data8,bins=30, density=True, color='blue', edgecolor='black', alpha=0.7)
    plt.title("distribution of total charges among customers")
    plt.show()

    # Visualize the relationship between monthly charges and total charge
    plt.scatter(data["Monthly Charges (INR)"],data["Total Charges (INR)"],alpha=0.5, color='blue')
    plt.title('Scatter Plot: Monthly Charges vs Total Charges')
    plt.xlabel('Monthly Charges (INR)')
    plt.ylabel('Total Charges (INR)')
    plt.show()

0





customer_churn()
