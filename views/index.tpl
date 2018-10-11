%rebase('base.tpl')
<h1>{{title}}</h1>
<p>{{lv1[0][1]}} er með ódýrasta bensínið</p>
<p>{{lv2[0][1]}} er með ódýrasta díeselið</p>
<table>
<tr>
<th>Fyrirtæki</th>
<th>Bensín verð(ódýrast)</th>
<th>Díesel verð(ódýrast)</th>

</tr>
%for i in skra:
    <tr>
    <td><a href="/page/{{a}}">{{i[0]}}</a></td>
    %if i[1]==lv1[0][0]:
         <td class="latt">{{i[1]}}</td>
    %else:
         <td>{{i[1]}}</td>
    %end
    %if i[2] == lv2[0][0]:
         <td class="latt">{{i[2]}}</td>
    %else:
         <td>{{i[2]}}</td>
    %end
%a+=1
%end
</tr>
%a+=1
%end
</table>


