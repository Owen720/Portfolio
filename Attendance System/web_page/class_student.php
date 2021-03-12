<?php
    include("connection.php");
		include('session_student.php');
    include('timezone.php');
?>

<!DOCTYPE html>

<html lang="en">
<head>
	<meta charset="UTF-8">
	<title>Class</title>
	<link rel="stylesheet" href="class_student.css">
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
			<a href="dashboard_student.php"><i class="bar-dashboard"></i><span>Dashboard</span></a>
      <a href="class_student.php"><i class="bar-class"></i><span>Class</span></a>
      <a href="attendance_student.php"><i class="bar-attendence"></i><span>Attendance</span></a>
      <a href="logout.php"><i class="bar-logout"></i><span>Logout</span></a>
  </div>

  <div class="main_container">
    <br><h1>Class</h1><br><hr><br><br><br>

    <strong>AST10201 Computer Organization - Lecture</strong><br>
    <table>
      <tr class="type">
        <td>Class Type</td>
        <td>Days</td>
        <td>Time</td>
        <td>Lecturer</td>
        <td>Credits</td>
      </tr>
      <tr>
        <td>Lecture</td>
        <td>Monday</td>
        <td>10:00 am - 11:50 am</td>
        <td>Bell Liu</td>
        <td>3.000</td>
      </tr>
    </table>

    <br>

    <strong>AST10201 Computer Organization - Tutorial</strong><br>
    <table>
      <tr class="type">
        <td>Class Type</td>
        <td>Days</td>
        <td>Time</td>
        <td>Lecturer</td>
        <td>Credits</td>
      </tr>
      <tr>
        <td>Tutorial</td>
        <td>Monday</td>
        <td>13:00 pm - 13:50 pm</td>
        <td>Bell Liu</td>
        <td>0.000</td>
      </tr>
    </table>

    <br>

    <strong>AST10303 Understanding the Network-Centric World - Lecture</strong><br>
    <table>
      <tr class="type">
        <td>Class Type</td>
        <td>Days</td>
        <td>Time</td>
        <td>Lecturer</td>
        <td>Credits</td>
      </tr>
      <tr>
        <td>Lecture</td>
        <td>Tuesday</td>
        <td>10:00 am - 11:50 am</td>
        <td>Fan Yan</td>
        <td>3.000</td>
      </tr>
    </table>

    <br>

    <strong>AST10303 Understanding the Network-Centric World - Tutorial</strong><br>
    <table>
      <tr class="type">
        <td>Class Type</td>
        <td>Days</td>
        <td>Time</td>
        <td>Lecturer</td>
        <td>Credits</td>
      </tr>
      <tr>
        <td>Tutorial</td>
        <td>Tuesday</td>
        <td>13:00 pm - 13:50 pm</td>
        <td>Fan Yan</td>
        <td>0.000</td>
      </tr>
    </table>

    <br>

    <strong>AST10106 Introduction to Programming - Lecture</strong><br>
    <table>
      <tr class="type">
        <td>Class Type</td>
        <td>Days</td>
        <td>Time</td>
        <td>Lecturer</td>
        <td>Credits</td>
      </tr>
      <tr>
        <td>Lecture</td>
        <td>Wednesday</td>
        <td>10:00 am - 11:50 am</td>
        <td>Pang</td>
        <td>3.000</td>
      </tr>
    </table>

    <br>

    <strong>AST10106 Introduction to Programming - Tutorial</strong><br>
    <table>
      <tr class="type">
        <td>Class Type</td>
        <td>Days</td>
        <td>Time</td>
        <td>Lecturer</td>
        <td>Credits</td>
      </tr>
      <tr>
        <td>Tutorial</td>
        <td>Wednesday</td>
        <td>13:00 pm - 13:50 pm</td>
        <td>Pang</td>
        <td>0.000</td>
      </tr>
    </table>
</div>

</body>
</html>
