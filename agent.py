# -*- coding: utf-8 -*-
import platform
import psutil 
import socket
import requests

processador = platform.processor()
sistemaOperacional = platform.system()
versaoSistemaOperacional = platform.release()
ip = socket.gethostbyname(socket.gethostname()).replace(".", "")
ipServidorAPI = "192.168.15.16"
portaServidorAPI = "8095"

usuarios = []
for usr in psutil.users():
    login = usr[0]
    usuarios.append(login)

processos = []
for proc in psutil.process_iter():
    nomeProcesso = proc.name()
    processos.append(nomeProcesso)
    
res = requests.post("http://"+ipServidorAPI+":"+portaServidorAPI+"/data"
                    , json={
                            "ip":ip,
                            "processador":processador,
                            "sistemaOperacional":sistemaOperacional,
                            "versaoSistemaOperacional":versaoSistemaOperacional,
                            "usuarios":usuarios,
                            "processos":processos
                            })

    
    