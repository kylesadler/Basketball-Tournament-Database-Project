<html>
<body>
<?php
    require 'util/style.php';
    require 'util/nav.php';
    require 'util/util.php';
?>
<h3>Results by Date:</h3>

<form action="manage_games.php" method="post">
    Select a date: <input type="text" name="date" placeholder="mm/dd/yy"><br>
    <input name="submit" type="submit" >
</form>

<?php
if (isset($_POST['submit'])) 
{
    $args = parse_args($_POST, array("date"));

    list($headers, $rows) = database('get_results_by_date', $args);
    
    print_table($headers, $rows);
    
    echo '<script> document.getElementById("date").value = '.$args[0].'; </script>';
}

?>

<br><br>

</body>
</html>
