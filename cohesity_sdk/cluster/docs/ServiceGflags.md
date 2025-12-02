# ServiceGflags

Specifies the gflags for a service.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gflags** | [**List[Gflag]**](Gflag.md) | Specifies a list of gflags for the service. | [optional] 
**service_name** | **str** | Specifies the service name. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.service_gflags import ServiceGflags

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceGflags from a JSON string
service_gflags_instance = ServiceGflags.from_json(json)
# print the JSON string representation of the object
print(ServiceGflags.to_json())

# convert the object into a dict
service_gflags_dict = service_gflags_instance.to_dict()
# create an instance of ServiceGflags from a dict
service_gflags_from_dict = ServiceGflags.from_dict(service_gflags_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


