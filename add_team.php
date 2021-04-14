<html>
<body>
<?php require 'nav.php'; ?>
<h3>Add a new team:</h3>

<form action="add_team.php" method="post">
    Name: <input type="text" name="name"><br>
    Mascot: <input type="text" name="mascot"><br>
    Tournament Seed: <input type="text" name="tournamentSeed"><br>
    <input name="submit" type="submit" >
</form>
<br><br>

</body>
</html>

<?php
if (isset($_POST['submit'])) 
{
    // add ' ' around multiple strings so they are treated as single command line args
    $name = escapeshellarg($_POST[name]);
    $mascot = escapeshellarg($_POST[mascot]);
    $tournamentSeed = escapeshellarg($_POST[tournamentSeed]);

    // build the linux command that you want executed;  
    $command = 'python3 backend/hello.py ' . $name . $mascot . $tournamentSeed;

    // remove dangerous characters from command to protect web server
    $command = escapeshellcmd($command);
 
    // echo then run the command
    echo "command: $command <br>";
    system($command);           
}
?>

