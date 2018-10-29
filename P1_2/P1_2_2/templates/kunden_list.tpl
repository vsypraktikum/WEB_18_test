<!DOCTYPE html>
<html>
	<head>
		<title>Kunde_liste</title>
		<meta charset="UTF-8" />
		<link rel="stylesheet" type="text/css" href="/style.css">
		<style>
			@import "/style.css";

		</style>
		<script type="text/javascript" src="/ppm.js"></script>
	</head>
	<body onload="StandardListe_INIT()">
	<div class="kopf"></div>
		<div><a href="/">Zurück</a></div>
		<div><a href="/addStudent">Neu</a></div>
		<table>
			<tr>
				<th>Bezeichnung</th><th>Ansprechpartner</th><th>Nummer</th><th>Ort</th><th>ID</th>
			</tr>
			% for key_s in data_o:
				<tr id="${key_s}" class="noMark" onClick="markRow(${key_s});">
					<td >${data_o[key_s]['bezeichnung']}</td>
					<td>${data_o[key_s]['ap']}</td>
					<td>${data_o[key_s]['nummer']}</td>
					<td>${data_o[key_s]['ort']}</td>
					<td>${data_o[key_s]['id']}</td>

				</tr>
			% endfor
		</table>
		<div id="/deleteStudent/" class="likeabutton">Löschen</div>
		<div id="/editStudent/" class="likeabutton">Bearbeiten</div>
	</body>
</html>
