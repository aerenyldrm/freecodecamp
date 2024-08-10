import copy
import random

class Hat:
    def __init__(self, **argument_set):
        self.argument_set = dict(argument_set.items())
        content_list = []
        for key, value in self.argument_set.items():
            content_list.extend([key] * value)
        self.content = content_list
    # above is to initialize hat class and to represent attributes
    def draw(self, number_of_ball_to_draw):
        if number_of_ball_to_draw > len(self.content):
            number_of_ball_to_draw = len(self.content)
        content_copy = copy.deepcopy(self.content)
        drawn_ball_set = []
        for count in range(number_of_ball_to_draw):
            numeric_boundary = len(content_copy)
            random_index_to_draw = int(random.uniform(0, numeric_boundary))
            drawn_ball_set.append(content_copy.pop(random_index_to_draw))
        return drawn_ball_set
    # above is to define draw process
if __name__ == "__main__":
    def experiment(hat: Hat, expected_ball_set: dict, number_of_ball_drawn_for_each: int, number_of_experiment: int):
        incident_count = 0
        for count in range(number_of_experiment):
            expected_ball_set_proper = []
            for key, value in expected_ball_set.items():
                expected_ball_set_proper.extend([key] * value)
            hat_copy = copy.deepcopy(hat)
            drawn_ball_set = hat_copy.draw(number_of_ball_drawn_for_each)
            remain_length = len(expected_ball_set_proper)
            for ball in expected_ball_set_proper:
                if ball in drawn_ball_set:
                    index_to_pop = drawn_ball_set.index(ball)
                    drawn_ball_set.pop(index_to_pop)
                    remain_length -= 1
                else: continue
            if remain_length == 0:
                incident_count += 1
        return incident_count / number_of_experiment
    # above is to understand probability.
    a_hat = Hat(red = 2, green = 2, blue = 2)
    print(a_hat.content)
    print(a_hat.draw(3))
    probability = experiment(a_hat, {"blue": 2}, 2, 100)
    print(probability)