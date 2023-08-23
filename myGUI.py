import wx
import os
import apiCalls
from datetime import datetime

class MainPanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)

        mainSizer = wx.BoxSizer(wx.HORIZONTAL)
        flexSizer = wx.FlexGridSizer(4,2,10,10)
        buttomSizer = wx.BoxSizer(wx.VERTICAL)

        #Currently Detected User
        currentDesc = wx.StaticText(self,label = "Erkannter Benutzer")
        self.currentUser = wx.TextCtrl(self, size = (320,22), style = wx.TE_READONLY)

        #Eventlogger
        self.logger = wx.TextCtrl(self,size = (320,300), style = wx.TE_MULTILINE | wx.TE_READONLY)

        #Buttoms
        ButtomCheck = wx.Button(self, label = "Überprüfen")
        ButtomIn = wx.Button(self, label = "Einchecken")
        ButtomOut = wx.Button(self, label =  "Auschecken")

        self.Bind(wx.EVT_BUTTON, self.OnCheck, ButtomCheck)
        self.Bind(wx.EVT_BUTTON, self.OnIn, ButtomIn)
        self.Bind(wx.EVT_BUTTON, self.OnOut, ButtomOut)

        #Grid Layout
        buttomSizer.AddMany([(ButtomCheck),(ButtomIn),(ButtomOut)])
        flexSizer.AddMany([(currentDesc),(self.currentUser),(buttomSizer),(self.logger)])
        flexSizer.AddGrowableCol(1,1)
        flexSizer.AddGrowableRow(2,1)
        mainSizer.Add(flexSizer, proportion = 2, flag = wx.ALL | wx.EXPAND, border = 15)
        self.SetSizer(mainSizer)


    #Funtctions
    def OnCheck(self, e):
        self.logger.AppendText(datetime.now().strftime("%H:%M:%S") +" - "+ apiCalls.teamCheck()+"\n")
        return
    
    def OnIn(self, e):
        self.logger.AppendText(datetime.now().strftime("%H:%M:%S") +" - "+ apiCalls.teamPost()+"\n")
        return
    
    def OnOut(self, e):
        self.logger.AppendText(datetime.now().strftime("%H:%M:%S") +" - "+ apiCalls.guardedDelete()+"\n")
        return
    
    def Init(self):
        self.currentUser.AppendText(os.environ.get("Username"))

            

class MainWindow(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, parent = None, title = "Zentrale - Rein & Raus", size=(500,500))

        self.panel = MainPanel(self)
        
        #Statusbar
        self.CreateStatusBar()

        #Menu
        filemenu = wx.Menu()
        menuHelp = filemenu.Append(wx.ID_HELP, "Hilfe", "Programmhilfe")
        menuAbout = filemenu.Append(wx.ID_ABOUT, "Über", "Informationen über dieses Programm")
        filemenu.AppendSeparator()
        menuExit = filemenu.Append(wx.ID_EXIT,"Beenden","Schließt das Programm")
        menuBar = wx.MenuBar()
        menuBar.Append(filemenu,"Datei")
        
        
        self.SetMenuBar(menuBar)      
        self.Bind(wx.EVT_MENU, self.OnExit, menuExit)
        self.Bind(wx.EVT_MENU, self.OnAbout, menuAbout)
        self.Bind(wx.EVT_MENU, self.OnHelp, menuHelp)

    def OnExit(self,e):
        self.Close(True) #close the Frame

    def OnAbout(self,e):
        dlg = wx.MessageDialog(self, "IT","Informationen über dieses Programm")
        dlg.ShowModal()
        dlg.Destroy()
    
    def OnHelp(self,e):
        dlg = wx.MessageDialog(self, "Bei Problemen an die IT wenden","Hilfe")
        dlg.ShowModal()
        dlg.Destroy()

    def InitMain(self):
        MainPanel.Init(self.panel)