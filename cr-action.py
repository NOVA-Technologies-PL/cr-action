import enum

#Typy akcji
class ActionType(enum.Enum):
    ACTION_TYPE_UNKNOWN = 0
    ACTION_TYPE_SPAWN = 1
    ACTION_TYPE_FILTER = 2
    ACTION_TYPE_WITH_DURATION = 3

#klasa akcji bazowej
class Action:
    def __init__(self, type: ActionType, options: dict):
        self.type = type
        self.options = options
        
#klasa akcji spawn
class ActionSpawn(Action):
    def __init__(self, type: ActionType, options: dict):
        super().__init__(type, options)
        self.spawnType = options.get("spawnType", "CardType")
        self.spawnData = options.get("spawnData", None)
        self.spawnTime = options.get("spawnTime", 0)

#klasa akcji filtrującej
class ActionFilter(Action):
    def __init__(self, type: ActionType, options: dict):
        super().__init__(type, options)
        self.condition = options.get("condition", None)
        self.onTrueAction = options.get("onTrueAction", None)
        self.onFalseAction = options.get("onFalseAction", None)

#klasa skcji z czasem trwania
class ActionWithDuration(Action):
    def __init__(self, type: ActionType, options: dict):
        super().__init__(type, options)
        self.actionDuration = options.get("actionDuration", 0)
        self.gameTagsToSet = options.get("gameTagsToSet", [])
        self.nextAction = options.get("nextAction", None)

#Tworzy nową akcję

def createAction(type: ActionType, options: dict) -> Action:
    if type == ActionType.ACTION_TYPE_SPAWN:
        return ActionSpawn(type, options)
    elif type == ActionType.ACTION_TYPE_FILTER:
        return ActionFilter(type, options)
    elif type == ActionType.ACTION_TYPE_WITH_DURATION:
        return ActionWithDuration(type, options)
    else:
        return Action(type, options)

#wywoluje akcje
def executeAction(action: Action):
    pass
