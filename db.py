#sebastian solorzano -- python<->sql template(?)
#part of a larger thing I'm making for a discord I don't want to share my real name with,
#so I'm splitting it into parts
#this is the SQL element of that, somewhat templatized for future use


import sqlite3
import re
from constants import * #I think this is how its done??

class dbthingy:
    cnctn:sqlite3.Connection
    crsr: sqlite3.Cursor

    #autoconnects (that should be fine?)
    def __init__(self, db):
        self.cnctn=sqlite3.connect(db)
        self.crsr = self.cnctn.cursor()

    def finish(self):
        self.cnctn.commit()
        self.cnctn.close()
        #this should be good enough I think?


    #sets up the database. intended to only be run once on initial setup,
    #but its not like running it again causes any problems
    def SetupDB(self):
        #apparently sqlite doesn't need a 'create database' command

        #JUST MAKE SURE YOU SET UP THE TABLE PROPERLY BEFORHAND, RAW TEMPLATE PROLLY DOESN'T WORK
        for tables in TABLE_GEN: 
            self.crsr.execute(tables[TSQL_INDEX]) 

        self.cnctn.commit()

    #man honestly I miss the {} they actually make things easier to read
    
    #adds a record to the database. format: name, '(<csv>)' <--as you would if you were typing the sql yourself
    #one at a time i'm not processing multiple lmao
    def addRecord(self,tableName:str, addingvalues:str):
        for table in TABLE_GEN: 
            #checks for valid table name and values that match the table
            if tableName == table[TNAME_INDEX] and (re.search(table[TREGEX_INDEX],addingvalues))!= None:  
                self.crsr.execute(gener_INSERT.format(table=tableName,values=addingvalues))
                self.cnctn.commit()
    
    #updates a record in the database. figure out the sql yourself
    def updRecord(self, tableName:str, newvalue:str, sqlcond:str):
        #I do not think you can regex for a valid sql statement lmao
        for table in TABLE_GEN:
            if tableName == table[TNAME_INDEX]:
                self.crsr.execute(gener_UPDATE.format(table=tableName,changed=newvalue,conditions=sqlcond)) 
                self.cnctn.commit
                #this method won't take care of it, but you can use something like gener_cond yourself to
                #make sure sqlcond is valid

    def dltRecord(self, tableName:str, sqlcond:str):
        #same as previous, no way I can check for valid sql
        for table in TABLE_GEN:
            if(tableName) == table[TNAME_INDEX]:
                self.crsr.execute(gener_DELETE.format(table=tableName,conditions=sqlcond)) 
                #I should probably do some error checking but I can't be bothered ngl
                self.cnctn.commit

    def rdRecords(self, tableName:str, valsToSee:str, sqlcond:str) ->list: #fetchall returns a string right?
        for table in TABLE_GEN:
            if(tableName) == table[TNAME_INDEX]:
                self.crsr.execute(gener_SELECT.format(csvalues=valsToSee,table=tableName,conditions=sqlcond))
                retval = self.crsr.fetchall()
                return retval
            else:
                return None #this is basically NULL right? should be fine

    #in the project this is for the tables are fixed, so drop, alter etc. do not need to be supported
    #and I can't be bothered to implement them here
                    