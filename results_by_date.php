<html>
<body>
<?php
    require 'util/style.php';
    require 'util/nav.php';
    require 'util/util.php';
?>
<h3>Results by Date:</h3>

<form action="results_by_date.php" method="post">
    Select a date: <input type="text" name="date" placeholder="mm/dd/yy"><br>
    <input name="submit" type="submit" >
</form>

<?php
if (isset($_POST['submit'])) 
{
    $args = parse_args($_POST, array("date"));

    list($keys, $values) = database('get_results_by_date', $args);
    
    
    $headers = array("Home", "Away", "Score", "Court", "Date");
    $rows = array();
    
    foreach ($values as $i => $value) {
        
        $data = array_combine($keys, $value);

        $result = ($data['HOME_ID'] == $_POST['teamID']) == ($data['HOME_SCORE'] > $data['AWAY_SCORE']);

        $row = array(
            $data['HOME_NAME'].' '.$data['HOME_MASCOT'],
            $data['AWAY_NAME'].' '.$data['AWAY_MASCOT'],
            $data['HOME_SCORE'].'-'.$data['AWAY_SCORE'],
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
