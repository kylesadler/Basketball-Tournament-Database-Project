<html>
<body>
<?php
    require 'util/style.php';
    require 'util/nav.php';
    require 'util/util.php';
    list($headers, $court_nums) = database('get_court_numbers');
?>
<h3>View Game Schedule by Court Number</h3>

<form action="games_by_court.php" method="post">
    Select a court number: <select name="num" id="num">
            <?php
                foreach ($court_nums as $i => $num) {
                    echo '<option value="'.$num[0].'">'.$num[0].'</option>';
                }
            ?>
        </select><br>
    <input name="submit" type="submit" >
</form>

<?php
if (isset($_POST['submit'])) 
{
    $args = parse_args($_POST, array("num"));

    
    list($keys, $values) = database('get_games_by_court', $args);

        
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
}
?>

<br><br>

</body>
</html>
