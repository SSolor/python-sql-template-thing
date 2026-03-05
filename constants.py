#constants because this is apparently how you do it in python? I think?
#idk there's no #defs so...


DB_FILEN: str = 'dnametemp.db'

#ok so I think I read that __x makes it semi-invisible outside this file? (though i'm still unsure if __ or _ is more proper...)
__EXAMPLE_SQLCOM:str = '''
                    CREATE TABLE IF NOT EXISTS Users(
                        user_id varchar[35] PRIMARY KEY,
                        username varchar[35],
                        name varchar[35]
                    );
                '''
__EXAMPLE_TABLE_REGEX:str = r"^\([\"\'].+[\"\'],[\"\'].+[\"\'],[\"\'].+[\"\']\);$"    #beautiful isn't it? lmao


TEMPL_SQLCOM:str = '''
                CREATE TABLE IF NOT EXISTS {name}(
                {attributes_formatted}
                );
'''
TEMPL_TABLE_REGEX:str = "^\({delimiters}\);$"

#anyway this all isn't strictly necessary its just my way of ensuring that if you add more tables
#you add all these other things too
#(...if this were java there'd be some nonsense about injecting a class or something stupid like that)

TABLE_GEN:str = [ ['Example', __EXAMPLE_SQLCOM, __EXAMPLE_TABLE_REGEX], ['name', TEMPL_SQLCOM, TEMPL_TABLE_REGEX]]
                                                        #not sure if this works exactly but you get the picture
#for the actual project the tables we need are static so it was fine to make a constant list like above
#if using this as a template it might actually be better to do that java-style nonsenes

TNAME_INDEX:int = 0
TSQL_INDEX:int = 1
TREGEX_INDEX:int = 2

gener_INSERT:str = "INSERT INTO {table} VALUES {values};"
gener_UPDATE:str = "UPDATE {table} SET {changed} WHERE {conditions};"
gener_DELETE:str = "DELETE FROM {table} WHERE {conditions};"
gener_SELECT:str = "SELECT {csvalues} FROM {table} WHERE {conditions}"
    #if you want  HAVING yer on yer own
    #also simple JOINS but who does those

#simple condition you can slap into {conditions} that should work for nearly everything?
gener_CONDITION:str = "{values} {operation} {condition}"

#for anything more complex just make unholy concactenations of 
#gener_SELECT(value, table, gener_CONDITION(value, "IN(" , gener_SELECT(...)))