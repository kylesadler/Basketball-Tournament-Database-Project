<html>
<body>
<?php
    require 'util/style.php';
    require 'util/nav.php';
    require 'util/util.php';
    list($headers, $teams) = database('get_team_name_mascot_id');
?>

<h3>Roster by Team</h3>

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
    
    list($headers, $rows) = database('get_roster_by_team', $args);
    
    print_table($headers, $rows);
    
    echo '<script> document.getElementById("teamID").value = '.$args[0].'; </script>';
}
?>

<br><br>
</body>
</html>
