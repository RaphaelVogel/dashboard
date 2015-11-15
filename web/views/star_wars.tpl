<!DOCTYPE html>
<html lang="de">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" href="/lib/bootstrap.min.css">
    <style type="text/css">
      body {color: white !important; font-size: 15px !important; background-color: black !important;}
    </style>
    <script src="/lib/jquery-1.11.2.min.js"></script>
    <title>Darth Vader</title>
    <script>
        $.ajax({
            url: "http://192.168.1.15:8080/playsound/breath"
        });
    </script>
  </head>
   <body class="container">
   <div class="col-lg-12">
     <img src="{{pic_url}}" width="100%" >
   </div>
  </body>
</html>