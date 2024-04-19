
class Television():

    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

def __init__(self):
    self.status == False
    self.muted = False
    self.volume = 0
    self.channel = 0

def power(self):
    if self.status == False:
        self.status = True
    elif self.status == True:
        self.status == False
        
def mute(self):
    if self.muted == False:
        self.muted = True
    elif self.muted == True:
        self.muted == False

def channel_up(self):
    if self.channel < 3:
        self.channel += 1
    else:
        self.channel = 0


def channel_down(self):
    if self.channel > 0:
        self.channel -= 1
    else:
        self.channel = 3

def volume_up(self):
    if self.volume < 2:
        self.volume += 1
    else:
        self.volume = 0


def volume_down(self):
    if self.volume > 0:
        self.volume -= 1
    else:
        self.volume = 2

def __str__(self):
    shit = 'fuck'

    



    