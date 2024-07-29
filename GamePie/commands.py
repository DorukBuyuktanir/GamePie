from resources.importer import import_json 
from resources.switch import Switch
import subprocess

#Definening Stuff
commands = import_json("GamePie\commands.json");
commandSwitch = Switch({
     
})




#Compress the Commands
if(commands and commands["currentState"] == "unproced"):
        commandList = commands["message"].split(';');
        for command in commandList:
            compressedCommand = command.split(" ");
            if(command != ""):
                print(compressedCommand);
                commandSwitch.use(compressedCommand[0], compressedCommand);