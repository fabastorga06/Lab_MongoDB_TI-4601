use LAB_DB

/* create database collections */
db.createCollection("movies")
db.createCollection("companies")

/* database population */
db.movies.insert(
					{
					  "name":"Pulp Fiction",
					  "genre":"Crime",
					  "director_name":"Quentin Tarantino",
					  "franchise":"",
					  "country":"USA",
					  "year":"1994", 
					  "duration":"2h34m", 
					  "company":"Miramax", 
					  "actors":[{"name":"John Travolta"},{"name":"Samuel L. Jackson"},{"name":"Uma Thurman"}]
					}

               )
					  
db.companies.insert(
						{
						  "name":"Miramax",
						  "year":"1985",
						  "web_address":"www.miramax.com"	  
						}
				   )

/* Select */
db.movies.find( {}, {"name":1,"country":1} ) // Columns

/* Or sentence */
db.movies.find(
	{
		$or: [ {"name":"Pulp Fiction"}, {"country":"USA"} ]
	}
)

/* Update */
db.movies.update(
	{"_id":"5bb01d126d5ae3810a3f0e54"}, //pulp fiction ID
	{ $set: {"name":"Reservoir Dogs"} }
)


show collections

