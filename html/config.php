<?php
$host = '127.0.0.1';
$username = 'ciscn2019';
$password = "Tiaonmmn.ZMZ";
$database = 'flag3726792b7c92';
$link = mysqli_connect($host, $username, $password, $database);
mysqli_query($link,"set names utf8");
header("content-type: text/html; charset=utf-8");
if (!$link) {
    echo "Unable to connect to MySQL Server.";
    exit();
}function guidv4()
{
    if (function_exists('com_create_guid') === true)
        return trim(com_create_guid(), '{}');

    $data = openssl_random_pseudo_bytes(16);
    $data[6] = chr(ord($data[6]) & 0x0f | 0x40);
    $data[8] = chr(ord($data[8]) & 0x3f | 0x80);
    return vsprintf('%s%s-%s-%s-%s-%s%s%s', str_split(bin2hex($data), 4));
}

if (basename($_SERVER['PHP_SELF']) == basename(__FILE__)) {
    echo "flag{".guidv4()."}";
}

?>
