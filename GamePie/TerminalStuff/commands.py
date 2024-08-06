
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from resources.importer import import_json 
from resources.switch import Switch
import subprocess


#Definening Stuff
commands = import_json("GamePie\TerminalStuff\commands.json");
commandSwitch = Switch({
     
})

#Compress the Commands
if(commands and commands["currentState"] == "unprocessed"):
        commandList = commands["message"].split(';');
        for command in commandList:
            compressedCommand = command.split(" ");
            if(command != ""):
                print(compressedCommand);
                commandSwitch.use(compressedCommand[0], compressedCommand);