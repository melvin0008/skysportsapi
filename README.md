skysportsapi
============

Unofficial Skysports Api

https://skysportsapi.herokuapp.com/


<!doctype html>
<html>
<head>
	<title>Unofficial Skysports Api</title>
</head>
<body>
	<p>
	Three Api's :
	<ul>
		<li>Get latest News : use "/sky/getlatest/v1.0/"</li>
		<li> Get individual Sport news "/sky/getnews/< name_of_sport >/v1.0/" </li>
		<ul>
			<li>for eg. 
			<li>cricket => "/sky/getnews/cricket/v1.0/"</li>
			<li>tennis => "/sky/getnews/tennis/v1.0/"</li>
			<li>golf => "/sky/getnews/golf/v1.0/"</li>		
			<li>football => "/sky/getnews/football/v1.0/"</li>
			 
		</ul>
		<li> Get Team News for your team "/sky/< name of sport >/getteamnews/< name of team >/v1.0"</li>
		<ul>
			<li>for eg. 
			<li>cricket and india => "/sky/cricket/getteamnews/india/v1.0/"</li>
			<li>football and liverpool  => "/sky/football/getteamnews/liverpool/v1.0/"</li>
		</ul>
	</ul>
	<p>For other sports please replace football with one of these
		<ul>
			Sports Supported are: Football Cricket Golf Tennis Rugby-League Rugby-Union Boxing Horse-Racing 
			<li>cricket => "/sky/getnews/cricket/v1.0/"</li>
			<li>tennis => "/sky/getnews/tennis/v1.0/"</li>
			<li>golf => "/sky/getnews/golf/v1.0/"</li>		
			<li>horse-racing => "/sky/getnews/horse-racing/v1.0/"</li>
			<li>football => "/sky/getnews/football/v1.0/"</li>
			<li>rugby-league => "/sky/getnews/rugby-league/v1.0/"</li>
			<li>rugby-union => "/sky/getnews/rugby-union/v1.0/"</li>
			<li>boxing => "/sky/getnews/boxing/v1.0/"</li>
		</ul>
	</p>
	If the Team Name contains spaces replace with '-' for example
	For Borussia Dortmund news => /sky/football/getteamnews/borussia-dortmund/v1.0
	<p>List Of teams included in Football:
		<ul>
			<li>All English Premiership Teams</li>
			<li>All Championship Teams</li>
		<li>All Spanish La Liga Teams</li>
		<li>All Serie A Teams</li>
		<li>All Ligue 1 Teams</li>
		<li>All Bundesliga Teams</li>
		<li>All Scottish Teams</li>
		<li>International Teams </li>
		
		</ul>
		
	</p>
	<p>

List of Cricket Teams
<ul> <li>All Indian Premier League Teams</li>

<li>Internationals</li>
<!--
    <li>Afghanistan</li>
    <li>Australia</li>
    <li>Bangladesh</li>
    <li>England</li>
    <li>Holland</li>

    <li>India</li>
    <li>Ireland</li>
    <li>Kenya</li>
    <li>New Zealand</li>
    <li>Pakistan</li>

    <li>Scotland</li>
    <li>South Africa</li>
    <li>Sri Lanka</li>
    <li>West Indies</li>
    <li>Zimbabwe</li>
-->
<li>Domestic
<!--
    <li>Derbyshire</li>
    <li>Durham</li>
    <li>Essex</li>
    <li>Glamorgan</li>
    <li>Gloucestershire</li>
    <li>Hampshire</li>

    <li>Kent</li>
    <li>Lancashire</li>
    <li>Leicestershire</li>
    <li>Middlesex</li>
    <li>Northamptonshire</li>
    <li>Nottinghamshire</li>

    <li>Somerset</li>
    <li>Surrey</li>
    <li>Sussex</li>-->
</li>
    </ul> 
	</p>
</p>
<p>List of Rugby Union Teams
<ul>
	<li>British and Irish Lions</li>
	<li>All Six Nations i.e England Wales France Ireland Italy Scotland</li>
	<li>All teams of Aviva Championship</li>
	<li>All teams of Rugb Championship</li>
	<li>Guiness Pro 12 Teams</li>
	<li>All Top 14 Teams</li>
</ul>
</p>
<p> List Of Rugby Teams
	<ul>
		<li>All Super League Teams</li>
		<li>All World Cup Teams</li>
	</ul>
</p>
	<p>More Sports and leagues coming</p>
	


</body>

</html>