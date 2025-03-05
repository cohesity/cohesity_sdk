# FailedProtectionGroupDetails

Specifies a list of ids of Protection Group that failed to update along with error details

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error_message** | **str** | Specifies the error mesage for failed protection group. | [optional] 
**protection_group_id** | **str** | Specifies the id of the failed protection group. | [optional] 

## Example

```python
from cohesity_sdk.models.failed_protection_group_details import FailedProtectionGroupDetails

# TODO update the JSON string below
json = "{}"
# create an instance of FailedProtectionGroupDetails from a JSON string
failed_protection_group_details_instance = FailedProtectionGroupDetails.from_json(json)
# print the JSON string representation of the object
print(FailedProtectionGroupDetails.to_json())

# convert the object into a dict
failed_protection_group_details_dict = failed_protection_group_details_instance.to_dict()
# create an instance of FailedProtectionGroupDetails from a dict
failed_protection_group_details_from_dict = FailedProtectionGroupDetails.from_dict(failed_protection_group_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


