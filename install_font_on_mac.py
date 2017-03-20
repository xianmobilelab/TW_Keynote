import os

def findFilesRecurse(path, ls = None):
    if ls == None:
        ls = []
        
    for p in os.listdir(path):
        p = os.path.join(path, p)
        if os.path.isdir(p):
            findFilesRecurse(p, ls)
        elif os.path.isfile(p):
            ls.append(p)
            
    return ls

# main
for f in findFilesRecurse(os.getcwd() + '/Font'):
    cmd = 'cp {0} /Library/Fonts'.format(f)
    print(cmd)
    os.system(cmd)
    
print('Done')
