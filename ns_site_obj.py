import rhinoscriptsyntax as rs

class site_obj(object):
    def __init__(self,O):
        self.site=O
        self.pts=rs.DivideCurve(O,100)
    def getPts(self):
        return self.pts
    def displayPts(self):
        rs.EnableRedraw(False)
        u=0
        for i in self.pts:
            #rs.AddTextDot(str(u)+','+str(v),j)
            u+=1
        rs.EnableRedraw(True)