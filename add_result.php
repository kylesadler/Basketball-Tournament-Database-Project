<html>
<body>
<?php
    require 'util/style.php';
    require 'util/nav.php';
    require 'util/util.php';
?>
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
    $args = parse_args($_POST, array("game", "home", "away"));

    $result = database('add_result', $args);
    print_r($result);
}
?>

