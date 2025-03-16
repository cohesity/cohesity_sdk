# ServiceVersionInfo

Specifies version information for a cohesity service.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**last_commit_time** | **str** | LastCommitTime of the service. | [optional] 
**service_name** | **str** | Name of the service. | [optional] 
**service_version** | **str** | Version of the service. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.service_version_info import ServiceVersionInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceVersionInfo from a JSON string
service_version_info_instance = ServiceVersionInfo.from_json(json)
# print the JSON string representation of the object
print(ServiceVersionInfo.to_json())

# convert the object into a dict
service_version_info_dict = service_version_info_instance.to_dict()
# create an instance of ServiceVersionInfo from a dict
service_version_info_from_dict = ServiceVersionInfo.from_dict(service_version_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


