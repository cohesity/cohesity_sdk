# ExperimentalAdapterProtectionGroupParams

Specifies parameters related to the Experimental Adapter Protection job.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**concurrency** | **int** | Specifies the maximum number of concurrent IO streams that will be created to exchange data with the cluster. If not specified, the default value is taken as 1. | [optional] [default to 1]
**excluded_object_ids** | **List[int]** | Specifies the objects to be excluded in the Protection Group. | [optional] 
**objects** | [**List[ExperimentalAdapaterProtectionGroupObjectParams]**](ExperimentalAdapaterProtectionGroupObjectParams.md) | Specifies a list of fully qualified names of the objects to be protected. | [optional] 
**workflow_params** | **str** | Specifies the discover source workflow parameters. This is a stringified JSON representation of the parameters. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.experimental_adapter_protection_group_params import ExperimentalAdapterProtectionGroupParams

# TODO update the JSON string below
json = "{}"
# create an instance of ExperimentalAdapterProtectionGroupParams from a JSON string
experimental_adapter_protection_group_params_instance = ExperimentalAdapterProtectionGroupParams.from_json(json)
# print the JSON string representation of the object
print(ExperimentalAdapterProtectionGroupParams.to_json())

# convert the object into a dict
experimental_adapter_protection_group_params_dict = experimental_adapter_protection_group_params_instance.to_dict()
# create an instance of ExperimentalAdapterProtectionGroupParams from a dict
experimental_adapter_protection_group_params_from_dict = ExperimentalAdapterProtectionGroupParams.from_dict(experimental_adapter_protection_group_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


