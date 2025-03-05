import xbmc
import xbmcgui
import xbmcaddon

# create a class for your addon, we need this to get info about your addon
ADDON = xbmcaddon.Addon()
# get the full path to your addon, decode it to unicode to handle special (non-ascii) characters in the path
CWD = ADDON.getAddonInfo('path')
# add a class to create your xml based window
class GUI(xbmcgui.WindowXMLDialog):
    # [optional] this function is only needed of you are passing optional data to your window
    def __init__(self, *args, **kwargs):
        # get the optional data and add it to a variable you can use elsewhere in your script
        self.data = kwargs['optional1']

    # until now we have a blank window, the onInit function will parse your xml file
    def onInit(self):
        self.setFocusId(self.getCurrentContainerId())

# this is the entry point of your addon, execution of your script will start here
if (__name__ == '__main__'):
   
    ui = GUI('CustomDialogSelectView.xml', CWD, 'default', '1080i', optional1='some data') # for kodi 18 and up..
    #ui.doModal()
    xbmcgui.WindowXMLDialog.doModal(ui)
    # window closed, now cleanup a bit: delete your window before the script fully exits
    del ui
