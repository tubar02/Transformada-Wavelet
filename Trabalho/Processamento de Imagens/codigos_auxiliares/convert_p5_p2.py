import sys

def convert(fname_in: str, fname_out: str):
    res = []
    with open(fname_in, 'rb') as f:
        assert f.readline() == b'P5\n'

        data = f.readline().decode().strip().split()
        assert len(data) == 2
        width, height = map(int, data)

        max_val = int(f.readline().decode())
        assert 0 < max_val < 256

        for _ in range(height):
            res.append(list(f.read(width)))

    with open(fname_out, 'w') as fout:
        fout.write(f'P2\n{width} {height}\n{max_val}\n')
        for line in res:
            fout.write(' '.join(map(str, line)) + '\n')



if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('Uso: python script.py <arq_p5_entrada> <arq_p2_saida>')
    else:
        convert(sys.argv[1], sys.argv[2])

