


def run_variation_counter(dataset:dict) ->dict:

    run_data = {}

    for key,dataset_tuple in dataset.items():
        runs_per_size = []

        for data in dataset_tuple:
            for arr in dataset_tuple:
                if len(data) < 2:
                    runs_per_size.append(1)
                    continue

            runs = 1
            direction = 0 

            for i in range(1,len(data)):
                if data[i] > data[i-1]:
                    new_dir = 1

                elif data[i] < data[i -1]:
                    new_dir = -1
                
                else:
                    continue


                if direction == 0:
                    direction = new_dir
                elif new_dir != direction:
                    runs +=1
                    direction = new_dir

                    
            runs_per_size.append(runs)
        run_data[key] = runs_per_size   
        
    return run_data

