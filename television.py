

class Television:
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3


    def __init__(self):
        self.__status = False
        self.__muted = False
        self.__volume = Television.MIN_VOLUME
        self.__channel = Television.MIN_CHANNEL

    def power(self):
        """
        toggles power state
        """

        if self.__status:
            self.__status = False
        else:
            self.__status = True

    def mute(self):
        """
        toggles mute
        """
        if self.__status:
            if self.__muted:
                self.__muted = False
            else:
                self.__muted = True

    def channel_up(self):
        """
        changes channel to next one
        """
        if self.__status:
            if self.__channel == Television.MAX_CHANNEL:
                self.__channel = Television.MIN_CHANNEL
            else:
                self.__channel += 1

    def channel_down(self):
        """
        changes channel to previous one
        """
        if self.__status:
            if self.__channel == Television.MIN_CHANNEL:
                self.__channel = Television.MAX_CHANNEL
            else:
                self.__channel -= 1




    def volume_up(self):
        """
        increases volume by 1
        """
        if self.__status:
            if self.__muted:
                self.__muted = False
            if self.__volume == Television.MAX_VOLUME:
                pass
            else:
                self.__volume += 1


    def volume_down(self):
        """
        decreases volume by 1
        """
        if self.__status:
            if self.__muted:
                self.__muted = False
            if self.__volume == Television.MIN_VOLUME:
                pass
            else:
                self.__volume -= 1

    def __str__(self):
        if self.__muted:
            return (f"Power = {self.__status}, Channel = {self.__channel}, Volume = {0}")
        else:
            return (f"Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}")