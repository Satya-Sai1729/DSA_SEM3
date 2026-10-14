https://1drv.ms/w/c/2A13EDEFEB2755B2/IQAitD5Y8qw8RKs-8dqpOojXATCVF-j7n_WuGrkc0paxzlY?e=4AVZU2
DECLARE
gs emp.sal%type;
ns emp.sal%type;
ded number(8,2);
t_empno emp.empno%type;
t_deptno emp.deptno%type;
t_name emp.ename%type;
t_sal emp.sal%type;

BEGIN
selelct empno,ename,deptno,sal into t_empno,t_name,t_deptno,t_sal from emp where empno='&empno';

t_sal:=nvl(t_sal,0)*12;

ded=3000;
gs:=t_sal+1200+1200;
ns:=gs_ded;
dbms_output.put_line('employee no is ....'||t_empno);
dbms_output.put_line('employee name is ...'||t_name);
dbms_output.put_line('employee deptno is ...'||t_deptno);
dbms_output.put_line('employee deductions are ..'||ded);
dbms_output.put_line('the gross salary is ...'||gs);
dbms_output.put_line('the net salary is ....'||ns);

EXCEPTION
when NO_DATA_FOUND then
dbms_output.put_line('the specified employee no does not exist');

END;
