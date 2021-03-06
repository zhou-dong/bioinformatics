# Markov

#### Markov Chain

State   Ranny   Sunny   P_0         P_1             P_2             P_3  
Rainy   0.6     0.2     P(R_0) = 1  P(R_1) = 0.6    P(R_2) = 0.44   P(R_3) = 0.376  
Sunny   0.4     0.8     P(S_0) = 0  P(S_1) = 0.4    P(S_2) = 0.56   P(S_3) = 0.624

Know That:

0.6 + 0.4 = 1  
0.8 + 0.2 = 1  
1.0 + 0.0 = 1  

Method 1:

P(R_1) = P(R_0) * P(R_1|R_0) + P(S_0) * P(R_1|S_0)  
       = 1.0 * 0.6 + 0 * 0.2 = 0.6  
P(S_1) = P(R_0) * P(S_1|R_0) + P(S_0) * P(S_1|S_0)  
       = 1.0 * 0.4 + 0 * 0.8 = 0.4

P(R_2) = P(R_1) * P(R_2|R_1) + P(S_1) * P(R_2|S_1)  
       = 0.6 * 0.6 + 0.4 * 0.2 = 0.44  
P(S_2) = P(R_1) * P(S_2|R_1) + P(S_1) * P(S_2|S_1)  
       = 0.6 * 0.4 + 0.4 * 0.8 = 0.56

P(R_3) = P(R_2) * P(R_3|R_2) + P(S_2) * P(R_3|S_2)  
       = 0.44 * 0.6 + 0.56 * 0.2 = 0.376  
P(S_3) = P(R_2) * P(S_3|R_2) + P(S_2) * P(S_3|S_2)  
       = 0.44 * 0.4 + 0.56 * 0.8 = 0.624

Method 2:

[ 0.6 0.2 ] --- | 1 | = | 0.6 | = | 0.44 | =  | 0.376 |   
[ 0.4 0.8 ] --- | 0 | = | 0.4 | = | 0.56 | =  | 0.624 |

Stationary Distribution:

P(R_T) = P(R_{T_1})

P(R_{T-1}) * P(R_T|R_{T_1}) + P(S_{T_1}) * P(R_T|S_{T_1}) = P(R_{T_1})

Let:

P(R_{T_1}) = x  
P(S_{T_1}) = 1 - x

Then:

x * 0.6 + 0.2 * (1 - x) = x  
        0.2 = 0.6x  
        x = 1/3

P(R) = 1/3  
P(S) = 2/3

#### Transition Probabilities:

R S S S R S R

P(R_0) = 1  
P(R|S) = 2/4 = 1/2  
P(S|S) = 2/4 = 1/2  
P(R|R) = 0/2 = 0  
P(S|R) = 2/2 = 1  

#### Happy or Grumpy problem

State   Happy   Grumpy
Rain    0.4     0.6
Sunny   0.9     0.1

Let P(R_0) = 1 P(S_0) = 0  

OBSERVE: H_1

PROBABILITY: Rain

P(H_1) * P(R_1|H_1)  = P(R_1) * P(H_1|R_1)

P(R_1|H_1) = P(R_1) * P(H_1|R_1) / P(H_1) = 0.6 * 0.4 / (0.6 * 0.4 + 0.4 * 0.9)
