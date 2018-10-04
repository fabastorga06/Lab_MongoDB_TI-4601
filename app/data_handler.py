from PyQt4 import QtGui

movie_spaces = ["name","genre","director_name","franchise","country","year","duration","company","actors"]
producer_spaces = ["name","genre","year"]
MOVIES_COLS = 9
PROD_COLS = 3
AVG_COLS = 2

# Serialize JSON data to array list
def serialize_table(pmovies, pspaces, pcols, isAct ):
    arr_movies = []
    for i in range ( len(pmovies) ):
        new_package = []
        for j in range( pcols ):
            if (isAct):
                if (pspaces[j] == "actors"):
                    _actors = ""
                    for z in range(3):
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