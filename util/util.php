<?php
function backend($python_command, $params = []) {
    /* run command on backend. returns array containing returned values */
    
    $command = 'python3 backend/api.py '.$python_command.' '.implode(' ', $params);
    
    // remove dangerous characters from command to protect web server
    $command = escapeshellcmd($command);
    
    // echo "command: $command <br>";
    // system($command);

    $output = null;
    $return_code = null;
    exec($command, $output, $return_code);

    if ($return_code != 0 || $output[0] == "ERROR") {
        throw new Exception(implode('\n', $output));
    }

    $json_string = implode("\n", $output);

    return json_decode($json_string, $true)["return"];
}

function parse_args($post_body, $valid_params) {
    /* reads valid_params from post body and returns them as an array
        TODO: check that args are always in the correct order
    */
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