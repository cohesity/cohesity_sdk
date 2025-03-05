# RunTargetsConfiguration

Specifies the replication and archival targets.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**archivals** | [**List[RunArchivalConfig]**](RunArchivalConfig.md) | Specifies a list of archival targets configurations. | [optional] 
**cloud_replications** | [**List[RunCloudReplicationConfig]**](RunCloudReplicationConfig.md) | Specifies a list of cloud replication targets configurations. | [optional] 
**replications** | [**List[RunReplicationConfig]**](RunReplicationConfig.md) | Specifies a list of replication targets configurations. | [optional] 
**use_policy_defaults** | **bool** | Specifies whether to use default policy settings or not. If specified as true then &#39;replications&#39; and &#39;arcihvals&#39; should not be specified. In case of true value, replicatioan targets congfigured in the policy will be added internally. | [optional] [default to False]

## Example

```python
from cohesity_sdk.models.run_targets_configuration import RunTargetsConfiguration

# TODO update the JSON string below
json = "{}"
# create an instance of RunTargetsConfiguration from a JSON string
run_targets_configuration_instance = RunTargetsConfiguration.from_json(json)
# print the JSON string representation of the object
print(RunTargetsConfiguration.to_json())

# convert the object into a dict
run_targets_configuration_dict = run_targets_configuration_instance.to_dict()
# create an instance of RunTargetsConfiguration from a dict
run_targets_configuration_from_dict = RunTargetsConfiguration.from_dict(run_targets_configuration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


