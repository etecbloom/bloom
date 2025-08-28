from enum import Enum

class ExperienceLevel(str, Enum):
    YOUNG = "YOUNG"
    EXPERIENCED = "EXPERIENCED"

class Role(str, Enum):
    MOTHER = "MOTHER"
    FATHER = "FATHER" 
    PROFESSIONAL = "PROFESSIONAL"