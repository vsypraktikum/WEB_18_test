<!DOCTYPE html>
<html>
	<head>
		<title>Kunden_form</title>
		<meta charset="UTF-8" />

		<style>

		</style>
		<script type="text/javascript" src="/sit.js"></script><!--<script type="text/javascript" src="sorttable.js"></script>-->

	</head>
	<body>
	
		<form id="idWTForm" action="/saveStudent" method="POST">
		
			<input type="hidden" value="${key_s}" id="id_s" name="id_s" />
			<div>
				<label for="bezeichnung">Bezeichnung</label></div>
				<input type="text" value="${data_o['bezeichnung']}" id="bezeichnung" name="bezeichnung" required />
			</div>
			<div>
				<label for="ap">Ansprechpartner</label>
				<input type="text" value="${data_o['ap']}" id="ap" name="ap" required />
			</div>
			<div>
				<label for="nummer">Nummer</label>
				<input type="text" value="${data_o['nummer']}" id="nummer" name="nummer" required />
			</div>
			<div>
				<label for="ort">Ort</label>
				<input type="text" value="${data_o['ort']}" id="ort" name="ort" required />
			</div>
			<div>
				<label for="id">ID</label>
				<input type="text" value="${data_o['id']}" id="id" name="id" required />
			</div>
			<div>
				<input type="submit" id="saveButton"  value="Speichern" />
				<a href="/"><input type="submit" value="Abbrechen"  /></a>
			</div>
		</form>
	</body>
</html>
