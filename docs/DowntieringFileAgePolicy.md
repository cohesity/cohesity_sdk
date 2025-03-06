# DowntieringFileAgePolicy

Specifies the file's selection rule by file age for down tiering data tiering task eg. 1. select files older than 10 days. 2. select files last accessed 2 weeks ago. 3. select files last modified 1 month ago.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**age_msecs** | **int** | Specifies the number of msecs used for file selection. | [optional] 
**condition** | **str** | Specifies the condition for the file age. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.downtiering_file_age_policy import DowntieringFileAgePolicy

# TODO update the JSON string below
json = "{}"
# create an instance of DowntieringFileAgePolicy from a JSON string
downtiering_file_age_policy_instance = DowntieringFileAgePolicy.from_json(json)
# print the JSON string representation of the object
print(DowntieringFileAgePolicy.to_json())

# convert the object into a dict
downtiering_file_age_policy_dict = downtiering_file_age_policy_instance.to_dict()
# create an instance of DowntieringFileAgePolicy from a dict
downtiering_file_age_policy_from_dict = DowntieringFileAgePolicy.from_dict(downtiering_file_age_policy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


