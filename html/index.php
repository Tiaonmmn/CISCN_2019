<?php
error_reporting(0);
session_start();
include "./config.php";
if ($_POST['username']=='test' &&$_POST['password']=='test') {
    $_SESSION['guest'] = true;
    header("location:console.php");
}

$black_list = "/select|insert|\(\)|mid|having|concat|if|like|where|union|admin|guest|%00|\'|";
$black_list .= "=|_|greatest|<|test|flag|_|\.|limit|#|and| |database|char|by|conact|>|sleep|substr/i";
if (preg_match($black_list, $_POST['username'])) exit(":P username");
if (preg_match($black_list, $_POST['password'])) exit(":P password");


$query = "select username from `user8dc69c2d` where username='$_POST[username]' and password='$_POST[password]'";

$result = mysqli_query($link, $query);
$result = mysqli_fetch_array($result);
$admin_pass = mysqli_fetch_array(mysqli_query($link, "select password from `user8dc69c2d` where username='admin'"));
if (($admin_pass['password']) && ($admin_pass['password'] === $_POST['password'])) {
    $_SESSION['admin'] = true;
	$_SESSION['first'] = true;
    header("location:consolef11b376b9766.php");
}
?>
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width,initial-scale=1">
    <title>Simple Admin Login</title><!-- Welcome to part2. -->
    <link rel="stylesheet" href="css/auth.css">
</head>

<body>
<div class="lowin">
    <div class="lowin-brand">
        <img src="kodinger.jpg" alt="logo">
    </div>
    <div class="lowin-wrapper">
        <div class="lowin-box lowin-login">
            <div class="lowin-box-inner">
                <form method="post" action="">
                    <p>Sign in to continue</p>
                    <div class="lowin-group">
                        <label>Username <a href="#" class="login-back-link">Sign in?</a></label>
                        <input type="text" autocomplete="text" name="username" class="lowin-input">
                    </div>
                    <div class="lowin-group password-group">
                        <label>Password <a href="Don't ask me." class="forgot-link">Don't have an account? </a></label>
                        <input type="password" name="password" autocomplete="current-password" class="lowin-input">
                    </div>
                    <button class="lowin-btn login-btn">
                        Sign In
                    </button>
                    <div class="text-foot">
                        <?php
                        if ($result['username']) echo "<h2>Welcome {$result['username']}</h2>";
                        ?>
                    </div>
                </form>
            </div>
        </div>
    </div>
</div>
<script src="js/auth.js"></script>
</body>
<!--
/*
0952a94ec50a593d5b8b91545738dacd9e75b83357e2c0f573cb89ab97ebbfda
*/
$black_list = "/select|insert|\(\)|mid|having|concat|if|like|where|union|admin|guest|%00|\'|";
$black_list .= "=|_|greatest|<|test|flag|_|\.|limit|#|and| |database|char|by|conact|>|sleep|substr/i";
/*
6218e8dbae1da2fd0e883874719b2afcd80fd3b416b9fee2cb4414b8df8f841b
*/
$query = "select username from `user8dc69c2d` where username='$_POST[username]' and password='$_POST[password]'";

$result = mysqli_query($link, $query);
$result = mysqli_fetch_array($result);
$admin_pass = mysqli_fetch_array(mysqli_query($link, "select password from `user8dc69c2d` where username='admin'"));
if (($admin_pass['password']) && ($admin_pass['password'] === $_POST['password'])) {
    $_SESSION['admin'] = true;
    header("location:AHm5JWv&BFPaIqwLosSEUkX1KTfy6YQ.php");//Ah,I forget to modify it!ヾ(｡｀Д´｡)
}

 -->
</html>
