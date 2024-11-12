from metaflow import FlowSpec, step, card, project

@project(name='mlproject')
class GitHubActionsDemo3(FlowSpec):

    @step
    def start(self):
        print("Hello GitHub Actions! Hello")
        self.next(self.end)

    @step
    def end(self):
        print('fixed')

if __name__ == "__main__":
    GitHubActionsDemo3()
