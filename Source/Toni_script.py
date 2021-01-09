import os

import wx
import wx.lib.agw.thumbnailctrl as TC

class Main(wx.App):
    def __init__(self, redirect=False, filename=None):
        wx.App.__init__(self, redirect, filename)
        self.frame = wx.Frame(None, title='Thumbssss')
        self.panel = wx.Panel(self.frame)

        sizer = wx.BoxSizer(wx.VERTICAL)

        thumbnail = TC.ThumbnailCtrl(self.panel, imagehandler=TC.NativeImageHandler)
        sizer.Add(thumbnail, 1, wx.EXPAND | wx.ALL, 10)

        thumbnail.ShowDir("F:\\Semestrul 1\\IOM\\Proiect\\Image-similarity\\Images")
        self.panel.SetSizer(sizer)
        self.frame.Show()


# our normal wxApp-derived class, as usual

#app = wx.App(0)
if __name__ == '__main__':
    app = Main()
    app.MainLoop()

#panel = wx.Panel(frame, wx.ID_ANY)
#app.SetTopWindow(frame)
#frame.Show()

#Schimbam linia 432 de la caption