# HdfsBrowseRequestParams


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**parent_path** | **str** | Specifies the path whose contents are to be returned. The last token in the path can be a regex. In this case the regex is applied on the contents of the path upto the second-last token and the matching contents are returned. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.hdfs_browse_request_params import HdfsBrowseRequestParams

# TODO update the JSON string below
json = "{}"
# create an instance of HdfsBrowseRequestParams from a JSON string
hdfs_browse_request_params_instance = HdfsBrowseRequestParams.from_json(json)
# print the JSON string representation of the object
print(HdfsBrowseRequestParams.to_json())

# convert the object into a dict
hdfs_browse_request_params_dict = hdfs_browse_request_params_instance.to_dict()
# create an instance of HdfsBrowseRequestParams from a dict
hdfs_browse_request_params_from_dict = HdfsBrowseRequestParams.from_dict(hdfs_browse_request_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


