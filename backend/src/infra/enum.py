import enum

class ExpLevelEnum(str, enum.Enum):
    NOVICE = "NOVICE"
    VETERAN =  "VETERAN"

class RoleEnum(str, enum.Enum):
    MOM = "MOM"
    FATHER = "FATHER"
    PSYCHOLOGIST = "PSYCHOLOGIST"
    GYNECOLOGIST = "GYNECOLOGIST"