<html>
<body>
<?php
    require 'nav.php';
    require 'util.php';
?>
<h3>View teams:</h3>

<?php
$teams = run_command('view_teams');
echo $teams;
?>


<br><br>

</body>
</html>


