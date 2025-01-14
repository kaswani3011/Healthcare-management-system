import pandas as pd
import mysql.connector as sql
&quot;&quot;&quot;
username: admin
password: password
&quot;&quot;&quot;
def run_admin_mode():
print(&quot;1. ABOUT THE PROJECT&quot;)
print(&quot;2. CREATE TABLE doctor_details&quot;)
print(&quot;3. DESCRIBE doctor_details&quot;)

print(&quot;4. REGISTER doctor_details&quot;)
print(&quot;5. ALL DOCTOR DETAILS&quot;)
print(&quot;6. CREATE TABLE patient_details&quot;)
print(&quot;7. DESCRIBE patient_details&quot;)
print(&quot;8. REGISTER patient_details&quot;)
print(&quot;9. ALL PATIENT DETAILS&quot;)
print(&quot;10. CREATE TABLE worker_details&quot;)
print(&quot;11. DESCRIBE worker_details&quot;)
print(&quot;12. REGISTER worker_details&quot;)
print(&quot;13. ALL WORKER DETAILS&quot;)
print(&quot;14. SEARCH DOCTOR DETAILS&quot;)
print(&quot;15. SEARCH PATIENT DETAILS&quot;)
print(&quot;16. SEARCH WORKER DETAILS&quot;)
print(&quot;17. UPDATE DOCTOR DETAILS&quot;)
print(&quot;18. UPDATE PATIENT DETAILS&quot;)
print(&quot;19. UPDATE WORKER DETAILS&quot;)
print(&quot;20. bill_details&quot;)
print(&quot;21. ENTER CHARGES OF PATIENT for bill_details:&quot;)
print(&quot;22. SHOW RECORD OF BILL&quot;)
print(&quot;23. DELETE A COLUMN&quot;)
print(&quot;24. DELETE A RECORD&quot;)
print(&quot;25. SORT WORKERS&quot;)
print(&quot;0. EXIT&quot;)
while True:
opt=&quot;&quot;
opt=int(input(&quot;Please enter your choice:&quot;))
if opt==1:
about()
elif opt==2:
create_doctor_details()
elif opt==3:
desc_doctor_details()
elif opt==4:
insert_doctor_details()
elif opt==5:
show_records_doctor_details()
elif opt==6:
create_patient_details()
elif opt==7:
desc_patient_details()
elif opt==8:
insert_patient_details()
elif opt==9:
show_records_patient_details()
elif opt==10:
create_worker_details()
elif opt==11:
desc_worker_details()
elif opt==12:
insert_worker_details()
elif opt==13:
show_records_worker_details()
elif opt==14:
search_doctor_details()
elif opt==15:

search_patient_details()
elif opt==16:
search_worker_details()
elif opt==17:
update_doctor_details()
elif opt==18:
update_patient_details()
elif opt==19:
update_worker_details()
elif opt==20:
create_bill_details()
elif opt==21:
insert_bill_details()
elif opt==22:
show_records_bill()
elif opt==23:
delcol()
elif opt==24:
delrecord_worker()
elif opt==25:
sort_workers()
elif opt == 0:
exit()
else:
print(&quot;invalid option, please try again&quot;)
def run_user_mode():
print(&quot;1. ABOUT THE PROJECT&quot;)
def about():
print(&quot;this is a hospital management system&quot;)
def create_doctor_details():
c1=conn.cursor()
c1.execute(&#39;create table doctor_details (d_id int(5),d_name varchar(20)
primary key,d_age int(3),d_departement varchar(20),d_phono int(11))&#39;)
print(&#39;table created&#39;)
def desc_doctor_details():
print(&quot;show structure of doctor_details table&quot;)
df=pd.read_sql(&quot;desc doctor_details&quot;,conn)
print(df)
def insert_doctor_details():
print(&quot;enter details of new doctor-&quot;)
d_id=int(input(&quot;enter the ID of new doctor:&quot;))
d_name=input(&quot;enter doctor name:&quot;)
d_age=int(input(&quot;enter age:&quot;))
d_department=input(&quot;enter the department:&quot;)
d_phono=int(input(&quot;enter the phono:&quot;))
## sql_insert=&quot;insert into
doctor_details(d_id,d_name,d_age,d_department,d_phono) values (%s, %s, %s,
%s, %s)&quot; (&quot; + str(d_id) + &quot;,&quot; + d_name + &quot;,&quot; + str(d_age) + &quot;,&quot; +
d_department + &quot;,&quot; + str(d_phono) + &quot;)&quot;

sql_insert=&quot;insert into
doctor_details(d_id,d_name,d_age,d_department,d_phono) values (%s, %s, %s,
%s, %s)&quot;
val = (str(d_id), d_name, str(d_age), d_department, str(d_phono))
c1.execute(sql_insert, val)
print(&quot;REGISTERED NEW DOCTOR&quot;)
conn.commit()
def show_records_doctor_details():
print(&quot;all records of doctors&quot;)
df=pd.read_sql(&quot;select * from doctor_details&quot;,conn)
print(df)
def create_patient_details():
c1=conn.cursor()
c1.execute(&#39;create table patient_details (p_id int(5),p_name
varchar(30),primary key,p_age int(3),p_diagnosis varchar(40),p_phono
int(11)&#39;)
print(&quot;table created&quot;)
def desc_patient_details():
print(&quot;show structure of patient_details table&quot;)
df=pd.read_sql(&quot;desc patient_details&quot;,conn)
print(df)
def insert_patient_details():
print(&quot;enter details of patient:&quot;)
p_id=int(input(&quot;enter the ID of new patient:&quot;))
p_name=input(&quot;enter name of patient:&quot;)
p_age=int(input(&quot;enter age:&quot;))
p_diagnosis=input(&quot;enter patient diagnosis:&quot;)
p_phono=int(input(&quot;enter the phono:&quot;))
sql_insert=&quot;insert into
patient_details(p_id,p_name,p_age,p_diagnosis,p_phono) values (%s, %s, %s,
%s, %s)&quot;
val= (str(p_id),p_name,str(p_age),p_diagnosis,str(p_phono))
c1.execute(sql_insert,val)
print(&quot;REGISTERED SUCCESSFULLY&quot;)
conn.commit()
def show_records_patient_details():
print(&quot;all records of patient&quot;)
df=pd.read_sql(&quot;select*from patient_details&quot;,conn)
print(df)
def create_worker_details():
c1=conn.cursor()
c1.execute(&#39;create table worker_details (w_id int(5),w_name
varchar(30),primary key, w_age int(3), w_position varchar(50), w_phono
int(11)&#39;)
print(&quot;table created&quot;)
def desc_worker_details():
print(&quot;show structure of worker_details table&quot;)
df=pd.read_sql(&quot;desc worker_details&quot;,conn)

print(df)
def insert_worker_details():
print(&quot;enter details of workers:&quot;)
w_id=int(input(&quot;enter ID of new worker:&quot;))
w_name=input(&quot;enter worker name:&quot;)
w_age=int(input(&quot;enter age of worker:&quot;))
w_position=input(&quot;enter worker position:&quot;)
w_phono=int(input(&quot;enter worker phono:&quot;))
sql_insert=&quot;insert into worker_details
(w_id,w_name,w_age,w_position,w_phono) values (%s, %s, %s, %s, %s)&quot;
val= (str(w_id),w_name,str(w_age),w_position,str (w_phono))
c1.execute(sql_insert,val)
print(&quot;REGISTERED SUCCESSFULLY&quot;)
conn.commit()
def show_records_worker_details():
print(&quot;all records of workers&quot;)
df=pd.read_sql(&quot;select*from worker_details&quot;,conn)
print(df)

def search_doctor_details():
print(&quot;search doctor record by entering ID&quot;)
exp=float(input(&quot;enter doctor ID:&quot;))
qry=&quot;select*from doctor_details where d_id=%s;&quot;%(exp,)
df=pd.read_sql(qry,conn)
print(df)
def search_patient_details():
print(&quot;search patient record by entering ID:&quot;)
exp=float(input(&quot;enter patient ID:&quot;))
qry=&quot;select*from patient_details where p_id=%s;&quot;%(exp,)
df=pd.read_sql(qry,conn)
print(df)
def search_worker_details():
print(&quot;search worker record by entering ID&quot;)
exp=float(input(&quot;enter worker ID:&quot;))
qry=&quot;select*from worker_details where w_id=%s;&quot;%(exp,)
df=pd.read_sql(qry,conn)
print(df)

def update_doctor_details():
print(&quot;change department of doctor&quot;)
dept1=input(&quot;enter new department:&quot;)
id_1=int(input(&quot;enter the doctor ID :&quot;))
c1=conn.cursor()
c1.execute(&quot;update doctor_details set d_department=&#39;&quot; + dept1 + &quot;&#39;
where d_id=&#39;&quot; + str(id_1) + &quot;&#39;&quot;)
conn.commit()
df=pd.read_sql(&quot;select*from doctor_details&quot;,conn)
print(df)
print(&quot;department updated&quot;)

def update_patient_details():
print(&quot;change phono of patient &quot;)
phon1=int(input(&quot;enter new phone number:&quot;))
id_1=int(input(&quot;enter patient ID:&quot;))
c1=conn.cursor()
c1.execute(&quot;update patient_details set p_phono=&#39;&quot; + str(phon1) + &quot;&#39;
where p_id=&#39;&quot; + str(id_1) + &quot;&#39;&quot;)
conn.commit()
df=pd.read_sql(&quot;select*from patient_details&quot;,conn)
print(df)
print(&quot;phono updated&quot;)
def update_worker_details():
print(&quot;change age of worker&quot;)
age1=int(input(&quot;enter new age of worker:&quot;))
id_1=int(input(&quot;enter worker ID:&quot;))
c1=conn.cursor()
c1.execute(&quot;update worker_details set w_age=&#39;&quot; + str(age1) + &quot;&#39; where
w_id=&#39;&quot; + str(id_1) + &quot;&#39;&quot;)
conn.commit()
df=pd.read_sql(&quot;select*from worker_details&quot;,conn)
print(df)
print(&quot;age updated&quot;)

def create_bill_details():
c1=conn.cursor()
c1.execute(&#39;create table bill_details(p_id int(5),p_name varchar(20)
primary key,p_age int(3), drvisit varchar(35),medicines varchar(50), room
int(2),totalbill int(20))&#39;)
print(&quot;table created&quot;)
def insert_bill_details():
print(&quot;enter patient details for a bill&quot;)
p_id=int(input(&quot;enter ID of patient:&quot;))
p_name=input(&quot;enter the name of the patient:&quot;)
p_age=int(input(&quot;enter the age of the patient:&quot;))
drvisit=int(input(&quot;enter fee of drvisit:&quot;))
medicines=int(input(&quot;enter the cost of medicines:&quot;))
room=int(input(&quot;enter room charges:&quot;))
totalbill=drvisit+medicines+room
sql_insert=&quot;insert into
bill_details(p_id,p_name,p_age,drvisit,medicines,room,totalbill) values
(%s, %s, %s, %s, %s,%s,%s)&quot;
val=(str(p_id),
p_name,str(p_age),str(drvisit),str(medicines),str(room), str(totalbill))
c1.execute(sql_insert,val)
conn.commit()
def show_records_bill():
print(&quot;all records of bill&quot;)
df=pd.read_sql(&quot;select*from bill_details&quot;,conn)
print(df)

def delcol():
df=pd.read_sql(&quot;select*from bill_details&quot;,conn)
print(df)
dc=input(&quot;enter the column you want to delete:&quot;)
print()
print()
print(&quot;column deleted&quot;)
del df[dc]
print(df)

def delrecord_worker():
name1=input(&quot;enter name of the worker you want to delete:&quot;)
c1=conn.cursor()
c1.execute(&quot;delete from worker_details where w_name=&#39;&quot;+name1+&quot;&#39;&quot;)
print(&quot;record deleted&quot;)
conn.commit()
def sort_workers():
print(&quot;sorting worker names in ascending order&quot;)
print()
df=pd.read_sql(&quot;select*from worker_details&quot;,conn)
df=df.sort_values(&#39;w_name&#39;)
print(df)

conn=sql.connect(host=&#39;Localhost&#39;,user=&#39;root&#39;,passwd=&#39;bhavani27&#39;,database=&#39;
hospital&#39;)
if conn.is_connected():
print(&#39;successfully connected&#39;)
c1=conn.cursor()
print(&quot;*********************************&quot;)
print(&quot; HOSPITAL MANAGAEMENT SYSTEM&quot;)
print(&quot;*********************************&quot;)

print(&quot;Please Enter your login details:&quot;)
inp_username=input(&quot;enter your username:&quot;)
inp_password=input(&quot;enter your password:&quot;)
if inp_username == &quot;admin&quot; and inp_password == &quot;password&quot;:
run_admin_mode()
elif inp_username == &quot;user&quot; and inp_password == &quot;pass&quot;:
run_user_mode()
else:
print(&quot;Wrong credentials, please try again&quot;)
quit()
