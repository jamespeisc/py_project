# 模块导入不会重复，基于字典，模块导入认文件名
# 解释器初始化的时候，会初始化sys.modules字典(保存已加载的模块)，创建buildins（全局函数，常量）模块，__main__模块，sys模块，以及模块搜索路径sys.path
#
# if __name__ == '__main__'的用途
# 1，本模块功能测试 对于非主模块，测试本模块的函数，类
# 2，避免主模块变更的副作用， 顶层代码，没有封装，主模块使用时没有问题，但是，一旦有了新的主模块，老的主模块成了被导入模块，由于原来代码没有封装，一并执行了。

