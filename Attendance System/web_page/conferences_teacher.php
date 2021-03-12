<?php
    include("connection.php");
		include('session_teacher.php');
    include('timezone.php');

    if(isset($_POST["post"])) {

      $week = $_POST['week'];
      $selectCourse = $_POST['selector_course'];
      $selectClass = $_POST['selector_class'];
      $link = $_POST['link'];
      $date = date("Y-m-d h:i:s");

      $sql = "INSERT INTO conferences (week, course, class, link, time)
      VALUES ('$week', '$selectCourse', '$selectClass', '$link', '$date')";

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
      <a href="dashboard_teacher.php"><i class="bar-dashboard"></i><span>Dashboard</span></a>
      <a href="attendance_teacher.php"><i class="bar-attendence"></i><span>Attendance</span></a>
      <a href="logout.php"><i class="bar-logout"></i><span>Logout</span></a>
    </div>

  <div class="main_container">
    <br><h1>Conferences</h1><br><hr>

    <div class="bar">
      <a href="home_teacher.php"><i class="bar-home"></i><span>Home</span></a>
      <a href="#"><i class="bar-announcements"></i><span>Announcements</span></a>
      <a href="#"><i class="bar-asm"></i><span>Assignments</span></a>
      <a href="#"><i class="bar-pages"></i><span>Pages</span></a>
      <a href="conferences_teacher.php"><i class="bar-conferences"></i><span>Conferences</span></a>
    </div>

    <div class="link">
      <form action="#" method="POST">
          <input name="week"type="text" placeholder="Week">
          <select name="selector_course">
            <option value="0">Course</option>
            <option value="AST10201 Computer Organization">AST10201 Computer Organization</option>
            <option value="AST10303 Understand Net-Centric World">AST10303 Understand Net-Centric World</option>
            <option value="AST10106 Introduction to Programming">AST10106 Introduction to Programming</option>
          </select>
          <select name="selector_class">
            <option value="0">Class</option>
            <option value="Lecture">Lecture</option>
            <option value="Tutorial">Tutorial</option>
          </select>
          <input name="link" type="text" placeholder="Post a link">&emsp;&emsp;
          <input name="post" type="submit" value="Post">
       </form>
    </div>

    <table>
      <tr class="type">
        <td>Week</td>
        <td>Course</td>
        <td>Class</td>
        <td>Link</td>
        <td>Time</td>
      </tr>
      <?php

      $sql_1 = "SELECT * FROM `conferences` ";
      $result = mysqli_query($conn, $sql_1);

      if(isset($_POST["del"])) {

        $sql_2 = "DELETE FROM conferences;";

        if ($conn->query($sql_2) === TRUE) {
        }
        else {
        }
      }

      else if($row = mysqli_fetch_array($result, MYSQLI_ASSOC)) {
      ?>
      <tr>
        <td>Week <?php echo $row['week']; ?></td>
        <td><?php echo $row['course']; ?></td>
        <td><?php echo $row['class']; ?></td>
        <td><?php echo $row['link']; ?></td>
        <td><?php echo $row['time']; ?></td>
        <?php
        }
        ?>
        }
      }
      </tr>
    </table>
    <div class="link">
      <form action="#" method="POST">
          <input name="del" type="submit" value="Delete">
       </form>
    </div>
  </div>
</div>

</body>
</html>
