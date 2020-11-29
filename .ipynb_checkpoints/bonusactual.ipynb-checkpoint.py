{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {},
   "outputs": [],
   "source": [
    "#imports\n",
    "from sqlalchemy import create_engine\n",
    "import matplotlib.pyplot as plt\n",
    "import numpy as np\n",
    "import pandas as pd\n",
    "import psycopg2"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 38,
   "metadata": {},
   "outputs": [],
   "source": [
    "# collaborated with Tim Schurmann "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 39,
   "metadata": {},
   "outputs": [],
   "source": [
    "#import database from pgadmin\n",
    "username = 'postgres'\n",
    "password = 'maxine'\n",
    "engine = create_engine(f'postgresql://{username}:{password}@localhost:5432/sql-challenge')\n",
    "connection = engine.connect()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 40,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>title_id</th>\n",
       "      <th>title</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>s0001</td>\n",
       "      <td>Staff</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>s0002</td>\n",
       "      <td>Senior Staff</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>e0001</td>\n",
       "      <td>Assistant Engineer</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>e0002</td>\n",
       "      <td>Engineer</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>e0003</td>\n",
       "      <td>Senior Engineer</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>e0004</td>\n",
       "      <td>Technique Leader</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6</th>\n",
       "      <td>m0001</td>\n",
       "      <td>Manager</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "  title_id               title\n",
       "0    s0001               Staff\n",
       "1    s0002        Senior Staff\n",
       "2    e0001  Assistant Engineer\n",
       "3    e0002            Engineer\n",
       "4    e0003     Senior Engineer\n",
       "5    e0004    Technique Leader\n",
       "6    m0001             Manager"
      ]
     },
     "execution_count": 40,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "pd.read_sql_query(\"\"\"\n",
    "    SELECT\n",
    "    * \n",
    "    FROM\n",
    "    titles\"\"\", connection)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 56,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>emp_no</th>\n",
       "      <th>salary</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>10001</td>\n",
       "      <td>60117</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>10002</td>\n",
       "      <td>65828</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>10003</td>\n",
       "      <td>40006</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>10004</td>\n",
       "      <td>40054</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>10005</td>\n",
       "      <td>78228</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   emp_no  salary\n",
       "0   10001   60117\n",
       "1   10002   65828\n",
       "2   10003   40006\n",
       "3   10004   40054\n",
       "4   10005   78228"
      ]
     },
     "execution_count": 56,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Create a histogram to visualize the most common salary ranges for employees.\n",
    "salary_df = pd.DataFrame()\n",
    "salary_df = pd.read_sql_query(\"\"\"SELECT emp_no, salary FROM salaries\"\"\", connection)\n",
    "salary_df.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 59,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "salary_df.salary.hist(color = 'seagreen')\n",
    "# Give our chart some labels and a tile\n",
    "plt.title(\"Most Common Salary Ranges\", fontname = 'Times New Roman', fontsize = 14, fontweight = 'bold')\n",
    "plt.xlabel(\"Salary Range\", fontname = 'Times New Roman',fontsize = 12)\n",
    "plt.ylabel(\"Number of Employees\", fontsize = 12, fontname = 'Times New Roman')\n",
    "#show/save\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "pd.read_sql_query(\"\"\"\n",
    "    SELECT\n",
    "    * \n",
    "    FROM\n",
    "    titles\"\"\", connection)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 42,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>avg_salary</th>\n",
       "      <th>title</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>48564.434447</td>\n",
       "      <td>Assistant Engineer</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>48535.336511</td>\n",
       "      <td>Engineer</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>51531.041667</td>\n",
       "      <td>Manager</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>48506.799871</td>\n",
       "      <td>Senior Engineer</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>58550.172704</td>\n",
       "      <td>Senior Staff</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "     avg_salary               title\n",
       "0  48564.434447  Assistant Engineer\n",
       "1  48535.336511            Engineer\n",
       "2  51531.041667             Manager\n",
       "3  48506.799871     Senior Engineer\n",
       "4  58550.172704        Senior Staff"
      ]
     },
     "execution_count": 42,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Create a bar chart of average salary by title\n",
    "\n",
    "salaries_by_title = pd.DataFrame()\n",
    "salaries_by_title = pd.read_sql_query(\"\"\"\n",
    "SELECT AVG(s.salary) AS avg_salary, t.title\n",
    "FROM titles AS t \n",
    "    INNER JOIN employees AS e \n",
    "        ON e.emp_title_id = t.title_id\n",
    "    INNER JOIN salaries AS s\n",
    "        ON e.emp_no = s.emp_no\n",
    "GROUP BY t.title\n",
    "\"\"\", connection\n",
    ")\n",
    "\n",
    "salaries_by_title.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 61,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 720x432 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "x = salaries_by_title.title\n",
    "y = salaries_by_title.avg_salary\n",
    "\n",
    "#figsize\n",
    "plt.figure(figsize=(10,6))\n",
    "\n",
    "#raw plot\n",
    "plt.bar(x, y, color='seagreen', alpha=0.5, align=\"center\")\n",
    "\n",
    "#PADDING\n",
    "plt.xlim(-0.75, len(x)-0.25)\n",
    "plt.ylim(0, max(y)+5000)\n",
    "\n",
    "# Give our chart some labels and a tile\n",
    "plt.title(\"Average Salary by Title\", fontname = 'Times New Roman', fontsize = 14)\n",
    "plt.xlabel(\"Title\", fontname = 'Times New Roman', fontsize = 12)\n",
    "plt.ylabel(\"Average Salary\", fontname = 'Times New Roman', fontsize = 12)\n",
    "\n",
    "#show/save\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "salary_df.loc[salary_df.emp_no == "
   ]
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
