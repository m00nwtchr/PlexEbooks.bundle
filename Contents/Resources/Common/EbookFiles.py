#!/usr/bin/env python
import Filter
import os.path

ebook_exts = ['pdf','epub','azw','lit','mobi','odf']

# Remove files that aren't ebooks.
def Scan(path, files, mediaList, subdirs, root=None):
  
  # Filter out bad stuff.
  Filter.Scan(path, files, mediaList, subdirs, ebook_exts, root)
