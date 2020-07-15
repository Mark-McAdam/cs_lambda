# Kellis Method
""""
I commented this on a post earlier: but this is what I did. not sure which one did the trick:
Make sure there is an __init__.py folder in the directory I am trying to import from
make sure the import path is relative to where I am in the terminal when running the file
if that doesn't work, I create a relative python PATH variable by running this in the terminal: 
"""
export PYTHONPATH=.
# then run it in vscode terminal


# Roberts Method
import sys
sys.path.append(".")
from singly_linked_list.singly_linked_list import Node, LinkedList

# From Slack Chat  couple suggestions also 

# Sara Reidy 
import sys
sys.path.insert(1, '../singly_linked_list/')
from singly_linked_list import LinkedList

# Josiah Roa 
import sys
sys.path.append('../singly_linked_list/')
from singly_linked_list import LinkedList