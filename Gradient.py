

for i in list(range(len(s))): 
     for j in list(range(len(s[i]))): 
         print(s[i][j]) 


for i in list(range(len(s))):
	if s[i][2]==0:
		s[i]=(0,1,1)

print(s)
	



def adjust_list(term):
	for i in list(range(len(term)):
		if term[i][2]==0:
			term[i][:]=(0,1,1)
	



def df_dy(term):
        return ((term[0][0],term[0][1],term[0][2]-1),
                (term[1][0],term[1][1],term[1][2]-1),
                (term[2][0],term[2][1],term[2][2]-1))



def three_x_y_at_one(x):
    return 3*1*x

three_x_y_at_one(3) # 9

zero_to_ten = list(range(0, 11))


def y_values_for_at_one(x_values):
    return three_x_y_at_one(x_values)


def y_values_for_at_one(x_values): 
	y_val=list(map(lambda x:three_x_y_at_one(x),x_values))   
	return y_val


def multivariable_output_at(list_of_terms, x_value, y_value):
    return (list_of_terms[0][0]*x_value**list_of_terms[0][1]*y_value**list_of_terms[0][2]+
	   list_of_terms[1][0]*x_value**list_of_terms[1][1]*y_value**list_of_terms[1][2]+
	   list_of_terms[2][0]*x_value**list_of_terms[2][1]*y_value**list_of_terms[2][2])



def term_df_dx(term):
	return((term[0][0]*term[0][1],term[0][1]-1,term[0][2]),
		(term[1][0]*term[1][1],term[1][1]-1,term[1][2]),
		(term[2][0]*term[2][1],term[2][1]-1,term[2][2]))


def term_df_dx_at_x_y(term,x_value,y_value):
      return (list_of_terms[0][0]*list_of_terms[0][1]*x_value**(list_of_terms[0][1]-1)*y_value**list_of_terms[0][2]+
              list_of_terms[1][0]*list_of_terms[1][1]*x_value**(list_of_terms[1][1]-1)*y_value**list_of_terms[1][2]+
   	      list_of_terms[2][0]*list_of_terms[2][1]*x_value**(list_of_terms[2][1]-1)*y_value**list_of_terms[2][2])

