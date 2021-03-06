#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  untitled.py
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


Class Casher(object):
	
    def __init__(self):
        self.printer = Printer()
        self.parsers = {}
        self.purchases = []
    
    def output(self):
		total_price = 0
        for purchase in self.purchases:
			total_price += purchase.quantity() * purchase.price()
			saved_price += total_price - purchase.value(strategies)
			for 
            print purchase.serialize()
        print 'Total Price is %d, Saved Price is %d' % (total_price, saved_price)    

	def register_parser(method, parser):
		self.parsers[method] = parser

    def register_strategy(strategy):
		self.strategies.add(strategy)
		
	def read_from(self, parse_method, content_string):
		if parse_method == 'JSON':
			self.purchases = self.parsers[parse_method].parse(content_string)
		else:
		   pass
		   
	def clear(self):
		self.purchases = []
