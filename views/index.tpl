%rebase('base.tpl')
<h1>{{title}}</h1>
<table>
<tr>
<th>Fyrirtæki</th>
<th>Bensín verð(ódýrast)</th>
<th>Díesel verð(ódýrast)</th>

</tr>
<tr>
%for i in skra:

    <td><a href="/page/{{a}}">{{i[0]}}</a></td>
    %if i[1]==lv1:
         <td class="latt">{{i[1]}} kr.</td>
    %else:
         <td>{{i[1]}} kr.</td>
    %end
    %if i[2] == lv2:
         <td class="latt">{{i[2]}} kr.</td>
    %else:
         <td>{{i[2]}} kr.</td>
    %end
    </tr>
%a+=1
%end
</table>

