# ServiceProcessEntry

Specifies the process entry for a service.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**process_ids** | **List[int]** | Specifies the process Ids. | [optional] 
**service_name** | **str** | Specifies the service name. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.service_process_entry import ServiceProcessEntry

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceProcessEntry from a JSON string
service_process_entry_instance = ServiceProcessEntry.from_json(json)
# print the JSON string representation of the object
print(ServiceProcessEntry.to_json())

# convert the object into a dict
service_process_entry_dict = service_process_entry_instance.to_dict()
# create an instance of ServiceProcessEntry from a dict
service_process_entry_from_dict = ServiceProcessEntry.from_dict(service_process_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


