from flask import Flask, request, send_file
import subprocess
import os
import sys
import argparse
import zipfile
from camel.typing import ModelType
from chatdev.chat_chain import ChatChain
from chatdev.utils import log_and_print_online, now
import argparse
import threading
import time


#import pyautogui

root = os.path.dirname(__file__)
front = os.path.dirname(root)
sys.path.append(root)
frontend_directory = os.path.join(front, "frontend")
streamlit = f"streamlit run app.py"

    
parser = argparse.ArgumentParser(description='argparse')
parser.add_argument('--config', type=str, default="Default",
                    help="Name of config, which is used to load configuration under CompanyConfig/")
parser.add_argument('--org', type=str, default="DefaultOrganization",
                    help="Name of organization, your software will be generated in WareHouse/name_org_timestamp")
parser.add_argument('--task', type=str, default="Develop a basic Gomoku game.",
                    help="Prompt of software")
parser.add_argument('--name', type=str, default="Gomoku",
                    help="Name of software, your software will be generated in WareHouse/name_org_timestamp")
parser.add_argument('--model', type=str, default="GPT_3_5_TURBO",
                    help="GPT Model, choose from {'GPT_3_5_TURBO','GPT_4','GPT_4_32K'}")
parser.add_argument('--path', type=str, default="",
                    help="Your file directory, ChatDev will build upon your software in the Incremental mode")
args = parser.parse_args()




        

def createZip(name, software_path):
     zip = ''+name +'.zip'
     with zipfile.ZipFile(zip,'w',zipfile.ZIP_DEFLATED) as z:
          z.write(software_path, os.path.basename(software_path))

     return send_file(zipfile, as_attachment=True)



subprocess.Popen(["start", "cmd", "/k", streamlit], shell=True, cwd=frontend_directory)


app = Flask(__name__)
names = ''
desc_ = ''
times = ''
spath = ''

def setName(name):
    global names 
    names = name
    return names

def get_config(company):
    """
    return configuration json files for ChatChain
    user can customize only parts of configuration json files, other files will be left for default
    Args:
        company: customized configuration name under CompanyConfig/

    Returns:
        path to three configuration jsons: [config_path, config_phase_path, config_role_path]
    """
    config_dir = os.path.join(root, "CompanyConfig", company)
    default_config_dir = os.path.join(root, "CompanyConfig", "Default")

    config_files = [
        "ChatChainConfig.json",
        "PhaseConfig.json",
        "RoleConfig.json"
    ]

    config_paths = []

    for config_file in config_files:
        company_config_path = os.path.join(config_dir, config_file)
        default_config_path = os.path.join(default_config_dir, config_file)

        if os.path.exists(company_config_path):
            config_paths.append(company_config_path)
        else:
            config_paths.append(default_config_path)

    return tuple(config_paths)


def getName():
     return names

def setTime(start_time):
     global times
     times = start_time
     return times

def getTime():
     return times

def runChatDev(n,d):
     process = f"python run.py --task \"{d}\" --name \"{n}\""
     subprocess.run(process, shell=True, check=True)


def GetOnlineLog():
    port = [8000]
    parser = argparse.ArgumentParser(description='argparse')
    parser.add_argument('--port', type=int, default=8000, help="port")
    args = parser.parse_args()
    port.append(args.port)
    message = (f"Please visit http://127.0.0.1:{port[-1]}/ to follow along. \n.")
    return message


def getPath():
    return spath

def setPath(path):
    global spath
    spath = path


@app.route('/api/data', methods = ['POST'])
def appRun():
    print("Server HIT!")
    desc = request.form.get("desc")
    name = request.form.get("name")
   
    setName(name)
    
    API_KEY = "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"
    # Scripts  --------------->
    process = f"python run.py --task \"{desc}\" --name \"{name}\"" #Script of actual chatdev
    
    #online = f"python3 online_log/app.py"                          #Script of the online logger
    config_path, config_phase_path, config_role_path = get_config("DefaultOrganization")
    args2type = {'GPT_3_5_TURBO': ModelType.GPT_3_5_TURBO, 'GPT_4': ModelType.GPT_4, 'GPT_4_32K': ModelType.GPT_4_32k}
    chat_chain = ChatChain(config_path=config_path,
                       config_phase_path=config_phase_path,
                       config_role_path=config_role_path,
                       task_prompt= desc,
                       project_name= name,
                       org_name=args.org,
                       model_type=args2type[args.model],
                       code_path=args.path)
    
    print(name,"  ",desc)
    os.environ["OPENAI_API_KEY"] = API_KEY
    start_time, softwarepath = chat_chain.get_logfilepath()
    setPath(softwarepath)
    try:
        # Use subprocess to run the command
        
        
        
        subprocess.run(process, shell=True, check=True)
        #thread1 = threading.Thread(target=runChatDev, args=(name,desc))
        #thread1.start()
        
        #time.sleep(10)
        #runOnline()
        #thread1.join()
        
        #onlinethread = threading.Timer(20, runOnline)
        #onlinethread.start()
        #onlinethread.join()
        #onlinelog = GetOnlineLog()
       

       
    except subprocess.CalledProcessError as e:
        a = print(f"Error running script: {e}")
        return a, 500
    except Exception as e:
        a = print(f"An error occurred: {e}")
        return a, 500

   
   
    return "onlinelog", 200

@app.route('/download_zip', methods=['GET'])
def zipDownload():
    
    name = getName()

    software_path = getPath()
    print(name," ", software_path)
    zip = createZip(name, software_path)
    return zip, 200
















      
   
        
      
   






if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9000, debug=True)

