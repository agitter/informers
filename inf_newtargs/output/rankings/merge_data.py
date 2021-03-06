#!/home/ssericksen/anaconda2/bin/python2.7

import pandas as pd
import numpy as np
import sys

matrix = sys.argv[1] # 1 or 2
targ = sys.argv[2]   # bglf4 or pknb

df1 = pd.read_csv('./bl/BL_'+targ+'_pkis'+matrix+'.csv', index_col='molid' )
df2 = pd.read_csv('./cp/RS_'+targ+'_pkis'+matrix+'.csv', index_col='molid' ) 
df3 = pd.read_csv('./hz/CS_'+targ+'_pkis'+matrix+'.csv', index_col='molid' ) 
df4 = pd.read_csv('./hz/AS_'+targ+'_pkis'+matrix+'.csv', index_col='molid' )

df5 = pd.concat( [df1, df2, df3, df4], axis=1 )


df5[ ['b_cs', 'b_cl', 'b_cw', 'b_bs', 'b_bl', 'b_bw', 'RS', 'CS', 'AS' ] ].to_csv('pkis'+matrix+'_'+targ+'_model_rankings.csv', index_label='molid')

