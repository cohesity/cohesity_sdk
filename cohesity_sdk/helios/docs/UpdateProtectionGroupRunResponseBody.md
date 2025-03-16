# UpdateProtectionGroupRunResponseBody

Specifies the response of update Protection Group Runs request.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**failed_runs** | [**List[FailedRunDetails]**](FailedRunDetails.md) | Specifies a list of ids of Protection Group Runs that failed to update along with error details. | [optional] 
**successful_run_ids** | **List[str]** | Specifies a list of ids of Protection Group Runs that are successfully updated. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.update_protection_group_run_response_body import UpdateProtectionGroupRunResponseBody

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateProtectionGroupRunResponseBody from a JSON string
update_protection_group_run_response_body_instance = UpdateProtectionGroupRunResponseBody.from_json(json)
# print the JSON string representation of the object
print(UpdateProtectionGroupRunResponseBody.to_json())

# convert the object into a dict
update_protection_group_run_response_body_dict = update_protection_group_run_response_body_instance.to_dict()
# create an instance of UpdateProtectionGroupRunResponseBody from a dict
update_protection_group_run_response_body_from_dict = UpdateProtectionGroupRunResponseBody.from_dict(update_protection_group_run_response_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


