# UptieringFileAgePolicy

Specifies the file's selection rule by file age for up tiering data tiering task eg. 1. select files last accessed 2 weeks ago. 2. select files last modified 1 month ago.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**age_msecs** | **int** | Specifies the number of msecs used for file selection. | [optional] 
**condition** | **str** | Specifies the condition for the file age. | [optional] 
**num_file_access** | **int** | Specifies number of file access in last ageMsecs. | [optional] 

## Example

```python
from cohesity_sdk.models.uptiering_file_age_policy import UptieringFileAgePolicy

# TODO update the JSON string below
json = "{}"
# create an instance of UptieringFileAgePolicy from a JSON string
uptiering_file_age_policy_instance = UptieringFileAgePolicy.from_json(json)
# print the JSON string representation of the object
print(UptieringFileAgePolicy.to_json())

# convert the object into a dict
uptiering_file_age_policy_dict = uptiering_file_age_policy_instance.to_dict()
# create an instance of UptieringFileAgePolicy from a dict
uptiering_file_age_policy_from_dict = UptieringFileAgePolicy.from_dict(uptiering_file_age_policy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


