<?php

function run_command($python_command, $params = []) {
    $command = 'python3 backend/api.py ' . $python_command . ' ' . implode(' ', $params);
    
    // remove dangerous characters from command to protect web server
    $command = escapeshellcmd($command);
    
    // echo "command: $command <br>";
    system($command);    
}

function parse_args($post_body, $valid_params) {
    $params = array();
    
    foreach ($post_body as $param_name => $param_val) {
        if (in_array($param_name, $valid_params)) {
            array_push($params, escapeshellarg($post_body[$param_name]));
        }
        // echo "Param: $param_name; Value: $param_val<br />\n";
    }

    return $params;
}
?>