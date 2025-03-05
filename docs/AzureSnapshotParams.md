# AzureSnapshotParams

Specifies parameters of Azure type snapshots.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**protection_type** | **str** | Specifies the protection type of Azure snapshots. | [optional] 

## Example

```python
from cohesity_sdk.models.azure_snapshot_params import AzureSnapshotParams

# TODO update the JSON string below
json = "{}"
# create an instance of AzureSnapshotParams from a JSON string
azure_snapshot_params_instance = AzureSnapshotParams.from_json(json)
# print the JSON string representation of the object
print(AzureSnapshotParams.to_json())

# convert the object into a dict
azure_snapshot_params_dict = azure_snapshot_params_instance.to_dict()
# create an instance of AzureSnapshotParams from a dict
azure_snapshot_params_from_dict = AzureSnapshotParams.from_dict(azure_snapshot_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


