<!DOCTYPE html>
<html>
	<head>
		<title>Lehrerliste</title>
		<meta charset="UTF-8" />
		<link rel="stylesheet" href="/style.css">
		<style>
			@import "/style.css";

		</style>
		<script type="text/javascript" src="/ppm.js"></script>
	</head>
	<body onload="StandardListe_INIT()">
	<div class="kopf"></div>
		<div><a href="/">Zurück</a></div>
		<div><a href="/addLehrer">Neu</a></div>
		<table>
			<tr>
				<th>ID</th><th>Titel</th><th>Name</th><th>Vorname</th><th>Lehrgebiet</th>
			</tr>
			
			% for key_s in data_o:
				<tr id="${key_s}" class="noMark" onClick="markRow(${key_s});">
					<td>${key_s}</td>
					<td>${data_o[key_s]['titel']}</td>
					<td>${data_o[key_s]['name']}</td>
					<td>${data_o[key_s]['vorname']}</td>
					<td>${data_o[key_s]['lehrgebiet']}</td>
				</tr>
			% endfor
		
		</table>
		<div id="/deleteLehrer/" class="likeabutton">Löschen</div>
		<div id="/editLehrer/" class="likeabutton">Bearbeiten</div>
	</body>
</html>