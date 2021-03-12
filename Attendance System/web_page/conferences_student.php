<?php
    include("connection.php");
		include('session_student.php');
    include('timezone.php');
?>

<!DOCTYPE html>

<html lang="en">
<head>
	<meta charset="UTF-8">
	<title>Conferences</title>
	<link rel="stylesheet" href="conferences_teacher.css">
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
    <br><h1>Conferences</h1><br><hr>

    <div class="bar">
      <a href="home_student.php"><i class="bar-home"></i><span>Home</span></a>
      <a href="#"><i class="bar-announcements"></i><span>Announcements</span></a>
      <a href="#"><i class="bar-asm"></i><span>Assignments</span></a>
      <a href="#"><i class="bar-pages"></i><span>Pages</span></a>
      <a href="conferences_student"><i class="bar-conferences"></i><span>Conferences</span></a>
    </div>

    <table>
      <tr class="type">
        <td>Week</td>
        <td>Course</td>
        <td>Class</td>
        <td>Link</td>
      </tr>
      <?php

      $sql_1 = "SELECT * FROM `conferences` ";
      $result = mysqli_query($conn, $sql_1);

      if($row = mysqli_fetch_array($result, MYSQLI_ASSOC)) {
        $week = $row['week'];
        $course = $row['course'];
        $class = $row['class'];
        $link = $row['link'];
      ?>
      <tr>
          <td>Week <?php echo $week; ?></td>
          <td><?php echo $course; ?></td>
          <td><?php echo $class; ?></td>
          <td><?php echo $link; ?></td>
        <?php
        }
        ?>
        }
      }
      </tr>
    </table>
    <div class="link">
      <form action="live.php" method="POST">
          <input href="live.php" name="join" type="submit" value="Join">
       </form>
    </div>
  </div>
</div>

</body>
</html>
