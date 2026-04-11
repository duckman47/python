import unittest

from television import Television


class MyTestCase(unittest.TestCase):
    def test_init(self):
        tv1=Television()
        self.assertEqual((str(tv1))[8], "F")
        self.assertEqual((str(tv1))[25], "0")
        self.assertEqual((str(tv1))[37], "0")

    def test_power(self):
        tv2 = Television()
        self.assertEqual((str(tv2))[8], "F")
        tv2.power()
        self.assertEqual((str(tv2))[8], "T")


    def test_mute(self):
        tv3 = Television()
        tv3.power()
        tv3.volume_up()
        tv3.mute()
        self.assertEqual((str(tv3))[36], 0)
        tv3.mute()
        self.assertEqual((str(tv3))[36], 1)
        tv3.power()
        tv3.mute()
        self.assertEqual((str(tv3))[37], 1)
        tv3.mute()
        self.assertEqual((str(tv3))[37], 1)


    def test_channel_up(self):
        tv4 = Television()
        tv4.channel_up()
        self.assertEqual((str(tv4))[25], 0)
        tv4.power()
        tv4.channel_up()
        self.assertEqual((str(tv4))[24], 1)
        tv4.channel_up()
        tv4.channel_up()
        tv4.channel_up()
        self.assertEqual((str(tv4))[24], 0)


    def test_channel_down(self):
        tv5 = Television()
        tv5.channel_down()
        self.assertEqual((str(tv5))[25], 0)
        tv5.power()
        tv5.channel_down()
        self.assertEqual((str(tv5))[24], 3)


    def test_volume_up(self):
        tv6 = Television()
        tv6.volume_up()
        self.assertEqual((str(tv6))[37], 0)
        tv6.power()
        tv6.volume_up()
        self.assertEqual((str(tv6))[36], 1)
        tv6.mute()
        tv6.volume_up()
        self.assertEqual((str(tv6))[36], 2)
        tv6.volume_up()
        self.assertEqual((str(tv6))[36], 2)



    def test_volume_down(self):
        tv7 = Television()
        tv7.volume_down()
        self.assertEqual((str(tv7))[37], 0)
        tv7.power()
        tv7.volume_up()
        tv7.volume_up()
        tv7.volume_down()
        tv7.volume_down()
        self.assertEqual((str(tv7))[36], 0)
        tv7.mute()
        tv7.volume_down()
        self.assertEqual((str(tv7))[36], 0)
        tv7.volume_down()
        self.assertEqual((str(tv7))[36], 0)



if __name__ == '__main__':
    unittest.main()
