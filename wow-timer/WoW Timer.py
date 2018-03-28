import os, time

def wow_launch():
    os.startfile('E:\\Program Files\World of Warcraft\Wow-64.exe')
    print 'Starting WoW'
    start = time.time()

def wow_close():
    end = time.time()
    print 'Shutting down WoW'

wow_launch()
