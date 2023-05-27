#coding=utf-8
"""
PythonSQL Demo
Python Version 2.7
Python Doc https://docs.python.org/2.7/contents.html


CREATE TABLE IF NOT EXISTS wx_saas.dwd_wx_paas_api_log_d_i (
	f_remote_addr string,
	f_remote_user string,
	f_time_local string,
	f_connection string,
	f_scheme string,
	f_status string,
	f_request_id string,
	f_request_time string,
	f_request_method string,
	f_request_body string,
	f_request_uri string,
	f_request_completion string,
	f_body_bytes_sent string,
	f_http_referer string,
	f_http_user_agent string,
	f_http_x_forwarded_for string,
	f_http_x_real_ip string,
	f_upstream_response_time string,
	f_upstream_connect_time string,
	f_upstream_header_time string,
	f_upstream_response_status string,
	f_upstream_addr string,
	f_server_protocol string,
	f_server_addr string,
	f_request_uri_path string,
	f_request_uri_param string
) PARTITIONED BY (
	year string,
	month string,
	day string
);

"""
import re
import datetime


def TDW_PL(tdw, argv):
    ''' 基本用法
            tdw.execute(sql:str)
                1. 传入sql字符串，多句sql每次只传入一句，不能用分号分隔；
                2. 返回结果默认2万行，应该使用insert或ctas保存海量分析结果；
            tdw.WriteLog(log:str)
                1. 避免使用print打印调试日志；
    '''
    argv=['20221127']
    tdw.WriteLog('PythonSQL dwd_wx_paas_api_log_d_i')
    tdw.WriteLog(argv[0])
    ds = argv[0]
    match = re.match(r"([\d]{4})([\d]{2})([\d]{2})",ds)
    daySub = match.group(1,2,3)

    ds_year = daySub[0]
    ds_month = daySub[1]
    ds_day = daySub[2]

    sql = '''
     insert overwrite table wx_saas::dwd_wx_paas_api_log_d_i partition(year='$year',month='$month',day='$day')
    select
f_remote_addr ,
f_remote_user ,
f_time_local ,
f_connection ,
f_scheme ,
f_status ,
f_request_id ,
f_request_time ,
f_request_method ,
f_request_body ,
f_request_uri ,
f_request_completion ,
f_body_bytes_sent ,
f_http_referer ,
f_http_user_agent ,
f_http_x_forwarded_for ,
f_http_x_real_ip ,
f_upstream_response_time ,
f_upstream_connect_time ,
f_upstream_header_time ,
f_upstream_response_status ,
f_upstream_addr ,
f_server_protocol ,
f_server_addr ,
f_request_uri_path ,
f_request_uri_param 
from etl_wx_saas::ods_wx_kong_log_paas_api_d_i 
    where 
        tdbank_imp_date='$ds'
    '''

    sql = sql.replace('$ds', ds)
    sql = sql.replace('$year', ds_year)
    sql = sql.replace('$month', ds_month)
    sql = sql.replace('$day', ds_day)

    tdw.WriteLog('query_sql=%s' % sql)

    #切换引擎
    tdw.execute("set `supersql.bypass.forceAll` = true;")
    res = tdw.execute(sql)
    tdw.WriteLog(res)


