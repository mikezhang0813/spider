"""
该模块提供了对pymysql的封装
Create_date: 2020-02-04
Author: zhangdda
"""
import pymysql
class DbHelper():
    def __init__(self,host='localhost',user='mike',password='123',charset='utf8',database=None,port=3306):
        """
        Required paramater
            user,password ,database
        :param host: ip for mysql-server
        :param user: privileges for apply
        :param password: password for user
        :param charset: encoding type
        :param database:  DB to connect
        :param port: dafault to 3306
        """
        try:
            self.db = pymysql.connect(host=host,user=user,password=password,database=database,charset=charset,port=port)
        except Exception as e:
            print(e)
        else:

            self.cursor = self.db.cursor()

    def insert(self,itera,table):
        """
        itera : dict  tuple(key,value)
        :param itera:
        :param table:
        :return:
        """
        if  not isinstance(itera,dict):
            itera = dict(itera)

        sql = 'insert into {}({})values({})'.format(table,','.join([key for key in itera.keys()]),
                                                                   ','.join(['%s']*len(itera.values())))
        try:
            self.cursor.execute(sql,list(itera.values()))
        except Exception as e:
            print('插入失败',e)
            self.db.rollback()
        else:
            self.db.commit()
            return True
    def bulk_insert(self,itera_list,table):
        """
        多条记录插入

        :param itera: 列表中
        :return: 查询结果
        """
        for row in itera_list:
            sql = 'insert into {}({})values({})'.format(table,','.join([key for key in row.keys()]),
                                                                   ','.join(['%s']*len(row.values())))
            try:
                self.cursor.execute(sql,[row.values for row in itera_list])
            except Exception as e:
                print(e)
                print('数据插入失败',row)

            else:
                self.db.commit()
                return True
    def get(self,table,dict_mapping):
        if not isinstance(dict_mapping,dict):
            try:
                dict_mapping =dict(dict_mapping)
            except Exception:
                raise  TypeError
        sql = 'select {} from {} where {}={}'.format(','.join(list(dict_mapping.keys())),table,''.join(list(dict_mapping.keys())),''.join(list(dict_mapping.values())))
        self.cursor.execute(sql)
        return self.cursor.fetchone()





