<html>
<body>
<?php
    require 'util/nav.php';
    require 'util/util.php';
?>
<h3>View teams:</h3>

<?php
    list($headers, $rows) = database('get_teams');

    print_table($headers, $rows);

?>


<br><br>

</body>
</html>


