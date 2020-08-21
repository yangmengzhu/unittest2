import HTMLTestRunner
import os
import sys
import time
import unittest


#def createsuite():
    # suite=unittest.TestSuite()
    # suite.addTest(baidu20.baidu02("test_hao"))
    # suite.addTest(baidu20.baidu02("test_baidusearch"))
    # suite.addTest(baidu19.baidu01("test_hao"))
    # return suite
    # suite=unittest.TestSuite()
#     # suite.addTest(unittest.makeSuite(baidu19.baidu01) )
#     # suite.addTest(unittest.makeSuite(baidu20.baidu02))
#     # return suite
# def createsuite():
#      suite1=unittest.TestLoader().loadTestsFromTestCase(baidu19.baidu01)
#      suite2=unittest.TestLoader().loadTestsFromTestCase(baidu20.baidu02)
#      suite=unittest.TestSuite([suite1,suite2])
#      return suite

def createsuite():
    discovers=unittest.defaultTestLoader.discover("..", pattern="baidu*.py", top_level_dir=None)
    return discovers

if __name__=="__main__":
    # suite=createsuite()
    # runner=unittest.TextTesctRunner(verbosity=2)
    # runner.run(suite)
    curpath=sys.path[0]
    #创建一个存放报告的文件夹
    if not os.path.exists(curpath+'/resultreport'):
        os.makedirs(curpath+'/resultreport')
    #解决文件名相同的问题（根据时间取名）
    now=time.strftime("%Y-%m-%d %H-%M-%S",time.localtime(time.time()))
    file_name=curpath+'/resultreport'+now+'resultreport.html'
    #打开文件跑测试用例
    with open(file_name,'wb') as fp:
        runner=HTMLTestRunner.HTMLTestRunner(stream=fp,title=u"测试报告"
                                             ,description=u"用例执行结果",verbosity=2)
        suite = createsuite()
        runner.run(suite)

