import MySQLdb

#IMPORTANT THIS SCRIPT IS STILL VERY CUSTOMIZED USE IT AS A REFERENCE
#TO IMPLEMENT YOUR OWN CUSTOM SCRIPT OR WAIT FOR A MORE DYNAMIC RELEASE

def main() :
    
    conn = connect_db()
    col_names = create_col_names(conn)
    logfile = open('file_name.csv', 'r').readlines()

    for i,line in enumerate(logfile) :
        
        values = extract_values(line)
        full_sql_statement = create_statement(col_names, values)
        execute_statement(conn, full_sql_statement)
        

    print 'all done\n'

def extract_values(value_list) :
    values = ""
    for value in value_list.split(';') :
        values = values + "'" + value + "',"
        
    if len(value_list.split(';')) < 291 :
        index = 291 - len(value_list.split(';'))
        while index is not 0 :
            if index is 1 :
                values = values + "''"
                index = index -1
            else :
                values = values + "'',"
                index = index - 1
            
    return values


def create_statement(col_names, values) :
    
    full_sql_statement = "INSERT INTO alarm (" + col_names + ") VALUES (" + values + ")"

    return full_sql_statement

def create_col_names(conn) :
    
    index = 1
    num_of_col = 291 
    col_names = ""
    cursor = conn.cursor()
    
    while index <= num_of_col :
        if index == num_of_col :
            col_names = col_names + "`col" + str(index) + "`"
            current_col = "col%s"%index
            cursor.execute ("ALTER TABLE alarm ADD %s TEXT(1100)" %current_col)
            index = index + 1

    
        else :
            col_names = col_names + "`col" + str(index) + "`," 
            current_col = "col%s"%index
            cursor.execute ("ALTER TABLE alarm ADD %s TEXT(1100)" %current_col)
            index = index + 1
       

    return col_names
   

def execute_statement(conn, sql_statement) :
    cursor = conn.cursor()
    cursor.execute(sql_statement)
    

def connect_db() :
    conn = MySQLdb.connect (host = "localhost",
                            user = "mysql_user",
                            passwd = "password",
                            db = "db_name")
    return conn
    

if __name__ == '__main__':
     main() 
