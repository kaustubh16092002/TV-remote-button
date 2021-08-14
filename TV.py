class TV:
    def __init__(self):
        self.channel=1
        self.volumelevel=1
        self.on=False
    def turnon(self):
        self.on =True
        
    def turnoff(self):
        self.on =False
    def getchannel(self):
        return self.channel
    def setchannel(self,channel):
        if self.on and 1 <= self.channel <=120:
            self.channel = channel
    def getvolumelevel(self):
        return self.volumelevel
    def setvolume(self,volumelevel):
        if self.on and \
               1 <= self.volumelevel <= 7:
            self.volumelevel= volumelevel
    def channelup(self):
        if self.on and self.channel < 120:
            self.channel +=1
    def channeldown(self):
        if self.on and self.channel >1:
            self.channel -=1
    def volumeup(self):
        if self.on and self.volumelevel < 7:
            self.volumelevel +=1
    def volumedown(self):
        if self.on and self.volumelevel >1:
            self.volumelevel -=1
