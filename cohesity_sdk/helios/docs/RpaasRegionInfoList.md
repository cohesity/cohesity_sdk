# RpaasRegionInfoList

List of Rpaas enabled regions.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**regions** | [**List[RpaasRegionInfo]**](RpaasRegionInfo.md) | Specifies an Rpaas region. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.rpaas_region_info_list import RpaasRegionInfoList

# TODO update the JSON string below
json = "{}"
# create an instance of RpaasRegionInfoList from a JSON string
rpaas_region_info_list_instance = RpaasRegionInfoList.from_json(json)
# print the JSON string representation of the object
print(RpaasRegionInfoList.to_json())

# convert the object into a dict
rpaas_region_info_list_dict = rpaas_region_info_list_instance.to_dict()
# create an instance of RpaasRegionInfoList from a dict
rpaas_region_info_list_from_dict = RpaasRegionInfoList.from_dict(rpaas_region_info_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


