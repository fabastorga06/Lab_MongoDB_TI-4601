use LAB_DB

/* create database collections */
db.createCollection("movies")
db.createCollection("companies")

/*****************       database population        ****************************/
/* movies */
db.movies.insert(
					{
					  "name":"Pulp Fiction",
					  "genre":"Crime",
					  "director_name":"Quentin Tarantino",
					  "franchise":"",
					  "country":"USA",
					  "year":NumberInt(1994), 
					  "duration":154, 
					  "company":"Miramax", 
					  "actors":[{"name":"John Travolta"},{"name":"Samuel L. Jackson"},{"name":"Uma Thurman"}]
					}
							 )
db.movies.insert(
					{
						"name":"Rocky",
						"genre":"Drama & Sport",
						"director_name":"John G. Avildsen",
						"franchise":"Rocky Franchise",
						"country":"USA",
						"year":NumberInt(1976), 
						"duration":120, 
						"company":"Metro Goldwyn Mayer", 
						"actors":[{"name":"Sylvester Stallone"},{"name":"Talia Shire"},{"name":"Burgess Meredith"}]
					}
			)
db.movies.insert(
	{
					"name":"Rocky II",
					"genre":"Drama & Sport",
					"director_name":"Sylvester Stallone",
					"franchise":"Rocky Franchise",
					"country":"USA",
					"year":NumberInt(1979), 
					"duration":119, 
					"company":"Metro Goldwyn Mayer", 
					"actors":[{"name":"Sylvester Stallone"},{"name":"Talia Shire"},{"name":"Burgess Meredith"}]
				}
		)
	
db.movies.insert(
{
						"name":"Rocky III",
						"genre":"Drama & Sport",
						"director_name":"Sylvester Stallone",
						"franchise":"Rocky Franchise",
						"country":"USA",
						"year":NumberInt(1982), 
						"duration":99, 
						"company":"Metro Goldwyn Mayer", 
						"actors":[{"name":"Sylvester Stallone"},{"name":"Talia Shire"},{"name":"Burgess Meredith"}]
					}
			)
	
db.movies.insert(
	{
							"name":"Rocky V",
							"genre":"Drama & Sport",
							"director_name":"John G. Avildsen",
							"franchise":"Rocky Franchise",
							"country":"USA",
							"year":NumberInt(1990), 
							"duration":104, 
							"company":"Metro Goldwyn Mayer", 
							"actors":[{"name":"Sylvester Stallone"},{"name":"Talia Shire"},{"name":"Burt Young "}]
						}
				)
db.movies.insert(
	{
							"name":"Star Trek II: The Wrath of Khan",
							"genre":"Adventure",
							"director_name":"Nicholas Meyer",
							"franchise":"Star Trek Franchise",
							"country":"USA",
							"year":NumberInt(1982), 
							"duration":113, 
							"company":"StarTree Productions", 
							"actors":[{"name":"William Shatner"},{"name":"Leonard Nimoy"},{"name":"DeForest Kelley"}]
						}
				)	

db.movies.insert(
	{
							"name":"Star Trek III: The Search for Spock",
							"genre":"Adventure",
							"director_name":"Leonard Nimoy",
							"franchise":"Star Trek Franchise",
							"country":"USA",
							"year":NumberInt(1984), 
							"duration":105, 
							"company":"StarTree Productions", 
							"actors":[{"name":"William Shatner"},{"name":"Leonard Nimoy"},{"name":"DeForest Kelley"}]
						}
				)
db.movies.insert(
	{
							"name":"Star Trek IV: The Voyage Home",
							"genre":"Adventure",
							"director_name":"Leonard Nimoy",
							"franchise":"Star Trek Franchise",
							"country":"USA",
							"year":NumberInt(1986), 
							"duration":119, 
							"company":"StarTree Productions", 
							"actors":[{"name":"William Shatner"},{"name":"Leonard Nimoy"},{"name":"DeForest Kelley"}]
						}
				)		
		
db.movies.insert(
	{
							"name":"X-Men",
							"genre":"Action & Sci-Fi",
							"director_name":"Bryan Singer",
							"franchise":"X-Men Franchise",
							"country":"USA",
							"year":NumberInt(2000), 
							"duration":104, 
							"company":"Marvel Studios", 
							"actors":[{"name":"Patrick Stewart"},{"name":"Hugh Jackman"},{"name":"Ian McKellen"}]
						}
				)	
db.movies.insert(
	{
							"name":"X-Men 2",
							"genre":"Action & Sci-Fi",
							"director_name":"Bryan Singer",
							"franchise":"X-Men Franchise",
							"country":"USA",
							"year":NumberInt(2003), 
							"duration":134, 
							"company":"Marvel Studios", 
							"actors":[{"name":"Patrick Stewart"},{"name":"Hugh Jackman"},{"name":"Ian McKellen"}]
						}
				)	

db.movies.insert(
	{
							"name":"X-Men: The Last Stand",
							"genre":"Action & Sci-Fi",
							"director_name":"Brett Ratner",
							"franchise":"X-Men Franchise",
							"country":"USA",
							"year":NumberInt(2006), 
							"duration":104, 
							"company":"Marvel Studios", 
							"actors":[{"name":"Patrick Stewart"},{"name":"Hugh Jackman"},{"name":"Halle Berry"}]
						}
				)	

db.movies.insert(
	{
							"name":"X-Men: First Class",
							"genre":"Action & Sci-Fi",
							"director_name":"Matthew Vaughn",
							"franchise":"X-Men Franchise",
							"country":"USA",
							"year":NumberInt(2011), 
							"duration":131, 
							"company":"Marvel Studios", 
							"actors":[{"name":"James McAvoy"},{"name":"Michael Fassbender"},{"name":"Jennifer Lawrence"}]
						}
				)	

db.movies.insert(
	{
							"name":"X-Men: Days of Future Past",
							"genre":"Action & Sci-Fi",
							"director_name":"Bryan Singer",
							"franchise":"X-Men Franchise",
							"country":"USA",
							"year":NumberInt(2014), 
							"duration":132, 
							"company":"Marvel Studios", 
							"actors":[{"name":"Patrick Stewart"},{"name":"Hugh Jackman"},{"name":"Ian McKellen"}]
						}
				)	
	
db.movies.insert(
	{
							"name":"Shrek",
							"genre":"Animation",
							"director_name":"Andrew Adamson",
							"franchise":"Shrek Franchise",
							"country":"USA",
							"year":NumberInt(2001), 
							"duration":90, 
							"company":"DreamWorks", 
							"actors":[{"name":"Mike Myers"},{"name":"Eddie Murphy"},{"name":"Cameron Diaz"}]
						}
				)	

db.movies.insert(
	{
							"name":"Shrek 2",
							"genre":"Animation",
							"director_name":"Andrew Adamson",
							"franchise":"Shrek Franchise",
							"country":"USA",
							"year":NumberInt(2004), 
							"duration":93, 
							"company":"DreamWorks", 
							"actors":[{"name":"Mike Myers"},{"name":"Eddie Murphy"},{"name":"Cameron Diaz"}]
						}
				)	
	
db.movies.insert(
	{
							"name":"Shrek The Third",
							"genre":"Animation",
							"director_name":"Chris Miller",
							"franchise":"Shrek Franchise",
							"country":"USA",
							"year":NumberInt(2007), 
							"duration":93, 
							"company":"DreamWorks", 
							"actors":[{"name":"Mike Myers"},{"name":"Eddie Murphy"},{"name":"Cameron Diaz"}]
						}
				)	

db.movies.insert(
	{
							"name":"Shrek Forever After",
							"genre":"Animation",
							"director_name":"Mike Mitchell",
							"franchise":"Shrek Franchise",
							"country":"USA",
							"year":NumberInt(2010), 
							"duration":93, 
							"company":"DreamWorks", 
							"actors":[{"name":"Mike Myers"},{"name":"Eddie Murphy"},{"name":"Cameron Diaz"}]
						}
				)	

db.movies.insert(
	{
							"name":"Madagascar",
							"genre":"Animation",
							"director_name":"Eric Darnell",
							"franchise":"Madagascar Franchise",
							"country":"USA",
							"year":NumberInt(2005), 
							"duration":86, 
							"company":"DreamWorks", 
							"actors":[{"name":"Chris Rock"},{"name":"Ben Stiller"},{"name":"David Schwimmer"}]
						}
				)	

db.movies.insert(
	{
							"name":"Madagascar: Escape 2 Africa",
							"genre":"Animation",
							"director_name":"Eric Darnell",
							"franchise":"Madagascar Franchise",
							"country":"USA",
							"year":NumberInt(2008), 
							"duration":89, 
							"company":"DreamWorks", 
							"actors":[{"name":"Chris Rock"},{"name":"Ben Stiller"},{"name":"David Schwimmer"}]
						}
				)	
			
db.movies.insert(
	{
							"name":"Madagascar 3: Europe's Most Wanted",
							"genre":"Animation",
							"director_name":"Eric Darnell",
							"franchise":"Madagascar Franchise",
							"country":"USA",
							"year":NumberInt(2012), 
							"duration":93, 
							"company":"DreamWorks", 
							"actors":[{"name":"Chris Rock"},{"name":"Ben Stiller"},{"name":"Jada Pinkett Smith"}]
						}
				)							

db.movies.insert(
	{
							"name":"Ant-Man",
							"genre":"Action",
							"director_name":"Peyton Reed",
							"franchise":"",
							"country":"USA",
							"year":NumberInt(2015), 
							"duration":117, 
							"company":"Marvel Studios", 
							"actors":[{"name":"Paul Rudd"},{"name":"Michael Douglas"},{"name":"Corey Stoll"}]
						}
				)				
				
db.movies.insert(
	{
							"name":"Hereditary",
							"genre":"Horror",
							"director_name":"Ari Aster",
							"franchise":"",
							"country":"USA",
							"year":NumberInt(2018), 
							"duration":127, 
							"company":"A24", 
							"actors":[{"name":"Toni Collette"},{"name":"Milly Shapiro"},{"name":"Gabriel Byrne"}]
						}
				)	

db.movies.insert(
	{
							"name":"Enter the Void",
							"genre":"Drama",
							"director_name":"Gaspar Noé",
							"franchise":"",
							"country":"France",
							"year":NumberInt(2009), 
							"duration":161, 
							"company":"Film France", 
							"actors":[{"name":"Nathaniel Brown"},{"name":"Paz de la Huerta"},{"name":"Cyril Roy"}]
						}
				)	

db.movies.insert(
	{
							"name":"Amélie",
							"genre":"Romance",
							"director_name":"Jean-Pierre Jeunet",
							"franchise":"",
							"country":"France",
							"year":NumberInt(2009), 
							"duration":122, 
							"company":"Film France", 
							"actors":[{"name":"Audrey Tautou"},{"name":"Mathieu Kassovitz"},{"name":"Rufus"}]
						}
				)	

db.movies.insert(
	{
							"name":"Contratiempo",
							"genre":"Crime",
							"director_name":"Oriol Paulo",
							"franchise":"",
							"country":"Spain",
							"year":NumberInt(2016), 
							"duration":106, 
							"company":"Antena 3 Films", 
							"actors":[{"name":"Mario Casas"},{"name":"Ana Wagener"},{"name":"Jose Coronado"}]
						}
				)	

db.movies.insert(
	{
							"name":"City of God",
							"genre":"Crime",
							"director_name":"Fernando Meirelles",
							"franchise":"",
							"country":"Brasil",
							"year":NumberInt(2002), 
							"duration":130, 
							"company":"02 Filmes", 
							"actors":[{"name":"Alexandre Rodrigues"},{"name":"Leandro Firmino"},{"name":"Matheus Nachtergaele"}]
						}
				)	

db.movies.insert(
	{
							"name":"Trainspotting",
							"genre":"Drama",
							"director_name":"Danny Boyle",
							"franchise":"",
							"country":"England",
							"year":NumberInt(1996), 
							"duration":94, 
							"company":"UK Films", 
							"actors":[{"name":"Ewan McGregor"},{"name":"Ewen Bremner"},{"name":"Jonny Lee Miller"}]
						}
				)	

db.movies.insert(
	{
							"name":"A Clockwork Orange",
							"genre":"Crime",
							"director_name":"Stanley Kubrick",
							"franchise":"",
							"country":"England",
							"year":NumberInt(1971), 
							"duration":136, 
							"company":"UK Films", 
							"actors":[{"name":"Malcolm McDowell"},{"name":"Patrick Magee"},{"name":"Michael Bates"}]
						}
				)	

db.movies.insert(
	{
							"name":"Dr. Strangelove or: How I Learned to Stop Worrying and Love the Bomb",
							"genre":"Comedy",
							"director_name":"Stanley Kubrick",
							"franchise":"",
							"country":"England",
							"year":NumberInt(1964), 
							"duration":95, 
							"company":"UK Films", 
							"actors":[{"name":"Peter Sellers"},{"name":"George C. Scott"},{"name":"Sterling Hayden"}]
						}
				)	

/*********************************************************************************************/
/* companies */
db.companies.insert(
						{
						  "name":"Miramax",
						  "year":"1985",
						  "web_address":"www.miramax.com"	  
						}
					 )

db.companies.insert(
					{
						"name":"Marvel Studios",
						"year":"1993",
						"web_address":"www.marvel.com"	  
					}
				)

db.companies.insert(
						{
							"name":"Metro Goldwyn Mayer",
							"year":"1924",
							"web_address":"www.mgm.com"	  
						}
)
db.companies.insert(
	{
		"name":"StarTree Productions",
		"year":"1970",
		"web_address":"www.startreeproductions.com"	  
	}
)

db.companies.insert(
	{
		"name":"DreamWorks",
		"year":"1994",
		"web_address":"www.dreamworksanimation.com"	  
	}
)

db.companies.insert(
	{
		"name":"A24",
		"year":"2012",
		"web_address":"www.a24films.com"	  
	}
)

db.companies.insert(
	{
		"name":"Film France",
		"year":"2000",
		"web_address":"www.filmfrance.net"	  
	}
)

db.companies.insert(
	{
		"name":"Antena 3 Films",
		"year":"1989",
		"web_address":"www.antena3.com"	  
	}
)

db.companies.insert(
	{
		"name":"02 Filmes",
		"year":"2001",
		"web_address":"www.02filmes.com"	  
	}
)

db.companies.insert(
	{
		"name":"UK Films",
		"year":"1978",
		"web_address":"www.ukfilms.com"	  
	}
)
