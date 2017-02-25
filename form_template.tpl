<!DOCTYPE html>
<head>
	<title>URL to Interact</title>
</head>
<body>
	<center>
	<h3>Convert URL to Interact Link</h2>
	<form action="/" method="post">
		<p>URL:</p>
		<p><textarea rows="2" cols="100" name="url"></textarea></p>
		<p><input value="Convert to interact link!" type="submit"/></p>
	</form>
	%if show_url and not error and not blank:
	<p>Your interact URL is: </p>
	{{url}}
	<textarea rows="2" cols="100">{{url}}</textarea>
	%if not show_url and error and not blank:
	<p>{{error}}</p>
	</center>
</body>