import os
import time
from itertools import product
from tqdm import tqdm
def mutate(visual_shape):
    # ['.##', '###', '##.']
    def rotate_90(s):
        return [''.join(row) for row in zip(*s[::-1])]

    def flip_h(s):
        return [row[::-1] for row in s]

    def flip_v(s):
        return s[::-1]
    
    vs1 = visual_shape
    vs2 = rotate_90(vs1)
    return [vs1,flip_h(vs1), flip_v(vs1),flip_h(flip_v(vs1)), vs2, flip_h(vs2), flip_v(vs2), flip_h(flip_v(vs2))]
    
    

def main(file_name):
    file_path = os.path.abspath(__file__)
    directory = os.path.dirname(file_path)
    with open(os.path.join(directory, file_name), "r") as f:
        data = f.read()

    d = data.split("\n\n")

    shapes = [0]*6
    for i,shape in enumerate(d[:-1]):
        s = shape.split("\n")
        idx=int(s[0][:-1])
        for row in s[1:]:
            for c in row:
                if c == "#":
                    shapes[idx] +=1


    ans = 0
    for row in tqdm(d[-1].split('\n')):
        xy = row.split(": ")[0]
        [width,height] = list(map(int,xy.split("x")))

        cnts = row.split(": ")[1]
        cnts = list(map(int,cnts.split(" ")))
        required = sum([a*b for a,b in zip(shapes,cnts)])

        if width//3 * height//3 >= sum(cnts):
            ans += 1
        elif width*height < required:
            continue
        else:
            raise Exception(f'{row} maybe possible')
    print(ans)


        


if __name__ == "__main__":
    start_time = time.perf_counter()
    # main("input_demo.txt")
    main("input.txt")
    end_time = time.perf_counter()
    print(f"Execution time: {end_time - start_time:.5f} seconds")
