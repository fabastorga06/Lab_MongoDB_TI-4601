from PyQt4 import QtGui

movie_spaces = ["name","genre","director_name","franchise","country","year","duration","company","actors"]
producer_spaces = ["name","genre","year"]
MOVIES_COLS = 9
PROD_COLS = 3
AVG_COLS = 2
ACTOR_AMT = 3

# JSON's to register movies & companies #
movie_json = {
                "name":"",
                "genre":"",
                "director_name":"",
                "franchise":"",
                "country":"",
                "year":"",
                "duration":"",
                "company":"",
                "actors":[{"name":""},{"name":""},{"name":""}]
             }

company_json = {
                "name":"",
                "year":"",
                "web_address":""
               }

# Serialize JSON data to array list
def serialize_table(pmovies, pspaces, pcols, isAct ):
    arr_movies = []
    for i in range ( len(pmovies) ):
        new_package = []
        for j in range( pcols ):
            if (isAct):
                if (pspaces[j] == "actors"):
                    _actors = ""
                    for z in range(ACTOR_AMT):
                        _actor = pmovies[i][pspaces[j]][z]["name"]
                        _actors += _actor + ", " 
                    new_package.append( _actors )
                else:
                    new_package.append( str(pmovies[i][pspaces[j]]) )
            else:    
                new_package.append( str(pmovies[i][pspaces[j]]) )   
        arr_movies.append( new_package )
    return arr_movies

# Fill table with the corresponding data
def fill_table( ptable, ptuples, pcols ):
    ptable.clearContents()
    _row = 0
    for i in ptuples:
        ptable.setRowCount(_row + 1)    
        for j in range (pcols):
            _item = QtGui.QTableWidgetItem(i[j]) 
            ptable.setItem( _row, j, _item )
        _row += 1


# Converts json to array list
def serialize_data(pfranchises, pkey):
    arr_franchise = []
    for i in range( len(pfranchises) ):
        arr_franchise.append( pfranchises[i][pkey] )
    return arr_franchise

def order_array(parray):
    new_arr = []
    for i in range( len(parray) ):
        if (parray[i] != ""):
            new_arr.append( parray[i] )
    return list( set(new_arr) )

