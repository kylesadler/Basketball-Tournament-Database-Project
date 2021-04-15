<html>
<body>
<?php
    require 'util/style.php';
    require 'util/nav.php';
    require 'util/util.php';
?>
<h3>Add a new team:</h3>

<form action="add_game.php" method="post">
    Home Team: <input type="text" name="home"><br>
    Away Team: <input type="text" name="away"><br>
    Court Number: <input type="text" name="court_num"><br>
    Date: <input type="text" name="date"><br>
    <input name="submit" type="submit" >
</form>

<?php
if (isset($_POST['submit'])) 
{
    $args = parse_args($_POST, array("home", "away", "court_num", "date"));

    database('add_game', $args);
}

list($headers, $rows) = database('get_games');
print_table($headers, $rows);
?>

<br><br>

</body>
</html>
