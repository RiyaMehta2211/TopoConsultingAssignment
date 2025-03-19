import pandas as pd

class DataProcessor:
    def _init_(self, datasets):
        self.datasets = datasets
    def merge_data(self):
        #concatenating and saving the final data
        final_data = pd.concat(self.datasets["csv"], self.datasets["json"], 
                               pd.DataFrame(self.datasets["pptx"]), self.datasets['pdf'],
                               axis = 1
        )
        final_data.to_csv('unified_data.csv')
        return final_data