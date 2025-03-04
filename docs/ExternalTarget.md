# ExternalTarget

External Target.

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
**archival_params** | [**ArchivalExternalTargetParams**](ArchivalExternalTargetParams.md) |  | [optional] 
**tiering_params** | [**TieringExternalTargetParams**](TieringExternalTargetParams.md) |  | [optional] 

## Example

```python
from cohesity_sdk.models.external_target import ExternalTarget

# TODO update the JSON string below
json = "{}"
# create an instance of ExternalTarget from a JSON string
external_target_instance = ExternalTarget.from_json(json)
# print the JSON string representation of the object
print(ExternalTarget.to_json())

# convert the object into a dict
external_target_dict = external_target_instance.to_dict()
# create an instance of ExternalTarget from a dict
external_target_from_dict = ExternalTarget.from_dict(external_target_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


