<html>
<body>
<h3>Enter information about an item to add to the database:</h3>

<form action="python_insert_item.php" method="post">
    Name: <input type="text" name="name"><br>
    Price_Per_LB: <input type="text" name="price_per_lb"><br>
    Roasting: <input type="text" name="roasting"><br>
    <input name="submit" type="submit" >
</form>
<br><br>

</body>
</html>

<?php
if (isset($_POST['submit'])) 
{
    // replace ' ' with '\ ' in the strings so they are treated as single command line args
    $name = escapeshellarg($_POST[name]);
    $price_per_lb = escapeshellarg($_POST[price_per_lb]);
    $roasting = escapeshellarg($_POST[roasting]);

    $command = 'python3 insert_new_item.py' . ' '.  $name . ' ' . $price_per_lb . ' ' . $roasting;

    // remove dangerous characters from command to protect web server
    $escaped_command = escapeshellcmd($command);
    echo "<p>command: $command <p>"; 
    // run insert_new_item.py
    system($escaped_command);           
}
?>


