# 提供事件解析函数
# 事件解析函数会读入一个事件文件的路径，然后以行为单位解析事件文件


#以下若干行引入各种类的定义
from Define_Character import Character
from Define_Scene import Scene
from Define_Runtime_Env import Runtime_Env
# 不确定这里以后要不要用，引入了运行时环境的定义，但事实上运行时环境是在读取存档时产生的，解析时只是修改


#————[下面是事件解析器本体，代码量很少，哈哈骗你的]————


def EventParser(Path,Current_Runtime_Env):  # 记住，调用解析器的时候，还要传入读取存档后生成的运行时环境
    EventFile_Line_List=EventParser_Read(path)
    EventParser_Parse(EventFile_Line_List,Current_Runtime_Env)
    # 一次处理一整个事件文件，意味着行和行之间可以产生联系，为分支的实现提供便利
    # 记住，要把运行时环境作为参数传入，切记！


#————[下面是事件解析器的各种部件]————


#读入
def EventParser_Read(Path):
    EventFile=open(path,"r")  # 只读模式打开
    EventFile_Line_List=[]  # 一个空列表，一个由事件文件中的行组成的列表
    while True:
        CurrentLine=EventFile.readline()

        if(CurrentLine==""):  # 文件末尾（什么都读不到）处退出
            break
        elif(CurrentLine=="\n"):  # 空行（一个换行符）跳过
            continue

        CurrentLine=CurrentLine.replace("\n","")
        EventFile_Line_List.append(CurrentLine)

    EventFile.close()

    return EventFile_Line_List  # 返回一个由行组成的列表


#解析
def EventParser_Parse(EventFile_Line_List,Current_Runtime_Env):
    Current_Runtime_Env=Current_Runtime_Env # 从参数中初始化一个运行时环境，之后在这里修改

    EventFile_Line_List_Index=0  # 遍历索引初始化
    while EventFile_Line_List_Index<len(EventFile_Line_List):
        CurrentLine=EventFile_Line_List[EventFile_Line_List_Index]

        CurrentLine=CurrentLine.split(" ")  # 在此处将读入的行转化为一个列表，方便后续处理
        CurrentLine_Keyword=EventParser_GetKeyword(CurrentLine)  # 获取关键词（也就是每行的第一个词）

        #定义角色/场景等
        if(CurrentLine_Keyword=="Define"):
            if(CurrentLine[1]=="Character"):
                New_Character=EventParser_Define_Character(CurrentLine)
                Current_Runtime_Env.Character_Dict[New_Character.Id]=New_Character  # 向环境中加入刚刚创建的人物，如果id冲突那就会覆盖
            elif(CurrentLine[1]=="Scene"):
                New_Scene=EventParser_Define_Scene(CurrentLine)
                Current_Runtime_Env.Character_Dict[New_Scene.Id]=New_Scene  # 同上

        #角色好感度上升
        elif(CurrentLine_Keyword=="FavorValue_Up"):
            EventParser_FavorValue_Up(CurrentLine,Current_Runtime_Env)

        #角色好感度下降
        elif(CurrentLine_Keyword=="FavorValue_Down"):
            EventParser_FavorValue_Down(CurrentLine,Current_Runtime_Env)

        EventFile_Line_List_Index+=1  # 哈哈永远不要忘记维护索引，顺便说一句for循环一时爽，还是while好用


#获取事件文件中一行的关键词，其实吧，这个功能基本上是个鸡肋
def EventParser_GetKeyword(EventFile_Line):
    return EventFile_Line[0]


#————[事件解析器的不同解析模式]————


#定义角色
def EventParser_Define_Character(CurrentLine):
    New_Character=Character(
        Id=CurrentLine[2],
        Name=CurrentLine[3],
        Sex=CurrentLine[4],
        FavorValue=CurrentLine[5],
        Interactive_FavorValue=CurrentLine[6],
        Conquest_FavorValue=CurrentLine[7],
        Describe=CurrentLine[8]
    )

    return New_Character


#定义场景
def EventParser_Define_Scene(CurrentLine):
    New_Scene=Scene(
        Id=CurrentLine[2],
        Name=CurrentLine[3],
        Describe=[4],
    )

    return New_Scene


#角色好感度上升
def EventParser_FavorValue_Up(CurrentLine,Current_Runtime_Env):
    Id=CurrentLine[1]
    Value=int(CurrentLine[2])  # 字符串转数字，时刻谨记类型转换
    Character=Current_Runtime_Env[Id]
    Character.FavorValue_Up(Value)


#角色好感度下降
def EventParser_FavorValue_Down(CurrentLine,Current_Runtime_Env):
    Id=CurrentLine[1]
    Value=int(CurrentLine[2])  # 同上
    Character=Current_Runtime_Env[Id]
    Character.FavorValue_Down(Value)

