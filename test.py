#! /usr/bin/env python

from card import Card
card = Card(13091)
card.login('linhongl', "intel,123")
img = card.get_captches()
captcha = card.identify_captchas(img)
card_no = card.submit_captchas(captcha)