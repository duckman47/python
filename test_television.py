import pytest

from television import Television

class Test:


    def setup_method(self):
        self.tv1 = Television()
        self.tv2 = Television()
        self.tv3 = Television()
        self.tv4 = Television()
        self.tv5 = Television()
        self.tv6 = Television()
        self.tv7 = Television()

    def teardown_method(self):
        del self.tv1
        del self.tv2
        del self.tv3
        del self.tv4
        del self.tv5
        del self.tv6
        del self.tv7





    def test_init(self):

        assert str(self.tv1) == "Power = False, Channel = 0, Volume = 0"



    def test_power(self):

        assert str(self.tv2)== "Power = False, Channel = 0, Volume = 0"
        self.tv2.power()
        assert str(self.tv2)== "Power = True, Channel = 0, Volume = 0"


    def test_mute(self):

        self.tv3.power()
        self.tv3.volume_up()
        self.tv3.mute()
        assert str(self.tv3) == "Power = True, Channel = 0, Volume = 0"
        self.tv3.mute()
        assert str(self.tv3) == "Power = True, Channel = 0, Volume = 1"
        self.tv3.power()
        self.tv3.mute()
        assert str(self.tv3) == "Power = False, Channel = 0, Volume = 1"
        self.tv3.mute()
        assert str(self.tv3) == "Power = False, Channel = 0, Volume = 1"


    def test_channel_up(self):

        self.tv4.channel_up()
        assert str(self.tv4) =="Power = False, Channel = 0, Volume = 0"
        self.tv4.power()
        self.tv4.channel_up()
        assert str(self.tv4) =="Power = True, Channel = 1, Volume = 0"
        self.tv4.channel_up()
        self.tv4.channel_up()
        self.tv4.channel_up()
        assert str(self.tv4) =="Power = True, Channel = 0, Volume = 0"


    def test_channel_down(self):

        self.tv5.channel_down()
        assert str(self.tv5) =="Power = False, Channel = 0, Volume = 0"
        self.tv5.power()
        self.tv5.channel_down()
        assert str(self.tv5) =="Power = True, Channel = 3, Volume = 0"


    def test_volume_up(self):

        self.tv6.volume_up()
        assert str(self.tv6) =="Power = False, Channel = 0, Volume = 0"
        self.tv6.power()
        self.tv6.volume_up()
        assert str(self.tv6) =="Power = True, Channel = 0, Volume = 1"
        self.tv6.mute()
        self.tv6.volume_up()
        assert str(self.tv6) =="Power = True, Channel = 0, Volume = 2"
        self.tv6.volume_up()
        assert str(self.tv6) =="Power = True, Channel = 0, Volume = 2"


    def test_volume_down(self):

        self.tv7.volume_down()
        assert str(self.tv7) =="Power = False, Channel = 0, Volume = 0"
        self.tv7.power()
        self.tv7.volume_up()
        self.tv7.volume_up()
        self.tv7.volume_down()
        self.tv7.volume_down()
        assert str(self.tv7) =="Power = True, Channel = 0, Volume = 0"
        self.tv7.mute()
        self.tv7.volume_down()
        assert str(self.tv7) =="Power = True, Channel = 0, Volume = 0"
        self.tv7.volume_down()
        assert str(self.tv7) =="Power = True, Channel = 0, Volume = 0"



















