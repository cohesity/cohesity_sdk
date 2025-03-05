# FilterObjectsRequest

Specifies the filter details.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**application_environment** | **str** | Specifies the type of application enviornment needed for filtering to be applied on. This is needed because in case of applications like SQL, Oracle, a single source can contain multiple application enviornments. | [optional] 
**filter_type** | **str** | Specifies the type of filtering user wants to perform. Currently, we only support exclude type of filter. | 
**filters** | [**List[Filter]**](Filter.md) | Specifies the list of filters that need to be applied on given list of discovered objects. | 
**include_tenants** | **bool** | If true, the response will include objects which belongs to all tenants which the current user has permission to see. Default value is false. | [optional] [default to False]
**object_ids** | **List[int]** | Specifies a list of non leaf object ids to filter the leaf level objects. Non leaf object such host (physical or vm) or database instance can be specified. | 
**tenant_ids** | **List[str]** | TenantIds contains list of the tenant for which objects are to be returned. | [optional] 

## Example

```python
from cohesity_sdk.models.filter_objects_request import FilterObjectsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of FilterObjectsRequest from a JSON string
filter_objects_request_instance = FilterObjectsRequest.from_json(json)
# print the JSON string representation of the object
print(FilterObjectsRequest.to_json())

# convert the object into a dict
filter_objects_request_dict = filter_objects_request_instance.to_dict()
# create an instance of FilterObjectsRequest from a dict
filter_objects_request_from_dict = FilterObjectsRequest.from_dict(filter_objects_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


