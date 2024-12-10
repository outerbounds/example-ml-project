from metaflow import FlowSpec, step, card, project, current

@project(name='mlproject')
class GitHubActionsDemo(FlowSpec):

    @step
    def start(self):
        self.x = 'cucumber4'
        print('x is', self.x)
        print('branch is', current.branch_name)
        print("Hello GitHub Actions!")
        self.next(self.end)

    @step
    def end(self):
        self.model_accuracy = 0.91
        print('fixed')

if __name__ == "__main__":
    GitHubActionsDemo()
