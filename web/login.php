
<!DOCTYPE html>
<html lang="en" >
<head>
  <meta charset="UTF-8">
  <title>Login</title>
  <link rel="stylesheet" href="../menu/menu.css">
  <link rel="stylesheet" href="login.css">
  <script type="text/javascript" src="/eel.js"></script>

</head>
<body>
  <?php include '../menu/menuuu.html'; ?>

<div class="login">
  <div class="form">
<h1><a href="main.html"><img src="../Logo_Mister_elec_2022_540x.jpg" alt="logo mr elec"></a></h1><br>

<!-- si le nom d utilisateur ou mot de passe est incorrecte afficher le message d error -->


 <!-- si une chose vide afficher lz message d error -->

    <form class="login-form" method="post" >
      <input type="text" placeholder="formule infixe" id="infixe" name="infixe" >
      <input type="text" placeholder="voila la formule postfixe"name="password" id="password">
      <input  type="button" name="login" onclick="show_alert()">Se connecter</button>
      
    </form>
  </div>
  <script>
    // console.log("Calling Python...");
    // eel.my_python_function(1, 2); // This calls the Python function that was decorated
    // 
    
    let infixxe=document.getElementById("infixe");
    let postfixe=document.getElementById("password");
    // alert(infixxe.value)
    // eel.infix_to_postfix(infixxe.value);

    // alert(jadir)
    // alert(infixxe)


    function show_alert() {
      eel.infix_to_postfix(infixxe.value)(function(result) {
      postfixe.value=result;
        alert(result);
      });
    //   if (!infixxe.value) 
    //   alert("kjbkjb");
    // alert(infixxe.value)  ;
    }
    
  </script>
</div>
</body>
</html>

