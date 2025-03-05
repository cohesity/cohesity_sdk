# IsilonObjectProtectionParams

Specifies the parameters which are specific to Isilon object protection.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**continuous_snapshots** | [**ContinuousSnapshotParams**](ContinuousSnapshotParams.md) |  | [optional] 
**protocol** | **str** | Specifies the protocol of the NAS device being backed up. | [optional] 
**use_changelist** | **bool** | Specify whether to use the Isilon Changelist API to directly discover changed files/directories for faster incremental backup. Cohesity will keep an extra snapshot which will be deleted by the next successful backup. | [optional] 

## Example

```python
from cohesity_sdk.models.isilon_object_protection_params import IsilonObjectProtectionParams

# TODO update the JSON string below
json = "{}"
# create an instance of IsilonObjectProtectionParams from a JSON string
isilon_object_protection_params_instance = IsilonObjectProtectionParams.from_json(json)
# print the JSON string representation of the object
print(IsilonObjectProtectionParams.to_json())

# convert the object into a dict
isilon_object_protection_params_dict = isilon_object_protection_params_instance.to_dict()
# create an instance of IsilonObjectProtectionParams from a dict
isilon_object_protection_params_from_dict = IsilonObjectProtectionParams.from_dict(isilon_object_protection_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


