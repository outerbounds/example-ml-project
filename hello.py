from metaflow import FlowSpec, step, card, schedule

class GitHubActionsDemo(FlowSpec):

    @step
    def start(self):
        print("Hello GitHub Actions!")
        self.next(self.end)

    @step
    def end(self):
        print('fixed')

if __name__ == "__main__":
    GitHubActionsDemo()
