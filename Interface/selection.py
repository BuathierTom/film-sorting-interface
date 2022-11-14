# --- import
from msilib.schema import CheckBox
from typing_extensions import Self
from PyQt6.QtWidgets import QWidget, QFrame
from PyQt6.QtWidgets import QVBoxLayout, QHBoxLayout, QCheckBox, QGroupBox
from PyQt6.QtWidgets import QPushButton, QScrollArea
from PyQt6.QtCore import pyqtSignal
import annuaire
class selection (QWidget):
    
    filterChanged : pyqtSignal = pyqtSignal()

    

    def __init__(self : Self) -> None:
        super().__init__()
        
        # le Layout
        self.topLayout : QHBoxLayout = QHBoxLayout() 
        self.setLayout(self.topLayout)
    
        
        #Widget bouton gauche
        
        self.boutonGWidget : QWidget = QWidget()
        self.boutonGLayout : QVBoxLayout = QVBoxLayout()
        self.boutonGWidget.setLayout(self.boutonGLayout)
        self.select_film : QPushButton = QPushButton('select all')
        self.deselect_film : QPushButton = QPushButton('deselect all')
        
        #Widget bouton mid
        self.boutonMWidget : QWidget = QWidget()
        self.boutonMLayout : QVBoxLayout = QVBoxLayout()
        self.boutonMWidget.setLayout(self.boutonMLayout)
        self.select_genre : QPushButton = QPushButton ('select all')
        self.deselect_genre : QPushButton = QPushButton ('deselect all')

        #Widget bouton droite
        self.boutonDWidget : QWidget = QWidget()
        self.boutonDLayout : QVBoxLayout = QVBoxLayout()
        self.boutonDWidget.setLayout(self.boutonDLayout)
        self.select_licenses : QPushButton = QPushButton ('select all')
        self.deselect_licenses : QPushButton = QPushButton ('deselect all')
        
        # Widget Studio
        self.StudioWidget : QWidget = QWidget()
        self.StudioLayout : QVBoxLayout = QVBoxLayout() 
        self.StudioWidget.setLayout(self.StudioLayout)
        self.distriGroup : QGroupBox = QGroupBox()

        # Widget Genre
        self.GenreWidget : QWidget = QWidget()
        self.GenreLayout : QVBoxLayout = QVBoxLayout() 
        self.GenreWidget.setLayout(self.GenreLayout)
        self.genreGroup : QGroupBox = QGroupBox()

        # Widget Licence
        self.LicencesWidget : QWidget = QWidget()
        self.LicencesLayout : QVBoxLayout = QVBoxLayout() 
        self.LicencesWidget.setLayout(self.LicencesLayout)
        self.licenceGroup : QGroupBox = QGroupBox()



        #Widget de gauche
        self.gaucheWidget : QWidget = QWidget()
        self.gaucheLayout : QVBoxLayout = QVBoxLayout()
        self.gaucheWidget.setLayout(self.gaucheLayout)
        
        #Widget de milieu
        self.milieuWidget : QWidget = QWidget()
        self.milieuLayout : QVBoxLayout = QVBoxLayout()
        self.milieuWidget.setLayout(self.milieuLayout)
        
        #Widget de droite
        self.droiteWidget : QWidget = QWidget()
        self.droiteLayout : QVBoxLayout = QVBoxLayout()
        self.droiteWidget.setLayout(self.droiteLayout)
        
        
        
        #scroller distri
        self.distriScroller = QScrollArea()
        self.distriScroller.setWidgetResizable(True)
        
        #scroller genre
        self.genreScroller = QScrollArea()
        self.genreScroller.setWidgetResizable(True)
        
        #scroller licence
        self.licenceScroller = QScrollArea()
        self.licenceScroller.setWidgetResizable(True)
        self.licenceScroller.setMinimumHeight(600)
        
        
        #INSERTION

        self.boutonGLayout.addWidget(self.select_film)
        self.boutonGLayout.addWidget(self.deselect_film)
        self.boutonMLayout.addWidget(self.select_genre)
        self.boutonMLayout.addWidget(self.deselect_genre)
        self.boutonDLayout.addWidget(self.select_licenses)
        self.boutonDLayout.addWidget(self.deselect_licenses)
   

   
        self.gaucheLayout.addWidget(self.boutonGWidget)
        self.gaucheLayout.addWidget(self.distriScroller)
        
        self.milieuLayout.addWidget(self.boutonMWidget)
        self.milieuLayout.addWidget(self.genreScroller)
        
        self.droiteLayout.addWidget(self.boutonDWidget)
        # self.droiteLayout.addWidget(self.LicencesWidget)
        self.droiteLayout.addWidget(self.licenceScroller)
        self.droiteLayout.addStretch()
        
        
        self.topLayout.addWidget(self.gaucheWidget)
        self.topLayout.addWidget(self.milieuWidget)
        self.topLayout.addWidget(self.droiteWidget)
 

        
        self.buttonDistri  = []
        self.modele = annuaire.Annuaire('./Highest_Holywood_Grossing_Movies.json')
        studio = self.modele.getDistributor()
        for i in range(len(studio)):
            self.check : QCheckBox = QCheckBox(studio[i])
            self.buttonDistri.append(self.check)
            self.StudioLayout.addWidget(self.check)
            
            self.distriGroup.setLayout(self.StudioLayout)
            self.distriScroller.setWidget(self.distriGroup)
            
        self.buttonGenre  = []
        genre = self.modele.getGenre()
        for i in range(len(genre)):
            self.check : QCheckBox = QCheckBox(genre[i])
            self.buttonGenre.append(self.check)
            self.GenreLayout.addWidget(self.check)
            
            self.genreGroup.setLayout(self.GenreLayout)
            self.genreScroller.setWidget(self.genreGroup)
        
        self.buttonLi  = []
        licence = self.modele.getLicence()
        for i in range(len(licence)):
            self.check : QCheckBox = QCheckBox(licence[i])
            self.buttonLi.append(self.check)
            self.LicencesLayout.addWidget(self.check)
            
            self.licenceGroup.setLayout(self.LicencesLayout)
            self.licenceScroller.setWidget(self.licenceGroup)
        

        self.filterStudio : QPushButton = QPushButton ('filter')
        self.filterGenre : QPushButton = QPushButton ('filter')
        self.filterLicenses : QPushButton = QPushButton ('filter')
        
        self.gaucheLayout.addWidget(self.filterStudio)
        self.milieuLayout.addWidget(self.filterGenre)
        self.droiteLayout.addWidget(self.filterLicenses)

        self.select_film.clicked.connect(self.checkallFilm)
        self.deselect_film.clicked.connect(self.decheckallFilm)
        self.select_genre.clicked.connect(self.checkallGenre)
        self.deselect_genre.clicked.connect(self.decheckallGenre)
        self.select_licenses.clicked.connect(self.checkallLicen)
        self.deselect_licenses.clicked.connect(self.decheckallLicen)
        
        self.filterStudio.clicked.connect(self.DbFilter)
        self.filterGenre.clicked.connect(self.DbFilter)
        self.filterLicenses.clicked.connect(self.DbFilter)
        
        
        self.listeDistri : list[str] = self.modele.getDistributor()
        self.listeGenre : list[str] = self.modele.getGenre()
        self.listeLi : list[str] = self.modele.getLicence()
        
        # show() ! 
        self.show()

    
    def DbFilter(self):    
        self.filterChanged.emit()
            
    def checkallFilm(self):
        for i in self.buttonDistri:
            i.setChecked(True)
    
    def decheckallFilm(self):
        for i in self.buttonDistri:
            i.setChecked(False)
            
    
    def checkallGenre(self):
        for i in self.buttonGenre:
            i.setChecked(True)
            
    
    def decheckallGenre(self):
        for i in self.buttonGenre:
            i.setChecked(False)
    
    def checkallLicen(self):
        for i in self.buttonLi:
            i.setChecked(True)
    
    
    def decheckallLicen(self):
        for i in self.buttonLi:
            i.setChecked(False)
    
    
    def refreshDistributor(self):
        ListDistributor = []
        for index, i in enumerate(self.buttonDistri):
            if i.isChecked():
                ListDistributor.append(self.listeDistri[index])
        return ListDistributor
        
    
    def refreshGenre(self):
        ListGenre = []
        for index, i in enumerate(self.buttonGenre):
            if i.isChecked():
                ListGenre.append(self.listeGenre[index])
        return ListGenre

    
    def refreshLicence(self):
        ListLicence = []
        for index, i in enumerate(self.buttonLi):
            if i.isChecked():
                ListLicence.append(self.listeLi[index])
        return ListLicence
        

if __name__=="__main__":
    import sys
    from PyQt6.QtWidgets import QApplication
    app : QApplication = QApplication(sys.argv)
    sd : selection = selection()

    
    sys.exit(app.exec())












