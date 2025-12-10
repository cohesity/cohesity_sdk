# NutanixFSObjectParams

Specifies the common parameters for Nutanix FS objects.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**supported_nas_mount_protocols** | **List[str]** | Specifies a list of NAS mount protocols supported by this object. | [optional] 
**volume_type** | **str** | Specifies the Nutanix FS volume type. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.nutanix_fs_object_params import NutanixFSObjectParams

# TODO update the JSON string below
json = "{}"
# create an instance of NutanixFSObjectParams from a JSON string
nutanix_fs_object_params_instance = NutanixFSObjectParams.from_json(json)
# print the JSON string representation of the object
print(NutanixFSObjectParams.to_json())

# convert the object into a dict
nutanix_fs_object_params_dict = nutanix_fs_object_params_instance.to_dict()
# create an instance of NutanixFSObjectParams from a dict
nutanix_fs_object_params_from_dict = NutanixFSObjectParams.from_dict(nutanix_fs_object_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


