


def run_variation_counter(dataset:dict) ->dict:

    run_data = {}
    for key,dataset_tuple in dataset.items():
        runs_per_size = []

        for dataset in dataset_tuple:
            if not dataset.all():
                runs_per_size.append(0)
                continue

            current_run_length = 1
            total_runs = 0

            for i in range(1,len(dataset)):
                
                if (dataset[i] >= dataset[i-1]):
                    current_run_length += 1
                else:
                    total_runs +=current_run_length
                    current_run_length = 1
        
            total_runs += current_run_length
            runs_per_size.append(total_runs)

        run_data[key] = runs_per_size
    print(run_data)
    return run_data

