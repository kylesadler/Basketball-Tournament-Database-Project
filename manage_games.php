<html>
<body>
<?php
    require 'util/style.php';
    require 'util/nav.php';
    require 'util/util.php';
    list($headers, $teams) = database('get_team_name_mascot_id');
    
?>
<h3>Add a new game:</h3>

<form action="manage_games.php" method="post">
    Home Team: <select name="home" id="home">
            <?php
                foreach ($teams as $i => $team) {
                    echo '<option value="'.$team[2].'">'.$team[0].' '.$team[1].'</option>';
                }
            ?>
        </select><br>
    Away Team: <select name="away" id="away">
            <?php
                foreach ($teams as $i => $team) {
                    echo '<option value="'.$team[2].'">'.$team[0].' '.$team[1].'</option>';
                }
            ?>
        </select><br>
    Court Number: <input type="text" name="court_num"><br>
    Date: <input type="text" name="date" placeholder="mm/dd/yy'"><br>
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
