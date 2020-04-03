import requests
import json
import pymysql
import datetime


class GetDatabaseValue:

    def __init__(self, severVersion=222):
        self.severVersion = int(severVersion)
        self.urlPort = ':8002'
        if self.severVersion == 179:
            self.host = '192.168.100.179'
            self.databasePort = 3306
            self.databaseUser = 'root'
            self.databasePWD = 'Resico@2018'
        elif self.severVersion == 222:
            self.host = '39.104.18.222'
            self.databasePort = 3306
            self.databaseUser = 'root'
            self.databasePWD = 'resico2019Test'
        else:
            print('版本号不为179或222，请重新实例化')
            exit()


    '''
    连接数据库查询数据的方法
    入参为 sql语句
    return sql执行结果
    '''
    def conn_mysql(self, sql):
        conne_mysql = pymysql.connect(host=self.host, port=self.databasePort,
                                user=self.databaseUser, passwd=self.databasePWD, db='tom', charset='utf8')
        # 获取游标
        cursor = conne_mysql.cursor()
        # 获取登录密码
        cursor.execute(sql)
        resultSet = cursor.fetchall()
        cursor.close()
        conne_mysql.close()
        return resultSet

    '''
    获取所有接口请求头中鉴权值的方法
    入参 用户名
    连接数据库 查询该用户名密码后调用登陆接口模拟登陆获取
    return AuthenValue
    '''
    def getAuthenValue(self, userName):
        '''
        获取鉴权值的方法
        return authentication_value
        '''
        logInPWD = ''
        userName = str(userName)
        conn_mysql = GetDatabaseValue(self.severVersion)
        sql_getPwd = "SELECT pswd from tom.user where loginName=" + \
              "'" + userName + "';"
        passwordResult = conn_mysql.conn_mysql(sql_getPwd)
        for i in passwordResult:
            logInPWD = i[0]
        # 通过登录接口获取鉴权值
        urlLogIn = "http://" + self.host + self.urlPort + "/auth/oauth/token"
        headLogIn = {"Content-Type": "application/x-www-form-urlencoded",
                     "Authorization": "Basic YWRtaW4xOmFkbWluMQ=="}
        bodyLogIn = {"grant_type": "password", "auth_sys": "CSPC",
                     "username": userName, "password": logInPWD}
        # bodyLogIn_json = json.dumps(bodyLogIn)
        LogInRequest = requests.post(
            url=urlLogIn, data=bodyLogIn, headers=headLogIn)
        print("登录结果为 ", LogInRequest.status_code)
        if LogInRequest.status_code == 200:
            pass
        else:
            print('LogIn登录接口请求失败..')
            exit()
        logInResult = eval(LogInRequest.text)
        authentication_value = str.capitalize(
            logInResult['token_type']) + ' ' + logInResult['access_token']
        Authorization = authentication_value
        return Authorization

    '''
    入参 salemanName 销售名称
    获取销售Id的方法
    return user表salemanId
    '''
    def getSalemanId(self, salemanName):
        salemanName = str(salemanName)
        sql_getSalemanId = "SELECT id from tom.user where name=" + \
              "'" + salemanName + "';"
        conn_mysql = GetDatabaseValue(self.severVersion)
        salemanIdResult = conn_mysql.conn_mysql(sql_getSalemanId)
        for i in salemanIdResult:
            salemanId = i[0]
        return salemanId

    '''
    获取线索id
    入參 手机号码
    return crm_clue_manage表中的culeId
    '''
    def getCuleId(self, customerPhone):
        customerPhone = str(customerPhone)
        sql_queryCuleId = "SELECT id from tom.crm_clue_manage where main_contact_tel=" + \
              "'" + customerPhone + "';"
        conn_mysql = GetDatabaseValue(self.severVersion)
        culeIdResult = conn_mysql.conn_mysql(sql_queryCuleId)
        for i in culeIdResult:
            culeId = i[0]
        return culeId

    '''
    获取地址参数
    入参 第三级地址（区域名称）
    返回元组(区域code 区域名称 市code 市名称 省code 省名称)
    '''

    def get_customer_addressInfo(self, areaName):
        areaName = str(areaName)
        sql_queryAddressInfo = "SELECT a.`code`,a.`name`,c.`code`,c.`name`,p.`code`,p.`name` FROM c_area a LEFT JOIN c_city c " \
              "ON a.cityCode = c.`code` LEFT JOIN c_province p ON a.`provinceCode` = p.`code`" \
              "WHERE a.name = " + "'" + areaName + "';"
        conn_mysql = GetDatabaseValue(self.severVersion)
        addressInfoResult = conn_mysql.conn_mysql(sql_queryAddressInfo)
        for i in addressInfoResult:
            addressInfo = addressInfoResult[0]
        return addressInfo

    '''
    获取行业code
    入参 行业名称
    返回 行业code
    '''
    def get_tradeCode(self, tradeName):
        tradeName = str(tradeName)
        sql_query_tradeCode = "SELECT DISTINCT(pCode) from belongindustry where pName="+"'" + tradeName + "';"
        conn_mysql = GetDatabaseValue(self.severVersion)
        tradeCodeResult = conn_mysql.conn_mysql(sql_query_tradeCode)
        for i in tradeCodeResult:
            tradeCode = tradeCodeResult[0][0]
        return tradeCode


class CrmInfoWarn:

    '''
    发送请求类
    '''
    def __init__(self, userName='17585571190', severVersion=222):
        self.userName = userName
        self.severVersion = int(severVersion)
        '''
        获取鉴权值
        '''
        getValue = GetDatabaseValue(self.severVersion)
        Authorization = getValue.getAuthenValue(self.userName)
        header_value = {"Content-Type": "application/json",
                        "Authorization": Authorization}
        self.header_value = header_value
        self.urlPort = ':8002'
        '''
        利用传入服务器版本号判断主机和数据库地址
        '''
        if self.severVersion == 179:
            self.host = '192.168.100.179'
        elif self.severVersion == 222:
            self.host = '39.104.18.222'
        else:
            print('版本号不为179或222，请重新实例化')
            exit()

    # 发送生成新线索的请求方法
    def createNewClue(self, customerPhone):
        '''
        根据传入参数生成公司名称
        return 线索ID
        '''
        customerPhone = str(customerPhone)
        nowTime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        cityName = '深圳市'
        provinceName = '广东省'
        print('新增区域为', provinceName, ' ', cityName, '联系人电话为:', customerPhone, '新增时间:', nowTime)
        # 发送新增线索请求，获取线索id
        url_new_clue = "http://" + self.host + self.urlPort + "/crm/clue/manage"
        body_newclue = {"businessTime": nowTime, "cityCode": "4403", "cityName": cityName, "contact": {"tels": [
            customerPhone]}, "customerType": "1001", "industryCode": 1013, "provinceCode": "44", "provinceName":provinceName,
                        "trafficSourceId": "2c9858696e5d3d60016e5d47c29400c4"}  #
        body_newclue_json = json.dumps(body_newclue)
        createNewCluePost = requests.post(
            url_new_clue, data=body_newclue_json, headers=self.header_value)
        print("新增线索接口code： ", createNewCluePost.status_code)
        print("新增线索详情： ", createNewCluePost.text)
        if createNewCluePost.status_code == 200:
            getValue = GetDatabaseValue(self.severVersion)
            culeID_value = getValue.getCuleId(customerPhone)
            return culeID_value
        else:
            print('createNewClue接口请求失败..')
            exit()

    # 发送放入线索库的请求，该请求需要获取线索id
    def putInClueLibary(self, PutInculeId):
        PutInculeId = str(PutInculeId)
        # 调用创建线索的方法直接生成线索
        urlPutInLib = "http://" + self.host + self.urlPort + "/crm/clue/manage/" + \
                      PutInculeId + "/depot"
        PutInLibPATCH = requests.patch(
            urlPutInLib, headers=self.header_value)
        print('放入线索库code:', PutInLibPATCH.status_code)
        print('放入线索库详情', PutInLibPATCH.text)
        if PutInLibPATCH.status_code == 200:
            pass
        else:
            print('PutInClueLibary登录接口请求失败..')
            exit()

    # 发送分配给指定销售的请求,该接口需要线索ID，销售id两个字段
    def allotSaleman(self, PutInculeId, salemanName='彭椿的销售和商务专员'):
        salemanName = str(salemanName)
        PutInculeId = str(PutInculeId)
        # 通过传入值获取销售id
        getValue = GetDatabaseValue(self.severVersion)
        salemanId = getValue.getSalemanId(salemanName)
        urlAllotSaleman = "http://" + self.host + self.urlPort + "/crm/clue/manage/distribution"
        body_alloSaleman = {"clueId": PutInculeId,
                            "receiveUserId": salemanId, "receiveUserName": salemanName}
        body_alloSaleman_json = json.dumps(body_alloSaleman)
        allotSalemanPUT = requests.put(
            urlAllotSaleman, data=body_alloSaleman_json, headers=self.header_value)
        print("分配给客服: ", salemanName,
              ' 的接口请求code', allotSalemanPUT.status_code)
        print("分配给客服: ", salemanName, ' 的接口请求结果', allotSalemanPUT.text)
        if allotSalemanPUT.status_code == 200:
            pass
        else:
            print('allotSaleman登录接口请求失败.....')
            exit()


    '''
    私有库新建合作客户
    入参 客户名称后缀  电话  地区  行业  来源 
    '''
    def createNewProviteCustomer(self, count_customerName, customerTel='17585571190', areaName='渝中区', tradeName='互联网类',
                                 source='1001'):
        customerName = '彭一椿的私有库容量测试' + str(count_customerName)  # 拼接生成的客户名称
        print(customerName)                # 完整的客户名称
        customerTel = str(customerTel)     # 号码
        areaName = str(areaName)           # 区域名称
        tradeName = str(tradeName)              # 行业名称
        source = str(source)               # 来源
        getValue = GetDatabaseValue(self.severVersion)
        customer_address_info = getValue.get_customer_addressInfo(areaName)  # 利用传入的区域名称 查询获得地址详情
        customer_address_areaCode = customer_address_info[0]            # 区域code
        customer_address_areaName = str(customer_address_info[1])       # 区域名称
        customer_address_cityCode = customer_address_info[2]            # 城市code
        customer_address_cityName = str(customer_address_info[3])       # 城市名称
        customer_address_provinceCode = customer_address_info[4]        # 省code
        customer_address_provinceName = str(customer_address_info[5])   # 省名称
        tradeCode = int(getValue.get_tradeCode(tradeName))         # 利用传入行业名称查出行业code
        urlCNPC = "http://" + self.host + self.urlPort + "/crm/web/customer/private"
        bodyCNPC = {"areaCode": customer_address_areaCode, "areaName": customer_address_areaName,
                    "cityCode": customer_address_cityCode, "cityName": customer_address_cityName, "contacts": [],
                    "customerAddr": "1号", "customerName": customerName, "customerTelList": [customerTel],
                    "provinceCode": customer_address_provinceCode, "provinceName": customer_address_provinceName,
                    "source": source, "tradeCode": tradeCode, "tradeName":
                        tradeName}
        bodyCNPCJson = json.dumps(bodyCNPC)
        cNPCRequest = requests.post(urlCNPC, data=bodyCNPCJson, headers=self.header_value)
        print("私有库新增客户接口请求code：", cNPCRequest.status_code)
        print("私有库新增客户接口请求结果：", cNPCRequest.text)
        if cNPCRequest.status_code == 200:
            pass
        else:
            exit()

    '''
    数字转汉字的简单方法
    '''

    def createBatchChiName(self, nameCount):
        nameCount = int(nameCount)
        cNameCount = ''
        nameDict = {1: '一', 2: '二', 3: '三', 4: '四',
                    5: '五', 6: '六', 7: '七', 8: '八', 9: '九', 0: '零'}
        importCount = str(nameCount)
        countLen = len(importCount)
        for i in range(0, countLen):
            cNameCount = cNameCount + nameDict[int(importCount[i])]
        return cNameCount

