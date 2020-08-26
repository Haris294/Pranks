import random
import os

def snap(path):
    
    all_files = []
    
    for root,dirs,files in os.walk(path):
        for filename in files:
            file = os.path.join(root,filename)
            abs_path = os.path.abspath(file)
            all_files.append(abs_path)
    
    
    random.shuffle(all_files)
    
    for i in range(len(all_files)//2):
        os.remove(all_files[i])
        
path = "D:" #Mention the Drive
snap(path)