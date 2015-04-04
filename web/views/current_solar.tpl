<!DOCTYPE html>
<html lang="de">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" href="/lib/bootstrap.min.css">
    <style type="text/css">
      .vertical-center {
        min-height: 100%;
        min-height: 100vh;
        display: -webkit-box;
        display: -moz-box;
        display: -ms-flexbox;
        display: -webkit-flex;
        display: flex;
        -webkit-box-align : center;
        -webkit-align-items : center;
        -moz-box-align : center;
        -ms-flex-align : center;
        align-items : center;
        width: 100%;
        -webkit-box-pack : center;
        -moz-box-pack : center;
        -ms-flex-pack : center;
        -webkit-justify-content : center;
        justify-content : center;
      }
      .right {
        float: right
      }​
    </style>
    <title>Aktuelle Solarproduktion</title>
  </head>
  <body class="container">
    <div class="vertical-center">
        <div class="panel panel-success">
          <div class="panel-heading">
            <h3>Solarproduktion - Schatthäuser Str. 14</h3>
          </div>
          <div class="panel-body">
            <h1 class="text-success">Aktuell <span class="right">
                {{solar['current']}} {{solar['current_unit']}}</span></h1>
            <h1 class="text-success">Heute<span class="right">
                {{solar['day']}} {{solar['day_unit']}}</span></h1>
            <h1 class="text-success">Monat<span class="right">
                {{solar['month']}} {{solar['month_unit']}}</span></h1>
            <h1 class="text-success">Jahr<span class="right">
                {{solar['year']}} {{solar['year_unit']}}</span></h1>
            <h1 class="text-success">Gesammt<span class="right">
                {{solar['total']}} {{solar['total_unit']}}</span></h1>
        </div>
    </div>
  </body>
</html>