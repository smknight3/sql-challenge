# Happy April Fool's! 

## Background

### Posing as a newly employed Data Engineer at Pewlett Hackard, my task was to conduct research on a series of csvs to describe aspects of the company's employees from the 90's and 80's. After surmising that the database was fake, I then created various visualizations of the data for further exploration. I was, in fact, correct; I had been the victim of an April Fool's prank. 

## Method and Tools 

### I first used http://www.quickdatabasediagrams.com to sketch an ERD of the six given tables in the database. After building a skeletal model of the tables and designating primary and foreign keys, the code was then transferred to pgadmin (from Postgresql) and edited to fit the proper layout of the csvs. 

### Once all CSVs were imported, the next step was to perform queries to analyze parts of the data. This was done using Postgresql syntax. 

### A righteously skeptical employee, I then imported the SQL dataset into pandas. I used both matplotlib and pandas to create a bar chart and histogram to analyze the employees' salaries. 

## Trends

### Each last name was repeated over 100 times, save, of course, the singular employee "April Foolsday". The salaries were fairly evenly distributed among all job titles. The average salary was heavily skewed to the left, where 150,000 employees made below 50k. 

## Limitations

### The data did not make much sense, as it was fake.   
