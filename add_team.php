<html>
<body>
<?php
    require 'nav.php';
    require 'util.php';
?>
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
    $args = parse_args($_POST, array("name", "mascot", "tournamentSeed"));

    run_command('add_team', $args);
}
?>

