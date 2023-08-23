import wx
import myGUI

app = wx.App(False)
frame = myGUI.MainWindow()
frame.InitMain()
frame.Show()
app.MainLoop()