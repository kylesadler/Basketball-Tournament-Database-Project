<html>
<body>
<?php
    require 'util/style.php';
    require 'util/nav.php';
    require 'util/util.php';
    list($headers, $teams) = database('get_team_name_mascot_id');
?>

<h3>Results by Team</h3>

<form action="roster_by_team.php" method="post">

    Select a team: 
    <select name="teamID" id="teamID">
        <?php
            foreach ($teams as $i => $team) {
                // value is ID, text is Name Mascots
                echo '<option value="'.$team[2].'">'.$team[0].' '.$team[1].'</option>';
            }
        ?>
    </select>
    
    <input name="submit" type="submit" >
</form>
<?php
if (isset($_POST['submit'])) {
    
    $args = parse_args($_POST, array("teamID"));
    
    list($keys, $values) = database('get_results_by_team_id', $args);
    
    
    $headers = array("Home", "Away", "Score", "Result", "Court", "Date");
    $rows = array();
    
    foreach ($values as $i => $value) {
        
        $data = array_combine($keys, $value);

        $result = ($data['HOME_ID'] == $_POST['teamID']) == ($data['HOME_SCORE'] > $data['AWAY_SCORE']);

        $row = array(
            $data['HOME_NAME'].' '.$data['HOME_MASCOT'],
            $data['AWAY_NAME'].' '.$data['AWAY_MASCOT'],
            $data['HOME_SCORE'].'-'.$data['AWAY_SCORE'],
            $result ? 'Win' : 'Loss',
            $data['COURT_NUMBER'],
            $data['DATE']
        );

        array_push($rows, $row);
    }

    print_table($headers, $rows);
    
    echo '<script> document.getElementById("teamID").value = '.$args[0].'; </script>';
}
?>

<br><br>
</body>
</html>
