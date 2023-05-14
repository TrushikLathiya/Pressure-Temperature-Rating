from django.http import HttpResponse
from django.shortcuts import render
import pandas as pd
    
def read_data(Rating):
    data = pd.read_excel(Rating, index_col=0)
    return data

data_files = {
    'data150': 'E:\Django_Project\wscubtech\data\data150.xlsx',
    'data300': 'E:\Django_Project\wscubtech\data\data300.xlsx',
    'data600': 'E:\Django_Project\wscubtech\data\data600.xlsx',
    'data900': 'E:\Django_Project\wscubtech\data\data900.xlsx',
    'data1500': 'E:\Django_Project\wscubtech\data\data1500.xlsx',
    'data2500': 'E:\Django_Project\wscubtech\data\data2500.xlsx'
}

dataframes = {}
for i, value in data_files.items():
    dataframes[i] = read_data(value)

def index(request):
    if request.method == "POST":
        DT = str(request.POST.get('DT'))
        MOC = str(request.POST.get('MOC'))

        ratings = [150, 300, 600, 900, 1500, 2500]
        data = {'DT': DT, 'MOC': MOC}

        for r in ratings:
            data[f'r{r}'] = dataframes[f'data{r}'].loc[DT,MOC]
            if data[f'r{r}'] != '-':
                data[f'rpa{r}'] = round(data[f'r{r}']*6.895,2)
            else:
                data[f'rpa{r}'] = 'N/A'
        return render(request, "index.html", data)   
    else:
        return render(request, "index.html")