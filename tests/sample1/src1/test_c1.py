import json

class test1:
    def __init__(self) -> None:
        self.mydict=[{'item1':'val1','item2':'val2'},{'item3':'val3'}]
        
    
    def show(self,indent=4):
        self.json_str=json.dumps(self.mydict,indent=indent)
        print(self.json_str)
        return "Class Test done"