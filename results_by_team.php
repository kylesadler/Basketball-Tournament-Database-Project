<html>
<body>
<?php
    require 'util/nav.php';
    require 'util/util.php';
?>


<?php
   list($headers, $teams) = database('get_team_name_mascot_id');
?>

<h3>Results by Team</h3>

<form action="results_by_team.php" method="post">

    Select a Team: 
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
<br><br>

<h3>View teams:</h3>
<?php
if (isset($_POST['submit'])) {

    $args = parse_args($_POST, array("teamID"));

    list($headers, $rows) = database('get_results_by_team_id', $args);
    print_table($headers, $rows);
}
?>

</body>
</html>
