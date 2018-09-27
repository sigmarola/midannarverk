import bottle
from bottle import run, debug, route, template, error, abort, static_file,redirect
from dump import *
import sys from argv
"""import urllib.request, json
with urllib.request.urlopen("https://apis.is/petrol") as url:
    petrol = json.loads(url.read().decode())

verd =[]
for i in petrol['results']:
    verd.append(i['bensin95'])
verd.sort()
print(verd)"""
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

