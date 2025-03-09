def main() : 
	x = torch.tensor([[ i*0.4 for i in range(12)] for j in range(3) ] ) 
	tt = x.numpy() 
	tt.t_() 
	print(x) 
	print(tt)  


if __name__ == "__main__" : 
	print("hello my men ") 
	main() 
