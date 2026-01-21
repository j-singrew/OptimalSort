
#datasets[key] = (arr_small, arr_medium, arr_large)

def run_variation_counter(dataset:dict) ->dict:

    run_data = {}


    for key,dataset_tuple in dataset.items():
        runs_per_size = []


        for array_size in dataset_tuple:

            data_length = len(array_size)
            unique_length = len(set(array_size))
            
            if data_length == 0:
                runs = 0 
                normalised_run_metric = 0
                runs_per_size.append((0, 0.0,0.0))
            
            
            elif data_length < 2:
                    duplicate_ratio = ( data_length -  unique_length) / data_length
                    runs = 1

                    runs_per_size.append((1, 1.0,duplicate_ratio))
                    continue
            else:
                runs = 1
                direction = 0 
                for i in range(1,data_length):
                    if array_size [i] > array_size [i-1]:
                        new_dir = 1

                    elif array_size [i] < array_size [i -1]:
                        new_dir = -1
                
                    else:
                        continue


                    if direction == 0:
                        direction = new_dir
                    elif new_dir != direction:
                        runs +=1
                        direction = new_dir
                duplicate_ratio = ( data_length -  unique_length) / data_length
                normalised_run_metric = runs/data_length
                runs_per_size.append((runs,normalised_run_metric,duplicate_ratio ))
                
        run_data[key] = (runs_per_size,data_length)
        
    return run_data

