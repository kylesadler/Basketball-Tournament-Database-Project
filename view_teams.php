<html>
<body>
<?php
    require 'util/nav.php';
    require 'util/util.php';
?>
<h3>View teams:</h3>

<?php
    
    
    list($headers, $rows) = database('get_teams');


    echo '<table>';
    echo '<tr>';
    
    foreach ($headers as $i => $h) {
        echo '<th>'.$h.'</th>';
    }

    echo '</tr>';

    
    foreach ($rows as $i => $row) {
        echo '<tr>';
        foreach ($row as $j => $x) {
            echo '<td>'.$x.'</td>';
        }
        echo '</tr>';
    }


    print_r($teams);
?>


<br><br>

</body>
</html>


