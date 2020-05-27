import glassdoor_scraper as gs
import pandas as pd

path= r"E:/ds_salary_project/chromedriver"

df = gs.get_jobs('data scientist',10,False,path,10)
df
