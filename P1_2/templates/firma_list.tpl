<!DOCTYPE html>
<html>
	<head>
		<title>Studentliste</title>
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
		<div><a href="/addFirma">Neu</a></div>
		<table> 
		
			<tr>
				<th>Firma-ID</th><th>Name.</th><th>Branche</th><th>Taetigkeitsschwerpunkt</th><th>Sitz</th><th>Anzahl Mitarbeiter</th>
			</tr>
			
			% for key_s in data_o:
				<tr id="${key_s}" class="noMark" onClick="markRow(${key_s});">
					<td>${key_s}</td>
					<td>${data_o[key_s]['name']}</td>
					<td>${data_o[key_s]['branche']}</td>
					<td>${data_o[key_s]['schwerpunkt']}</td>
					<td>${data_o[key_s]['sitz']}</td>
					<td>${data_o[key_s]['mitarbeiteranzahl']}</td>
				</tr>
			% endfor
		</table>
		
		<div id="/deleteFirma/" class="likeabutton">Löschen</div>
		<div id="/editFirma/" class="likeabutton">Bearbeiten</div>
	</body>
</html>