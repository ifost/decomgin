
class Multiple:
    def __init__(self,name,identifier,ofWhat=None):
        """identifier is the keyname of the key that will be provided in
        the <TAG KEYNAME=1234> to uniquely identify each instance"""
        self.name = name
        self.ofWhat = ofWhat
        self.identifier = identifier

class Single:
    def __init__(self,name,ofWhat=None):
        self.name = name
        self.ofWhat = ofWhat

######################################################################

# anything can split into a text/signature part... instead of just
# having the text
replyTo = [ Single('PROTOCOL'),Single('SERVER'),Single('DETAILS') ]
lineItem = [ Single('PRODUCT'),Single('QUANTITY'),Single('UNITS'),
             Single('DELIVERY-ADDRESS'),Single('PRICE') ]
purchaseOrder = [ Multiple('LINE-ITEM','ITEM-NUM',lineItem),
                  Single('OUR-PURCHASE-ORDER-NUM'),
                  Single('PLACED-BY'),
                  Single('DATE'),
                  Single('TIMESTAMP'),
                  Multiple('REPLY-TO','PREF',replyTo) ]

######################################################################
