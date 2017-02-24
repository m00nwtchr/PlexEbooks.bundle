import os, os.path, time
import Filter, Media, EbookFiles

# Scans through files, and add to the media list.
def Scan(path, files, mediaList, subdirs, language=None, root=None, **kwargs):
  
  # Filter out bad stuff.
  EbookFiles.Scan(path, files, mediaList, subdirs, root)
  
  # Add all the ebooks to the list.
  for path in files:
    file = os.path.basename(path)
    title,ext = os.path.splitext(file)
    Ebook = Media.Ebook(title)
    
    # Creation date, year.
    created_at = time.localtime(os.path.getmtime(path))
    Ebook.released_at = time.strftime('%Y-%m-%d', created_at)
    Ebook.year = int(time.strftime('%Y', created_at))
    
    Ebook.parts.append(path)
    mediaList.append(Ebook)