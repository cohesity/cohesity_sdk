# McmSourceInfo

Specifies the Protection Source information.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**applications** | **List[str]** | Specifies the list of applications registered with current Source. | [optional] 
**cluster_id** | **int** | Specifies the cluster id. | [optional] 
**cluster_incarnation_id** | **int** | Specifies the cluster incarnation id. | [optional] 
**physical_source_info** | [**McmPhysicalSourceInfo**](McmPhysicalSourceInfo.md) |  | [optional] 
**protection_stats** | [**List[ObjectProtectionStatsSummary]**](ObjectProtectionStatsSummary.md) | Specifies the protection statistics of the Source. | [optional] 
**region_id** | **str** | Specifies the region id. | [optional] 
**registration_details** | [**McmSourceRegistrationInfo**](McmSourceRegistrationInfo.md) |  | [optional] 
**registration_id** | **str** | Specifies the registration id of the Protection Source. | [optional] 
**source_id** | **int** | Specifies the id of the Protection Source. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.mcm_source_info import McmSourceInfo

# TODO update the JSON string below
json = "{}"
# create an instance of McmSourceInfo from a JSON string
mcm_source_info_instance = McmSourceInfo.from_json(json)
# print the JSON string representation of the object
print(McmSourceInfo.to_json())

# convert the object into a dict
mcm_source_info_dict = mcm_source_info_instance.to_dict()
# create an instance of McmSourceInfo from a dict
mcm_source_info_from_dict = McmSourceInfo.from_dict(mcm_source_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


