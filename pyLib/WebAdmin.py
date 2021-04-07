from selenium import webdriver
from time import  sleep
from selenium.webdriver.support.select import Select
from cfg import *


class WebAdmin():
    ROBOT_LIBRARY_SCOPE = "GLOBAL"
    def setupWebsite(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
    def teardownWebsite(self):
        self.driver.quit()
    def loginSystem(self,username,password):
        self.driver.get(MgrLoginUrl)
        self.driver.find_element_by_id("username").send_keys(username)
        self.driver.find_element_by_id("password").send_keys(password)
        self.driver.find_element_by_tag_name("button").click()

#===========================关于课程页面的操作======================================================
    def addCourse(self, courseName, courseDesc, courseIndex):
        # 确保在课程界面操作
        self.driver.find_element_by_css_selector("a[href=\"#/\"]").click()
        sleep(1)
        self.driver.find_element_by_css_selector(
            "button[ng-click=\"showAddOne=true\"]").click()
        ele = self.driver.find_element_by_css_selector(
            "input[ng-model=\"addData.name\"]")
        ele.clear()
        ele.send_keys(courseName)
        ele = self.driver.find_element_by_css_selector(
            "textarea[ng-model=\"addData.desc\"]")
        ele.clear()
        ele.send_keys(courseDesc)
        ele = self.driver.find_element_by_css_selector(
            "input[ng-model=\"addData.display_idx\"]")
        ele.clear()
        ele.send_keys(courseIndex)
        self.driver.find_element_by_css_selector(
            "button[ng-click=\"addOne()\"]").click()
        sleep(1)

    def deleteList(self,flag):
        if flag == "course":
            # 确保在课程界面操作
            self.driver.find_element_by_css_selector(
                "a[href=\"#/\"]").click()
        elif flag == "teacher":
            # 确保在老师界面操作
            self.driver.find_element_by_css_selector(
                "a[href=\"#/teacher\"]").click()
        elif flag =="class":
            # 确保在培训班界面操作
            self.driver.find_element_by_css_selector(
                "a[href=\"#/training\"]").click()
        elif flag=="schedule":
            # 确保在培训班期界面操作
            self.driver.find_element_by_css_selector(
                "a[href=\"#/traininggrade\"]").click()
        elif flag == "student":
            # 确保在学生界面操作
            self.driver.find_element_by_css_selector(
                "a[href=\"#/student\"]").click()
        sleep(1)
        self.driver.implicitly_wait(1)
        while True:
            eles = self.driver.find_elements_by_css_selector(
                "button[ng-click=\"delOne(one)\"]")
            if eles == []:
                break
            eles[0].click()
            self.driver.find_element_by_css_selector(
                "button[class=\"btn btn-primary\"]").click()
            sleep(1)
        self.driver.implicitly_wait(10)

    # 修改课程
    def editCourse(self):
        pass

    # 列出课程
    def listCourse(self):
        # 确保在课程界面操作
        self.driver.find_element_by_css_selector(
            "a[href=\"#/\"]").click()
        sleep(1)
        # courseList = []
        eles = self.driver.find_elements_by_css_selector(
            "tr>td:nth-child(2)")
        # courseList = [ele.text for ele in eles]
        # for ele in eles:
        #     lesson = ele.text
        #     courseList.append(lesson)
        return [ele.text for ele in eles]

#=======================关于老师页面的操作=================================
# 添加老师,teachCourse是一个列表，表示所教授的课程名称
    def addTeacher(self,teacherName,teacherUserName,teacherDesc,teacherIndex,teachCourse):
        # 确保在老师界面操作
        self.driver.find_element_by_css_selector(
            "a[href=\"#/teacher\"]").click()
        self.driver.find_element_by_css_selector(
            "button[ng-click=\"showAddOne=true\"]").click()
        ele = self.driver.find_element_by_css_selector(
            "input[ng-model=\"addEditData.realname\"]")
        ele.clear()
        ele.send_keys(teacherName)
        ele = self.driver.find_element_by_css_selector(
            "input[ng-model=\"addEditData.username\"]")
        ele.clear()
        ele.send_keys(teacherUserName)
        ele = self.driver.find_element_by_css_selector(
            "textarea[ng-model=\"addEditData.desc\"]")
        ele.clear()
        ele.send_keys(teacherDesc)
        ele = self.driver.find_element_by_css_selector(
            "input[ng-model=\"addEditData.display_idx\"]")
        ele.clear()
        ele.send_keys(teacherIndex)

        self.driver.implicitly_wait(1)
        eles = self.driver.find_elements_by_css_selector(
            "button[ng-click=\"addEditData.delTeachCourse(course)\"]")
        for ele in eles:
            ele.click()
        self.driver.implicitly_wait(10)

        select = Select(self.driver.find_element_by_css_selector(
            "select[ng-model=\"$parent.courseSelected\"]"))
        for one in teachCourse:
            select.select_by_visible_text(one)
            self.driver.find_element_by_css_selector(
                "button[ng-click=\"addEditData.addTeachCourse()\"]").click()
        self.driver.find_element_by_css_selector(
            "button[ng-click=\"addOne()\"]").click()
        sleep(2)



    # #删除老师
    # def deleteAllTeacher(self):
    #     # 确保在老师界面操作
    #     self.driver.find_element_by_css_selector(
    #         "a[href=\"#/teacher\"]").click()
    #     self.driver.implicitly_wait(1)
    #     while True:
    #         eles = self.driver.find_elements_by_css_selector(
    #             "button[ng-click=\"delOne(one)\"]")
    #         if eles==[]:
    #             sleep(2)
    #             break
    #         eles[0].click()
    #         self.driver.find_element_by_css_selector("button[class=\"btn btn-primary\"]").click()
    #         sleep(2)
    #     self.driver.implicitly_wait(10)


    # 列出老师
    def listTeacher(self):

        # 确保在老师界面操作
        self.driver.find_element_by_css_selector(
            "a[href=\"#/teacher\"]").click()
        # teacherList = []
        self.driver.implicitly_wait(1)
        eles = self.driver.find_elements_by_css_selector(
            "tr>td:nth-child(2)")
        # for ele in eles:
        #     teacher = ele.text
        #     teacherList.append(teacher)
        # self.driver.implicitly_wait(10)
        return [ele.text for ele in eles]

#==========================关于培训班页面的操作==============
# 添加培训班,containCourse是一个列表，表示所包含的课程名称
    def addClass(self,trainingCourseName,trainingCourseDesc,trainingCourseIndex,containCourse):
        # 确保在培训班界面操作
        self.driver.find_element_by_css_selector(
            "a[href=\"#/training\"]").click()
        sleep(1)
        self.driver.find_element_by_css_selector("button[ng-click=\"showAddOne=true\"]").click()
        ele = self.driver.find_element_by_css_selector(
            "input[ng-model=\"addEditData.name\"]")
        ele.clear()
        ele.send_keys(trainingCourseName)
        ele = self.driver.find_element_by_css_selector("textarea[ng-model=\"addEditData.desc\"")
        ele.clear()
        ele.send_keys(trainingCourseDesc)
        ele = self.driver.find_element_by_css_selector("input[ng-model=\"addEditData.display_idx\"]")
        ele.clear()
        ele.send_keys(trainingCourseIndex)

        self.driver.implicitly_wait(1)
        eles = self.driver.find_elements_by_css_selector(
            "button[ng-click=\"addEditData.delTeachCourse(course)\"]")
        for ele in eles:
            ele.click()
        self.driver.implicitly_wait(10)

        select = Select(self.driver.find_element_by_css_selector(
            "select[ng-model=\"$parent.courseSelected\"]"))
        for one in containCourse:
            select.select_by_visible_text(one)
            self.driver.find_element_by_css_selector(
                "button[ng-click=\"addEditData.addTeachCourse()\"]").click()
        self.driver.find_element_by_css_selector(
            "button[ng-click=\"addOne()\"]").click()
        sleep(2)



    # #删除培训班
    # def deleteAllClass(self):
    #     # 确保在培训班界面操作
    #     self.driver.find_element_by_css_selector("a[href=\"#/training\"]").click()
    #     sleep(1)
    #     self.driver.implicitly_wait(1)
    #     while True:
    #         eles = self.driver.find_elements_by_css_selector("button[ng-click=\"delOne(one)\"]")
    #         if eles==[]:
    #             sleep(2)
    #             break
    #         eles[0].click()
    #         self.driver.find_element_by_css_selector("button[class=\"btn btn-primary\"]").click()
    #         sleep(2)
    #     self.driver.implicitly_wait(10)


    # 列出培训班
    def listTrainingCourseList(self):
        # 确保在培训班界面操作
        self.driver.find_element_by_css_selector(
            "a[href=\"#/training\"]").click()
        sleep(1)
        # trainingCourseList = []
        self.driver.implicitly_wait(1)
        eles = self.driver.find_elements_by_css_selector("tr>td:nth-child(2)")
        # for ele in eles:
        #     trainingCourse = ele.text
        #     trainingCourseList.append(trainingCourse)
        self.driver.implicitly_wait(10)
        return [ele.text for ele in eles]
#===================关于培训班期页面的操作===============================
# 添加培训班期,belongClass是一个列表，表示所属培训班
    def addTrainingSchedule(self, scheduleName, scheduleDesc, scheduleIndex, belongClass):
        # 确保在培训班期界面操作
        self.driver.find_element_by_css_selector(
            "a[href=\"#/traininggrade\"]").click()
        sleep(1)
        self.driver.find_element_by_css_selector(
            "button[ng-click=\"showAddOne=true\"]").click()
        ele = self.driver.find_element_by_css_selector("input[ng-model=\"addEditData.name\"]")
        ele.clear()
        ele.send_keys(scheduleName)
        ele = self.driver.find_element_by_css_selector("textarea[ng-model=\"addEditData.desc\"")
        ele.clear()
        ele.send_keys(scheduleDesc)
        ele = self.driver.find_element_by_css_selector("input[ng-model=\"addEditData.display_idx\"]")
        ele.clear()
        ele.send_keys(scheduleIndex)

        select = Select(self.driver.find_element_by_css_selector(
            "select[ng-model=\"$parent.addEditData.training_id\"]"))
        select.select_by_visible_text(belongClass)

        self.driver.find_element_by_css_selector(
            "button[ng-click=\"addOne()\"]").click()
        sleep(1)

    # # 删除培训班期
    # def deleteTrainingSchedule(self):
    #     # 确保在培训班界面操作
    #     self.driver.find_element_by_css_selector("a[href=\"#/traininggrade\"]").click()
    #     sleep(1)
    #     self.driver.implicitly_wait(1)
    #     while True:
    #         eles = self.driver.find_elements_by_css_selector("button[ng-click=\"delOne(one)\"]")
    #         if eles == []:
    #             sleep(2)
    #             break
    #         eles[0].click()
    #         self.driver.find_element_by_css_selector("button[class=\"btn btn-primary\"]").click()
    #         sleep(2)
    #     self.driver.implicitly_wait(10)

    # 列出培训班期
    def listTrainingScheduleList(self):
        # 确保在培训班期界面操作
        self.driver.find_element_by_css_selector(
            "a[href=\"#/traininggrade\"]").click()
        sleep(1)
        trainingCourseList = []
        self.driver.implicitly_wait(1)
        eles = self.driver.find_elements_by_css_selector(
            "tr>td:nth-child(2)")
        # for ele in eles:
        #     trainingCourse = ele.text
        #     trainingCourseList.append(trainingCourse)
        self.driver.implicitly_wait(10)
        return [ele.text for ele in eles]


#===================关于学生页面的操作===============================
# 添加学生,belongClass是一个字符串，表示所属培训班，belongschedule是一个字符串，表示所属培训班期
    def addStudent(self, studentRealName, studentUserName, studentDesc, belongClass,belongschedule):
        # 确保在学生界面操作
        self.driver.find_element_by_css_selector(
            "a[href=\"#/student\"]").click()
        sleep(1)
        self.driver.find_element_by_css_selector(
            "button[ng-click=\"showAddOne=true\"]").click()
        ele = self.driver.find_element_by_css_selector(
            "input[ng-model=\"addEditData.realname\"]")
        ele.clear()
        ele.send_keys(studentRealName)
        ele = self.driver.find_element_by_css_selector(
            "input[ng-model=\"addEditData.username\"]")
        ele.clear()
        ele.send_keys(studentUserName)
        ele = self.driver.find_element_by_css_selector(
            "textarea[ng-model=\"addEditData.desc\"]")
        ele.clear()
        ele.send_keys(studentDesc)

        select = Select(self.driver.find_element_by_css_selector(
            "select[ng-model=\"$parent.addEditData.training_id\""))
        select.select_by_visible_text(belongClass)

        select = Select(self.driver.find_element_by_css_selector(
            "select[ng-model=\"$parent.addEditData.traininggrade_id\""))
        select.select_by_visible_text(belongschedule)

        self.driver.find_element_by_css_selector(
            "button[ng-click=\"addOne()\"]").click()
        sleep(1)

    # 列出学生
    def listStudentList(self):
        # 确保在学生界面操作
        self.driver.find_element_by_css_selector(
            "a[href=\"#/student\"]").click()
        sleep(1)
        # trainingCourseList = []
        self.driver.implicitly_wait(1)
        eles = self.driver.find_elements_by_css_selector(
            "tr>td:nth-child(1)")
        # for ele in eles:
        #     trainingCourse = ele.text
        #     trainingCourseList.append(trainingCourse)
        self.driver.implicitly_wait(10)
        return [ele.text for ele in eles]