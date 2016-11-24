<html>

<?php 
	$texto=$_GET['texto'];
	echo "Texto enviado: "; 
	echo "</br>";
	echo $texto;
	$fp=fopen("mensaje.txt","w");
	fputs($fp,$texto);
	fclose($fp);
	exec("sudo python lee_fichero.py");
?>

<a href="/manda_txt.html">Volver </a>
</html>

