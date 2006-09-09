import sgmllib


class PreferenceStatement(sgmllib.SGMLParser):
    def __init__(self):
        sgmllib.SGMLParser.__init__(self)
        self.internal_state_stack = []
        self.data = ''
        self.everything = None
        
    def start_preferences(self,*args):
        print "Start_pref: I got ",`args`,"for arguments"
        newstate = CollectiveItem('PREFERENCES-LIST',WholeCaboodle)
        self.internal_state_stack = [newstate] + self.internal_state_stack
    def end_preferences(self,*args):
        print "End_pref: I got ",`args`,"for arguments"
        self.everything = self.internal_state_stack[0].finalise()
        self.internal_state_stack = self.internal_state_stack[1:]

    def start_text(self,*args):
        print "Start text: I got ",`args`,"for arguments"
        newstate = TextualItem('TEXT',TextPortion)
        self.internal_state_stack = [newstate] + self.internal_state_stack
    def end_text(self):
        textbit = self.internal_state_stack[0]
        part_of = self.internal_state_stack[1]
        part_of.append(textbit.name(),textbit.finalise())
        self.internal_state_stack = self.internal_state_stack[1:]

    def start_signature(self,*args):
        print "Start text: I got ",`args`,"for arguments"
        newstate = TextualItem('SIGNATURE',SignaturePortion)
        self.internal_state_stack = [newstate] + self.internal_state_stack
    def end_signature(self):
        textbit = self.internal_state_stack[0]
        part_of = self.internal_state_stack[1]
        part_of.append(textbit.name(),textbit.finalise())
        self.internal_state_stack = self.internal_state_stack[1:]

        
    def handle_data(self,data):
        if len(data)==0: return
        if len(self.internal_state_stack)==0:
            print "NOT HANDLING:....",data
        #if self.internal_state_stack
        self.internal_state_stack[0].handle(data)

class State:
    def __init__(self,name):
        self.__name = name
    def handle(self,data): pass
    def name(self): return self.__name

class TextualItem(State):
    def __init__(self,name,constructor):
        State.__init__(self,name)
        self.data = ''
        self.constructor = constructor
    def handle(self,data):
        self.data = self.data + data
    def finalise(self):
        return self.constructor(self.data)
class CollectiveItem(State):
    def __init__(self,name,constructor):
        self.__items = {}
        State.__init__(self,name)
        self.constructor = constructor
    def handle(self,data):
        print "Ignooring data",data
    def append(self,name,item):
        self.__items[name] = item
    def finalise(self):
        return self.constructor(self.__items)


class WholeCaboodle:
    def __init__(self,dictionary):
        self.text = dictionary['TEXT']
        self.signature = dictionary['SIGNATURE']

class TextPortion:
    def __init__(self,blat):
        self.blat = blat

class SignaturePortion:
    def __init__(self,content):
        self.content=content

