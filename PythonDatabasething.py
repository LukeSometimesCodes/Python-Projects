conn = sqlite3.connect('test2.db')
with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_test2( ID INTEGER PRIMARY KEY AUTOINCREMENT, \
                col_document TEXT)")
    conn.commit()

conn = sqlite3.connect('test2.db')

fileList = ('information.docx', 'Hello.txt', 'myImage.png', \
                'myMovie.mpg', 'World.txt', 'data.pdf', 'myPhoto.jpg')

for x in fileList:
    if x.endswith('.txt'):
        with conn:
            cur = conn.cursor()

            cur.execute('INSERT INTO tbl_test2(col_document) VALUES (?)', (x,))
            print(x)

conn.close
    
