#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  strategy.py
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


Class IStrategy(object):
    def apply(self, commodity, amount=0):
        pass
    
    def match(self, commodity):
		return True
	
	def get_priority(self):
		return self.priority	

Class ThreeForTwoStrategy(IStrategy):
    def _init_(self):
        pass
    
    def apply(self, commodity, quantity):
        if quantity > 2    
    
Class PercentileDiscountStrategy(IStrategy):
    def _init_(self, discount):
        self.discount = discount
    
    def apply(self, commodity, quantity):
        return commodity.price() * 0.95 * quantity 

