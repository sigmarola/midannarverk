% include('header.tpl')
<h1>{{title}}</h1>
<a href="/home">Til baka</a>
<div class="row">

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

% include('footer.tpl')

    </div>
    <div class="nine columns fpos">
        <img src="https://maps.googleapis.com/maps/api/staticmap?center=Iceland&scale=2&zoom=6&size=500x400&maptype=roadmap
        %for i in lst:
            &markers=color:blue%7Clabel:S%7C{{lst[a][4]['lat']}},{{lst[a][4]['lon']}}&
            %a+=1
        %end
        &key=AIzaSyCZqxxgbzP9CKg6o5eSG3UjfxbbjXBUpp0"/>
    </div>
</div>
