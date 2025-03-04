# AddRemoteDiskResponseBody

Specifies the response of creating remote disk.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**remote_disks** | [**List[CreateRemoteDiskStatus]**](CreateRemoteDiskStatus.md) | Specifies a list of remote disk creating status. | [optional] 

## Example

```python
from cohesity_sdk.models.add_remote_disk_response_body import AddRemoteDiskResponseBody

# TODO update the JSON string below
json = "{}"
# create an instance of AddRemoteDiskResponseBody from a JSON string
add_remote_disk_response_body_instance = AddRemoteDiskResponseBody.from_json(json)
# print the JSON string representation of the object
print(AddRemoteDiskResponseBody.to_json())

# convert the object into a dict
add_remote_disk_response_body_dict = add_remote_disk_response_body_instance.to_dict()
# create an instance of AddRemoteDiskResponseBody from a dict
add_remote_disk_response_body_from_dict = AddRemoteDiskResponseBody.from_dict(add_remote_disk_response_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


