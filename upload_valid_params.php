<?php

include "upload_valid_params.php";

$params = array();

foreach ($_POST as $param_name => $param_val) {
    if (in_array($param_name, $valid_params) {
        array_push($params, escapeshellarg($_POST[$param_name]));
    }
    echo "Param: $param_name; Value: $param_val<br />\n";
}

// build the linux command that you want executed;  
$command = 'python3 backend/add_result.py ' . implode(' ', $params);

// remove dangerous characters from command to protect web server
$command = escapeshellcmd($command);

// echo then run the command
echo "command: $command <br>";
system($command);           
?>