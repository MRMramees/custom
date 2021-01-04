import os
import shutil
from zipfile import ZipFile
from os import path
from shutil import make_archive
dir_name=input()
output_filename=dir_name+'/a'
shutil.make_archive(output_filename, 'zip', dir_name)