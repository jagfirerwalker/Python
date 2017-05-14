# -*- coding: utf-8 -*-
"""
Created on Mon Oct 24 09:57:15 2016

@author: mathias
"""

from facebookads.adobjects.adaccount import AdAccount
from facebookads.adobjects.adset import AdSet

account = AdAccount('act_<AD_ACCOUNT_ID>')
adsets = account.get_ad_sets(fields=[AdSet.Field.name])

for adset in adsets:
    print(adset[AdSet.Field.name])