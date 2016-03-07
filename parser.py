#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  parser.py
#  
#  Copyright 2016 Bin Ma <binma@thoughtworks.com>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  

import json

Class IParser(object):
	
	NAME_MAP = {'ITEM000001': '可口可乐',
	            'ITEM000002': '羽毛球',
	            'ITEM000003': '苹果' }
	            
	PRICE_MAP = {'ITEM000001': '3',
	             'ITEM000002': '1',
	             'ITEM000003': '6' }	            
	            
    def parse(self, content):
        pass

Class JSONParser(IParser):
	def __init__(self):
		pass
	
	def parse(self, content):
		rawcommodities = json.loads(content)
		purchases = []
		for rawcommodity in rawcommdities:
			segments = rawcommodity.split('-')
			purchase = None
			if segments is not None and segments.length() == 2:
				purchase = CommodityPurchase(Commodity(NAME_MAP.get(segments[0]), PRICE_MAP.get(segments[0]), segments[0]), segments[1])
			if purchase is not None:
				purchases.add(purchase)
		return purchases
