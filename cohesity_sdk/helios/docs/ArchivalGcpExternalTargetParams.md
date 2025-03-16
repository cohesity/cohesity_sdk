# ArchivalGcpExternalTargetParams

Specifies the parameters which are specific to GCP related External Targets of archival purpose type.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bucket_name** | **str** | Specifies the bucket name of the external target. | 
**client_email_address** | **str** | Specifies the client email address of the external target. | 
**client_private_key** | **str** | Specifies the client private key of the external target. | [optional] 
**project_id** | **str** | Specifies the project Id of the external target. | 
**is_forever_incremental_archival_enabled** | **bool** | Specifies if Forever Incremental Archival setting is enabled or not. | [optional] 
**is_incremental_archival_enabled** | **bool** | Specifies if Incremental Archival setting is enabled or not. | [optional] 
**source_side_deduplication** | **bool** | Specifies the Source Side Deduplication setting for the GCP external target | [optional] 
**storage_class** | **str** | Specifies the GCP External Target storage class. | 

## Example

```python
from cohesity_sdk.helios.models.archival_gcp_external_target_params import ArchivalGcpExternalTargetParams

# TODO update the JSON string below
json = "{}"
# create an instance of ArchivalGcpExternalTargetParams from a JSON string
archival_gcp_external_target_params_instance = ArchivalGcpExternalTargetParams.from_json(json)
# print the JSON string representation of the object
print(ArchivalGcpExternalTargetParams.to_json())

# convert the object into a dict
archival_gcp_external_target_params_dict = archival_gcp_external_target_params_instance.to_dict()
# create an instance of ArchivalGcpExternalTargetParams from a dict
archival_gcp_external_target_params_from_dict = ArchivalGcpExternalTargetParams.from_dict(archival_gcp_external_target_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


