#!/usr/bin/env python3
# UTF-8

# MIT License
# 
# Copyright (c) 2017 Jiří Tumpach
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.


# this program adds license headers to multiple files

import os


project_name = "WTlib"

licence_header = \
r"""/*
 *  This file is part of {0}.
 *
 *  {0} is free software: you can redistribute it and/or modify
 *  it under the terms of the GNU General Public License as published by
 *  the Free Software Foundation, either version 3 of the License, or
 *  (at your option) any later version.
 *
 *  {0} is distributed in the hope that it will be useful,
 *  but WITHOUT ANY WARRANTY; without even the implied warranty of
 *  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 *  GNU General Public License for more details.
 *
 *  You should have received a copy of the GNU General Public License
 *  along with {0}.  If not, see <http://www.gnu.org/licenses/>.
*/
""".format(project_name)



root = "../Bachelor_thesis"
folders = ["lib", "demo"]
source_types = [".cpp", ".h", ".hpp"]

restricted = [ "lib/src/entropicky_koder/ebcot/ebcot_ffmpeg" ,
               "lib/src/entropicky_koder/ebcot/mq_ffmpeg" ]

folders = list(map(lambda x: root + "/" + x, folders))
restricted = list(map(lambda x: root + "/" + x, restricted))


def generator ():
    '''
    generates valid paths (source type, restricted folders, target folders)
    '''
    for folder in folders:
        for root, dirs, files in os.walk(folder):
            if any((root.startswith(t) for t in restricted)):
                continue

            for file in files:
                if any((file.endswith(t) for t in source_types)):
                    filepath = root + "/" + file
                    yield filepath


def check_file_have_license (path):
    with open(path, 'r') as file:
        if "Copyright" in file.read():
            return True
    return False

def try_to_remove_license (path):
    raise NotImplementedError

def add_license (path):
    with open(path, 'r+') as file:
        content = f.read()
        f.seek(0,0)
        f.write(licence_header)
        f.write(content)



all_yes = False
for filepath in generator():
    add_to_this_file = True

    if not all_yes and check_file_have_license(filepath) :
        print("File {0} probably have licence header alredy")
        print("Write this header anyway? [YES,NO,YES_ALL]")
        while True:
            ui = input().lower()
            if ui == "yes":
                add_to_this_file = True
                break
            elif ui == "no":
                add_to_this_file = False
                break
            elif ui == "yes_all" or yi == "yes all":
                add_to_this_file = True
                all_yes = True
                break
            else:
                print("Invalid option")

    if add_to_this_file:
        print( "ADDING" )


