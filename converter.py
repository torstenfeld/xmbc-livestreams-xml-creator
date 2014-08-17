__author__ = 'Torsten'

from iniparse import ConfigParser
import xml.etree.cElementTree as Et
import xml.dom.minidom as minidom
import codecs
import re


class LiveStreamConfig(object):
    def __init__(self):
        self.items = None
        self.nicexml = None
        root = Et.Element('channels')
        # Et.set('encoding','UTF-8')
        # Et.set('standalone','yes')
        self.channels = root

        self._create_channels_info()
        self._create_channel()

    def write(self):
        # raw_string = Et.tostring(self.channels, encoding='utf-8')
        # raw_string = Et.(self.channels, encoding='utf-8')
        # # raw_string = Et.tostring(self.channels, encoding='utf-8', method='html')
        # print raw_string
        # reparsed = minidom.parseString(raw_string)
        # self.nicexml = reparsed.toprettyxml(indent='    ')
        #
        # f = codecs.open('phr3n1c.xml', 'w', encoding='utf-8')
        # f.write(self.nicexml)
        # f.close()

        tree = Et.ElementTree(self.channels)
        tree.write('meinesender.xml')
        # tree.write('meinesender.xml', method='html')

    def create_item(self, channel_name, channel_link, channel_info, channel_genre='TV'):
        items = self.items
        item = Et.SubElement(items, 'item')

        title = Et.SubElement(item, 'title')
        title.text = channel_name
        mylink = Et.SubElement(item, 'link')
        mylink.text = channel_link
        genre = Et.SubElement(item, 'genre')
        genre.text = channel_genre
        info = Et.SubElement(item, 'info')
        info.text = channel_info
        Et.SubElement(item, 'thumbnail')
        date = Et.SubElement(item, 'date')
        date.text = '17.08.2014'
        Et.SubElement(item, 'fanart')
        Et.SubElement(item, 'epg')

    def _create_channel(self):
        channels = self.channels
        channel = Et.SubElement(channels, 'channel')
        Et.SubElement(channel, 'thumbnail')
        Et.SubElement(channel, 'fanart')
        channel_name = Et.SubElement(channel, 'name')
        channel_name.text = 'Deutsche Sender'
        items = Et.SubElement(channel, 'items')
        self.items = items

    def _create_channels_info(self):
        channels = self.channels
        channels_info = Et.SubElement(channels, 'channels_info')

        title = Et.SubElement(channels_info, 'title')
        title.text = 'Torstens Sender'
        genre = Et.SubElement(channels_info, 'genre')
        genre.text = 'TV'
        description = Et.SubElement(channels_info, 'description')
        description.text = 'Livestreams'
        thecredits = Et.SubElement(channels_info, 'credits')
        thecredits.text = 'phr3n1c'
        Et.SubElement(channels_info, 'thumbnail')
        Et.SubElement(channels_info, 'fanart')
        Et.SubElement(channels_info, 'date')


iniparser = ConfigParser()
iniparser.read('sender2.ini')
item_count = int(iniparser.get('playlist', 'NumberOfEntries'))

xml = LiveStreamConfig()

for i in range(1, item_count):
    name = str(iniparser.get('playlist', 'Title' + str(i))).decode('utf-8')
    link = str(iniparser.get('playlist', 'File' + str(i))).decode('utf-8')
    # self, channel_name, channel_link, channel_info, channel_genre='TV'):
    xml.create_item(name, link, name)

xml.write()