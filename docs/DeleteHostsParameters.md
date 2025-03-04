# DeleteHostsParameters

Specifies the params for deleting hosts

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ips** | **List[str]** | Specifies the list of IPs to be deleted | [optional] 

## Example

```python
from cohesity_sdk.models.delete_hosts_parameters import DeleteHostsParameters

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteHostsParameters from a JSON string
delete_hosts_parameters_instance = DeleteHostsParameters.from_json(json)
# print the JSON string representation of the object
print(DeleteHostsParameters.to_json())

# convert the object into a dict
delete_hosts_parameters_dict = delete_hosts_parameters_instance.to_dict()
# create an instance of DeleteHostsParameters from a dict
delete_hosts_parameters_from_dict = DeleteHostsParameters.from_dict(delete_hosts_parameters_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


