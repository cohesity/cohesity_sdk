# UpdateProtectionGroupRunRequestBody

Specifies the params to update a list of Protection Group Runs.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**update_protection_group_run_params** | [**List[UpdateProtectionGroupRunParams]**](UpdateProtectionGroupRunParams.md) |  | 

## Example

```python
from cohesity_sdk.cluster.models.update_protection_group_run_request_body import UpdateProtectionGroupRunRequestBody

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateProtectionGroupRunRequestBody from a JSON string
update_protection_group_run_request_body_instance = UpdateProtectionGroupRunRequestBody.from_json(json)
# print the JSON string representation of the object
print(UpdateProtectionGroupRunRequestBody.to_json())

# convert the object into a dict
update_protection_group_run_request_body_dict = update_protection_group_run_request_body_instance.to_dict()
# create an instance of UpdateProtectionGroupRunRequestBody from a dict
update_protection_group_run_request_body_from_dict = UpdateProtectionGroupRunRequestBody.from_dict(update_protection_group_run_request_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


