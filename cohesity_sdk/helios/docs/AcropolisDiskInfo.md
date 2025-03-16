# AcropolisDiskInfo

Specifies information about a disk to be filtered.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**controller_type** | **str** | Specifies the disk controller type. | 
**unit_number** | **int** | Specifies the disk index number. | 

## Example

```python
from cohesity_sdk.helios.models.acropolis_disk_info import AcropolisDiskInfo

# TODO update the JSON string below
json = "{}"
# create an instance of AcropolisDiskInfo from a JSON string
acropolis_disk_info_instance = AcropolisDiskInfo.from_json(json)
# print the JSON string representation of the object
print(AcropolisDiskInfo.to_json())

# convert the object into a dict
acropolis_disk_info_dict = acropolis_disk_info_instance.to_dict()
# create an instance of AcropolisDiskInfo from a dict
acropolis_disk_info_from_dict = AcropolisDiskInfo.from_dict(acropolis_disk_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


