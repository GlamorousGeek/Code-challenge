
# coding: utf-8

# In[1]:


import pandas as pd  # imported pandas(it is a python tool for datastructure and analysis) from python libary 
import numpy as np   #imported numpy{ it is a numerical python libary for numerical computation} from python libary


# In[ ]:


# i have converted the files to a csv format for easy manipulation because I treated it as a dataset


# In[54]:


# i use the pd.read function from the pandas libary to read in the data
abiaV = pd.read_csv("Abia_votes.csv") 
enuguV = pd.read_csv("Enugu_votes.csv")
kadunaV = pd.read_csv("Kaduna_votes.csv")
lagosV = pd.read_csv("Lagos_votes.csv")
oyoV = pd.read_csv("oyo_votes.csv")


# In[55]:


# created a copy of the dataset (each state data for easy reference to original)
abiaC = abiaV.copy()
enuguC = enuguV.copy()
kadunaC = kadunaV.copy()
lagosC =lagosV.copy()
oyoC = oyoV.copy()


# # a. Using a function/class, count the number of votes  each party received in each state.  

# In[57]:


lagosC.Lagos.value_counts() # i use the count function from pandas to count all the party vote  in lagos


 In[60]:ACP    113
        YYP    106
        SDP    100
        APC     97
        PDP     84


abiaC.Abia.value_counts() # i use the count function from pandas to count all the party vote  in abia


 In[61]:YYP    74
        ACP    67
        PDP    67
        APC    64
        SDP    53


enuguC.Enugu.value_counts() # i use the count function from pandas to count all the party vote  in enugu


 In[62]:PDP    67
        APC    63
        SDP    59
        ACP    56
        YYP    55


oyoC.Oyo.value_counts() # i use the count function from pandas to count all the party vote  in oyo

 In[63]:SDP    82
        ACP    74
        YYP    70
        APC    70
        PDP    54


kadunaC.Kaduna.value_counts() # i use the count function from pandas to count all the party vote  in kaduna
In[63]: YYP    89
        PDP    83
        ACP    81
        APC    75
        SDP    72



# # b. Which party had the most votes in each state?  

abiaC["Abia"].value_counts().idxmax() #i use the count.idxmax() function from pandas to count and return the party with the highest vote count


In[65]:'YYP'


lagosC["Lagos"].value_counts().idxmax()


In[66]:'ACP'


enuguC["Enugu"].value_counts().idxmax()


In[67]:'PDP'


oyoC["Oyo"].value_counts().idxmax()


In[69]:'SDP'


kadunaC["Kaduna"].value_counts().idxmax()


In[11]:'YYP'


abiaVoteCount = abiaC["Abia"].value_counts()
abiaVoteCount.head()


# # c. who had the most votes in the entire country ? 

# # i use pandas function (pd.Dataframe) to convert the votes of each party in a state into a dataframe (dataframe means a pandas dataset entity treating all elements as one) 

abiaVoteCountN = pd.DataFrame(abiaVoteCount)
abiaVoteCountN.head()
enuguVoteCountN = pd.DataFrame(enuguVoteCount)
enuguVoteCountN.head()
lagosVoteCountN = pd.DataFrame(lagosVoteCount)
lagosVoteCountN.head()
oyoVoteCountN = pd.DataFrame(oyoVoteCount)
oyoVoteCountN.head()
kadunaVoteCountN = pd.DataFrame(kadunaVoteCount)
kadunaVoteCountN.head()

 ## after converting each dataset to a dataframe i will now concatenate them to form one large dataset for easy manipulation

Total = pd.concat([enuguVoteCountN,kadunaVoteCountN,abiaVoteCountN,lagosVoteCountN,oyoVoteCountN], axis=1) # i the pd.concat functon from pandas libary to concatenate dataframe of the state from the previous solution
Total['Sum']= Total.apply(lambda row: row.Enugu + row.Kaduna + row.Abia + row.Lagos + row.Oyo, axis=1) # i use the lambda function to get of the total votes of each party in every state to produce another column called sum  
Total["Sum"].argmax()  #i use the arg.max function to print out the party with in highest total vote the entire country

In[83]:'YYP'


# # d. Now suppose we find out that 20% of the APC votes from Lagos were from voters that did not exist, 
# #and 30% of PDP's votes from Enugu were also falsified, determine who might be the new winner? 




Total.loc['APC','Lagos'] # i use the .loc funtion to locate and index out the value of apc in lagos
Total.loc['APC','Lagos'] = Total.loc['APC','Lagos']-(Total.loc['APC','Lagos'] * 0.2) # we calculated 20% of apc vote in lagos and deducted it from the actual value of apc vote and replaced it 
Total.loc['PDP','Enugu']  # i use the .loc funtion to locate and index out the value of pdp in enugu
Total.loc['PDP','Enugu'] = Total.loc['PDP','Enugu']-(Total.loc['PDP','Enugu'] * 0.30) # we calculated 30% of pdp vote in enugu and deducted it from the actual value of pdp vote and replace it
Total["Sum"].argmax() # Use the new values to calculate the new winner


 In[27]:'YYP'


#In addition to the falsification,suppose we found out that 30% of the YYP's total votes recorded by INEC were changed to ACP's vote, 
#determine who might be the new winner ? 

Total.loc['YYP','Sum'] # i use the .loc funtion to locate and index out the value of total votes of yyp  
Total.loc['YYP','Sum'] = Total.loc['ACP','Sum'] + (Total.loc['YYP','Sum']*0.3) # i calculated 30% yyp total vote  and added it to acp totalvote and replace it
Total.loc['ACP','Sum'] #WE INDEX OUT THE VALUE OF ACP TOTAL VOTE(SUM)
Total.loc['ACP','Sum'] + (Total.loc['YYP','Sum']*0.3)  #WE ADDED 30% OF YYP TOTAL VOTE TO ACP TOTAL VOTE
Total.loc['YYP','Sum'] - (Total.loc['YYP','Sum']*0.3)# WE MINUS  30% OF YYP TOTALVOTE FROM THE SUM OF YYP
Total.loc['YYP','Sum'] = Total.loc['YYP','Sum'] - (Total.loc['YYP','Sum']*0.3) # WE EQUTED THE 30% OF 
Total.loc['ACP','Sum'] =Total.loc['ACP','Sum'] + (Total.loc['YYP','Sum']*0.3) #WE EQUATED THE 30% OF YYP TOTAL VOTE THAT WAS ADDED TO ACP TOTAL VOTE TO THE INITIAL STATE OF THE SUM OF YYP
Total["Sum"].argmax()    # Use the new values to calculate the new winner

 In[88]:'ACP'


# # Now suppose the inauguration date of the winner is May 15th 2019, write code that will always determine 
# #the current number of days until the ceremony.  

import datetime  #imports datetime from python libary

days_till_inauguration = (datetime.datetime(2019,5,29) - datetime.datetime.now()).days #subtracting present date from inauguration date
days_till_inauguration

 In[52]:209

# # Lastly out of these 5 parties,  tell me which party you are most likely to vote for? (free will answer). 

 In[1]:I will vote YYP


print('I will vote YYP')

