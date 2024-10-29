from azureml.core import Workspace, Experiment, ScriptRunConfig, Environment
from azureml.core.compute import AmlCompute, ComputeTarget
from azureml.core.run import Run
import os

class AzureMLHandler:
    def __init__(self, subscription_id, resource_group, workspace_name, compute_name):
        self.workspace = Workspace(subscription_id, resource_group, workspace_name)
        self.compute_target = self.get_compute_target(compute_name)

    def get_compute_target(self, compute_name):
        try:
            compute_target = ComputeTarget(workspace=self.workspace, name=compute_name)
            print(f"Found existing compute target: {compute_name}")
        except:
            compute_config = AmlCompute.provisioning_configuration(vm_size='STANDARD_D2_V2', max_nodes=4)
            compute_target = ComputeTarget.create(self.workspace, compute_name, compute_config)
            compute_target.wait_for_completion(show_output=True)
        return compute_target

    def train_model(self, script_path, script_args, environment_name):
        env = Environment.get(workspace=self.workspace, name=environment_name)
        src = ScriptRunConfig(source_directory=os.path.dirname(script_path),
                              script=os.path.basename(script_path),
                              arguments=script_args,
                              compute_target=self.compute_target,
                              environment=env)
        experiment = Experiment(self.workspace, "ami-ai-experiment")
        run = experiment.submit(src)
        run.wait_for_completion(show_output=True)
        return run

    def get_model(self, run_id):
        run = Run(self.workspace.experiments["ami-ai-experiment"], run_id)
        model = run.register_model(model_name="ami_model", model_path="outputs/model")
        return model