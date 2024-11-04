import os


def main():
    file_path = os.path.abspath(__file__)
    directory = os.path.dirname(file_path)
    with open(os.path.join(directory, "input.txt"), "r") as f:
        data = f.read().split("\n")

    score_shape = {"rock":1,"paper":2,"scissors":3}
    score_outcome = {"lose":0,"draw":3,"win":6}

    shape_dict = {'A':'rock','B':'paper','C':'scissors', 'X':'rock','Y':'paper','Z':'scissors'}
    outcome_dict = {('rock','rock'): 'draw', ('rock', 'paper'): 'win', ('rock', 'scissors'): 'lose', ('paper', 'rock'): 'lose', ('paper', 'paper'): 'draw', ('paper', 'scissors'): 'win', ('scissors', 'rock'): 'win', ('scissors', 'paper'): 'lose', ('scissors', 'scissors'): 'draw'} 

    ans = 0
    for round in data:
        opp, me = round.split(" ")
        opp_shape,me_shape = shape_dict[opp], shape_dict[me]
        outcome = outcome_dict[(opp_shape, me_shape)] 
        score = score_shape[me_shape] + score_outcome[outcome]
        ans += score

    print(ans)
    # 12458


if __name__ == "__main__":
    main()
