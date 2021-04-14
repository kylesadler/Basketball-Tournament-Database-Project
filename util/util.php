<?php
function backend($python_command, $params = []) {
    /* run command on backend. returns array with output lines */
    $command = 'python3 backend/api.py ' . $python_command . ' ' . implode(' ', $params);
    
    // remove dangerous characters from command to protect web server
    $command = escapeshellcmd($command);
    
    // echo "command: $command <br>";
    // system($command);    
    $output = null;
    // system($command);    
    exec($command,$output);    
    reutrn $output;
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