import wx


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
        img_path = openFileDialog.GetPath()
        #openFileDialog.Destroy()
        
        # if Linux == True: print("it is what it is!")
        img_name = img_path.split("\\")[len(img_path.split("\\")) - 1]
        
        chosen = wx.StaticBitmap(self, wx.ID_ANY, wx.Bitmap(img_name, wx.BITMAP_TYPE_ANY))
        chosen.SetPosition((30, 60))
        
        similar1 = wx.StaticBitmap(self, wx.ID_ANY, wx.Bitmap(img_name, wx.BITMAP_TYPE_ANY))
        similar1.SetPosition((670, 60))
        
        similar2 = wx.StaticBitmap(self, wx.ID_ANY, wx.Bitmap(img_name, wx.BITMAP_TYPE_ANY))
        similar2.SetPosition((470, 330))
        
        similar3 = wx.StaticBitmap(self, wx.ID_ANY, wx.Bitmap(img_name, wx.BITMAP_TYPE_ANY))
        similar3.SetPosition((870, 330))
        
        

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
    
   

    app.MainLoop()
    