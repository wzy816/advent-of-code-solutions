class Base:
    def __init__(self, name):
        self._name = name
        self._children = []
        self._parents = []

    @property
    def name(self):
        return self._name

    def add_child(self, m):
        self._children.append(m)

    def add_parent(self, m):
        self._parents.append(m)

    def _send(self, signal):
        ret = []
        for ch in self._children:
            ret.append({"input": self, "dest": ch, "signal": signal})
        return ret

    def receive(self, signal, from_module):
        return self._send(signal)


class FlipFlop(Base):
    def __init__(self, name):
        super().__init__(name)
        self.state = "OFF"

    def receive(self, signal, from_module):
        if signal == "HIGH":
            return []

        if self.state == "OFF":
            self.state = "ON"
            return self._send("HIGH")

        elif self.state == "ON":
            self.state = "OFF"
            return self._send("LOW")


class Conjunction(Base):
    def __init__(self, name):
        super().__init__(name)
        self.parent_last_signal = {}

    def add_parent(self, m):
        super().add_parent(m)
        self.parent_last_signal[m.name] = "LOW"

    def receive(self, signal, from_module):
        self.parent_last_signal[from_module.name] = signal

        if "LOW" in self.parent_last_signal.values():
            return self._send("HIGH")
        else:
            return self._send("LOW")


def main():
    with open("./input.txt", "r") as f:
        data = f.read().split("\n")

    # build modules
    modules = {}
    modules["button"] = Base("button")
    for line in data:
        _input, _ = line.split("->")
        _input = _input.strip()
        if _input == "broadcaster":
            modules["broadcaster"] = Base("broadcaster")
        else:
            input_type = _input[0]
            input_name = _input[1:]
            if input_type == "%":
                modules[input_name] = FlipFlop(input_name)
            if input_type == "&":
                modules[input_name] = Conjunction(input_name)

    # connect modules
    modules["button"].add_child(modules["broadcaster"])
    modules["broadcaster"].add_parent(modules["button"])
    for line in data:
        _input, outputs = line.split("->")
        _input = _input.strip()
        output_names = [o.strip() for o in outputs.split(",")]

        input_name = _input
        if _input[0] == "&" or _input[0] == "%":
            input_name = _input[1:]

        for output_name in output_names:
            # output?
            if output_name not in modules:
                modules[output_name] = Base(output_name)

            i = modules[input_name]
            d = modules[output_name]
            i.add_child(d)
            d.add_parent(i)
    print(modules)

    # part 1
    from collections import deque

    high_cnt = 0
    low_cnt = 0
    for _ in range(1000):

        events = deque()
        events.append(
            {
                "input": modules["button"],
                "signal": "LOW",
                "dest": modules["broadcaster"],
            }
        )
        low_cnt += 1

        while events:
            event = events.popleft()
            new_events = event["dest"].receive(event["signal"], event["input"])

            for e in new_events:
                events.append(e)

                if e["signal"] == "HIGH":
                    high_cnt += 1
                else:
                    low_cnt += 1

                # print(
                #     f"{e['input'].name}  -{e['signal']}-> {e['dest'].name}"
                # )

    print(high_cnt * low_cnt)


if __name__ == "__main__":
    main()
