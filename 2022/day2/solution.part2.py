import os


def main():
    file_path = os.path.abspath(__file__)
    directory = os.path.dirname(file_path)
    with open(os.path.join(directory, "input.txt"), "r") as f:
        data = f.read().split("\n")

    score_shape = {"rock":1,"paper":2,"scissors":3}
    score_outcome = {"lose":0,"draw":3,"win":6}

    shape_dict = {'A':'rock','B':'paper','C':'scissors', 'X':'lose','Y':'draw','Z':'win'}
    outcome_dict = {('rock','lose'): 'scissors', ('rock', 'draw'): 'rock', ('rock', 'win'): 'paper', ('paper', 'lose'): 'rock', ('paper', 'draw'): 'paper', ('paper', 'win'): 'scissors', ('scissors', 'lose'): 'paper', ('scissors', 'draw'): 'scissors', ('scissors', 'win'): 'rock'} 

    ans = 0
    for round in data:
        opp, outcome = round.split(" ")
        opp_shape, outcome_shape = shape_dict[opp], shape_dict[outcome]
        me_shape = outcome_dict[(opp_shape, outcome_shape)]

        score = score_shape[me_shape] + score_outcome[outcome_shape]
        ans += score
    print(ans)
    # 12683


if __name__ == "__main__":
    main()
