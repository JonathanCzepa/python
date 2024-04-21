
class Television():

    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self) -> None:
        self._status = False
        self._muted = False
        self._volume = Television.MIN_VOLUME
        self._channel = Television.MIN_CHANNEL

    def power(self) -> None:
        """
        Method the turns the tv on and off
        """
        self._status ^= True
            
    def mute(self) -> None:
        """
        Method that mutes the tv
        """
        if self._status:
            self._muted ^= True

    def channel_up(self) -> None:
        """
        Method to increase the tv channel
        """
        if self._status:
            if self._channel < Television.MAX_CHANNEL: 
                self._channel += 1
            else:
                self._channel = Television.MIN_CHANNEL

    def channel_down(self) -> None:
        """
        Method to decrease the tv channel
        """
        if self._status:
            if self._channel > Television.MIN_CHANNEL: 
                self._channel -= 1
            else:
                self._channel = Television.MAX_CHANNEL

    def volume_up(self) -> None:
        """
        Method to increase the tv volume
        """
        if self._status:
            self._muted = False
            if self._volume < Television.MAX_VOLUME: 
                self._volume += 1
            

    def volume_down(self) -> None:
        """
        Method to decrease the tv volume
        """
        if self._status:
            self._muted = False
            if self._volume > Television.MIN_VOLUME: 
                self._volume -= 1

    def __str__(self) -> str:
        """
        Method to show the tv status
        :return: tv status.
        """
        if self._muted == True:
            return f"Power = {self._status}, Channel = {self._channel}, Volume = {Television.MIN_VOLUME}"
        else:
            return f"Power = {self._status}, Channel = {self._channel}, Volume = {self._volume}"

