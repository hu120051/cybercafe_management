from flask import Flask
from flask import render_template
from flask import request
import pymysql
import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = '123456'


@app.route('/')     # 进入首页
def index():
    return render_template('index.html')

# ########管理员端######## #
@app.route('/adminlogin/', methods=['GET', 'POST'])     # 管理员登录页面
def adminlogin():
    if request.method == 'GET':
        return render_template('adminlogin.html')
    else:
        username = request.form['username']
        password = request.form['password']
        db = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='hhy123', db='cybercafe')
        cur1 = db.cursor()
        sql_select01 = '''SELECT Staff_ID FROM Staff WHERE Staff_ID=('%s') AND Password=('%s') ''' % (username, password)
        cur1.execute(sql_select01)
        return1 = cur1.fetchall()

        if len(return1):           # 对js和flask很不熟练，没想到更好的方法，这种方法只要管理员进入系统就要把所有表查一遍
            cur1.execute('''select ca.Card_ID, cu.CName, ca.Password, ca.Using_Status, ca.Checkout_Status,
             ca.Account_Balance FROM Card ca, Customer cu WHERE ca.C_ID = cu.C_ID ORDER BY ca.Card_ID asc''')
            d = cur1.fetchall()
            cur1.execute('''select o.Order_ID, o.Card_ID, o.Order_Time, s.SName, o.Quantity, o.Amount, o.Order_Status 
            FROM Order_T o, Snacks s WHERE o.S_ID = s.S_ID ORDER BY o.Order_ID desc''')
            c = cur1.fetchall()
            cur1.execute('''select * FROM Bill ORDER BY B_ID desc''')
            b = cur1.fetchall()
            cur1.execute('''select * FROM Computer ORDER BY PC_ID asc''')
            a = cur1.fetchall()
            cur1.execute('''select * FROM Snacks ''')
            e = cur1.fetchall()
            users = []
            orders = []
            bills = []
            computers = []
            snacks = []
            # 录入users所有用户信息
            for value in d:
                data = {}
                data['a'] = value[0]
                data['b'] = value[1]
                data['c'] = value[2]
                data['d'] = value[3]
                data['e'] = value[4]
                data['f'] = value[5]
                users.append(data)
            # 录入orders所有零食订单信息
            for value in c:
                data = {}
                data['a'] = value[0]
                data['b'] = value[1]
                data['c'] = value[2]
                data['d'] = value[3]
                data['e'] = value[4]
                data['f'] = value[5]
                data['g'] = value[6]
                orders.append(data)
            # 录入bills所有的上机账单信息
            for value in b:
                data = {}
                data['a'] = value[0]
                data['b'] = value[1]
                data['c'] = value[2]
                data['d'] = value[3]
                data['e'] = value[4]
                data['f'] = value[5]
                data['g'] = value[6]
                bills.append(data)
            # 录入computers所有的上机账单信息
            for value in a:
                data = {}
                data['a'] = value[0]
                data['b'] = value[1]
                data['c'] = value[2]
                computers.append(data)
            # 录入snacks所有的零食信息
            for value in e:
                data = {}
                data['a'] = value[0]
                data['b'] = value[1]
                data['c'] = value[2]
                data['d'] = value[3]
                snacks.append(data)
            return render_template('adminmain.html', users=users, orders=orders, bills=bills, computers=computers, snacks=snacks)
        else:
            return render_template("adminlogin.html", tips='用户名或密码错误')
            # flash('username or password is wrong')
            # return render_template("adminlogin.html")


@app.route('/addusers/', methods=['GET', 'POST'])    # 在系统里面添加新用户
def addusers():
    if request.method == 'GET':
        return render_template('addusers.html')
    else:
        c_id = request.form['CustomerID']
        cname = request.form['Cname']
        age = request.form['Age']
        gender = request.form['Gender']
        card_id = request.form['Card_ID']
        password = u'123456'        # 初始密码均为123456
        account_balance = request.form['Account_Balance']
        db = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='hhy123', db='cybercafe')
        cur = db.cursor()
        sql_insert1 = '''INSERT INTO Customer VALUES ('%s', '%s', '%s', '%s')''' % (c_id, cname, age, gender)
        sql_insert2 = '''INSERT INTO Card VALUES ('%s','%s','Free','Paid','%s','%s')''' \
                      % (card_id, password, account_balance, c_id)
        cur.execute(sql_insert1)
        cur.execute(sql_insert2)
        db.commit()
        db.close()
        return render_template('close.html')


@app.route('/changecharge/', methods=['GET', 'POST'])    # 充值/退款
def changecharge():
    if request.method == 'GET':
        return render_template('changecharge.html')
    else:
        card_id = request.form['CardID']
        change = int(request.form['Change'])
        db = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='hhy123', db='cybercafe')
        cur = db.cursor()
        sql_insert1 = '''UPDATE Card SET Account_Balance = (Account_Balance+(%d)) WHERE Card_ID= '%s' ''' % (change, card_id)
        cur.execute(sql_insert1)
        print(sql_insert1)
        db.commit()
        db.close()
        return render_template('close.html')


@app.route('/updateusers/', methods=['GET', 'POST'])    # 在系统里面更新用户信息
def updateusers():
    if request.method == 'GET':
        return render_template('updateusers.html')
    else:
        card_id = request.form['CardID']
        cname = request.form['Cname']
        age = request.form['Age']
        gender = request.form['Gender']
        password = request.form['Password']
        using_status = request.form['Using_Status']
        checkout_status = request.form['Checkout_Status']
        account_balance = request.form['Account_Balance']
        db = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='hhy123', db='cybercafe')
        cur = db.cursor()
        sql_insert1 = '''UPDATE Customer SET Cname='%s', Age='%s', Gender='%s' WHERE (C_ID=(SELECT C_ID FROM Card 
        WHERE Card_ID='%s')) ''' % (cname, age, gender, card_id)
        sql_insert2 = '''UPDATE Card SET Password='%s', Using_Status='%s', Checkout_Status='%s', Account_Balance='%s' 
        WHERE (Card_ID='%s') ''' % (password, using_status, checkout_status, account_balance, card_id)
        cur.execute(sql_insert1)
        cur.execute(sql_insert2)
        db.commit()
        db.close()
        return render_template('close.html')


@app.route('/deleteuser/<id>', methods=['GET', 'POST'])    # 删除系统中的用户
def deleteuser(id):
    db = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='hhy123', db='cybercafe')
    cur = db.cursor()
    sql_select1 = '''SELECT C_ID FROM Card WHERE Card_ID='%s' ''' % id
    cur.execute(sql_select1)
    c = cur.fetchone()
    cid = c[0]
    sql_delete1 = '''DELETE FROM Customer WHERE C_ID='%s' ''' % cid
    sql_delete2 = '''DELETE FROM Card WHERE Card_ID = '%s' ''' % id
    # 由于card表里C_ID是外键，参考Customer表，所以删除时应先删除有外键的值
    cur.execute(sql_delete2)
    cur.execute(sql_delete1)
    db.commit()
    db.close()
    return render_template('adminmain.html')


@app.route('/finishorder/<id>', methods=['GET', 'POST'])    # 完成零食订单(完成时不扣钱，结算账单时统一结算)
def finishorder(id):

    db = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='hhy123', db='cybercafe')
    cur = db.cursor()
    sql_insert1 = '''UPDATE Order_T SET Order_Status = 'Finished' WHERE Order_ID='%s' ''' % id
    print(sql_insert1)
    cur.execute(sql_insert1)
    db.commit()
    db.close()
    return render_template('adminmain.html')


@app.route('/deleteorder/<id>', methods=['GET', 'POST'])    # 删除零食订单
def deleteorder(id):

    db = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='hhy123', db='cybercafe')
    cur = db.cursor()
    sql_insert1 = '''delete FROM Order_T WHERE Order_ID='%s' ''' % id
    print(sql_insert1)
    cur.execute(sql_insert1)
    db.commit()
    db.close()
    return render_template('adminmain.html')


@app.route('/addbills/', methods=['GET', 'POST'])    # 添加上机账单
def addbills():
    if request.method == 'GET':
        return render_template('addbills.html')
    else:
        starttime = request.form['Start_Time']
        card_id = request.form['Card_ID']
        pc_id = request.form['PC_ID']
        staff_id = request.form['Staff_ID']
        db = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='hhy123', db='cybercafe')
        cur = db.cursor()
        cur.execute('''SELECT MAX(B_ID) FROM Bill''')
        num = cur.fetchone()
        bill_id = num[0]+1      #bill_id依次自动生成
        sql_insert1 = '''INSERT INTO Bill VALUES ('%s', '%s', null, null, '%s', '%s' ,'%s')''' \
                      % (bill_id, starttime, card_id, pc_id, staff_id)
        sql_update1 = '''UPDATE Card SET Using_Status='Using', Checkout_Status='Unpaid' WHERE (Card_ID='%s')''' \
                      % card_id
        sql_update2 = '''UPDATE Computer SET Card_ID='%s' WHERE (PC_ID='%s')''' % (card_id, pc_id)

        '''
        insert1：在bill表中添加新订单，结束时间和结算金额在结账时由管理员操作
        update1：在card表中将此卡使用状态设置为使用中，结算状态设置为未结算
        update2：将computer表中此计算机的使用用户设置为此卡
        '''

        cur.execute(sql_insert1)
        cur.execute(sql_update1)
        cur.execute(sql_update2)
        db.commit()
        db.close()
        return render_template('close.html')


@app.route('/finishbills/', methods=['GET', 'POST'])    # 结算账单
def finishbills():
    if request.method == 'GET':
        return render_template('finishbills.html')
    else:
        bill_id = request.form['Bill_ID']
        endtime = request.form['End_Time']
        total_amount = request.form['Total_Amount']
        db = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='hhy123', db='cybercafe')
        cur = db.cursor()

        '''
        结算对三个表进行处理：
            1.会员卡状态改为空闲，结算状态改为已结算，余额扣费
            2.账单表完善下机时间，总金额信息
            3.电脑表将使用状态的计算机的使用卡号改为null，即计算机空闲
        '''

        sql_update1 = '''UPDATE Card SET Using_Status='Free', Checkout_Status='Paid', Account_Balance=
        (Account_Balance-%s) WHERE Card_ID=(SELECT Card_ID FROM Bill WHERE B_ID = '%s')''' % (total_amount, bill_id)
        sql_update2 = '''UPDATE Bill SET End_Time='%s', Total_Amount='%s' WHERE (B_ID='%s')''' \
                      % (endtime, total_amount, bill_id)
        sql_update3 = '''UPDATE Computer SET Card_ID=null WHERE Card_ID=
        (SELECT Card_ID FROM Bill WHERE B_ID = '%s')''' % bill_id
        cur.execute(sql_update1)
        cur.execute(sql_update2)
        cur.execute(sql_update3)
        db.commit()
        db.close()
        return render_template('close.html')


@app.route('/addcomputer/', methods=['GET', 'POST'])    # 添加计算机
def addcomputer():
    if request.method == 'GET':
        return render_template('addcomputer.html')
    else:
        computer_id = request.form['Computer_ID']
        price = request.form['Price_Per_Hour']
        db = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='hhy123', db='cybercafe')
        cur = db.cursor()
        sql_insert1 = '''INSERT INTO Computer VALUES ('%s', '%s', null)''' % (computer_id, price)
        cur.execute(sql_insert1)
        db.commit()
        db.close()
        return render_template('close.html')


@app.route('/changeadpwd/', methods=['GET', 'POST'])       # 修改管理员密码
def changeadpwd():
    if request.method == 'GET':
        return render_template('adminmain.html')
    else:
        staff_id = request.form['Staff_ID']
        opwd = request.form['Old_Pwd']
        npwd = request.form['New_Pwd']
        db = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='hhy123', db='cybercafe')
        cur = db.cursor()
        sql_update1 = '''UPDATE Staff SET Password='%s' WHERE Staff_ID='%s' AND Password='%s' ''' % (npwd, staff_id, opwd)
        print(sql_update1)
        cur.execute(sql_update1)
        db.commit()
        db.close()
        return render_template('adminmain.html')


@app.route('/deletesnack/<id>', methods=['GET', 'POST'])    # 删除零食信息
def deletesnack(id):
    db = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='hhy123', db='cybercafe')
    cur = db.cursor()
    sql_delete1 = '''delete FROM Snacks WHERE S_ID='%s' ''' % id
    cur.execute(sql_delete1)
    db.commit()
    db.close()
    return render_template('adminmain.html')


@app.route('/changesnack/', methods=['GET', 'POST'])       # 修改零食信息
def changesnack():
    if request.method == 'GET':
        return render_template('adminmain.html')
    else:
        s_id = request.form['Snack_ID']
        sname = request.form['SName']
        sprice = request.form['SPrice']
        snack_status = request.form['Snack_Status']
        db = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='hhy123', db='cybercafe')
        cur = db.cursor()
        sql_update1 = '''UPDATE Snacks SET SName='%s', SPrice='%s', Snack_Status='%s' WHERE S_ID='%s' ''' \
                      % (sname, sprice, snack_status, s_id)
        print(sql_update1)
        cur.execute(sql_update1)
        db.commit()
        db.close()
        return render_template('adminmain.html')


@app.route('/addsnack/', methods=['GET', 'POST'])    # 添加零食
def addsnack():
    if request.method == 'GET':
        return render_template('addsnack.html')
    else:
        s_id = request.form['Snack_ID']
        sname = request.form['SName']
        sprice = request.form['SPrice']
        snack_status = request.form['Snack_Status']
        db = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='hhy123', db='cybercafe')
        cur = db.cursor()
        sql_insert1 = '''INSERT INTO Snacks VALUES ('%s', '%s', '%s', '%s')''' % (s_id, sname, sprice, snack_status)
        cur.execute(sql_insert1)
        db.commit()
        db.close()
        return render_template('close.html')


# ########用户端######## #
@app.route('/userlogin/', methods=['GET', 'POST'])    # 用户端
def userlogin():
    if request.method == 'GET':
        return render_template('userlogin.html')
    else:
        username = request.form['username']
        password = request.form['password']
        db = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='hhy123', db='cybercafe')
        cur2 = db.cursor()
        sql_select02 = '''SELECT Card_ID FROM Card WHERE Card_ID=('%s') AND Password=('%s')''' % (username, password)
        cur2.execute(sql_select02)
        return2 = cur2.fetchall()
        if len(return2):
            sql_select01 = '''select ca.Card_ID, cu.CName, ca.Using_Status, ca.Checkout_Status, ca.Account_Balance 
            FROM Card ca, Customer cu WHERE ca.C_ID=cu.C_ID AND Card_ID='%s' ''' % username
            cur2.execute(sql_select01)
            k = cur2.fetchall()
            sql_select03 = '''select * FROM Bill WHERE Card_ID='%s' ORDER BY B_ID desc''' % username
            cur2.execute(sql_select03)
            j = cur2.fetchall()
            sql_select04 = '''select * FROM Snacks WHERE Snack_Status='Onsale' ORDER BY S_ID asc'''
            cur2.execute(sql_select04)
            l = cur2.fetchall()
            member = []
            bills = []
            snacks = []
            for value in k:
                data = {}
                data['a'] = value[0]
                data['b'] = value[1]
                data['c'] = value[2]
                data['d'] = value[3]
                data['e'] = value[4]
                member.append(data)
            for value in j:
                data = {}
                data['a'] = value[0]
                data['b'] = value[1]
                data['c'] = value[2]
                data['d'] = value[3]
                data['e'] = value[4]
                data['f'] = value[5]
                data['g'] = value[6]
                bills.append(data)
            for value in l:
                data = {}
                data['a'] = value[0]
                data['b'] = value[1]
                data['c'] = value[2]
                data['d'] = value[3]
                snacks.append(data)
            return render_template('usermain.html', username=username, member=member, bills=bills, snacks=snacks)
        else:
            return render_template("userlogin.html")


@app.route('/changeuspwd/', methods=['GET', 'POST'])       # 修改用户密码
def changeuspwd():
    if request.method == 'GET':
        return render_template('usermain.html')
    else:
        card_id = request.form['Card_ID']
        opwd = request.form['Old_Pwd']
        npwd = request.form['New_Pwd']
        db = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='hhy123', db='cybercafe')
        cur = db.cursor()
        sql_update1 = '''UPDATE Card SET Password='%s' WHERE Card_ID='%s' AND Password='%s' ''' % (npwd, card_id, opwd)
        print(sql_update1)
        cur.execute(sql_update1)
        db.commit()
        db.close()
        return render_template('usermain.html')


@app.route('/addorder/', methods=['GET', 'POST'])       # 提交订单
def addorder():
    if request.method == 'GET':
        return render_template('usermain.html')
    else:
        s_id = request.form['Snack_ID']
        quantity = request.form['Quantity']
        time = datetime.datetime.now()
        card_id = request.form['Card_ID']
        db = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='hhy123', db='cybercafe')
        cur = db.cursor()
        cur.execute('''SELECT MAX(Order_ID) FROM ORDER_T''')
        num = cur.fetchone()
        order_id = num[0]+1
        sql_select1 = '''SELECT SPrice FROM Snacks WHERE S_ID = '%s' ''' % s_id
        cur.execute(sql_select1)
        amount = float(cur.fetchone()[0])*float(quantity)
        sql_insert1 = '''INSERT INTO Order_T VALUES ('%s', '%s', '%s', '%s', '%s', '%s', 'Unfinish') ''' \
                      % (order_id, card_id, time, s_id, quantity, amount)
        cur.execute(sql_insert1)
        db.commit()
        db.close()
        return render_template('usermain.html')


if __name__ == '__main__':
    app.run()
