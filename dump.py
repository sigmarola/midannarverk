from collections import *
import urllib.request, json
with urllib.request.urlopen("https://apis.is/petrol") as url:
    petrol = json.loads(url.read().decode())
#telja bensinstoðvar
comp=[]
g=''
#--Tók ekki eftir key í API skránni...--#
for i in petrol['results']:
    if i['company'] == g:
        None
    else:
        comp.append([i['company'],i['bensin95']])
    g=i['company']
#print(comp[7][0])
def finnaVerd(ll):
    out=[]
    for i in petrol['results']:
        if i['company'] == ll:
            out.append([i['company'],i['bensin95'],i['diesel']])
    return min(out)
gogn=[]
for i in range(len(comp)):
    gogn.append(finnaVerd(comp[i][0]))
#print(tst)
j= petrol['timestampPriceCheck']
j = j[:10]
j = str(j)
yr=''
day=''
mon=''
yr,mon,day = j.split('-')
j= '%s-%s-%s'%(yr,day,mon)

def oneComp(id,ll):
    cid=comp[id][0]
    out=[]
    b=0
    for i in petrol['results']:
        if i['company']==cid:
            out.append([i['name'],i['bensin95'],i['diesel'],i['key'],i['geo']])
            b+=1
    return out
"""lst=oneComp(2,comp)
a=0
for i in lst:
    print(lst[a][4]['lat'])
    print(lst[a][4]['lon'])
    a+=1"""
#print(oneComp(1,comp))
#for i in petrol['results']:
#    print(i['company'])
#print(oneComp(6,comp))

#print(j)



