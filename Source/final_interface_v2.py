import wx
import os
import identify_similar_img

img_path_lbp = 'D:\Facultate\IOM\Image-similarity\LBP_img'
img_path = ''


########################################################################
class Panel(wx.Panel):
    """"""

    # ----------------------------------------------------------------------
    def __init__(self, parent):
        """Constructor"""
        wx.Panel.__init__(self, parent)

        btn = wx.Button(self, label="Chose image", pos=(30, 30))
        btn.Bind(wx.EVT_BUTTON, self.onButton)

    # ----------------------------------------------------------------------
    def onButton(self, event):
        """
        Change the value of self.call_function
        """

        global img_path
        # Create button 'Find Similar images'
        btn_lbp = wx.Button(self, label="Compute LBP", pos=(130, 30))
        btn_lbp.Bind(wx.EVT_BUTTON, self.onButton_lbp)

        # Get the image location
        openFileDialog.ShowModal()
        img_path = openFileDialog.GetPath()

        # openFileDialog.Destroy()

        # trebuie returnata acest img_path
        # mai putem crea o functie ce apeleaza aceasta functie si primeste valoare img_path si apoi arata pozele

        chosen = wx.StaticBitmap(self, wx.ID_ANY, wx.Bitmap(img_path, wx.BITMAP_TYPE_ANY))
        chosen.SetPosition((670, 60))
        #
        # self.text = wx.StaticText(self, wx.ID_ANY, img_path)

        # timeout pana cand se termina lbd
        # afisare counter lbp
        # self.text = wx.StaticText(self, wx.ID_ANY, "Hello World!")

        # afisare imagini lbp
        # similar1 = wx.StaticBitmap(self, wx.ID_ANY, wx.Bitmap(os.path.join(img_path_lbp,'1.jpg'), wx.BITMAP_TYPE_ANY))
        # similar1.SetPosition((70, 330))
        #
        # similar2 = wx.StaticBitmap(self, wx.ID_ANY, wx.Bitmap(os.path.join(img_path_lbp,'2.jpg'), wx.BITMAP_TYPE_ANY))
        # similar2.SetPosition((470, 330))
        #
        # similar3 = wx.StaticBitmap(self, wx.ID_ANY, wx.Bitmap(os.path.join(img_path_lbp,'3.jpg'), wx.BITMAP_TYPE_ANY))
        # similar3.SetPosition((870, 330))

    def onButton_lbp(self, event):
        text = wx.StaticText(self, wx.ID_ANY, "Hello World!")
        text.SetPosition((100, 30))
        print(img_path)
        activate_lbp = lbp_imagines(images)


########################################################################
class Frame(wx.Frame):
    """"""

    # ----------------------------------------------------------------------
    def __init__(self):
        """Constructor"""
        wx.Frame.__init__(self, None, title="3 most similar images", size=(1300, 700))
        panel = Panel(self)
        panel.SetBackgroundColour("gray")
        self.Centre()

        self.Show()


# ----------------------------------------------------------------------
if __name__ == "__main__":
    app = wx.App(False)
    frame = Frame()
    # Create open file dialog
    openFileDialog = wx.FileDialog(frame, "Open", "", "", "", wx.FD_OPEN | wx.FD_FILE_MUST_EXIST)

    app.MainLoop()
