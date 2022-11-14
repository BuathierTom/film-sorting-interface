# --- import
import json
import datetime

# ---------------------------------
# --- class Film
# ---------------------------------
class Film:
    # constructor  
    def __init__(self, title : str, distributor : int, releaseDate : datetime.date, 
                license : int, runtime : str, info : str, domesticSales : str,
                internationalSales : str, worldSales : float, genre : list[int]) -> None: 
        self.__title : str = title
        self.__distributor : int = distributor
        self.__releaseDate : datetime.date = releaseDate
        self.__license : int = license
        self.__runtime : str = runtime
        self.__info : str = info
        self.__domesticSales : str = domesticSales
        self.__internationalSales : str = internationalSales
        self.__worldSales : float = worldSales
        self.__genre : list[int] = genre
        
    # def __repr__(self) -> str:
    #     res = ""
        
    #     res += self.__title + ", " + self.__distributor + ", ("
    #     res += str(self.__releaseDate) + "), "
    #     res += self.__license + ", " + self.__runtime + ", " + self.__info + ", "
    #     res += self.__domesticSales + ", " + self.__internationalSales + ", " + self.__worldSales + "."
    #     # res += self.__genre + "."
    #     return res

    @property
    def title(self) -> str: 
        return self.__title
    @title.setter
    def title(self, title :str) -> None: 
        self.__title = title

    @property
    def distributor(self) -> int: 
        return self.__distributor
    @distributor.setter
    def distributor(self, distributor :int) -> None: 
        self.__distributor = distributor
        
    @property
    def releaseDate(self) -> datetime.date : 
        return self.__releaseDate
    @releaseDate.setter
    def releaseDate(self, date : datetime.date) : 
        self.__releaseDate = date
        
    @property
    def license(self) -> int: 
        return self.__license
    @license.setter
    def license(self, license :int) -> None: 
        self.__license = license

    @property
    def runtime(self) -> str: 
        return self.__runtime
    @runtime.setter
    def runtime(self, runtime :str) -> None: 
        self.__runtime = runtime
        
    @property
    def info(self) -> str: 
        return self.__info
    @info.setter
    def info(self, info :str) -> None: 
        self.__info = info
    
    @property
    def domesticSales(self) -> str: 
        return self.__domesticSales
    @domesticSales.setter
    def domesticSales(self, domesticSales :str) -> None: 
        self.__domesticSales = domesticSales

    @property
    def internationalSales(self) -> str: 
        return self.__internationalSales
    @internationalSales.setter
    def internationalSales(self, internationalSales :str) -> None: 
        self.__internationalSales = internationalSales

    @property
    def worldSales(self) -> float: 
        return self.__worldSales
    @worldSales.setter
    def worldSales(self, worldSales :float) -> None: 
        self.__worldSales = worldSales
        
    @property
    def genre(self) -> list[int]: 
        return self.__genre
    @genre.setter
    def genre(self, genre :list[int]) -> None: 
        self.__genre = genre
    
    
    # toJSON
    def toJSON(self) -> str:
        dictP = {
            'title'  : self.__title,
            'distributor' : self.__distributor,
            'releaseDate' : str(self.__releaseDate),
            'license'  : self.__license,
            'runtime'  : self.__runtime,
            'info'  : self.__info,
            'domesticSales'  : self.__domesticSales,
            'internationalSales'  : self.__internationalSales,
            'worldSales'  : self.__worldSales,
            'genre' : self.__genre
        }
        return json.dumps(dictP,ensure_ascii=False)

    # buildFromJson
    @staticmethod
    def buildFromJSon(d: dict):
        title :str =  d['title'] 
        distributor : int =  d['distributor']
        releaseDateSTR : str = d['releaseDate']
        elts = releaseDateSTR.split('-')
        releaseDate = datetime.date(int(elts[0]),int(elts[1]),int(elts[2])) 
        license = d['license'] 
        runtime = d['runtime'] 
        info = d['info'] 
        domesticSales = d['domesticSales'] 
        internationalSales = d['internationalSales']
        worldSales = d['worldSales']
        genre = d['genre']
        

        return Film(title, distributor, releaseDate, license, runtime, info, domesticSales,
                    internationalSales, worldSales, genre)


