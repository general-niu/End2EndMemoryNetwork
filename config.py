class Config(object):
    learning_rate = 0.01
    epsilon = 1e-8
    max_grad_norm = 40.0
    evaluation_interval = 10
    batch_size = 32
    hops = 3
    epochs = 100
    embedding_size = 40
    memory_size = 50
    random_state = None
    task_ids = [1, 7, 8, 11, 12, 13, 18, 20]
    data_dir = 'data/tasks_1-20_v1-2/en/'
    output_file = 'results.csv'
    val_size = 0.1
    stddev = 0.1
    learning_rate = 1e-2
    name ='memory'
    save_file = './weights/memory09'
    load_file = './weights/memory09'
