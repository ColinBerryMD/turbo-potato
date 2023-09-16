# turbo-potato

 Flask app to serve my private files with password protection.

A note on directory structure. The blueprint layout is after https://realpython.com/flask-blueprint/. 
The root (file-server) has app.py and extension.py after cbmd/fluffy waffle. files.py is included as a blueprint in order to facilitate exporting it into fluffy-waffle. 

The idea is to serve the directory via xml/xsl allowing downloads or raw html or pdfs.
