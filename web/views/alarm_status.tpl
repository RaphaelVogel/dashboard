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
    <title>Alarm Log</title>
  </head>
  <body class="container">
    <div class="col-md-8">
      <table class="table table-striped">
        <thead>
          <tr>
            <th>Nachricht</th>
          </tr>
        </thead>
        <tbody>
        % for log in alarmlogs:
          <tr>
            <td>{{log}}</td>
          </tr>
        % end
        </tbody>
      </table>
    </div>
    <div class="col-md-4">
        <h3>Alarmanlage {{alarmstatus}}</h3>
    </div>
  </body>
</html>