from system import System
from reaction import Reaction
from species import Species

class Formatter:
    def handles(self):
        return ["csv"]
    def parse(self,file):
        system=System()
        return system
    def write(self,file,system):
        pass   

