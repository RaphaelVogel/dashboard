<!DOCTYPE html>
<html lang="de">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" href="/lib/bootstrap.min.css">
    <style type="text/css">
    body { font-size: 16px !important; }
</style>
    <title>Tabelle der {{liga}}. Bundesliga</title>
  </head>
  <body class="container" style="font-size:1.2em">
    <div class="col-lg-12">
      <table class="table table-striped">
        <thead>
          <tr>
            <th>PLATZ</th>
            <th>MANSCHAFT</th>
            <th>SPIELE</th>
            <th>G</th>
            <th>U</th>
            <th>V</th>
            <th>TORE</th>
            <th>DIFF.</th>
            <th>PKT.</th>
          </tr>
        </thead>
        <tbody>
        % for club in table:
          <tr>
            <td>{{club['rank']}}</td>
            <td><img src="{{club['image']}}" height="25" width="25"> {{club['name']}}</td>
            <td>{{club['games']}}</td>
            <td>{{club['won']}}</td>
            <td>{{club['equal']}}</td>
            <td>{{club['loose']}}</td>
            <td>{{club['goals']}}</td>
            <td>{{club['goal_diff']}}</td>
            <td>{{club['points']}}</td>
          </tr>
        % end
        </tbody>
      </table>
    </div>
  </body>
</html>