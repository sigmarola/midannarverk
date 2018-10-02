%rebase('base.tpl')
<h1>{{title}}</h1>
<p>{{lv}} er með ódýrasta eldsneytið</p>
<table>
<tr>
<th>Fyrirtæki</th>
<th>Bensín verð(ódýrast)</th>
<th>Díesel verð(ódýrast)</th>
</tr>
%for i in skra:
%a+=1
   %if i[0] == lv:
        <tr class="latt la">
            <td><a class ="la" href="/page/{{a}}">{{i[0]}}</a></td>
            <td>{{i[1]}}</td>
            <td>{{i[2]}}</td>
        </tr>
   %else:
        <tr>
            <td><a href="/page/{{a}}">{{i[0]}}</a></td>
            <td>{{i[1]}}</td>
            <td>{{i[2]}}</td>
        </tr>
   %end
%end
</table>




