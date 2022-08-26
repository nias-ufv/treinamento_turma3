from sys import displayhook
import pandas as pd

cvd = pd.read_csv(r"C:\Users\pedro\OneDrive\Área de Trabalho\psNIAS\archive\covid_19_clean_complete.csv")
##displayhook(cvd)

##1
#Print da forma da tabela e nome das colunas
print(cvd.shape)
print(cvd.columns)

#Troca o tipo  da coluna Date para datetime64
cvd["Date"] = cvd["Date"].astype("datetime64")
cvd.info()
displayhook(cvd.describe())
#Localiza as colunas com NaN
displayhook(cvd.loc[:, cvd.isna().any()])

##2
#Localiza os dados onde o país é China
china = cvd.loc[cvd["Country/Region"]=="China"]
#Separa apenas os dados desejados de onde o país é China
china_count = china.loc[:,['Province/State','Confirmed', 'Deaths', 'Recovered', 'Active']]
#Remove duplicatas
fchina_count = china_count.drop_duplicates(subset='Confirmed', keep='first')
#Gera um ranking das provincias com mais casos confirmados
fgchina_count = fchina_count.groupby('Province/State', sort=False).max().sort_values('Confirmed', ascending=False)
#Limita esse ranking a 5 índices
displayhook(fgchina_count.head(5))

##3
#Remove a '/' entre os nomes das colunas
cvd.columns=cvd.columns.str.replace("/","")
ntable = cvd
#Função que concatena as colunas caso haja necessidade
def fct(x):
    if pd.isnull(x.ProvinceState) == False:
        x.CountryRegion = x.CountryRegion + "/" + x.ProvinceState
    return(x)
#Aplicação da função no DataFrame
conc=ntable.apply(fct, axis=1)
#Retirada da coluna não mais necessaria
conc= conc.drop('ProvinceState', axis=1)
displayhook(conc)


##4
#Import do DataFrame
wrld = pd.read_csv(r"C:\Users\pedro\OneDrive\Área de Trabalho\psNIAS\archive\worldometer_data.csv")
#Retira a '/' do nome das colunas
wrld.columns=wrld.columns.str.replace("/","")
#Separa apenas os  dados desejados do DataFrame
wrlddt = wrld[['CountryRegion', 'Continent', 'Population','TotalDeaths']]
displayhook(wrlddt)

#Agrupa o DataFrame em por continente
k = wrlddt.groupby("Continent").sum("TotalDeaths")
#Define novo valor para a coluna 'Deaths/1MPop
k["Deaths/1MPop"] = ((k.TotalDeaths/k.Population) * 10**6)
k = k.sort_values(by='Deaths/1MPop',ascending = False)
displayhook(k)