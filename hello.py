from metaflow import FlowSpec, step, card, schedule

class GitHubActionsDemo(FlowSpec):

    @step
    def start(self):
        self.x = 123
        print("Hello world!")
        self.next(self.end)

    @step
    def end(self):
        print(self.x)

if __name__ == "__main__":
    GitHubActionsDemo()
