from django.conf.urls import url, include,re_path

from workflow.views import RevicePageData,Console,Mail,Index,NewPro,TicketCreate,MyTicket,TicketDetail,SaveTempFlow,FlowDataFlap,MyToDoTicket,MyRelatedTicket,TickeFlowDetail,AllTicket,TicketFlowStep,TicketFlowBack,TicketFlowlog,GetUserName,TicketBeforeFlowStep,downloadFile# , TicketDetail, TicketCreate


urlpatterns = [
    #控制台
    re_path(r'^$', Index.as_view(), name='workflow-index'),
    #选择工作流页面
    re_path(r'^newpro/$', NewPro.as_view(), name='workflow-newpro'),
    #我创建的
    re_path(r'^my/$', MyTicket.as_view(), name='ticket-my'),
    #我的待办
    re_path(r'^mytodo/$', MyToDoTicket.as_view(), name='ticket-my-todo'),
    #我相关的
    re_path(r'^myrelated/$', MyRelatedTicket.as_view(), name='ticket-my-related'),
    #所有项目
    re_path(r'^all/$', AllTicket.as_view(), name='ticket-all'),
    #工单详情
    re_path(r'^ticket/(?P<ticket_id>[0-9]+)/$',
        TicketDetail.as_view(), name='ticketdetailtable'),
    #业务流程
    re_path(r'(?P<ticket_id>[0-9]+)/flowsteps',
        TicketFlowStep.as_view(), name='ticketflowsteps'),
    #工单日志
    re_path(r'(?P<ticket_id>[0-9]+)/flowlogs',
        TicketFlowlog.as_view(), name='ticketflowlogs'),
    #驳回
    re_path(r'(?P<ticket_id>[0-9]+)/returnflowlogsback',
        TicketFlowBack.as_view(), name='returnflowlogsback'),
    #新建工单
    re_path(r'^ticket/(?P<workflow_id>[0-9]+)/new/$',
        TicketCreate.as_view(), name='ticketcreate'),
    #获取用户名
    re_path(r'^getusername/$',
        GetUserName.as_view(), name='getusername'),
    #项目已操作详情
    re_path(r'(?P<ticket_id>[0-9]+)/beforeflowsteps',
        TicketBeforeFlowStep.as_view(), name='ticketbeforeflowsteps'),
    #下载文件
    re_path(r'(?P<ticket_id>[0-9]+)/download_file',
        downloadFile.as_view(), name='download_file'),
    #查看施工进度
    re_path(r'(?P<ticket_id>[0-9]+)/tickeflowdetail',
        TickeFlowDetail.as_view(), name='tickeflowdetail'),
    #tickeflowdetail.html查询施工进度数据
    re_path(r'(?P<ticket_id>[0-9]+)/flowdataflap',
        FlowDataFlap.as_view(), name='flowdataflap'),
    #提交施工进度数据
    re_path(r'(?P<ticket_id>[0-9]+)/saveTempflow',
        SaveTempFlow.as_view(), name='saveTempflow'),


    #获取控制台信息
    re_path(r'console',
        Console.as_view(), name='console'),
    re_path(r'setpagedata',
        RevicePageData.as_view(), name='setpagedata'),
    ###hook
    re_path(r'emailchange',
            Mail.as_view(), name='emailchange'),

]
