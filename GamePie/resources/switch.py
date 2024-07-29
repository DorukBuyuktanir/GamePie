class Switch:
    def __init__(self, case:object) :
        self.case = case;
    
    def use(self, key:str, params = {}):
        for _key in self.case.keys():
            print(_key + " == " + key);
            print(key == _key);
            print(type(_key), " == ", type(key));
            print(repr(_key), " == ", repr(key));
            print(_key.strip(), " == ", key.strip());
            print(_key.strip() == key.strip());
            
            if(key == _key):
                return self.case[key](params);
