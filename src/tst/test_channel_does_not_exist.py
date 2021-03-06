#!/usr/bin/env python
# -*- coding: utf-8 -*-
from unittest import TestCase
from channel_does_not_exist import ChannelDoesNotExist


class TestChannelDoesNotExistException(TestCase):

    def testChannelDoesNotExistException(self):
        with self.assertRaises(ChannelDoesNotExist):
            raise ChannelDoesNotExist()
