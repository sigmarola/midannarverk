% rebase('base.tpl')
<h1>{{title}}</h1>
<a href="/home">Til baka</a>
<div>
    <div class="three columns" >
    <table>
    <th>Staðsetning</th>
    <th>Verð f. bensín</th>
    <th>Verð f. diesel</th>
    %for i in lst:
    <tr>
        <td>{{i[0]}}</td>
        <td>{{i[1]}}</td>
        <td>{{i[2]}}</td>
    </tr>
    %end
    </table>
    <a href="/home">Til baka</a>



</div>
<div class="nine columns fpos">
<img src="https://maps.googleapis.com/maps/api/staticmap?center=Iceland&scale=2&zoom=6&size=500x350&maptype=roadmap
%for i in lst:
    &markers=size:tiny%7Ccolor:0x5ca4fa%7C{{lst[a][3]['lat']}},{{lst[a][3]['lon']}}&
    %a+=1
%end
&key=AIzaSyCZqxxgbzP9CKg6o5eSG3UjfxbbjXBUpp0"/>
</div>

</div>
