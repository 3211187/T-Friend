import pandas as pd

class FILTER_RF(object):
    def __init__(self,T, excel_PATH, filter_name):
        self.T = T
        self.excel_PATH = excel_PATH
        self.filter_name = filter_name + '.xlsx'

    def main_f_rf(self):

        e_name = self.filter_name
        if self.T == '계산서':
            raw_DATA = 'e_bill_2019_uniq.xlsx'
            #e_name = '계산서_filter_rf.xlsx'
        elif self.T == '영수증':
            raw_DATA = 'cash_train.xlsx'
            # e_name = '영수증_filter_rf.xlsx'
        elif self.T == '기타':
            raw_DATA = 'etc.xlsx'
            #e_name = '영수증_filter_rf.xlsx'

        df = pd.read_excel(self.excel_PATH + raw_DATA, encoding='utf-8', sheet_name='Sheet1', index_col=0)

        list = []
        count = 0
        print('Selecting less than 80% accuracy...(RF)')
        for i in range(len(df)):
            if float(df.loc[i,['예측정도']].item())<0.8:
                df.loc[i, ['CD_ACCOUNT_R']] = df.loc[i, ['CD_ACCOUNT']].item()
                df.loc[i, ['CD_ACCOUNT']] = 250
                list.append(i)
                count +=1
        print('count : ',count)

        df_1 = df.iloc[list,:]

        df_1.to_excel('C:\\Users\\ialab\\Desktop\\T-Friend\\filter_rf\\' + e_name)

        del df['cc']
        del df['predict']
        del df['예측정도']
        df.to_excel(self.excel_PATH + raw_DATA)




