# CommonExternalTargetParams

Specifies the parameters which are common between all External Target.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cloud_domains** | [**List[CloudDomain]**](CloudDomain.md) | Specifies the cloud domain information. | [optional] 
**compression** | **str** | Specifies whether the type of compression of the External Target | [optional] 
**error_message** | **str** | Specifies the error message if the event is in failed state. | [optional] [readonly] 
**global_id** | **str** | Specifies the global identifier of the External Target. | [optional] 
**id** | **int** | Specifies the ID of the External Target. | [optional] [readonly] 
**is_worm_capable** | **bool** | Specifies whether this external target has been found to be capable of supporting WORM archives. | [optional] 
**name** | **str** | Specifies the name of the External Target. | 
**ownership_context** | **str** | Specifies whether how this external target is being consumed either Local or FortKnox. | [optional] 
**purpose_type** | **str** | Specifies the purpose of the External Target. | 
**status** | **str** | Specifies the registration status of the External Target | [optional] [readonly] 
**storage_domain_name** | **str** | Specifies the storage domain associated with the target. | [optional] 
**tenant_ids** | **List[str]** | Specifies the list of tenantIds for the External Target | [optional] 

## Example

```python
from cohesity_sdk.helios.models.common_external_target_params import CommonExternalTargetParams

# TODO update the JSON string below
json = "{}"
# create an instance of CommonExternalTargetParams from a JSON string
common_external_target_params_instance = CommonExternalTargetParams.from_json(json)
# print the JSON string representation of the object
print(CommonExternalTargetParams.to_json())

# convert the object into a dict
common_external_target_params_dict = common_external_target_params_instance.to_dict()
# create an instance of CommonExternalTargetParams from a dict
common_external_target_params_from_dict = CommonExternalTargetParams.from_dict(common_external_target_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


