<html>
<body>
<?php
    require 'util/style.php';
    require 'util/nav.php';
    require 'util/util.php';
    list($headers, $teams) = database('get_team_name_mascot_id');
?>
<h3>Add a new player:</h3>

<form action="manage_players.php" method="post">
    Name: <input type="text" name="name"><br>
    Team: <select name="teamId" id="teamId">
            <?php
                foreach ($teams as $i => $team) {
                    echo '<option value="'.$team[2].'">'.$team[0].' '.$team[1].'</option>';
                }
            ?>
        </select><br>
    Position: <input type="text" name="position"><br>
    <input name="submit" type="submit" >
</form>


<?php
if (isset($_POST['submit'])) 
{
    $args = parse_args($_POST, array("name", "position", "teamId"));

    database('add_player', $args);
}

list($headers, $rows) = database('get_players');
print_table($headers, $rows);
?>

<br><br>

</body>
</html>
