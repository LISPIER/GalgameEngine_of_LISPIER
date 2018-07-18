# 提供一个Data_Reader函数：读取一个存档文件，并返回一个


from Define_Character import Character
from Define_Scene import Scene
from Define_Runtime_Env import Runtime_Env


def Data_Reader(Path):
    Current_Runtime_Env=Runtime_Env()
    # 这里还有一堆东西
    # 设计上应和EventParser保持一致，读和加载部分单独写成函数，这里只是调用
    return Current_Runtime_Env