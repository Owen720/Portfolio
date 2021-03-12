<?php
    include("connection.php");
		include('session_student.php');
    include('timezone.php');

    if(isset($_POST["join"])) {

      $sql_2 = "SELECT * FROM `conferences` ";
      $result = mysqli_query($conn, $sql_2);

      if($row = mysqli_fetch_array($result)) {

        $week = $row['week'];
        $course = $row['course'];
        $class = $row['class'];
        $link = $row['link'];
        $date = date("Y-m-d h:i:s");

        $sql = "INSERT INTO attendance (week, name, course, class, logintime)
        VALUES ('$week', '$login_session', '$course', '$class', '$date')";

        if ($conn->query($sql) === TRUE) {
        }
        else {
        }
      }
    }

?>

<!DOCTYPE html>

<html lang="en">
<head>
	<meta charset="UTF-8">
	<title>Live</title>
	<link rel="stylesheet" href="live.css">
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
        <br>
        <h4><?php echo $login_session; ?></h4>
				<hr width="150px" border="1px" color="#808080">
      </center>
      <a href="dashboard_student.php"><i class="bar-dashboard"></i><span>Dashboard</span></a>
      <a href="class_student.php"><i class="bar-class"></i><span>Class</span></a>
      <a href="attendance_student.php"><i class="bar-attendence"></i><span>Attendance</span></a>
      <a href="logout.php"><i class="bar-logout"></i><span>Logout</span></a>
    </div>

  <div class="main_container">

    <?php

    $sql_1 = "SELECT * FROM `conferences` ";
    $result = mysqli_query($conn, $sql_1);

    if($row = mysqli_fetch_array($result, MYSQLI_ASSOC)) {
    ?>
    <br><h1>Conferences - Week
            <?php echo $row['week'] ?>
            <?php echo $row['course'] ?>
            <?php echo $row['class'] ?>
        </h1><br><hr>
        <?php
        }
        ?>

  <div class="center">
  <div class="header"></div>
       <form>
        </form>
  </div>
</div>

</body>
</html>
