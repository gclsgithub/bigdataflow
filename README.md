## ——待办任务——
1. 分页问题
2. 驳回提示"必填"bug
3. 等待发布测试发邮件问题

## ——未来版本——
1.  修改admin页面：用户添加电话信息（名字改成姓名，姓氏改成电话）
2.  发短信

## ——以下已完成——
1. 参考workflow和shutongflow，是否要建立bigdataflow
2. 写一个页面，连接上接口
3. 完成一个110工法页面显示，调用loonflow里的任意一张表
4. 梳理bigdataflow项目的思维导图
5. 继续研究loonflow的接口调用，接口获取数据在bigdataflow中的使用方法
6. 验证详情页面控件填写的数据，能否传到数据库，结果传不到数据库
7. 弄清楚suggestion字段是怎么传到后台数据库的，自定义字段怎么按照suggestion方式上传数据库
8. 学习html的控件标签，补齐详情页面的其他的几个控件
9. 文件上传控件与文件上传下载的的实现
10. 驳回功能
11. 文件保存多级目录
12. 第二步审核时看到第一步填写的内容（完成)
13. 文件下载，鼠标提示的链接（完成）
14. 驳回时，可以不填写必填控件 (完成)
15. 一个split()bug       （完成）
16. 业务流程比较难看   （完成）
17. 三方会签注意控件     （完成）
18. 文件上传只保存了一个，项目名称顺序 ，项目编号只在待办显示全（完成）
19. “标题”改成“项目名称”前端处理，施工进度横条可视化  （完成）
20. 结束项目的“工单详情”信息展示（展现表单），可下载所有文件  （完成）
21. 所有工单只能管理员、专家看，其他人只能待办、相关，创建工单只能企业和管理员  (完成)
22. 施工进度横条（看需求再定，让除现场人员的其他人也可以看，放在操作处或者详情页面）   （完成）
23. 上一步工单详情，弄成按照流程的报表形式（目前是后台添加控件，流程报表形式的话需要改loonflow接口）（师弟修改控件顺序）
24. 参考lonnflow可视化，制作控制台的可视化展示   （完成）
25. 建议项目编号110/N00+年份+编号，并且建议项目编号可更改（项目编号处理前显示“等待指定”，处理后显示对应的项目编号）

## 固定且不能改变的字段
b_guanliyuanshenpi_char_xiangmuliushuihao

g_sanfanghuiqian_text_sanfanghuiqian

        loonflow                          物理名      db
b_guanliyuanshenpi_char_xiangmubianhao  项目编号   project_id

> 新增

FLOWINPUTSTR
   * 总恒阻锚索/米               j_shigongjindu_float_zonghengzumaosuo
   * 当前已完成恒阻锚索/米        j_shigongjindu_float_muqianhengzumaosuo
   * 总切缝钻孔/米               j_shigongjindu_float_zongqiefengzhuankong
   * 当前已完成切缝钻孔/米        j_shigongjindu_float_muqianqiefengzhuankong
   * 总爆破裂缝/米               j_shigongjindu_float_zongbaopoliefeng
   * 当前已完成爆破裂缝/米        j_shigongjindu_float_muqianbaopoliefeng


## 关于数据保存工单信息的想法

> 进入 施工进度
* 查看 -- 数据库查询数据
* 保存 -- 数据库插入数据

## TODO 顾
[] 整合固定字段
[] 单独显示进度条
[] 数据柏村    

安装
python -m pip install djangorestframework

建议项目编号110/N00+年份+编号，并且建议项目编号可更改（项目编号处理前显示“等待指定”，处理后显示对应的项目编号）
add:
    1.创建公单  ok
    2.修改公单  (流程流转) ok
update
    1.修改工单 (流程流转) ok
 show 
    1.allticket
    2.index
    3.my
    4.myrelated
    5.mytodo
    6.修改公单

