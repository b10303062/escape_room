import pandas as pd
from itertools import islice

file_csv = open('items_scv', encoding='utf-8-sig', mode='r')
index_list = file_csv.readline().strip().split(',')
label_list = []
dict = {}
for line in islice(f, 1, None):
    inp = [t for t in line.strip().split(',')]
    dict[inp[0]] = inp[1:]
    label_list += [inp[0]]
df = pd.DataFrame.from_dict(dict, orient='index')
df.index = label_list
df.columns = index_list[1:]

class Map:
    
    def __init__(self, df):
        self.df = df
        # 屬於Map的物品資料dataframe
        
        
    def get_item_attribite(self, label, is_second):
        self.label = label
        self.is_second = is_second
        
        print(self.df.at[self.label, 'name'])
        if self.is_second:
            print(self.df.at[self.label, 'discription_trigger_no_key_or_puzzle'])
        else:
            print(self.df.at[self.label, 'description_normal'])
            
