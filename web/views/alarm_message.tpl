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
    <title>Alarm</title>
  </head>
  <body style="background-color: red;">
    <div class="vertical-center">
        <h1 style="font-size: 3.5em;">ALARM: {{alarm_type}} - {{alarm_location}}</h1>
    </div>
  </body>
</html>