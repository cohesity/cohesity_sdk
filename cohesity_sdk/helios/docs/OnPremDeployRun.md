# OnPremDeployRun

Specifies information about onprem deploy run for an object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**on_prem_deploy_target_results** | [**List[OnPremDeployTargetResult]**](OnPremDeployTargetResult.md) | OnPrem Deploy result for a target. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.on_prem_deploy_run import OnPremDeployRun

# TODO update the JSON string below
json = "{}"
# create an instance of OnPremDeployRun from a JSON string
on_prem_deploy_run_instance = OnPremDeployRun.from_json(json)
# print the JSON string representation of the object
print(OnPremDeployRun.to_json())

# convert the object into a dict
on_prem_deploy_run_dict = on_prem_deploy_run_instance.to_dict()
# create an instance of OnPremDeployRun from a dict
on_prem_deploy_run_from_dict = OnPremDeployRun.from_dict(on_prem_deploy_run_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


