<!DOCTYPE html>
<html lang="de">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" href="/lib/bootstrap.min.css">
    <style type="text/css">
      body {color: white !important; font-size: 14px !important; background-color: black !important;}
    </style>
    <style type="text/css">
      body { font-size: 15px !important;}
    </style>
    <title>Ebay in Meckesheim</title>
  </head>
  <body class="container">
  <div class="col-lg-12">
      <table class="table">
        <tbody>
        % for idx,offer in enumerate(offers):
          % if idx % 4 == 0:
          <tr>
          % end
            <td><img src="{{offer['image_url']}}" height="70%"><br>
            {{offer['text']}}&nbsp; {{offer['price']}}</td>
          % if idx+1 % 4 == 0:
          </tr>
          % end
        % end
        </tbody>
      </table>
  </div>
  </body>
</html>