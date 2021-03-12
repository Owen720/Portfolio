<?php
    include("connection.php");
    include('timezone.php');
    session_start();

    if($_SERVER["REQUEST_METHOD"] == "POST") {

        $username = mysqli_real_escape_string($conn,$_POST['username']);
        $password = mysqli_real_escape_string($conn,$_POST['pw']);

        $sql = "SELECT * FROM student WHERE student_id = '$username' and password = '$password'";
        $sql_1 = "SELECT * FROM teacher WHERE teacher_id = '$username' and password = '$password'";
        $result = mysqli_query($conn,$sql) or die( mysqli_error($conn));
        $result_1 = mysqli_query($conn,$sql_1) or die( mysqli_error($conn));
        $row = mysqli_fetch_array($result,MYSQLI_ASSOC);
        $row_1 = mysqli_fetch_array($result_1,MYSQLI_ASSOC);

        $count = mysqli_num_rows($result);
        $count_1 = mysqli_num_rows($result_1);

        if($count == 1) {
           $_SESSION['login_user'] = $username;
           header("location: dashboard_student.php");
        }
        else if($count_1 == 1 && $username == "bliu"){
           $_SESSION['login_user'] = $username;
           header("location: dashboard_teacher.php");
        }
        else if($count_1 == 1 && $username == "fyan"){
           $_SESSION['login_user'] = $username;
           header("location: dashboard_teacher.php");
        }
        else if($count_1 == 1 && $username == "pang"){
           $_SESSION['login_user'] = $username;
           header("location: dashboard_teacher.php");
        }
     }
?>

<!DOCTYPE html>
<!-- Created By CodingNepal -->
<html lang="en">
<head>
 <meta charset="UTF-8">
 <title>Login</title>
 <link rel="stylesheet" href="login.css">

</head>

<script>

</script>

<body>

  <div class="topnav">
        <h3>e<span>Learning</span></h3>
  </div>

  <br><br><br><br><br><br><br><br>

 <div class="center">
 <div class="header">Login</div>
      <form action="#" method="POST">
          <input name="username"type="text" placeholder="Username">
          <input name="pw" type="password" placeholder="Password">
          <input name="sign_in" type="submit" value="Sign in">
          <a href="#">Forgot Password?</a>
       </form>
   </div>

</body>
</html>
