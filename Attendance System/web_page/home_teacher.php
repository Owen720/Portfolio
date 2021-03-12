<?php
    include("connection.php");
		include('session_teacher.php');
    include('timezone.php');
?>

<!DOCTYPE html>

<html lang="en">
<head>
	<meta charset="UTF-8">
	<title>Home</title>
	<link rel="stylesheet" href="home_teacher.css">
	<link rel="stylesheet" href="main.css">
</head>

<body>

<div class="wrapper">
  <div class="top_navbar">
    <div class="hamburger">
    </div>
    <div class="top_menu">
      <div class="logo">eLearning</div>
    </div>
  </div>

	<div class="sidebar">
      <center>
        <img src="1.png" class="profile_image" alt="">
        <h4><?php echo $login_session; ?></h4>
				<hr width="150px" border="1px" color="#808080">
      </center>
      <a href="dashboard_teacher.php"><i class="bar-dashboard"></i><span>Dashboard</span></a>
      <a href="attendance_teacher.php"><i class="bar-attendence"></i><span>Attendance</span></a>
      <a href="logout.php"><i class="bar-logout"></i><span>Logout</span></a>
    </div>

  <div class="main_container">
    <br><h1>Home</h1><br><hr>

    <div class="bar">
      <a href="co.php"><i class="bar-home"></i><span>Home</span></a>
      <a href="#"><i class="bar-announcements"></i><span>Announcements</span></a>
      <a href="#"><i class="bar-asm"></i><span>Assignments</span></a>
      <a href="#"><i class="bar-pages"></i><span>Pages</span></a>
      <a href="conferences_teacher.php"><i class="bar-conferences"></i><span>Conferences</span></a>
    </div>
  </div>
</div>

</body>
</html>
