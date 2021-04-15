<html>
<body>
<?php
    require 'util/style.php';
    require 'util/nav.php';
    require 'util/util.php';
?>
<h3>Add a new team:</h3>

<form action="manage_games.php" method="post">
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


list($keys, $values) = database('get_games_and_results');

    
$headers = array("Home", "Away", "Home Score", "Away Score", "Court", "Date");
$rows = array();

foreach ($values as $i => $value) {
    
    $data = array_combine($keys, $value);

    $row = array(
        $data['HOME_NAME'].' '.$data['HOME_MASCOT'],
        $data['AWAY_NAME'].' '.$data['AWAY_MASCOT'],
        $data['HOME_SCORE'],
        $data['AWAY_SCORE'],
        $data['COURT_NUMBER'],
        $data['DATE']
    );

    array_push($rows, $row);
}

print_table($headers, $rows);

?>

<br><br>

</body>
</html>
