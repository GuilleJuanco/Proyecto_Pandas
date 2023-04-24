<!DOCTYPE html>
<html>
<head>
	<title>Proyecto_Pandas</title>
</head>
<body>
	<h1>Proyecto_Pandas</h1>
	<p>Este proyecto utiliza la librería Pandas de Python para realizar la limpieza y transformación de un conjunto de datos sobre ataques de tiburones, que se encuentra en un archivo CSV llamado "attacks.csv" en la carpeta src.</p>

	<h2>Requisitos</h2>
	<p>Para ejecutar el código de este proyecto se requieren las siguientes bibliotecas de Python:</p>
	<ul>
		<li>pandas</li>
		<li>numpy</li>
	</ul>

	<h2>Instalación</h2>
	<p>Para instalar las bibliotecas necesarias, ejecute el siguiente comando en la terminal:</p>
	<code>pip install pandas numpy</code>

	<h2>Ejecución</h2>
	<p>Para ejecutar el código de este proyecto, siga los siguientes pasos:</p>
	<ol>
		<li>Descargue o clone este repositorio en su computadora.</li>
		<li>Abra el archivo de Python que contiene el código en su IDE de Python preferido.</li>
		<li>Ejecute el archivo de Python.</li>
	</ol>
	<p>El archivo de Python leerá el archivo CSV "attacks.csv" ubicado en la carpeta src y limpiará y transformará los datos utilizando la biblioteca Pandas de Python.</p>
	<p>Los resultados de la limpieza y transformación de datos se guardarán en un nuevo archivo CSV llamado "attacks_clean.csv" en la carpeta src.</p>

	<h2>Funcionalidades</h2>
	<p>El archivo de Python que contiene el código realiza las siguientes tareas:</p>
	<ul>
		<li>Elimina las columnas innecesarias del conjunto de datos.</li>
		<li>Renombra las columnas restantes para que sean más descriptivas.</li>
		<li>Elimina las filas con valores faltantes o nulos.</li>
		<li>Agrega una columna llamada "timeofday" que clasifica los ataques en función de la hora del día en que ocurrieron.</li>
		<li>Agrega una columna llamada "ocean_sea" que clasifica los ataques en función de la región oceánica donde ocurrieron.</li>
		<li>Agrega una columna llamada "size" que clasifica los tiburones en función de su tamaño.</li>
		<li>Agrega una columna llamada "region" que clasifica los ataques en función de la región geográfica donde ocurrieron.</li>
		<li>Agrega una columna llamada "injury_outcome" que clasifica los ataques en función de la gravedad de las lesiones que causaron.</li>
		<li>Guarda los resultados de la limpieza y transformación de datos en un nuevo archivo CSV llamado "attacks_clean.csv" en la carpeta src.</li>
	</ul>

	<h2>Ánalisis de datos</h2>
	<p>El análisis de datos se realizará en una próxima actualización de este proyecto.</p>

	<h2>Contribución</h2>
	<p>Se aceptan contribuciones y sugerencias para mejorar este proyecto. Siéntase libre de
