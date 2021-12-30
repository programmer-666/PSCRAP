import os, shutil
from functions import folders

unit = '2'
os.system("rm -r pools/*")
for folder in folders:
    os.mkdir("pools/"+folder)
    shutil.copyfile("texts/"+folder+"/qa/pool.csv", "pools/"+folder+"/pool.csv")
    os.rename("pools/"+folder+'/pool.csv', 'pools/'+folder+'/pool'+unit+'.csv')
