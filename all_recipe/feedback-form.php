<?php
              
if(isset($_POST['submit']))
{
    $data=$_POST['firstname'] + $_POST['lastname'] + $_POST['mailid'] + $_POST['subject'];
    $fp = fopen('data.txt', 'a');
    fwrite($fp, $data);
    fclose($fp);
    }
?>