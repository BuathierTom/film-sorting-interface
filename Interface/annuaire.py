# --- import
import json, copy, os
from typing import Union
import film

# -------------------------------------------------
# --- class Annuaire ------------------------------
# -------------------------------------------------
class Annuaire:
    # constructor
    
    def __init__(self, jsonFile : (Union[str,None]) = None) -> None:
        # attributs
        self.__listFilm : list[film.Film] = []
        self.__current : (Union[int,None]) = None
        self.__genres : list[str] = []
        self.__distributors : list[str] = []
        self.__licenses: list[str] = []
        self.__worldSales : list[float] = []
        self.__releaseDate : list[float] = []
        
        # si un fichier est fourni : on charge 
        if jsonFile: self.open(jsonFile)
        
    @property
    def current(self) -> Union[int,None] : 
        return self.__current
    @current.setter
    def current(self, index :Union[int,None]) -> None : 
        self.__current = index

    def update(self,p: film.Film) -> None:
        pp = self.getFilm()
        if pp:
            pp.title = p.title
            pp.distributor = copy.deepcopy(p.distributor) ; print(f'Distrobutor: {p.distributor}')
            pp.releaseDate = copy.deepcopy(p.releaseDate)
            pp.license = copy.deepcopy(p.license)
            pp.runtime = copy.deepcopy(p.runtime)
            pp.info = copy.deepcopy(p.info)
            pp.domesticSales = copy.deepcopy(p.domesticSales)
            pp.internationalSales = copy.deepcopy(p.internationalSales)
            pp.worldSales = copy.deepcopy(p.worldSales)
            pp.genre = copy.deepcopy(p.genre)


    def open(self, jsonFile : str) -> None:
        with open(jsonFile, encoding='utf-8') as file:
            print(f'loading file: {jsonFile}', end='... ')
            js = json.load(file) 
            if  'distributors' in js.keys():
                listDistrib = js['distributors']
                for i in listDistrib:
                    self.__distributors.append(i)
                                                
            if  'genres' in js.keys():
                listGenre = js['genres']
                for i in listGenre :
                    self.__genres.append(i)
                
                
            if  'licenses' in js.keys():
                listLicenses = js['licenses']
                for i in listLicenses :
                    self.__licenses.append(i)
                
                self.__current = 0 if self.__listFilm else None
            if  'films' in js.keys():
                listFilm = js['films']
                for p in listFilm:  
                    pp = film.Film.buildFromJSon(p) 
                    self.__listFilm.append(pp)
                print(f'{len(self.__listFilm)} films trouvées')
                self.__current = 0 if self.__listFilm else None

    def save(self,jsonFile : str) -> None:
        print(f'saving file: {jsonFile}', end='... ')

        if not  os.path.exists(jsonFile): 
            f = open(jsonFile, "x"); f.close()

        with open(jsonFile, "w", encoding='utf-8') as file: 
            d : dict= {} 
            listFilm : list= []
            for p in self.__listFilm :listFilm.append(p.toJSON())
            d['annuaire'] = listFilm
            json.dump(d,file,ensure_ascii = False)
        print(f'done!')


    def addFilm(self, p : film.Film, index : Union[int,None] = None) -> None :
        if not isinstance(index, int) or not isinstance(self.__current, int):
            self.__listFilm.append(p)
            self.current = len(self.__listFilm) -1 if len(self.__listFilm) != 0 else None
        else:
            self.__listFilm.insert(self.__current,p)

    def next(self) -> None :
        if self.__current != None :
            print(self.__current)
            self.__current = (self.__current +1)% len(self.__listFilm) 
    
    def previous(self) -> None :
        if self.__current != None :
            self.__current = (self.__current - 1)% len(self.__listFilm)

    def getFilm(self) : 
        if self.__current != None: 
            return self.__listFilm[self.__current]  
        else:
            return None
        
    def getDistributor(self) : 
        return self.__distributors
    
    def getGenre(self) : 
        return self.__genres
    
    def getLicence(self) : 
        return self.__licenses
    
    @property
    def listFilm(self) -> list[film.Film]: 
        return self.__listFilm
    @listFilm.setter
    def listFilm(self, listFilm :list[film.Film]) -> None: 
        self.__listFilm = listFilm

    def TransNbrDistrib(self, chiffre : int):
        rep = self.__distributors[chiffre]
        return rep
    def TransNbrGenre(self, chiffre : int):
        rep = self.__genres[chiffre]
        return rep
    def TransNbrLicence(self, chiffre : int):
        rep = self.__licenses[chiffre]
        return rep
    
    def getWorldSales(self):
        return self.__worldSales
    
    def getReleaseDate(self):
        return self.__releaseDate
    

        
