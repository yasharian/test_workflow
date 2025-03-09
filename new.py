import torch , numpy 
def main() : 
	x = torch.tensor([[ i*0.4 for i in range(12)] for j in range(3) ] ) 
	tt = x.numpy() 
	x.t_() 
	print(x) 
	print(tt)  
	print(torch.cuda.is_available()) 

if __name__ == "__main__" : 
	print("hello my men ") 
	main() 
