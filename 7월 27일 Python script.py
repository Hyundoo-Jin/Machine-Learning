
# coding: utf-8

# In[1]:


################################## mnist 데이터를 이용하여 분석 실시하기 ##################################


# In[2]:


import tensorflow as tf


# In[3]:


from tensorflow.examples.tutorials.mnist import input_data


# In[4]:


mnist = input_data.read_data_sets('MNIST_data', one_hot = True)


# In[5]:


X = tf.placeholder(dtype = tf.float32, shape = [None, 784])
Y = tf.placeholder(dtype = tf.float32, shape = [None, 10])
drop_prob = tf.placeholder(dtype = tf.float32)


# In[6]:


W1 = tf.get_variable('W1', initializer = tf.contrib.layers.xavier_initializer(),
                    shape = [784, 588], dtype = tf.float32)     ### get_variable 함수를 이용하여 xavier initializtion 값 사용하기 ###
b1 = tf.Variable(tf.random_normal([588]), dtype = tf.float32)
L1 = tf.nn.relu(tf.matmul(X, W1) + b1)
L1 = tf.nn.dropout(L1, keep_prob = drop_prob)


# In[7]:


W2 = tf.get_variable('W2', initializer = tf.contrib.layers.xavier_initializer(),
                    shape = [588, 380], dtype = tf.float32)
b2 = tf.Variable(tf.random_normal([380]), dtype = tf.float32)
L2 = tf.nn.relu(tf.matmul(L1, W2) + b2)
L2 = tf.nn.dropout(L2, keep_prob = drop_prob)


# In[8]:


W3 = tf.get_variable('W3', initializer = tf.contrib.layers.xavier_initializer(),
                    shape = [380, 180], dtype = tf.float32)
b3 = tf.Variable(tf.random_normal([180]), dtype = tf.float32)
L3 = tf.nn.relu(tf.matmul(L2, W3) + b3)
L3 = tf.nn.dropout(L3, keep_prob = drop_prob)


# In[9]:


W4 = tf.get_variable('W4', initializer = tf.contrib.layers.xavier_initializer(),
                    shape = [180, 10], dtype = tf.float32)
b4 = tf.Variable(tf.random_normal([10]), dtype = tf.float32)
L4 = tf.nn.relu(tf.matmul(L3, W4) + b4)
L4 = tf.nn.dropout(L4, keep_prob = drop_prob)


# In[10]:


sess = tf.Session()
sess.run(tf.global_variables_initializer())


# In[16]:





# In[ ]:




