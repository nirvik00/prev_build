import rhinoscriptsyntax as rs
import random
import os
from ns_site_obj import site_obj as site_obj
from ns_inp_obj import inp_obj as inp_obj
from ns_genSite import genSite as genSite
from ns_main import main as main
class RunProc(object):
    def __init__(self):
        FileName="type_data.csv"
        FilePath=rs.GetString("Enter the working directory for the program : ")
        try:
            os.stat(FilePath)
        except:
            os.mkdir(FilePath)
        os.chdir(FilePath)
        site_bool=rs.GetString('Use default site Profile- (Y)? Or select - (N) ','Y').lower()
        n=rs.GetInteger('Enter number of variations required')
        if(n==0 or n==None):
            n=1
        for i in range(0,2000*n,2000):
            site=None
            site_crv=None
            if(site_bool=='y' or site_bool=='Y'):
                site=genSite(i,0)
                site_crv=site.getSite()
            else:
                site_crv=rs.GetObject('pick site boundary')
                site_crv=rs.CopyObject(site_crv,[i,0,0])
            m=main(FileName,site_crv)
            m.getInpObj()
            m.genFuncObj_Site()
            m.writeToCsv()
RunProc()
