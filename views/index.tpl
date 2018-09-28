%rebase('base.tpl')
<h1>{{title}}</h1>
<table>
<tr>
<th>Fyrirtæki</th>
<th>Bensín verð(ódýrast)</th>
<th>Díesel verð(ódýrast)</th>
</tr>
%for i in skra:
%a+=1
<tr>
    <td><a href="/page/{{a}}">{{i[0]}}</a></td>
    <td>{{i[1]}}</td>
    <td>{{i[2]}}</td>
</tr>
%end
</table>




