DROP TABLE IF EXISTS departments;

CREATE TABLE departments(
	id serial primary key,
	dept_no varchar(30),
	dept_name varchar(30)
	);

DROP TABLE IF EXISTS dept_emp;

CREATE TABLE dept_emp(
	id serial primary key,
	emp_no int,
	dept_no varchar(30)
	);

DROP TABLE IF EXISTS dept_manager;

CREATE TABLE dept_manager(
	id serial primary key,
	dept_no varchar(30),
	emp_no int
	);

DROP TABLE IF EXISTS employees;

CREATE TABLE employees(
	id serial primary key,
	emp_no int,
	emp_title_id VARCHAR(30),
	birth_date DATE,
	first_name VARCHAR(30),
	last_name VARCHAR(30),
	sex VARCHAR(3),
	hire_date DATE
	);

DROP TAblE IF EXISTS salaries;

CREATE TABLE salaries(
	id serial primary key,
	emp_no int, 
	salary int
	);

DROP TABLE IF EXISTS titles;

CREATE TABLE titles(
	id serial primary key, 
	title_id varchar(30),
	title varchar(30)
	);