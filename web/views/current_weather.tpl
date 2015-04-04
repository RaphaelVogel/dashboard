<!DOCTYPE html>
<html lang="de">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" href="/lib/bootstrap.min.css">
    <style type="text/css">
    </style>
    <title>Aktuelles Wetter in Meckesheim</title>
  </head>
  <body class="container">
    <div class="panel panel-primary">
      <div class="panel-heading"><h3>Wetter in Meckesheim -- Station Schatthäuser Str. 14</h3></div>
      <div class="panel-body bg-info"">
        <h1 class="text-primary">Temperatur&nbsp;&nbsp;&nbsp;&nbsp;
            {{weather['temperature']}} {{weather['temperature_unit']}}</h1>
        <h1 class="text-primary">Luftfeuchte&nbsp;&nbsp;&nbsp;&nbsp;
            {{weather['humidity']}} {{weather['humidity_unit']}}</h1>
        <h1 class="text-primary">Luftdruck&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
            {{weather['pressure']}} {{weather['pressure_unit']}}</h1>
      </div>
    </div>
  </body>
</html>