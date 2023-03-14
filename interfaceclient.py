# -*- coding: utf-8 -*-
"""
Created on Wed Feb 15 21:29:28 2023

@author: Silvia
"""

from abc import abstractmethod
from abc import ABCMeta

class interfaceClient(metaclass=ABCMeta):
    
    @abstractmethod
    def signIn(self,user:str,password:str) ->str:
        pass
    @abstractmethod
    def signUp(self,user:str,password:str,name:str,email:str) ->bool:
        pass
    @abstractmethod
    def forgotPass(self,email:str) ->str:
        pass
    @abstractmethod
    def changePass(self,actualPass:str,newPass:str,confirmNewPass:str) ->bool:
        pass
    @abstractmethod
    def signOff(self,token:str) ->bool:
        pass
    @abstractmethod
    def editUser(self,name:str) ->str:
        pass
    @abstractmethod
    def loadFiles(self,token:str,files:list,) ->bool:
        pass    
    @abstractmethod
    def serializeFiles(self,token:str,files:list,) ->list:
        pass    
    @abstractmethod
    def sendFilesServer(self,token:str,idReq:str,fileSerilize:list) ->bool:
        pass
    @abstractmethod
    def sendFilesServer(self,token:str,idReq:str) ->str:
        pass