<?php
    include("connection.php");
		include('session_teacher.php');
    include('timezone.php');

    if (isset($_POST["submit"])) {

      $name = $_POST['name'];
      $student_id = $_POST['id'];
      $password = $_POST['pw'];

      $sql = "INSERT INTO student (student_id, name, password)
      VALUES ('$name', '$student_id', '$password')";

      if ($conn->query($sql) === TRUE) {
      }
      else {
      }
    }

?>

<!DOCTYPE html>

<html lang="en">
<head>
	<meta charset="UTF-8">
	<title>Insert Student</title>
	<link rel="stylesheet" href="rollcall.css">
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
      <a href="#"><i class="bar-dashboard"></i><span>Dashboard</span></a>
      <a href="attendance_teacher.php"><i class="bar-attendence"></i><span>Attendance</span></a>
      <a href="logout.php"><i class="bar-logout"></i><span>Logout</span></a>
    </div>

  <div class="main_container">
    <br><h1>Insert Student</h1><br><hr>

    <div class="bar">
      <a href="attendance_teacher.php"><i class="bar-home"></i><span>Home</span></a><br>
      <a href="all_attendance.php"><i class="bar-home"></i><span>All</span></a><br>
      <a href="rollcall.php"><i class="bar-announcements"></i><span>Rollcall</span></a><br>
      <a href="add_student.php"><i class="bar-announcements"></i><span>Insert Student</span></a>
    </div>

    <div class="link">
      <form action="#" method="POST">
          <input name="name"type="text" placeholder="Student Name">
          <input name="id"type="text" placeholder="Student ID">
          <input name="pw" type="password" placeholder="Password">
          <input name="submit" type="submit" value="Insert">
       </form>
    </div>

  </div>
</div>

</body>
</html>
