from VectorizedbAbI import VectorizedbAbI


task_ids = [1]


data_pipe = VectorizedbAbI(
    task_ids=task_ids
)

for s, q, a in data_pipe.train_data_pipe:

    for ss in s:

        for idx in ss:
            print(data_pipe.train_vocab.get_itos()[idx], end=' ')
        print('\n')
    for qq in q:
        for idx in qq:
            print(data_pipe.train_vocab.get_itos()[idx], end=' ')
        print('\n')
    for aa in a:
        for idx in aa:
            print(data_pipe.train_vocab.get_itos()[idx], end=' ')

    break

