# --- import
from ctypes import Union
from PyQt6.QtWidgets import QWidget, QHBoxLayout, QApplication
from typing import Union
import annuaire
from FilmView import FilmView
from selection import selection
import FigureWidget as fi

# Ouis je sais ils font peur


# --> class
class main(QWidget):
    
    def __init__(self):
        super().__init__()
        #----------------------------On importe les classes----------------------------
        self.topLayout: QHBoxLayout = QHBoxLayout()
        self.select : selection = selection()
        self.topLayout.addWidget(self.select)
        self.FilmV : FilmView = FilmView({})
        self.topLayout.addWidget(self.FilmV)
        #--------------------------Le graphe---------------------------------------------
        self.graphe = QHBoxLayout()
        self.topLayout.addLayout(self.graphe)
        
        self.figure = fi.FigureWidget()
        self.topLayout.addWidget(self.figure)
        
        self.figure.scatter([1940,1960,1980,2000,2020], [0.0, 0.5, 1.0, 1.5, 2.0], 3, True, 1)
        
        self.figure.show()  
        
        
        
        
        
        
        self.setLayout(self.topLayout)
        self.modele = annuaire.Annuaire('./Highest_Holywood_Grossing_Movies.json')
        self.FilmV.update(self.modele.getFilm(),self.modele.getGenre(),self.modele.getDistributor(),self.modele.getLicence())  # type: ignore
        
        self.vueFilm = self.FilmV
        p = self.modele.getFilm(),self.modele.getGenre(),self.modele.getDistributor(),self.modele.getLicence()
        # if isinstance(p, film.Film): 
        #     self.vueFilm.update(p)
        self.vueFilm.next.connect(self.fnext)
        self.vueFilm.previous.connect(self.fprevious)
        
        self.select.filterChanged.connect(self.filterz)
        
        self.show()
        
    
    def filterz(self):
        self.upd = []
        # Recuperation des infos checks
        self.DistriCheck = self.select.refreshDistributor()
        self.GenreCheck = self.select.refreshGenre()
        self.LicenceCheck = self.select.refreshLicence()
        print(self.DistriCheck, self.GenreCheck, self.LicenceCheck)
        #Comparaison avec la liste Film
        
        for i in self.modele.listFilm:
            print(self.modele.TransNbrDistrib(i.distributor))
            if self.modele.TransNbrDistrib(i.distributor) in self.DistriCheck:
                # if i.genre in self.GenreCheck:
                    if self.modele.TransNbrLicence(i.license) in self.LicenceCheck:
                        self.upd.append(i)
                
        
        
    
    def fnext(self) -> None:
        self.modele.next()
        self.vueFilm.update(self.modele.getFilm(),self.modele.getGenre(),self.modele.getDistributor(),self.modele.getLicence())  # type: ignore
         
    def fprevious(self) -> None:
        self.modele.previous()
        self.vueFilm.update(self.modele.getFilm(),self.modele.getGenre(),self.modele.getDistributor(),self.modele.getLicence())   # type: ignore
        
    @property
    def current(self) -> Union[int,None] : 
        return self.__current
    @current.setter
    def current(self, index :Union[int,None]) -> None : 
        self.__current = index


# --- main: kind of unit test
if __name__ == "__main__" :
    import sys
    from PyQt6.QtWidgets import QApplication
    import annuaire
    
    app = QApplication(sys.argv)
    Mainview=main()
    sys.exit(app.exec())