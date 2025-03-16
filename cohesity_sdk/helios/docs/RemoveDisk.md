# RemoveDisk

Specifies details of disk removal response.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Specifies id of the disk. | [optional] 
**marked_for_removal** | **bool** | If true, Disk is marked for removal. | [optional] 
**timestamp_secs** | **int** | Specifies the last run time of the pre-checks execution in Unix epoch timestamp (in seconds). | [optional] 
**validation_checks** | [**List[PreCheckValidation]**](PreCheckValidation.md) | Specifies the pre-check validations results. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.remove_disk import RemoveDisk

# TODO update the JSON string below
json = "{}"
# create an instance of RemoveDisk from a JSON string
remove_disk_instance = RemoveDisk.from_json(json)
# print the JSON string representation of the object
print(RemoveDisk.to_json())

# convert the object into a dict
remove_disk_dict = remove_disk_instance.to_dict()
# create an instance of RemoveDisk from a dict
remove_disk_from_dict = RemoveDisk.from_dict(remove_disk_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


