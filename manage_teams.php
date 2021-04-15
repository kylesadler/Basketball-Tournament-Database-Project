<html>
<body>
<?php
    require 'util/style.php';
    require 'util/nav.php';
    require 'util/util.php';
?>
<h3>Add a New Team:</h3>

<form action="manage_teams.php" method="post">
    Name: <input type="text" name="name"><br>
    Mascot: <input type="text" name="mascot"><br>
    Tournament Seed: <input type="text" name="tournamentSeed"><br>
    <input name="submit" type="submit" >
</form>


<?php
if (isset($_POST['submit'])) 
{
    $args = parse_args($_POST, array("name", "mascot", "tournamentSeed"));

    database('add_team', $args);
}

list($headers, $rows) = database('get_teams');
print_table($headers, $rows);
?>

<br><br>

</body>
</html>
