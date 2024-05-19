from metaflow import FlowSpec, step, card, project, current

@project(name='mlproject')
class GitHubActionsDemo(FlowSpec):

    @step
    def start(self):
        print("Hello I am branch", current.branch_name)
        self.item = 'daikon'
        print("X is", self.item)
        self.next(self.end)

    @step
    def end(self):
        print('fixed')

if __name__ == "__main__":
    GitHubActionsDemo()
