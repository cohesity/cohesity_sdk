# OnpremDeployParams

Specifies the details about OnpremDeploy target where backup snapshots may be converted and deployed.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Specifies the unique id of the onprem entity. | [optional] 
**restore_v_mware_params** | [**RestoreVMwareVMParams**](RestoreVMwareVMParams.md) |  | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.onprem_deploy_params import OnpremDeployParams

# TODO update the JSON string below
json = "{}"
# create an instance of OnpremDeployParams from a JSON string
onprem_deploy_params_instance = OnpremDeployParams.from_json(json)
# print the JSON string representation of the object
print(OnpremDeployParams.to_json())

# convert the object into a dict
onprem_deploy_params_dict = onprem_deploy_params_instance.to_dict()
# create an instance of OnpremDeployParams from a dict
onprem_deploy_params_from_dict = OnpremDeployParams.from_dict(onprem_deploy_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


