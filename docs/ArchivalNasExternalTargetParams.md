# ArchivalNasExternalTargetParams

Specifies the parameters which are specific to Nas related External Targets of archival purpose type.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**host** | **str** | Specifies the host of the NAS external target. | 
**is_forever_incremental_archival_enabled** | **bool** | Specifies if Forever Incremental Archival setting is enabled or not. | [optional] 
**is_incremental_archival_enabled** | **bool** | Specifies if Incremental Archival setting is enabled or not. | [optional] 
**kerberos_realm_name** | **str** | Specifies the Kerberos realm name for a Kerberos-secured target. | [optional] 
**mount_path** | **str** | Specifies the mount path of the NAS external target. | 
**nfs_security_type** | **str** | Specifies the NFS security type of the target. | [optional] 
**nfs_version_number** | **str** | Specifies the NFS version number of the target. | [optional] 
**share_type** | **str** | Specifies the share type of the NAS external target. | [optional] [readonly] 
**source_side_deduplication** | **bool** | Specifies the Source Side Deduplication setting for the Nas external target | [optional] 

## Example

```python
from cohesity_sdk.models.archival_nas_external_target_params import ArchivalNasExternalTargetParams

# TODO update the JSON string below
json = "{}"
# create an instance of ArchivalNasExternalTargetParams from a JSON string
archival_nas_external_target_params_instance = ArchivalNasExternalTargetParams.from_json(json)
# print the JSON string representation of the object
print(ArchivalNasExternalTargetParams.to_json())

# convert the object into a dict
archival_nas_external_target_params_dict = archival_nas_external_target_params_instance.to_dict()
# create an instance of ArchivalNasExternalTargetParams from a dict
archival_nas_external_target_params_from_dict = ArchivalNasExternalTargetParams.from_dict(archival_nas_external_target_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


