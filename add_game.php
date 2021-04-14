<html>
<body>
<?php require 'nav.php'; ?>
<h3>Add a new team:</h3>

<form action="add_game.php" method="post">
    Home Team: <input type="text" name="home"><br>
    Away Team: <input type="text" name="away"><br>
    Court Number: <input type="text" name="court_num"><br>
    Date: <input type="text" name="date"><br>
    <input name="submit" type="submit" >
</form>
<br><br>

</body>
</html>

<?php
if (isset($_POST['submit'])) 
{
    // add ' ' around multiple strings so they are treated as single command line args
    $home = escapeshellarg($_POST[home]);
    $away = escapeshellarg($_POST[away]);
    $court_num = escapeshellarg($_POST[court_num]);
    $date = escapeshellarg($_POST[date]);

    // build the linux command that you want executed;  
    $command = 'python3 backend/add_game.py ' . $home . ' ' . $away . ' ' . $court_num . ' ' . $date;

    // remove dangerous characters from command to protect web server
    $command = escapeshellcmd($command);
 
    // echo then run the command
    echo "command: $command <br>";
    system($command);           
}
?>

