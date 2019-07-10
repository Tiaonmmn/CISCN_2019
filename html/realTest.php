<?php
include('config.php');
header("content-type: text/html; charset=utf-8");
if (isset($_POST['id'])) {
    $id = $_POST['id'];
    if ($id == '23333333') {
        echo 'Sorry,wrong place.';
    }
    else{
		mysqli_query($link,"set names utf8");
        $query = "select message from `message` where id=".$_POST['id'];
		$result = mysqli_fetch_array(mysqli_query($link, $query));
		echo $result['message'];
    }

}
else{
    echo "flag{".guidv4()."}";
}


?>
