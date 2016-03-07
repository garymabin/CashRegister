#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  commodity.py
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

Class Commdity(object):
    
    def __init__(self, name, price, barcode):
        self.name = name
        self.price = price
        self.barcode = barcode
    
    def price(self):
        return self.price
        
    def serialize(self):
        return "Name: %s, Price: %.02f" % (name, price)

Class CommdityPurchase(object):
    
    def __init__(self, commodity, quantity):
        self.commodity = commodity
        self.quantity = quantity
		
    def value(self):
        strategy = self._find_proper_strategy()
        return strategy.apply(self)
    
    def price(self):
		return self.commodity.price()    
        
    def quantity(self):
		return self.quantity
		    
	def _find_proper_strategy(self, strategies):
		best_match = None;
		for strategy in strategies
			if strategy.match(self.commodity):
				if best_match is None or best_match.priority > strategy.priority:
					best_match = strategy;
			
		return best_match	
		
	def serialize(self):
		return ',{0}, Amount: %d'.format(self.commodity.serialize(), self.value())
