
#datasets[key] = (arr_small, arr_medium, arr_large)

def run_variation_counter(dataset:dict) ->dict:

    run_data = {}

    for key,dataset_tuple in dataset.items():
        runs_per_size = []


        for array_size in dataset_tuple:

            data_length = len(array_size)
            if data_length == 0:
                runs = 0 
                normalised_run_metric = 0
                runs_per_size.append((runs, normalised_run_metric))
            elif data_length < 2:
                    
                    runs = 1
                    normalised_run_metric = runs/data_length
                    runs_per_size.append((runs, normalised_run_metric))
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

                normalised_run_metric = runs/data_length
                runs_per_size.append((runs,normalised_run_metric))
        run_data[key] = runs_per_size
        
    return run_data

