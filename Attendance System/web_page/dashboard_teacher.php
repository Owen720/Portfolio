<?php
    include("connection.php");
		include('session_teacher.php');
    include('timezone.php');
?>

<!DOCTYPE html>

<html lang="en">
<head>
	<meta charset="UTF-8">
	<title>Dashboard</title>
	<link rel="stylesheet" href="dashboard_student.css">
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

  <div class="main_container" >
    <br><h1>Dashboard</h1><br><hr>

    <div class="class1">
        <a href="home_teacher.php"><div class="header"></div></a>
        <a href="home_teacher.php"><form class="CO">
          <strong style="color: #AF5D5D;">AST10201<br>Computer Organization</strong>
          <a href="home_teacher.php">2020AST10201</a>
        </form></a>
    </div>

    <div class="class2">
        <a href="home_teacher.php"><div class="header"></div></a>
        <a href="home_teacher.php"><form class="CO">
          <strong style="color: #5EB258;">AST10303<br>Understand Net-Centric World</strong>
          <a href="home_teacher.php">2020AST10303</a>
        </form></a>
    </div>

    <div class="class3">
        <a href="home_teacher.php"><div class="header"></div></a>
        <a href="home_teacher.php"><form class="CO">
          <strong style="color: #FF8000">AST10106<br>Introduction to Programming</strong>
          <a href="home_teacher.php">2020AST10106</a>
        </form></a>
    </div>

</div>

</body>
</html>
