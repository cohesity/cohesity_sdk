# HostEntry

Specifies the parameters of a host entry that can be stored in the cluster's /etc/hosts file.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | Description the host entry. | [optional] 
**domain_names** | **List[str]** | Specifies the domain names of the host. | 
**ip** | **str** | Specifies the IP address of the host. | 

## Example

```python
from cohesity_sdk.helios.models.host_entry import HostEntry

# TODO update the JSON string below
json = "{}"
# create an instance of HostEntry from a JSON string
host_entry_instance = HostEntry.from_json(json)
# print the JSON string representation of the object
print(HostEntry.to_json())

# convert the object into a dict
host_entry_dict = host_entry_instance.to_dict()
# create an instance of HostEntry from a dict
host_entry_from_dict = HostEntry.from_dict(host_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


