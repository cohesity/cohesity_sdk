# McmPhysicalSourceInfo

Specifies the information for a physical source.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**agents_info** | [**List[McmAgentInfo]**](McmAgentInfo.md) | Specifies the information for agents related to source. | [optional] 
**host_type** | **str** | Specifies the operating system of the physical host. | [optional] 
**upgradability** | **str** | Specifies the upgradability of the agent software. | [optional] 
**upgrade_error** | **str** | Specifies the upgrade error if any for the agent. | [optional] 
**upgrade_status** | **str** | Specifies the current upgrade status of the agent. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.mcm_physical_source_info import McmPhysicalSourceInfo

# TODO update the JSON string below
json = "{}"
# create an instance of McmPhysicalSourceInfo from a JSON string
mcm_physical_source_info_instance = McmPhysicalSourceInfo.from_json(json)
# print the JSON string representation of the object
print(McmPhysicalSourceInfo.to_json())

# convert the object into a dict
mcm_physical_source_info_dict = mcm_physical_source_info_instance.to_dict()
# create an instance of McmPhysicalSourceInfo from a dict
mcm_physical_source_info_from_dict = McmPhysicalSourceInfo.from_dict(mcm_physical_source_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


