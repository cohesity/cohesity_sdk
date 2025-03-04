# ArchivalOracleExternalTargetParams

Specifies the common parameters which are specific to Oracle related External Targets.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_key_id** | **str** | Specifies the access key id of the external target. | 
**bucket_name** | **str** | Specifies the bucket name of the external target. | 
**region** | **str** | Specifies the region of the external target. | 
**storage_access_key** | **str** | Specifies the storage access key of the external target. | [optional] 
**tenancy** | **str** | Specifies the tenancy of the external target. | 
**is_forever_incremental_archival_enabled** | **bool** | Specifies if Forever Incremental Archival setting is enabled or not. | [optional] 
**is_incremental_archival_enabled** | **bool** | Specifies if Incremental Archival setting is enabled or not. | [optional] 
**source_side_deduplication** | **bool** | Specifies the Source Side Deduplication setting for the Oracle external target | [optional] 
**storage_class** | **str** | Specifies the Oracle External Target storage class. | 

## Example

```python
from cohesity_sdk.models.archival_oracle_external_target_params import ArchivalOracleExternalTargetParams

# TODO update the JSON string below
json = "{}"
# create an instance of ArchivalOracleExternalTargetParams from a JSON string
archival_oracle_external_target_params_instance = ArchivalOracleExternalTargetParams.from_json(json)
# print the JSON string representation of the object
print(ArchivalOracleExternalTargetParams.to_json())

# convert the object into a dict
archival_oracle_external_target_params_dict = archival_oracle_external_target_params_instance.to_dict()
# create an instance of ArchivalOracleExternalTargetParams from a dict
archival_oracle_external_target_params_from_dict = ArchivalOracleExternalTargetParams.from_dict(archival_oracle_external_target_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


