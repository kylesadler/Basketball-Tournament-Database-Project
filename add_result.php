<html>
<body>
<?php require 'nav.php'; ?>
<h3>Add a new team:</h3>

<form action="add_result.php" method="post">
    Game: <input type="text" name="game"><br>
    Home Team Score: <input type="text" name="home"><br>
    Away Team Score: <input type="text" name="away"><br>
    <input name="submit" type="submit" >
</form>
<br><br>

</body>
</html>

<?php
if (isset($_POST['submit'])) 
{
    // add ' ' around multiple strings so they are treated as single command line args
    $valid_params = array("game", "home", "away");

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
}
?>

