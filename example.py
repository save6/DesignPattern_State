from abc import ABCMeta, abstractmethod

class StatePatternYumichan():
    
    def changeState(self,state):
        self.state = state
    
    def morningGreet(self):
        return self.state.morningGreet()
    
    def getProtectionForCold(self):
        return self.state.getProtectionForCold()

class State(metaclass=ABCMeta):
    @abstractmethod
    def morningGreet(self):
        pass

    @abstractmethod
    def getProtectionForCold(self):
        pass

class BadMoodState(State):
    def morningGreet(self):
        return "おお"
    
    def getProtectionForCold(self):
        return "ももひき"

class OrdinaryState(State):
    def morningGreet(self):
        return "おっす！"
    
    def getProtectionForCold(self):
        return "走る"

class LoveMoodState(State):
    def morningGreet(self):
        return "おはよう"
    
    def getProtectionForCold(self):
        return "ピンクの毛糸のパンツ"

if __name__=='__main__':
    yumi = StatePatternYumichan()
    
    yumi.changeState(BadMoodState())
    print(yumi.morningGreet())
    print(yumi.getProtectionForCold())

    yumi.changeState(OrdinaryState())
    print(yumi.morningGreet())
    print(yumi.getProtectionForCold())

    yumi.changeState(LoveMoodState())
    print(yumi.morningGreet())
    print(yumi.getProtectionForCold())

