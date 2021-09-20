import urllib, json
import urllib.request


class img_Dj:
    def __init__(self,_id, dj, stat,usr,imgUrl):
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
        return f'{self.imgUrl}'
    
    def get_dj(*args):
        with open("dj.json", "r") as read_file:
            data = json.load(read_file)
        users_list= []
        for d in data:
            users_list.append(img_Dj(**d))
        return users_list

