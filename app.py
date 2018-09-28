
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
        comp.append([i['company'],i['bensin95']])
    g=i['company']

def finnaVerd(ll):
    out=[]
    for i in petrol['results']:
        if i['company'] == ll:
            out.append([i['company'],i['bensin95'],i['diesel']])
    return min(out)

gogn=[]
for i in range(len(comp)):
    gogn.append(finnaVerd(comp[i][0]))

yr,mon,day = petrol['timestampPriceCheck'][:10].split('-')
j= 'Síðast uppfært: %s-%s-%s'%(yr,day,mon)

def oneComp(id,ll):
    out=[]
    for i in petrol['results']:
        if i['company']==comp[id][0]:
            out.append([i['name'],i['bensin95'],i['diesel'],i['geo']])
    return out
#

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
    return template('villa.tpl',title='404',time=None)

@route('/static/<skra:path>')
def static_skra(skra):
    return static_file(skra, root='./public')

#run(debug=True, port='9000')
bottle.run(host='0.0.0.0', port=argv[1])

