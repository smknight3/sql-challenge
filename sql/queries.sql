-- Question One

SELECT
e.emp_no, e.last_name, e.first_name, e.sex, s.salary
FROM 
employees e 
JOIN salaries s ON e.emp_no = s.emp_no;

--Question Two 

SELECT 
first_name, last_name, hire_date
FROM 
employees
WHERE 
EXTRACT(YEAR FROM hire_date) = 1986;

--Question Three 


SELECT
d.dept_no, d.dept_name, x.emp_no, e.last_name, e.first_name
FROM 
departments d
JOIN dept_manager x ON d.dept_no = x.dept_no
	JOIN employees as e ON x.emp_no = e.emp_no;

--Question Four

SELECT
d.dept_no, d.dept_name, x.emp_no, e.last_name, e.first_name
FROM 
departments d
JOIN dept_emp x ON d.dept_no = x.dept_no
	JOIN employees as e ON x.emp_no = e.emp_no;
	
--Question Five 

SELECT 
first_name, last_name, sex
FROM 
employees
WHERE first_name LIKE 'Hercules' AND last_name LIKE 'B%';

--Question Six 

SELECT
d.dept_name, x.emp_no, e.last_name, e.first_name
FROM 
departments d
JOIN dept_emp x ON d.dept_no = x.dept_no
	JOIN employees as e ON x.emp_no = e.emp_no
WHERE dept_name = 'Sales';

--Question Seven

SELECT
d.dept_name, x.emp_no, e.last_name, e.first_name
FROM 
departments d
JOIN dept_emp x ON d.dept_no = x.dept_no
	JOIN employees as e ON x.emp_no = e.emp_no
WHERE dept_name = 'Sales' OR dept_name = 'Development';

--Question Eight

SELECT 
last_name, COUNT(1) AS frequency
FROM 
employees
GROUP BY last_name
ORDER BY frequency DESC;
