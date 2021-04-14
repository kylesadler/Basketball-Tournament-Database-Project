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
    $params = parse_args($_POST, array("home", "away", "court_num", "date"));

    run_command('add_game', $params);
}
?>

