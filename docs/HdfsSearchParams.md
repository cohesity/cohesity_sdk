# HdfsSearchParams

Specifies the parameters for searching HDFS Folders and Files.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hdfs_types** | **List[str]** | Specifies types as Folders or Files or both to be searched. | 
**search_string** | **str** | Specifies the search string to search the HDFS Folders and Files. | 

## Example

```python
from cohesity_sdk.models.hdfs_search_params import HdfsSearchParams

# TODO update the JSON string below
json = "{}"
# create an instance of HdfsSearchParams from a JSON string
hdfs_search_params_instance = HdfsSearchParams.from_json(json)
# print the JSON string representation of the object
print(HdfsSearchParams.to_json())

# convert the object into a dict
hdfs_search_params_dict = hdfs_search_params_instance.to_dict()
# create an instance of HdfsSearchParams from a dict
hdfs_search_params_from_dict = HdfsSearchParams.from_dict(hdfs_search_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


