import os
import re
from shutil import copy, rmtree

print("Initialization")

address_directory_origin = os.getcwd() + os.path.sep + "DirectoryAssets"
address_directory_result = os.getcwd() + os.path.sep + "Result"

print("Final directory creation")

# If resultat directory exists, erase it, then create it
if os.path.isdir(address_directory_result):
    rmtree(address_directory_result)
os.mkdir(address_directory_result)

listdirectories = os.walk(address_directory_origin).__next__()[1]

print("Start Loop")

for namedirectory in listdirectories:
    addressdirectory = address_directory_origin + os.path.sep + namedirectory
    address_passname = addressdirectory + os.path.sep + "pathname"
    address_target_file = addressdirectory + os.path.sep + "asset"

    with open(address_passname, "r") as f:
        address_theorical = f.readline()[26:]
        namefilefinal = os.path.basename(address_theorical).rstrip()
        namedirectoryfinal = os.path.dirname(address_theorical).split("/")[0]
        address_directory_final = address_directory_result + os.path.sep + namedirectoryfinal

        print(namedirectoryfinal + os.path.sep + namefilefinal)

        # Check if the folder exists, if not, create it
        if not (os.path.isdir(address_directory_final)):
            os.mkdir(address_directory_final)

        # Finaly copy the asset with the final name if it exists (some folders are empty)
        address_file_final = address_directory_final + os.path.sep + namefilefinal

        if os.path.isfile(address_target_file):
            copy(address_target_file, address_file_final)
