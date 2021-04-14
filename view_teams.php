<html>
<body>
<?php
    require 'util/nav.php';
    require 'util/util.php';
?>
<h3>View teams:</h3>

<?php
$teams = database('get_teams');
print_r($teams);
?>


<br><br>

</body>
</html>


