# -*- coding:utf-8 -*-
# Author : seajay
# Data : 2019-12-25 15:52 
"""
DESC
"""

class Pagination(object):
    def __init__(self,totalCount,currentPage,perPageItemNumber=10,maxPageNum=7):
        # 数据总个数
        self.total_count = totalCount
        #当前页，并做异常处理
        try:
            v = int(currentPage)
            if v <=0:
                v = 1
            self.currentPage = v
        except Exception as E:
            self.currentPage = 1
        # 每页显示的行数、即数据条数
        self.perPageItemNumber = perPageItemNumber
        # 最多显示页码
        self.maxPageNum = maxPageNum

    def start(self):
        return (self.currentPage-1)*self.perPageItemNumber
    def end(self):
        return self.currentPage*self.perPageItemNumber
    @property
    #因为返回值为数值 所以可以转化为静态属性 使用时当做变量即可 省掉括号。
    def num_pages(self):
        """
        总页数
        :return:
        """
        a,b = divmod(self.total_count,self.perPageItemNumber)
        if b == 0:
            return a
        return a+1
    def pager_num_range(self):
        # 总页数 self.per_pager_num
        if self.num_pages < self.maxPageNum:
            return range(1,self.num_pages+1)
        # 总页数特别多的时候
        part = int(self.maxPageNum/2)
        if int(self.currentPage) <= part:
            return range(1,self.maxPageNum+1)
        if self.currentPage+part >self.num_pages:
            return range(self.num_pages-self.maxPageNum,self.num_pages+1)
        return range(int(self.currentPage)-part,int(self.currentPage)+part+1)
    def page_str(self):
        page_list = []
        first = "<li><a href='/fenye?p=1'>首页</a></li>"
        page_list.append(first)
        if self.currentPage == 1:
            prev = "<li><a href='#'>上一页</a></li>"
        else:
            prev = "<li><a href='/fenye?p=%s'>上一页</a></li>"%(self.currentPage-1,)
        page_list.append(prev)
        for i in self.pager_num_range():
            if i == self.currentPage:
                temp = "<li class='active'><a href='/fenye?p=%s'>%s</a></li>"%(i,i)
            else:
                temp = "<li><a href='/fenye?p=%s'>%s</a></li>"%(i,i)
            page_list.append(temp)
        #下一页 先有极限值处理
        if self.currentPage == self.num_pages:
            nex = "<li><a href='#'>下一页</a></li>"
        else:
            nex = "<li><a href='/fenye?p=%s'>下一页</a></li>" % (self.currentPage + 1,)
        page_list.append(nex)
        last = "<li><a href='/fenye?p=%s'>尾页</a></li>"%self.num_pages
        page_list.append(last)
        return ''.join(page_list)