'''
Created on Dec 27, 2015

@author: shaibujnr
'''
from Interface.extra.customscreen import CustomScreen

class DeterminantScreen(CustomScreen):
    def __init__(self,*args,**kwargs):
        super(DeterminantScreen,self).__init__(**kwargs)
        self.op_button_text = "Determinant"
        self.type_button_text = "Square Matrix"