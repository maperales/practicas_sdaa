<html>
	<?php
//	echo "Empezando...";
//	print $_REQUEST[Estado];
	if ($_REQUEST[Estado]=="On"){
		echo "Encendiendo";
		exec("sudo python led_on.py");
//		echo "Se ha encendido el led";
		}
	if ($_REQUEST[Estado]=="Off"){
		echo "Apagando";
		exec("sudo python led_off.py");
//		echo "Se ha apagado el led";
		}
	echo "<br/>";
        ?>

<a href="cambia_led.html"> Volver </a>
</html>
