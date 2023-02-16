def game(terra, power):
    for ind, val in enumerate(terra):
        for ind_1, val_1 in enumerate(val):            
            if power < val_1:
                break
            else:
                power += val_1
        
        
                



            

   
    






terra = [[1, 1, 5, 10], [10, 2], [1, 1, 1]]
power = 1 

game(terra , power)