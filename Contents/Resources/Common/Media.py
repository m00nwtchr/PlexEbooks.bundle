class MediaRoot:
  def __init__(self, type):
    self.name = ''
    self.year = None
    self.type = type
    self.parts = []
    self.subtitles = []
    self.thumbs = []
    self.arts = []
    self.trailers = []
    self.released_at = None
    self.display_offset = 0
    self.source = None
    self.themes = []
class Ebook(MediaRoot):
  def __init__(self, title):
    MediaRoot.__init__(self, 'Ebook')
    self.name = title
