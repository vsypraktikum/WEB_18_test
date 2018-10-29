<!DOCTYPE html>
<html>
	<head>
		<title>Praktikum2</title>
		<meta charset="UTF-8" />

		<style>

		</style>
		<script type="text/javascript" src="/sit.js"></script><!--<script type="text/javascript" src="sorttable.js"></script>-->

	</head>
	<body>

		<form id="idWTForm" action="/saveFirma" method="POST">	
			<input type="hidden" value="${key_s}" id="id_s" name="id_s" />
			<div>
				<label for="name">Name</label></div>
				<input type="text" value="${data_o['name']}" id="name" name="name" required />
			</div>
			<div>
				<label for="branche">Branche</label>
				<input type="text" value="${data_o['branche']}" id="branche" name="branche" required />
			</div>
			<div>
				<label for="schwerpunkt">Tätigkeitsschwerpunkt</label>
				<input type="text" value="${data_o['schwerpunkt']}" id="schwerpunkt" name="schwerpunkt" required />
			</div>
			<div>
				<label for="sitz">Sitz</label>
				<input type="text" value="${data_o['sitz']}" id="sitz" name="sitz" required />
			</div>
			<div>
				<label for="mitarbeiteranzahl">Mitarbeiteranzahl</label>
				<input type="text" value="${data_o['mitarbeiteranzahl']}" id="mitarbeiteranzahl" name="mitarbeiteranzahl" required />
			</div>
			<div>
				<input type="submit" id="saveButton"  value="Speichern" />
				<a href="/"><input type="submit" value="Abbrechen"  /></a>
			</div>
		</form>
	</body>
</html>
