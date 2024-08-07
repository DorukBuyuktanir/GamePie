import json
from cffi import FFI
import execjs
import os

from buildInfo import buildInfo


path = buildInfo["path"];

def open_file(file_path:str):
    return open(path + file_path, 'r', encoding='utf-8');

def write_file(file_path:str, innerText="",rewrite=True):
    if(buildInfo["platform"] == "windows"):
        pass
        #os.system("../ConsoleCommands/" +)

def import_json(file_path:str):
    try:
        with open_file(file_path) as file:
            data = json.load(file);
            return data;
    except FileNotFoundError:
        print(f"Error: The file '{path + file_path}' was not found.");
    except json.JSONDecodeError:
        print("Error: Failed to decode JSON.");
    except Exception as e:
        print(f"An unexpected error occurred: {e}");

def import_js(file_path:str):
    try:
        with open_file(file_path) as jsfile:
            return execjs.compile(jsfile.read());
    except FileNotFoundError:
        print(f"Error: The file '{path + file_path}' was not found.");
    except Exception as e:
        print(f"An unexpected error occurred: {e}");

def import_c(file_path:str, header_path:str):
    try:
        ffi = FFI();
        with (open_file(file_path), open_file(header_path)) as files:
            datas = (files[0].read(), files[1].read());
            ffi.cdef(datas[1]);
            return ffi.verify(datas[0]);
    except FileNotFoundError:
        print(f"Error: The file '{path + file_path}' was not found.");
    except Exception as e:
        print(f"An unexpected error occurred: {e}");