import glob
import pandas as pd
import os
import datetime
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib import style
import matplotlib
import csv

style.use('ggplot')

#matplotlib.use('agg')

nov_files= glob.glob( os.getcwd()+ "/nov*.csv")
dec_files=glob.glob(os.getcwd()+"/dec*.csv")
jan_infi=glob.glob(os.getcwd()+"/*nse_equity_stats.csv")
fils=glob.glob(os.getcwd()+"/*.csv")
gainers=glob.glob(os.getcwd()+"/*gainers.csv")
losers=glob.glob(os.getcwd()+"/*losers.csv")


list_ = []
list2=[]
list3=[]
list4=[]
list5=[]
comps=[]


def first():

    for file_ in jan_infi:
        df = pd.read_csv(file_,index_col=0, header=None)
        #df['date'] = file_[26:36]
        list_.append(df)




    frame = pd.concat(list_, axis = 0, ignore_index = False,sort=False)


    #data4 = data4.rename(columns={0: 'Company', 1: 'volume',2: 'high',3: 'low',4: 'last_traded',5: 'change'},inplace=True)
    comps=frame.axes[0].tolist()
    comps2 = { i : comps[i] for i in range(0, len(comps) ) }
    return comps2
    #for i in range(0,65):
    #    print comps[i]


def second():

    for file_ in dec_files:
        df = pd.read_csv(file_,index_col=0, header=None)
        df['date'] = file_[26:36]
        list2.append(df)




    frame = pd.concat(list2, axis = 0, ignore_index = False,sort=False)
    frame=frame.rename(columns={0: 'Company', 1: 'volume',2: 'high',3: 'low',4: 'last_traded',5: 'previous_price',6: 'change'})
    data2= frame.iloc[10,-1]

    data=frame.loc["Standard Group  Ltd Ord 5.00"]
    data2=frame.loc["TPS Eastern Africa (Serena) Ltd Ord 1.00"]
    data3=frame.loc["Scangroup  Ltd Ord 1.00"]
    data4=frame.loc["Kenya Airways Ltd Ord 5.00"]


    #data4 = data4.rename(columns={0: 'Company', 1: 'volume',2: 'high',3: 'low',4: 'last_traded',5: 'change'},inplace=True)
    print data3





def third(n):

        for file_ in jan_infi:
            df = pd.read_csv(file_,index_col=1, header=None, decimal=',')
            df['date'] = file_[27:37]

            list3.append(df)





        frame = pd.concat(list3, axis = 0, ignore_index = False,sort=False)
        frame=frame.rename(columns={1: 'company',2: 'volume',3: 'high',4: 'low',5: 'last_traded',6:'previous_price',7:'change',8:'date'})
        comps=frame.axes[0].tolist()
        comps2 = { i : comps[i] for i in range(0, len(comps) ) }





        #data5=data4.loc[data4['high'].isin(['36','40'])]
        #data6=data4.loc[data4['low'].isin(range(33,36))]
        #data4['50ma'] = data4['high'].rolling(window=50,min_periods=0).mean()
        #print data4.head()
        #data4.high=pd.to_numeric(data4.high)
        #data4.previous_price=pd.to_numeric(data4.previous_price)
        #data4.set_index('date',inplace=True)
        #mask2 = (data4['date'] > '2019-05-06') & (data4['date'] <= '2019-05-16')
        #print(data4.loc[mask2])

        #frame['date'] = frame['date'].astype('datetime64[ns]')
        #data=frame.loc["Scangroup  Ltd Ord 1.0"]
        #mask2 = (data['date'] > '2019-05-17') & (data['date'] <= '2019-06-04')
        #data2=data.loc[mask2]


        frame['volume'] = frame['volume'].replace(',', '', regex=True)
        frame['volume']=pd.to_numeric(frame['volume'], errors='coerce')
        frame['high']=pd.to_numeric(frame['high'],errors='coerce')
        frame['low']=pd.to_numeric(frame['low'],errors='coerce')
        frame['last_traded']=pd.to_numeric(frame['last_traded'],errors='coerce')
        frame['date'] = frame['date'].astype('datetime64[ns]')
        frame['change']=pd.to_numeric(frame['change'],errors='coerce')
        #print frame

        data=frame.loc[comps[n]]
        da_1=frame.loc['Equity Group Holdings Ord 0.50'] #10
        da_2=frame.loc['Centum Investment Co Ltd Ord 0.50']
        da_3=frame.loc['Standard Group  Ltd Ord 5.00']
        da_4=frame.loc['NIC Group PLC']
        da_5=frame.loc['KCB Group Ltd Ord 1.00'] #13
        da_6=frame.loc['East African Breweries Ltd Ord 2.00']
        da_7=frame.loc['Jubilee Holdings Ltd Ord 5.00']
        da_8=frame.loc['Williamson Tea Kenya Ltd Ord 5.00'] #5





        timestamp=max(frame['date'])
        timestamp=str(timestamp)
        date_max,time_max=timestamp.split()
        price_mask=(frame['last_traded'] >200.00) & (frame['last_traded'] <=500.00)
        print da_8.loc[(da_8['volume'] > 200) & (da_8['date'] <= date_max)]
        print frame.loc[price_mask]


        mask2 = (data['date'] > '2019-11-01') & (data['date'] <= date_max)
        mask3 = (da_1['date'] > '2019-11-01') & (da_1['date'] <= date_max)
        mask4 = (da_2['date'] > '2019-11-01') & (da_2['date'] <= date_max)
        mask5 = (da_3['date'] > '2019-11-01') & (da_3['date'] <= date_max)
        mask6 = (da_4['date'] > '2019-11-01') & (da_4['date'] <= date_max)
        mask7 = (da_5['date'] > '2019-11-01') & (da_5['date'] <= date_max)
        mask8 = (da_6['date'] > '2019-11-01') & (da_6['date'] <= date_max)



    #    price_mask1 = (da_1['last_traded'] ) & (da_1['date'] == date_max)
    #    price_mask2= (da_2['last_traded'] ) & (da_2['date'] == date_max)
    #    price_mask3= (da_3['last_traded'] ) & (da_3['date'] == date_max)
    #    price_mask4= (da_4['last_traded'] ) & (da_4['date'] == date_max)
    #    price_mask5= (da_5['last_traded'] ) & (da_5['date'] == date_max)
    #    price_mask6= (da_6['last_traded'] ) & (da_6['date'] == date_max)

        #p_1=da_1.loc[price_mask1]
        #p_2=da_2.loc[price_mask2]
        #p_3=da_3.loc[price_mask3]
        #p_4=da_4.loc[price_mask4]
        #p_5=da_5.loc[price_mask5]
        #p_6=da_6.loc[price_mask6]

        #print p_1,p_2,p_3

        data2=data.loc[mask2]
        #print data2

        da_1=da_1.loc[mask3]
        da_2=da_2.loc[mask4]
        da_3=da_3.loc[mask5]
        da_4=da_4.loc[mask6]
        da_5=da_5.loc[mask7]
        da_6=da_6.loc[mask8]


        data2.plot(x='date',y='last_traded')
        plt.title(comps[n]+":company_no:"+str(n))
        plt.show(block=False)


def fourth():
    df = pd.read_csv('jan.csv',index_col=0, header=None)
    #df=df.rename(columns={1: 'volume',2: 'high',3: 'low',4: 'last_traded',5: 'previous_price',6: 'change'})

    mask = (df[3] > '5.00') & (df[3] <= '30.00')
    mask2 = (df[6] > '2019-04-06') & (df[6] <= '2019-04-10') # search any range date for a company maybe used in another function
    mask3 = (df[2] > 10.00) & (df[2] <= 50.00)
    #print df[2].loc[mask3]
    #print(df.loc[df[2].isin(['33.0','50.0'])]) #search any high price for any company ,more needs to be create for to find any change for any company,any feature for any company
    return df



def date_frame(fr,company,start_date,end_date):
        data=fr.loc[company]
        #mask1 = (data['date'] > start_date) & (data['date'] <= end_date)
        #mask2 = (data['date']==end_date)
        #high=(df.loc[df['high'].isin(['33.0','50.0'])])
        #data2=data.loc[mask1]
        #print float(data2['high'].get_value(0)) * 100.0
        print data







def gainer():
    for file_ in gainers:
        df = pd.read_csv(file_,index_col=0, header=None)
        df['date'] = file_[26:36]
        list4.append(df)




    frame = pd.concat(list4, axis = 0, ignore_index = False,sort=False)
    mask = (frame['date'] > '2019-05-06') & (frame['date'] <= '2019-05-10')
    mask2 = (frame[2] > 30.00)
    print(frame.loc[mask2])




def loser():
    for file_ in losers:
        df=pd.read_csv(file_,index_col=0,header=None)
        df['date'] = file_[26:36]
        list5.append(df)

    frame=pd.concat(list5,axis=0,ignore_index=False,sort=False)
    mask = (frame['date'] > '2019-05-06') & (frame['date'] <= '2019-05-16')
    frame2=frame.loc([mask])
    print frame2[frame2['1']]





#df2=third()
n=0


#second()
while not(n=='stop'):
    #print dt


    third(n)
    n=n + 1

#fourth()
#gainer()
#loser()
