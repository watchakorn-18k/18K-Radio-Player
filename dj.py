import urllib, json
import urllib.request
from threading import Thread 
class Dj(Thread):
    def __init__(self,_id, dj, stat,usr,imgUrl):
        Thread.__init__(self)
        self._id = _id
        self.dj = dj
        self.stat = stat
        self.imgUrl = imgUrl
        self.list_dj = [self.dj,self.imgUrl]
    @classmethod
    def from_json(cls,json_string):
        json_dict = json.loads(json_string)
        return cls(**json_dict)
        
    def __repr__(self):
        return f'{self.dj}'
    
    def get_dj(*args):
        # url = "https://web-18k-mongodb-crud.herokuapp.com/api/get_18k_list_dj"
        # response = urllib.request.urlopen(url)
        with open("dj.json", "r") as read_file:
            data = json.load(read_file)
        users_list= []
        for d in data:
            users_list.append(Dj(**d))
        return users_list

