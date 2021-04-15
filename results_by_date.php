<html>
<body>
<?php
    require 'util/style.php';
    require 'util/nav.php';
    require 'util/util.php';
    list($_, $dates) = database('get_result_dates');
?>
<h3>Results by Date</h3>

<form action="results_by_date.php" method="post">

    <!-- TODO: make dropdown -->
    Select a date: <select name="date" id="date">
        <?php
            foreach ($dates as $i => $date) {
                // value is ID, text is Name Mascots
                echo '<option value="'.$date[0].'">'.$date[0].'</option>';
            }
        ?>
    </select>
    <input name="submit" type="submit" >
</form>

<?php
if (isset($_POST['submit'])) 
{
    $args = parse_args($_POST, array("date"));

    list($keys, $values) = database('get_results_by_date', $args);
    
    
    $headers = array("Home", "Away", "Score", "Winner", "Court", "Date");
    $rows = array();
    
    foreach ($values as $i => $value) {
        
        $data = array_combine($keys, $value);

        $result = $data['HOME_SCORE'] > $data['AWAY_SCORE'];

        $row = array(
            $data['HOME_NAME'].' '.$data['HOME_MASCOT'],
            $data['AWAY_NAME'].' '.$data['AWAY_MASCOT'],
            $data['HOME_SCORE'].'-'.$data['AWAY_SCORE'],
            $result ? $data['HOME_NAME'] : $data['AWAY_NAME'],
            $data['COURT_NUMBER'],
            $data['DATE']
        );

        array_push($rows, $row);
    }

    print_table($headers, $rows);
    
    echo '<script> document.getElementById("date").value = '.$args[0].'; </script>';
}

?>

<br><br>

</body>
</html>
