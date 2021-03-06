{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [],
   "source": [
    "# imports \n",
    "from sqlalchemy import create_engine\n",
    "import matplotlib.pyplot as plt\n",
    "import numpy as np\n",
    "import pandas as pd\n",
    "import psycopg2"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [],
   "source": [
    "#import database from pgadmin\n",
    "dataset_ref = psycopg2.connect(host=\"localhost\", port = 5432, database=\"sql-challenge\", user=\"postgres\", password=\"maxine\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Create a cursor object \n",
    "dataset = dataset_ref.cursor()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "metadata": {},
   "outputs": [
    {
     "ename": "AttributeError",
     "evalue": "'psycopg2.extensions.connection' object has no attribute 'table'",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mAttributeError\u001b[0m                            Traceback (most recent call last)",
      "\u001b[0;32m<ipython-input-20-ed6a9621faa7>\u001b[0m in \u001b[0;36m<module>\u001b[0;34m\u001b[0m\n\u001b[0;32m----> 1\u001b[0;31m \u001b[0manswers_table_ref\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mdataset_ref\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mtable\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\"titles\"\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[0;31mAttributeError\u001b[0m: 'psycopg2.extensions.connection' object has no attribute 'table'"
     ]
    }
   ],
   "source": [
    "emp_salary = dataset.execute(\"\"\"\n",
    "    SELECT   \n",
    "    FROM employees AS e \n",
    "        INNER JOIN salaries as s\n",
    "            ON e.id = s.id\n",
    "    GROUP BY \n",
    "    \"\"\")\n",
    "query_results = cur.fetchall()\n",
    "print(query_results)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "metadata": {},
   "outputs": [
    {
     "ename": "AttributeError",
     "evalue": "'NoneType' object has no attribute 'to_dataframe'",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mAttributeError\u001b[0m                            Traceback (most recent call last)",
      "\u001b[0;32m<ipython-input-22-248d445e95c1>\u001b[0m in \u001b[0;36m<module>\u001b[0;34m\u001b[0m\n\u001b[1;32m     10\u001b[0m \"\"\")\n\u001b[1;32m     11\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 12\u001b[0;31m \u001b[0msalary_by_title\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0msalarytitle_query\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mto_dataframe\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[0;31mAttributeError\u001b[0m: 'NoneType' object has no attribute 'to_dataframe'"
     ]
    }
   ],
   "source": [
    "#Create a bar chart of average salary by title\n",
    "salarytitle_query = dataset.execute(\"\"\"\n",
    "    SELECT AVG(s.salary) AS avg_salary, t.title\n",
    "    FROM titles AS t \n",
    "        INNER JOIN employees AS e\n",
    "            ON e.emp_title_id = t.title_id\n",
    "        INNER JOIN salaries s \n",
    "           ON e.emp_no = s.emp_no\n",
    "    GROUP BY t.title \n",
    "\"\"\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[(473302, 's0001', datetime.date(1953, 7, 25), 'Hideyuki', 'Zallocco', 'M', datetime.date(1990, 4, 28)), (475053, 'e0002', datetime.date(1954, 11, 18), 'Byong', 'Delgrande', 'F', datetime.date(1991, 9, 7)), (57444, 'e0002', datetime.date(1958, 1, 30), 'Berry', 'Babb', 'F', datetime.date(1992, 3, 21)), (421786, 's0001', datetime.date(1957, 9, 28), 'Xiong', 'Verhoeff', 'M', datetime.date(1987, 11, 26)), (282238, 'e0003', datetime.date(1952, 10, 28), 'Abdelkader', 'Baumann', 'F', datetime.date(1991, 1, 18))]\n"
     ]
    }
   ],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
