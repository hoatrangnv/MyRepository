from __future__ import unicode_literals
from resources.lib.modules import client
import re,sys,xbmcgui,os,urllib
from resources.lib.modules.log_utils import log

from addon.common.addon import Addon
addon = Addon('plugin.video.castaway', sys.argv)

AddonPath = addon.get_path()
IconPath = AddonPath + "/resources/media/"
def icon_path(filename):
    return os.path.join(IconPath, filename)

class info():
    def __init__(self):
    	self.mode = 'tvone1'
        self.name = 'tvone1.com'
        self.icon = 'tvone1.png'
        self.paginated = False
        self.categorized = False
        self.multilink = False
        self.special = True

class main():
    def __init__(self):
      self.base = ''

    def channels(self):
      events = [('http://www.finecast.tv/embed4.php?u=bbcnews&vw=640&vh=450&referer=http://www.247tvstream.com/', 'BBC News', icon_path(info().icon)), ('http://www.finecast.tv/embed4.php?u=cn99&vw=640&vh=450&referer=http://www.247tvstream.com/', 'CNN Europe', icon_path(info().icon)), ('http://www.finecast.tv/embed4.php?u=cnbc&vw=640&vh=450&referer=http://www.247tvstream.com/', 'CNBC', icon_path(info().icon)), ('http://www.finecast.tv/embed4.php?u=skynews&vw=640&vh=450&referer=http://www.247tvstream.com/', 'Sky News', icon_path(info().icon)), ('http://www.finecast.tv/embed4.php?u=discoverys&vw=640&vh=450&referer=http://www.247tvstream.com/', 'Discovery Science', icon_path(info().icon)), ('http://www.finecast.tv/embed4.php?u=discoveryi&vw=640&vh=450&referer=http://www.247tvstream.com/', 'Investigation Discovery', icon_path(info().icon)), ('http://www.finecast.tv/embed4.php?u=animal&vw=640&vh=450&referer=http://www.247tvstream.com/', 'Animal Planet', icon_path(info().icon)), ('http://www.finecast.tv/embed4.php?u=natgeo&vw=640&vh=450&referer=http://www.247tvstream.com/', 'National Geograpic', icon_path(info().icon)), ('http://www.finecast.tv/embed4.php?u=natgeohd&vw=640&vh=450&referer=http://www.247tvstream.com/', 'Nat Geo WILD', icon_path(info().icon)), ('http://www.finecast.tv/embed4.php?u=cn888&vw=640&vh=450&referer=http://www.247tvstream.com/', 'Cartoon Network', icon_path(info().icon)), ('http://www.finecast.tv/embed4.php?u=disney&vw=640&vh=450&referer=http://www.247tvstream.com/', 'Disney Channel', icon_path(info().icon)), ('http://www.finecast.tv/embed4.php?u=disneyjr&vw=640&vh=450&referer=http://livetvweb.net/', 'Disney Junior', icon_path(info().icon)), ('http://www.finecast.tv/embed4.php?u=nick666&vw=640&vh=450&referer=http://www.247tvstream.com/', 'Nick', icon_path(info().icon)), ('http://www.finecast.tv/embed4.php?u=foodnetwork&vw=640&vh=450&referer=http://livetvweb.net/', 'Food Network', icon_path(info().icon)), ('http://www.finecast.tv/embed4.php?u=travel3&vw=640&vh=450&referer=http://livetvweb.net/', 'Travel Channel', icon_path(info().icon)), ('http://www.finecast.tv/embed4.php?u=vch12&vw=640&vh=450&referer=http://livetvweb.net/', 'VH1', icon_path(info().icon)), ('http://www.finecast.tv/embed4.php?u=magic&vw=640&vh=450&referer=http://livetvweb.net/', 'Magic', icon_path(info().icon)), ('http://www.finecast.tv/embed4.php?u=heart&vw=640&vh=450&referer=http://livetvweb.net/', 'Heart TV', icon_path(info().icon)), ('http://www.finecast.tv/embed4.php?u=mtvclassic&vw=640&vh=450&referer=http://livetvweb.net/', 'MTV Classic', icon_path(info().icon)), ('http://www.finecast.tv/embed4.php?u=mtvhits&vw=640&vh=450&referer=http://livetvweb.net/', 'MTV Hits', icon_path(info().icon)), ('http://www.finecast.tv/embed4.php?u=mtvmusic&vw=640&vh=450&referer=http://livetvweb.net/', 'MTV Music', icon_path(info().icon)), ('http://www.finecast.tv/embed4.php?u=skymd&vw=640&vh=450&referer=http://livetvweb.net/', 'Sky Movies Drama & Romance', icon_path(info().icon)), ('http://www.finecast.tv/embed4.php?u=skymf&vw=640&vh=450&referer=http://livetvweb.net/', 'Sky Movies Family', icon_path(info().icon)), ('http://www.finecast.tv/embed4.php?u=skyma&vw=640&vh=450&referer=http://livetvweb.net/', 'Sky Movies Action', icon_path(info().icon)), ('http://www.finecast.tv/embed4.php?u=trum2&vw=640&vh=450&referer=http://livetvweb.net/', 'True Movies 2', icon_path(info().icon)), ('http://www.finecast.tv/embed4.php?u=skypm&vw=640&vh=450&referer=http://livetvweb.net/', 'Sky Movies Premiere', icon_path(info().icon)), ('http://www.finecast.tv/embed4.php?u=skymcc&vw=640&vh=450&referer=http://livetvweb.net/', 'Sky Movies Crime & Thriller', icon_path(info().icon)), ('http://www.finecast.tv/embed4.php?u=skyf1488&vw=640&vh=450&referer=http://livetvweb.net/', 'Sky Sports F1', icon_path(info().icon)), ('http://www.finecast.tv/embed4.php?u=skymc&vw=640&vh=450&referer=http://livetvweb.net/', 'Sky Movies Comedy', icon_path(info().icon)), ('http://www.finecast.tv/embed4.php?u=trum1&vw=640&vh=450&referer=http://livetvweb.net/', 'True Movies 1', icon_path(info().icon)), ('http://www.finecast.tv/embed4.php?u=film4&vw=640&vh=450&referer=http://livetvweb.net/', 'Film4', icon_path(info().icon)), ('http://www.finecast.tv/embed4.php?u=skymh&vw=640&vh=450&referer=http://livetvweb.net/', 'Dave', icon_path(info().icon)), ('http://www.finecast.tv/embed4.php?u=cc698&vw=640&vh=450&referer=http://livetvweb.net/', 'Comedy Central', icon_path(info().icon)), ('http://www.finecast.tv/embed4.php?u=ee34&vw=640&vh=450&referer=http://livetvweb.net/', 'E!', icon_path(info().icon)), ('http://www.finecast.tv/embed4.php?u=skyatlantic&vw=640&vh=450&referer=http://livetvweb.net/', 'Sky Atlantic', icon_path(info().icon)), ('http://www.finecast.tv/embed4.php?u=drama&vw=640&vh=450&referer=http://livetvweb.net/', 'Drama', icon_path(info().icon)), ('http://www.finecast.tv/embed4.php?u=cbsdrama&vw=640&vh=450&referer=http://livetvweb.net/', 'CBS Drama', icon_path(info().icon)), ('http://www.finecast.tv/embed4.php?u=cbsaction&vw=640&vh=450&referer=http://livetvweb.net/', 'CBS Action', icon_path(info().icon)), ('http://www.finecast.tv/embed4.php?u=cbsreality&vw=640&vh=450&referer=http://livetvweb.net/', 'CBS Reality', icon_path(info().icon)), ('http://www.finecast.tv/embed4.php?u=skyarts1&vw=640&vh=450&referer=http://livetvweb.net/', 'Sky Arts 1', icon_path(info().icon)), ('http://www.finecast.tv/embed4.php?u=skyarts2&vw=640&vh=450&referer=http://livetvweb.net/', 'Sky Arts 2', icon_path(info().icon)), ('http://www.finecast.tv/embed4.php?u=skyliving&vw=640&vh=450&referer=http://livetvweb.net/', 'Sky Living', icon_path(info().icon)), ('http://www.finecast.tv/embed4.php?u=sky2uk&vw=640&vh=450&referer=http://livetvweb.net/', 'Sky 2', icon_path(info().icon)), ('http://www.finecast.tv/embed4.php?u=itv13552&vw=640&vh=450&referer=http://livetvweb.net/', 'ITV1', icon_path(info().icon)), ('http://www.finecast.tv/embed4.php?u=itv2l&vw=640&vh=450&referer=http://livetvweb.net/', 'ITV2', icon_path(info().icon)), ('http://www.finecast.tv/embed4.php?u=itv3l&vw=640&vh=450&referer=http://livetvweb.net/', 'ITV3', icon_path(info().icon)), ('http://www.finecast.tv/embed4.php?u=itv448&vw=640&vh=450&referer=http://livetvweb.net/', 'ITV4', icon_path(info().icon)), ('http://www.finecast.tv/embed4.php?u=bloomberg&vw=640&vh=450&referer=http://livetvweb.net/', 'Bloomberg', icon_path(info().icon)), ('http://www.finecast.tv/embed4.php?u=5usa4&vw=640&vh=450&referer=http://livetvweb.net/', '5 USA', icon_path(info().icon)), ('http://www.finecast.tv/embed4.php?u=five4&vw=640&vh=450&referer=http://livetvweb.net/', 'Channel 5', icon_path(info().icon)), ('http://www.finecast.tv/embed4.php?u=itv1l&vw=640&vh=450&referer=http://livetvweb.net/', 'ITV1 London', icon_path(info().icon)), ('http://www.finecast.tv/embed4.php?u=tv37&vw=640&vh=450&referer=http://livetvweb.net/', 'TV3 Ireland', icon_path(info().icon)), ('http://www.finecast.tv/embed4.php?u=dmax4&vw=640&vh=450&referer=http://livetvweb.net/', 'DMAX', icon_path(info().icon)), ('http://www.finecast.tv/embed4.php?u=quest&vw=640&vh=450&referer=http://livetvweb.net/', 'Quest', icon_path(info().icon)), ('http://www.finecast.tv/embed4.php?u=alibi&vw=640&vh=450&referer=http://livetvweb.net/', 'Alibi', icon_path(info().icon)), ('http://www.finecast.tv/embed4.php?u=thevault&vw=640&vh=450&referer=http://livetvweb.net/', 'The Vault', icon_path(info().icon)), ('http://www.finecast.tv/embed4.php?u=flava&vw=640&vh=450&referer=http://livetvweb.net/', 'Flava', icon_path(info().icon)), ('http://www.finecast.tv/embed4.php?u=bbc2448&vw=640&vh=450&referer=http://livetvweb.net/', 'BBC Two', icon_path(info().icon)), ('http://www.finecast.tv/embed4.php?u=tg47&vw=640&vh=450&referer=http://livetvweb.net/', 'TG4', icon_path(info().icon)), ('http://www.finecast.tv/embed4.php?u=boxoo&vw=640&vh=450&referer=http://livetvweb.net/', 'Box Nation', icon_path(info().icon)), ('http://www.finecast.tv/embed4.php?u=setantaa&vw=640&vh=450&referer=http://livetvweb.net/', 'Setanta Sports', icon_path(info().icon)), ('http://www.finecast.tv/embed4.php?u=rte111&vw=640&vh=450&referer=http://livetvweb.net/', 'RTE One', icon_path(info().icon)), ('http://www.finecast.tv/embed4.php?u=rte222&vw=640&vh=450&referer=http://livetvweb.net/', 'RTE Two', icon_path(info().icon))]
      events.sort(key=lambda x: x[1])
      
      return events

    def resolve(self,url):
        import liveresolver
        return liveresolver.resolve_it(url)