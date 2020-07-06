from django.conf.urls import url, include,re_path

from workflow.views import Index,NewPro,TicketCreate,MyTicket,TicketDetail,SaveTempFlow,FlowDataFlap,MyToDoTicket,MyRelatedTicket,TickeFlowDetail,AllTicket,TicketFlowStep,TicketFlowBack,TicketTransition,TicketFlowlog,GetUserName,TicketBeforeFlowStep,downloadFile# , TicketDetail, TicketCreate


urlpatterns = [
    re_path(r'^$', Index.as_view(), name='workflow-index'),
    #控制台
    re_path(r'^newpro/$', NewPro.as_view(), name='workflow-newpro'),
    #选择工作流页面
    re_path(r'^my/$', MyTicket.as_view(), name='ticket-my'),
    #我创建的
    re_path(r'^mytodo/$', MyToDoTicket.as_view(), name='ticket-my-todo'),
    #我的待办
    re_path(r'^myrelated/$', MyRelatedTicket.as_view(), name='ticket-my-related'),
    #我相关的
    re_path(r'^all/$', AllTicket.as_view(), name='ticket-all'),
    #所有项目
    re_path(r'^ticket/(?P<ticket_id>[0-9]+)/$',
        TicketDetail.as_view(), name='ticketdetailtable'),
    #工单详情
    re_path(r'(?P<ticket_id>[0-9]+)/flowsteps',
        TicketFlowStep.as_view(), name='ticketflowsteps'),
    #业务流程
    re_path(r'(?P<ticket_id>[0-9]+)/flowlogs',
        TicketFlowlog.as_view(), name='ticketflowlogs'),
    #工单日志
    re_path(r'(?P<ticket_id>[0-9]+)/returnflowlogsback',
        TicketFlowBack.as_view(), name='returnflowlogsback'),
    #驳回
    re_path(r'(?P<ticket_id>[0-9]+)/transitions',
        TicketTransition.as_view(), name='tickettranstion'),
    #工单流转
    re_path(r'^ticket/(?P<workflow_id>[0-9]+)/new/$',
        TicketCreate.as_view(), name='ticketcreate'),
    #新建工单
    re_path(r'^getusername/$',
        GetUserName.as_view(), name='getusername'),
    #获取用户名
    re_path(r'(?P<ticket_id>[0-9]+)/beforeflowsteps',
        TicketBeforeFlowStep.as_view(), name='ticketbeforeflowsteps'),
    #项目已操作详情
    re_path(r'(?P<ticket_id>[0-9]+)/download_file',
        downloadFile.as_view(), name='download_file'),
    #下载文件
    re_path(r'(?P<ticket_id>[0-9]+)/tickeflowdetail',
        TickeFlowDetail.as_view(), name='tickeflowdetail'),
    #查看施工进度
    re_path(r'(?P<ticket_id>[0-9]+)/flowdataflap',
        FlowDataFlap.as_view(), name='flowdataflap'),
    #tickeflowdetail.html查询施工进度数据
    re_path(r'(?P<ticket_id>[0-9]+)/saveTempflow',
        SaveTempFlow.as_view(), name='saveTempflow'),
    #提交施工进度数据
]
