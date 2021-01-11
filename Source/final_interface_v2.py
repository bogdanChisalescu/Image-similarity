import wx
import os

########################################################################
class Panel(wx.Panel):
    """"""

    #----------------------------------------------------------------------
    def __init__(self, parent):
        """Constructor"""
        wx.Panel.__init__(self, parent)


        btn = wx.Button(self, label="Chose image", pos = (30, 30))
        btn.Bind(wx.EVT_BUTTON, self.onButton)

    #----------------------------------------------------------------------
    def onButton(self, event):
        """
        Change the value of self.call_function
        """
        #Get the image location
        openFileDialog.ShowModal()

        global img_path

        img_path = openFileDialog.GetPath()
        img_path_lbp='D:\Facultate\IOM\Image-similarity\LBP_img'
        #openFileDialog.Destroy()
        return img_path

#trebuie returnata acest img_path
#mai putem crea o functie ce apeleaza aceasta functie si primeste valoare img_path si apoi arata pozele

        # chosen = wx.StaticBitmap(self, wx.ID_ANY, wx.Bitmap(img_path, wx.BITMAP_TYPE_ANY))
        # chosen.SetPosition((30, 60))
        #
        # self.text = wx.StaticText(self, wx.ID_ANY, img_path)

        #timeout pana cand se termina lbd
        # #afisare counter lbp
        # self.text = wx.StaticText(self, wx.ID_ANY, "Hello World!")
        #
        # #afisare imagini lbp
        # similar1 = wx.StaticBitmap(self, wx.ID_ANY, wx.Bitmap(os.path.join(img_path_lbp,'1.jpg'), wx.BITMAP_TYPE_ANY))
        # similar1.SetPosition((670, 60))
        #
        # similar2 = wx.StaticBitmap(self, wx.ID_ANY, wx.Bitmap(os.path.join(img_path_lbp,'2.jpg'), wx.BITMAP_TYPE_ANY))
        # similar2.SetPosition((470, 330))
        #
        # similar3 = wx.StaticBitmap(self, wx.ID_ANY, wx.Bitmap(os.path.join(img_path_lbp,'3.jpg'), wx.BITMAP_TYPE_ANY))
        # similar3.SetPosition((870, 330))
        
        

########################################################################
class Frame(wx.Frame):
    """"""

    #----------------------------------------------------------------------
    def __init__(self):
        """Constructor"""
        wx.Frame.__init__(self, None, title="3 most similar images", size=(1300, 700))
        panel = Panel(self)
        panel.SetBackgroundColour("gray")
        self.Centre()
    
        
        self.Show()
        
   
        

#----------------------------------------------------------------------
if __name__ == "__main__":
    app = wx.App(False)
    frame = Frame()
    # Create open file dialog
    openFileDialog = wx.FileDialog(frame, "Open", "", "", "", wx.FD_OPEN | wx.FD_FILE_MUST_EXIST)
    
    app.onButton
    img_path3=img_path
    app.MainLoop()
    