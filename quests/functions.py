import numpy as np
import matplotlib.pyplot as plt
RN = { }
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

def prodT_por_palhaEdireto(data):

   prodBd = data['ProdBd']
   prodBi = data['ProdBi']
   prod_total = []

   for i in range(data.__len__()):
      prod_total.append( (prodBd[i] + prodBi[i]) )
   
   MetdCult = data['MetdCult']

   prodT_metd_direto = {}
   prodT_metd_direto['prod_total'] = []
   prodT_metd_palha = {}
   prodT_metd_palha['prod_total'] = []

   for i in range(data.__len__()):
      if MetdCult[i] == 'DIRETO':
         prodT_metd_direto['prod_total'].append(prod_total[i])
      elif MetdCult[i] == 'PALHA': 
         prodT_metd_palha['prod_total'].append(prod_total[i])
   return prodT_metd_direto, prodT_metd_palha

def prod_por_palhaEdireto(prod, data):
    
   MetdCult = data['MetdCult']

   prod_metd_direto = {}
   prod_metd_direto['prod'] = []
   prod_metd_palha = {}
   prod_metd_palha['prod'] = []

   for i in range(data.__len__()):
      if MetdCult[i] == 'DIRETO':
         prod_metd_direto['prod'].append(prod[i])

      elif MetdCult[i] == 'PALHA': 
         prod_metd_palha['prod'].append(prod[i])

   return prod_metd_direto, prod_metd_palha

def prodT_por_espacamen(data):

   prodBd = data['ProdBd']
   prodBi = data['ProdBi']
   prod_total = []

   for i in range(data.__len__()):
      prod_total.append( (prodBd[i] + prodBi[i]) )
   
   Espacamen = data['Espacamen']

   prodT_esp05 = {}
   prodT_esp05['prod'] = []
   prodT_esp10 = {}
   prodT_esp10['prod'] = []
   prodT_esp15 = {}
   prodT_esp15['prod'] = []

   for i in range(data.__len__()):
      if Espacamen[i] == 0.5:
         prodT_esp05['prod'].append(prod_total[i])

      elif Espacamen[i] == 1: 
         prodT_esp10['prod'].append(prod_total[i])

      elif Espacamen[i] == 1.5: 
         prodT_esp15['prod'].append(prod_total[i])

   return prodT_esp05, prodT_esp10, prodT_esp15
def prod_por_espacamen(data):

   prodBd = data['ProdBd']
   prodBi = data['ProdBi']
   # prod_total = []

   # for i in range(data.__len__()):
   #    prod_total.append( (prodBd[i] + prodBi[i]) )
   
   Espacamen = data['Espacamen']

   prodT_esp05 = {}
   prodT_esp05['prodBd'] = []
   prodT_esp05['prodBi'] = []

   prodT_esp10 = {}
   prodT_esp10['prodBd'] = []
   prodT_esp10['prodBi'] = []

   prodT_esp15 = {}
   prodT_esp15['prodBd'] = []
   prodT_esp15['prodBi'] = []

   for i in range(data.__len__()):
      if Espacamen[i] == 0.5:
         prodT_esp05['prodBd'].append(prodBd[i])
         prodT_esp05['prodBi'].append(prodBi[i])

      elif Espacamen[i] == 1: 
         prodT_esp10['prodBd'].append(prodBd[i])
         prodT_esp10['prodBi'].append(prodBi[i])

      elif Espacamen[i] == 1.5: 
         prodT_esp15['prodBd'].append(prodBd[i])
         prodT_esp15['prodBi'].append(prodBi[i])

   return prodT_esp05, prodT_esp10, prodT_esp15

def get_quartil_espacamen(prodT_esp05, prodT_esp10, prodT_esp15):

   prodT_esp05['prod'] = sorted(prodT_esp05['prod'])
   prodT_esp10['prod'] = sorted(prodT_esp10['prod'])
   prodT_esp15['prod'] = sorted(prodT_esp15['prod'])

    #quartil
   esp05q1 = np.percentile(prodT_esp05['prod'], 25)
   esp05q2 = np.percentile(prodT_esp05['prod'], 50)
   esp05q3 = np.percentile(prodT_esp05['prod'], 75)

   esp05 = [esp05q1,esp05q2,esp05q3]

   esp05q1 = np.percentile(prodT_esp10['prod'], 25)
   esp05q2 = np.percentile(prodT_esp10['prod'], 50)
   esp05q3 = np.percentile(prodT_esp10['prod'], 75)

   esp10 = [esp05q1,esp05q2,esp05q3]

   esp05q1 = np.percentile(prodT_esp15['prod'], 25)
   esp05q2 = np.percentile(prodT_esp15['prod'], 50)
   esp05q3 = np.percentile(prodT_esp15['prod'], 75)

   esp15 = [esp05q1,esp05q2,esp05q3]

   return esp05, esp10, esp15


def get_median_quartil_q7(prodT_metd_direto,prodT_metd_palha):
   #aplicar media
   prodT_metd_direto['prod_total'] = sorted(prodT_metd_direto['prod_total'])
   prodT_metd_palha['prod_total'] = sorted(prodT_metd_palha['prod_total'])

   media_prod_metd_Di = np.mean(prodT_metd_direto['prod_total'])
   media_prod_metd_Pa = np.mean(prodT_metd_palha['prod_total'])

   #quartil
   direto_q1 = np.percentile(prodT_metd_direto['prod_total'], 25)
   direto_q2 = np.percentile(prodT_metd_direto['prod_total'], 50)
   direto_q3 = np.percentile(prodT_metd_direto['prod_total'], 75)

   quartil_direto = [direto_q1,direto_q2,direto_q3]

   palha_q1 = np.percentile(prodT_metd_palha['prod_total'], 25)
   palha_q2 = np.percentile(prodT_metd_palha['prod_total'], 50)
   palha_q3 = np.percentile(prodT_metd_palha['prod_total'], 75)

   quartil_palha = [palha_q1,palha_q2,palha_q3]

   return media_prod_metd_Di, media_prod_metd_Pa, quartil_direto, quartil_palha

def get_median_quartil_q7_prd(metd_direto,metd_palha):
   #aplicar media
   metd_direto['prod'] = sorted(metd_direto['prod'])
   metd_palha['prod'] = sorted(metd_palha['prod'])

   media_prod_metd_Di = np.mean(metd_direto['prod'])
   media_prod_metd_Pa = np.mean(metd_palha['prod'])

   #quartil
   direto_q1 = np.percentile(metd_direto['prod'], 25)
   direto_q2 = np.percentile(metd_direto['prod'], 50)
   direto_q3 = np.percentile(metd_direto['prod'], 75)

   quartil_direto = [direto_q1,direto_q2,direto_q3]

   palha_q1 = np.percentile(metd_palha['prod'], 25)
   palha_q2 = np.percentile(metd_palha['prod'], 50)
   palha_q3 = np.percentile(metd_palha['prod'], 75)

   quartil_palha = [palha_q1,palha_q2,palha_q3]

   return media_prod_metd_Di, media_prod_metd_Pa, quartil_direto, quartil_palha

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

