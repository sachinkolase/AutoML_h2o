
# coding: utf-8

# In[1]:


import h2o


# In[2]:


from h2o.automl import H2OAutoML


# In[3]:


h2o.init()


# In[4]:


df = h2o.import_file('loan prediction.csv')


# In[5]:


df.head()


# In[6]:


df.names()


# In[7]:


df.name


# In[8]:


df.names


# In[9]:


df['Loan_Status']=df['Loan_Status'].asfactor()


# In[10]:


y = "Loan_Status"
x = ['Gender','Married','Education','ApplicantIncome','LoanAmount','CoapplicantIncome','Loan_Amount_Term','Credit_History','Property_Area']


# In[11]:


aml = H2OAutoML(max_models = 30, max_runtime_secs=300, seed = 1)


# In[12]:


aml.train(x = x, y = y, training_frame = df)


# In[13]:


lb = aml.leaderboard


# In[14]:


lb.head()


# In[15]:


lb.head(rows=lb.nrows)

