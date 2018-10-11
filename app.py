
import bottle
from bottle import run, debug, route, template, error, abort, static_file,redirect
import urllib.request, json
from collections import *
from sys import argv

#

with urllib.request.urlopen("https://apis.is/petrol") as url:
    petrol = json.loads(url.read().decode())

comp=[]
g=''
#--Tók ekki eftir key í API skránni...--#
for i in petrol['results']:
    if i['company'] == g:
        None
    else:
        comp.append([i['company'],round(i['bensin95']),round(i['diesel'])])
    g=i['company']

def finnaVerd(ll):
    out=[]
    for i in petrol['results']:
        if i['company'] == ll:
            out.append([i['company'],round(i['bensin95']),round(i['diesel'])])
    return min(out)

gogn=[]
for i in range(len(comp)):
    gogn.append(finnaVerd(comp[i][0]))

m=['Janúar','Febrúar','Mars','Apríl','Maí','Júní','Júlí','Ágúst','September','Október','Nóvember','Desember']
yr,mon,day = petrol['timestampPriceCheck'][:10].split('-')
mon=int(mon)
day=int(day)
j= 'Síðast uppfært: %s. %s, %s'%(day,m[mon-1],yr)

def oneComp(id):
    out=[]
    for i in petrol['results']:
        if i['company']==comp[id][0]:
            out.append([i['name'],round(i['bensin95']),round(i['diesel']),i['geo']])
    return out
mm=min(comp, key=lambda x: x[1])
def lattverd(slot):
    out=[]
    for i in comp:
        if i == mm:
            out=i[slot]
    return out

#

@route('/')
def redir():
    redirect('/home')
@route('/home')
def index():
    lstvrd1 = lattverd(1)
    lstvrd2 = lattverd(2)
    return template('index.tpl', skra=gogn, title='Verðskrá', time=j, a=1,lv1=lstvrd1,lv2=lstvrd2)

@route('/page/<id:int>')
def pages(id):
    t=0

    for i in oneComp(id-1):
        t+=1
    if id <= len(comp):
        staktComp=oneComp((id-1))
        return template('pages.tpl', id=id-1,title=gogn[id-1][0],time=j,lst=staktComp,a=0,t=t)
    else:
        abort(404)
@error(404)
def villa(error):
    return template('villa.tpl',title='404',time=None)

@route('/static/<skra:path>')
def static_skra(skra):
    return static_file(skra, root='./public')

#run(debug=True, port='9000')
bottle.run(host='0.0.0.0', port=argv[1])

