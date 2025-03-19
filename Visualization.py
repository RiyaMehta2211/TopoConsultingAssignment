import pandas as pd
import re
import plotly.express as px
class Visualization:
    #3 visualisations, hence I will use pie chart, bar graph and tabular data to convey the data representation
    def __init__(self, data):
        self.data = data
    def create_pie_chart(self):
        target_cell = None
        for col in self.data.columns:
            for value in self.data[col].dropna():
                if "Revenue Breakdown by Activity" in str(value):
                    target_cell = value
                    break
            if target_cell:
                break
        #to extract the relevant percentages using regex
        pattern = r"(\w+\s?\w*):\s?(\d+)%"
        matches = re.findall(pattern, target_cell)

        revenue_distribution_data = pd.DataFrame(matches, columns=["Activity", "Percentage"])
        revenue_distribution_data["Percentage"] = revenue_distribution_data["Percentage"].astype(int)

        pie_fig = px.pie(
            revenue_distribution_data,
            names="Activity",
            values="Percentage",
            title="Revenue Breakdown by Activity for FitPro"
        )
        return pie_fig.to_html()
    def create_bar_chart(self):
        #to remove duplicates in the dataset when plotting the bar graph
        unique_companies = self.data.drop_duplicates(subset=["company_name"], keep="first")
        bar_fig = px.bar(
            self.data,
            x=unique_companies["company_name"],
            y=unique_companies["company_revenue"],
            title="Revenue Comparison by Company",
            labels={"company_revenue": "Revenue", "company_name": "Company"}
        )
        bar_fig.update_layout(
            xaxis_title="Company Name",
            yaxis_title="Total Revenue"
        )
        return bar_fig.to_html()
    
    def create_table(self):
        return self.data.head(10).to_dict(orient="records")

    def merge_data(self):
        #concatenating and saving the final data
        final_data = pd.concat(self.datasets["csv"], self.datasets["json"], 
                               pd.DataFrame(self.datasets["pptx"]), self.datasets['pdf'],
                               axis = 1
        )
        final_data.to_csv('unified_data.csv')
        return final_data