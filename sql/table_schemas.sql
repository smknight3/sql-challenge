DROP TABLE IF EXISTS employees;

CREATE TABLE employees(
	emp_no int NOT NULL,
	emp_title_id VARCHAR(30) NOT NULL,
	birth_date DATE NOT NULL,
	first_name VARCHAR(30) NOT NULL,
	last_name VARCHAR(30) NOT NULL,
	sex VARCHAR(3) NOT NULL,
	hire_date DATE,
	PRIMARY KEY(emp_no)
	);
	
DROP TABLE IF EXISTS departments;

CREATE TABLE departments(
	dept_no varchar(30) NOT NULL,
	dept_name varchar(30) NOT NULL, 
	Primary Key (dept_no)
	);

DROP TABLE IF EXISTS dept_emp;

CREATE TABLE dept_emp(
	emp_no int NOT NULL,
	dept_no varchar(30) NOT NULL,
	PRIMARY KEY (emp_no, dept_no),
	FOREIGN KEY (dept_no) REFERENCES departments(dept_no),
	FOREIGN KEY (emp_no) REFERENCES employees (emp_no)
	);

DROP TABLE IF EXISTS dept_manager;

CREATE TABLE dept_manager(
	dept_no varchar(30) NOT NULL,
	emp_no int NOT NULL,
	PRIMARY KEY (emp_no, dept_no),
	FOREIGN KEY (dept_no) REFERENCES departments (dept_no), 
	FOREIGN KEY (emp_no) REFERENCES employees (emp_no)
		);

DROP TABLE IF EXISTS salaries;

CREATE TABLE salaries(
	emp_no int NOT NULL, 
	salary int NOT NULL,
	PRIMARY KEY (emp_no),
	FOREIGN KEY (emp_no) REFERENCES employees (emp_no)
);

DROP TABLE IF EXISTS titles;

CREATE TABLE titles(
	title_id varchar(30) NOT NULL,
	title varchar(30) NOT NULL,
	PRIMARY KEY (title_id)
	);

ALTER TABLE "employees" ADD CONSTRAINT "fk_employees_emp_title_id" FOREIGN KEY ("emp_title_id") REFERENCES "titles"(title_id);
