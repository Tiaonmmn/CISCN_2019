<?php

error_reporting(0);
session_start();
if ($_SESSION['guest'] != true) {
    header('location:index.php');
} else {
    header("important:wrong place.");
}
function getMessage($id) {
        $url = 'http://127.0.0.1/admin448bfdcd-c968-4d05-b9aa-7563a9e9cd19/realTest.php'; //TODO: Modify this.
		$data = 'id=1';
		$ch = curl_init();
		curl_setopt($ch, CURLOPT_URL, $url);
		curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
		curl_setopt($ch, CURLOPT_POST, 1);
		curl_setopt($ch, CURLOPT_POSTFIELDS, $data);
		$re = curl_exec($ch);
		curl_close($ch);
		return $re;
}
?>
<!DOCTYPE html>
<html lang="en">

<head>

    <meta charset="utf-8">
    <!-- Welcome to the final part.A phpinfo.php may help you.-->
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="description" content="">
    <meta name="author" content="">

    <title>Deprecated portal!</title>

    <!-- Bootstrap Core CSS -->
    <link href="css/bootstrap.min.css" rel="stylesheet">

    <!-- Custom CSS -->
    <link href="css/shop-item.css" rel="stylesheet">

    <!-- HTML5 Shim and Respond.js IE8 support of HTML5 elements and media queries -->
    <!-- WARNING: Respond.js doesn't work if you view the page via file:// -->
    <!--[if lt IE 9]>
    <script src="https://oss.maxcdn.com/libs/html5shiv/3.7.0/html5shiv.js"></script>
    <script src="https://oss.maxcdn.com/libs/respond.js/1.4.2/respond.min.js"></script>
    <![endif]-->

</head>

<body>


<!-- Page Content -->
<div class="container">

    <div class="row">

        <div class="col-md-9">

            <div class="thumbnail">
                <!--

                -->
                <div class="caption-full">
                    <h4><a href="#"><?php
			print(getMessage(23333333));
		?>

                        </a></h4>

                </div>

            </div>

            <div class="well">
                <div class="col-lg-6">
                    <img class="img-responsive" src="img/logo.png" alt="">
                    </p>
                </div>

                <hr>

            </div>

        </div>

    </div>

</div>
<!-- /.container -->


<!-- /.container -->

<!-- jQuery -->
<script src="js/jquery.js"></script>

<!-- Bootstrap Core JavaScript -->
<script src="js/bootstrap.min.js"></script>

</body>

</html>

