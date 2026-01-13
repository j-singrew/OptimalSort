


def run_variation_counter(run_dataset:list):
    run_counter = 0

    for dataset in run_dataset:
        if not dataset:
            continue
        current_run_length = 1

        for i in range(1,len(dataset)):
            if dataset[i] >= dataset[i-1]) or (dataset[i] <= dataset[i-1]):
                current_run_length += 1
            else :
                current_run_length = 1
        
        run_counter += current_run_length

    return run_counter

