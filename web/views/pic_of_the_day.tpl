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
    <title>Bild des Tages</title>
  </head>
   <body class="container">
   <div class="col-lg-12">
     <img src="{{data['url']}}" width="100%" >
     <p>{{data['text']}}</p>
   </div>
  </body>
</html>