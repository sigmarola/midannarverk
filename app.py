
import bottle
from bottle import run, debug, route, template, error, abort, static_file,redirect
import sys from argv
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
gogn = gogn
@route('/')
def redir():
    redirect('/home')
@route('/home')
def index():
    return template('index.tpl', skra=gogn, title='Verðskrá', time=j,a=0)

@route('/page/<id:int>')
def pages(id):
    if id <= len(comp):
        staktComp=oneComp((id-1),comp)
        return template('pages.tpl', id=id-1,title=gogn[id-1][0],time=j,lst=staktComp,a=0)
    else:
        abort(404)
@error(404)
def villa(error):
    return template('villa.tpl',title='404')

@route('/static/<skra:path>')
def static_skra(skra):
    return static_file(skra, root='./public')

#run(debug=True, port='9000')
bottle.run(host='0.0.0.0', port=argv[1])

