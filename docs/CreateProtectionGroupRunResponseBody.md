# CreateProtectionGroupRunResponseBody

Specifies the response for create a protection run. On success, the system will accept the request and return the Protection Group id for which the run is supposed to start. The actual run may start at a later time if the system is busy. Consumers must query the Protection Group to see the run.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**protection_group_id** | **str** | Specifies id of the Protection Group which must be polled for seeing the new run. | [optional] 
**uda_params** | [**UdaCreateRunResponseParams**](UdaCreateRunResponseParams.md) |  | [optional] 

## Example

```python
from cohesity_sdk.models.create_protection_group_run_response_body import CreateProtectionGroupRunResponseBody

# TODO update the JSON string below
json = "{}"
# create an instance of CreateProtectionGroupRunResponseBody from a JSON string
create_protection_group_run_response_body_instance = CreateProtectionGroupRunResponseBody.from_json(json)
# print the JSON string representation of the object
print(CreateProtectionGroupRunResponseBody.to_json())

# convert the object into a dict
create_protection_group_run_response_body_dict = create_protection_group_run_response_body_instance.to_dict()
# create an instance of CreateProtectionGroupRunResponseBody from a dict
create_protection_group_run_response_body_from_dict = CreateProtectionGroupRunResponseBody.from_dict(create_protection_group_run_response_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


