# 定义角色


class Character():
    Id="Unknown"
    Name="Unknown"
    Sex="Unknown"
    FavorValue=0
    Interactive_FavorValue=0
    Conquest_FavorValue=0
    Describe="Unknown"

    def __init__(self,Id,Name,Sex,FavorValue,Interactive_FavorValue,Conquest_FavorValue,Describe):
        self.Id=Id
        self.Name=Name
        self.Sex=Sex
        self.FavorValue=FavorValue
        self.Interactive_FavorValue=Interactive_FavorValue
        self.Conquest_FavorValue=Conquest_FavorValue
        self.Describe=Describe

    def FavorValue_Up(self,Value):
        self.FavorValue+=Value

    def FavorValue_Down(self,Value):
        self.FavorValue-=Value

