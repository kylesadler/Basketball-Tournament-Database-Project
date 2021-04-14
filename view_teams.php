<html>
<body>
<?php
    require 'util/nav.php';
    require 'util/util.php';
?>
<h3>View teams:</h3>

<?php
$teams = backend('view_teams');
print_r($teams);
?>


<br><br>

</body>
</html>


