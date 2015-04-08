<!DOCTYPE html>
<html lang="de">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" href="/lib/bootstrap.min.css">
    <style type="text/css">
      body { font-size: 15px !important; }
    </style>
    <title>Aktuelle Spiele der {{liga}}. Bundesliga</title>
  </head>
  <body class="container">
    <div class="col-lg-10">
      <table class="table table-striped">
        <thead>
          <tr>
            <th>DATUM</th>
            <th>HEIM</th>
            <th></th>
            <th></th>
            <th></th>
            <th>AUSWÄRTS</th>
          </tr>
        </thead>
        <tbody>
        % for match in matches:
          <tr>
            <td>{{match['date']}}</td>
            <td>{{match['home_team']}}</td>
            <td><img src="{{match['home_image']}}" height="25" width="25"></td>
            <td>{{match['result']}}</td>
            <td><img src="{{match['guest_image']}}" height="25" width="25"></td>
            <td>{{match['guest_team']}}</td>
          </tr>
        % end
        </tbody>
      </table>
    </div>
  </body>
</html>