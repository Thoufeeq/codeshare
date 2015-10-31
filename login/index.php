<?php
include('login.php'); // Includes Login Script

if(isset($_SESSION['login_user'])){
header("location: dashboard.php");
}
?>
<!DOCTYPE html>
<html>
<head>
<link href='http://fonts.googleapis.com/css?family=Montserrat:400,700' rel='stylesheet' type='text/css'>
<link rel="stylesheet" type="text/css" href="style.css">
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Classroom Surveillance Using Raspberry Pi</title>
</head>
<body>
<br>
<div class="heading"><h1>Classroom Surveillance</h1></div>

<br>
<div class="login-block">
    <h1>Login</h1>
    <form action="" method="post">
    <input type="text" value="" placeholder="Username" id="username" />
    <input type="password" value="" placeholder="Password" id="password" />
    <!-- <button>Login</button> -->
    <input name="submit" type="submit" value=" Login ">
    <span><?php echo $error; ?></span>
	</form>
</div>
</body>
</html>
