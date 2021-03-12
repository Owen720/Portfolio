<?php
    include("connection.php");
		include('session_teacher.php');
    include('timezone.php');
?>

<!DOCTYPE html>

<html lang="en">
<head>
	<meta charset="UTF-8">
	<title>All Student Attendance</title>
	<link rel="stylesheet" href="all_attendance.css">
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
    <br><h1>All Student Attendance</h1><br><hr>

    <div class="bar">
      <a href="attendance_teacher.php"><i class="bar-home"></i><span>Home</span></a><br>
      <a href="all_attendance.php"><i class="bar-home"></i><span>All</span></a><br>
      <a href="rollcall.php"><i class="bar-announcements"></i><span>Rollcall</span></a><br>
      <a href="add_student.php"><i class="bar-announcements"></i><span>Insert Student</span></a>
    </div>

    <div class="link">
      <form action="#" method="POST">
          <input name="name"type="text" placeholder="Student Name">
          <select name="selector_course">
            <option value="0">Course</option>
            <option value="AST10201 Computer Organization">AST10201 Computer Organization</option>
            <option value="AST10303 Understand Net-Centric World">AST10303 Understand Net-Centric World</option>
            <option value="AST10106 Introduction to Programming">AST10106 Introduction to Programming</option>
          </select>
          <input name="post" type="submit" value="Search">
       </form>
    </div>

    <table>
      <tr class="type">
        <td>Week</td>
        <td>Course</td>
        <td>Class</td>
        <td>Time</td>
        <td>Rollcall</td>
      </tr>
      <?php

      if (isset($_POST["post"])) {

        $name = $_POST['name'];
        $selectCourse = $_POST['selector_course'];

        $sql = "SELECT * FROM attendance WHERE name = '$name' and course = '$selectCourse'";
        $result = mysqli_query($conn, $sql);

        if ($result = $conn->query($sql)) {

          while ($row = $result->fetch_row()) {

      ?>
      <tr>
        <td>Week <?php echo $row['0']; ?></td>
        <td><?php echo $row['2']; ?></td>
        <td><?php echo $row['3']; ?></td>
        <td><?php echo $row['4']; ?></td>
        <td><?php echo $row['5']; ?></td>
        <?php
        }
      }
    }
        ?>
      </tr>
    </table>

  </div>
</div>

</body>
</html>
