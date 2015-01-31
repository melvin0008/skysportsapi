Unofficial Skysports Api
============

Unofficial REST API for [SkySports](www.skysports.com) 


Usage
==========

**Base URL:** [https://skysportsapi.herokuapp.com/](https://skysportsapi.herokuapp.com/)

**Output:** JSON


Three Main REST operations
====================
	
###Get latest News 
####GET `/sky/getlatest/v1.0/`

###Get individual Sport news 
#### GET `/sky/getnews/< name_of_sport >/v1.0/` 
		
			for eg. 
			*cricket => "/sky/getnews/cricket/v1.0/" 
			*tennis => "/sky/getnews/tennis/v1.0/" 
			*golf => "/sky/getnews/golf/v1.0/" 		
			*football => "/sky/getnews/football/v1.0/" 	 

**Parameters:**

| Name | Type | Description |
| ---- | ---- | ----------- |
| `name_of_sport` | string | Name of the Sport |
		 
###Get Team News for your team 
#### GET `/sky/< sport >/getteamnews/< team >/v1.0/` 
		 
			for eg. 
			*cricket and india => "/sky/cricket/getteamnews/india/v1.0/" 
			*football and liverpool  => "/sky/football/getteamnews/liverpool/v1.0/" 
		 
**Parameters:**

| Name | Type | Description |
| ---- | :----: | :-----------: |
| `sport` | string | Name of the Sport |
| `team` | string | Name of the Team |

	 
#####For other sports please replace football with one of these
		 
######Sports Supported are: Football Cricket Golf Tennis Rugby-League Rugby-Union Boxing Horse-Racing 
			* cricket => "/sky/getnews/cricket/v1.0/" 
			* tennis => "/sky/getnews/tennis/v1.0/" 
			* golf => "/sky/getnews/golf/v1.0/" 		
			* horse-racing => "/sky/getnews/horse-racing/v1.0/" 
			* football => "/sky/getnews/football/v1.0/" 
			* rugby-league => "/sky/getnews/rugby-league/v1.0/" 
			* rugby-union => "/sky/getnews/rugby-union/v1.0/" 
			* boxing => "/sky/getnews/boxing/v1.0/" 
		 
	 
**If the Team Name contains spaces replace with '-' for example**
######For Borussia Dortmund news => /sky/football/getteamnews/borussia-dortmund/v1.0   

####List Of teams included in Football:
		 
+ All English Premiership Teams   
+ All Championship Teams   
+ All Spanish La Liga Teams   
+ All Serie A Teams   
+ All Ligue 1 Teams   
+ All Bundesliga Teams   
+ All Scottish Teams   
+ International Teams    
		 
	 
	 

####List of Cricket Teams
* All Indian Premier League Teams 
* Internationals 
<!--
     Afghanistan 
     Australia 
     Bangladesh 
     England 
     Holland 

     India 
     Ireland 
     Kenya 
     New Zealand 
     Pakistan 

     Scotland 
     South Africa 
     Sri Lanka 
     West Indies 
     Zimbabwe 
-->
* Domestic
<!--
     Derbyshire 
     Durham 
     Essex 
     Glamorgan 
     Gloucestershire 
     Hampshire 

     Kent 
     Lancashire 
     Leicestershire 
     Middlesex 
     Northamptonshire 
     Nottinghamshire 

     Somerset 
     Surrey 
     Sussex -->
 
      
	 
####List of Rugby Union Teams
 
+ British and Irish Lions 
+ All Six Nations i.e England Wales France Ireland Italy Scotland 
+ All teams of Aviva Championship 
+ All teams of Rugb Championship 
+ Guiness Pro 12 Teams 
+ All Top 14 Teams 
 
 
####List Of Rugby Teams
+ All Super League Teams 
+ All World Cup Teams      
	 
 
More Sports and leagues coming
	
