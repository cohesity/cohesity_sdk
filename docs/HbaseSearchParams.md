# HbaseSearchParams

Specifies the parameters which are specific for searching Hbase objects.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hbase_object_types** | **List[str]** | Specifies one or more Hbase object types be searched. | 
**search_string** | **str** | Specifies the search string to search the Hbase Objects | 

## Example

```python
from cohesity_sdk.models.hbase_search_params import HbaseSearchParams

# TODO update the JSON string below
json = "{}"
# create an instance of HbaseSearchParams from a JSON string
hbase_search_params_instance = HbaseSearchParams.from_json(json)
# print the JSON string representation of the object
print(HbaseSearchParams.to_json())

# convert the object into a dict
hbase_search_params_dict = hbase_search_params_instance.to_dict()
# create an instance of HbaseSearchParams from a dict
hbase_search_params_from_dict = HbaseSearchParams.from_dict(hbase_search_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


