#Get Current Stock Price

import json, urllib
from fb.db import db

from twisted.python import log

import fb.intent as intent
from fb.modules.base import FritbotModule, response

class StocksModule(FritbotModule):

	name="Stocks"
	description="Functionality for stock quotes"
	author="Kyle Varga (kyle.varga@bazaarvoice.com)"

	def register(self):
		intent.service.registerCommand("stock", self.stock, self, "Stock Quote", "Returns current Stock Price")

	@response
	def stock(self, bot, room, user, args):
		query = ','.join(args)
		url = "http://www.google.com/finance/info?infotype=infoquoteall&q=" + query
		print 'url= ' + url
		stock_response = urllib.urlopen(url)
		stock_results = stock_response.read()
		if len(stock_results) > 0:
			stock_results = stock_results[3:]
			results = json.loads(stock_results)
			msg = 'Stock Prices for ' + query + '\n'
			for data in results:
				msg += data['name'] + ' opened at $' + data['op'] + ' and is currently at  $' + data["l"] + '\n'
		else:
			msg = 'No stocks found for ' + query
		
		return msg

module = StocksModule()

