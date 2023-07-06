import numpy as np
import matplotlib.pyplot as plt
RN = {}
PB = {}
CE = {}

RN['temp'] = []
PB['temp'] = []
CE['temp'] = []

RN['umidade'] = []
PB['umidade'] = []
CE['umidade'] = []

RN['prec'] = []
PB['prec'] = []
CE['prec'] = []

def var_por_estados(data):
   RN['PBd'] = []
   PB['PBd'] = []
   CE['PBd'] = []

   RN['PBi'] = []
   PB['PBi'] = []
   CE['PBi'] = []
   ProdBd = data['ProdBd']
   ProdBi = data['ProdBi'] 
   uf  = data['UF']
   temp = data['temp']
   umidade = data['umidade']
   prec = data['prec']

   for i in range(data.__len__()):
      if uf[i] == 'RN':
         RN['PBd'].append(ProdBd[i])
         RN['PBi'].append(ProdBi[i])
         RN['temp'].append(temp[i])
         RN['umidade'].append(umidade[i])
         RN['prec'].append(prec[i])
         
      elif uf[i] == 'PB':
         PB['PBd'].append(ProdBd[i])
         PB['PBi'].append(ProdBi[i])
         PB['temp'].append(temp[i])
         PB['umidade'].append(umidade[i])
         PB['prec'].append(prec[i])

      elif uf[i] == 'CE':
         CE['PBd'].append(ProdBd[i])
         CE['PBi'].append(ProdBi[i])
         CE['temp'].append(temp[i])
         CE['umidade'].append(umidade[i])
         CE['prec'].append(prec[i])
   return RN, PB, CE


def producao_total_estados(RN,PB,CE):
   prod_rnT =   np.sum(RN['PBd']) + np.sum(RN['PBi'])
   prod_pbT =   np.sum(PB['PBd']) + np.sum(PB['PBi'])
   prod_ceT =   np.sum(CE['PBd']) + np.sum(CE['PBi'])

   return prod_rnT, prod_pbT, prod_ceT

def media_producao_total(RN,PB,CE):

   mean_rnT =   np.mean(RN['PBd']) + np.mean(RN['PBi'])
   mean_pbT =   np.mean(PB['PBd']) + np.mean(PB['PBi'])
   mean_ceT =   np.mean(CE['PBd']) + np.mean(CE['PBi'])
   
   return mean_rnT,mean_pbT,mean_ceT

def plot_prod_total( prod_rnT, prod_pbT, prod_ceT):

    fig, ax = plt.subplots(figsize=(4,4))

    estados = ['RN', 'PB', 'CE']
    counts = [prod_rnT, prod_pbT, prod_ceT]
    bar_labels = ['RN', 'PB', 'CE']
    bar_colors = ['tab:gray', 'tab:blue', 'tab:red',]

    ax.bar(estados, counts, label=bar_labels, color=bar_colors,width=[0.5])

    ax.set_ylabel('produção total')
    ax.set_title('produção total')
    ax.legend(title='Estados')
    # ax.xaxis.offsetText.set_fontsize('x-small')

    plt.show()
