# RecoverPureSanVolumeNewSourceConfig

Specifies the new destination Source configuration where the Pure volume will be recovered.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type** | Specifies the id of the new target parent source to recover the Pure SAN Volume to. This field must be specified if recoverToNewSource is true. | 
**rename_recovered_volume_params** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type** | Specifies params to rename the recovered SAN volumes. If not specified, the original names of the volumes are preserved. | [optional] 
**resource_pool** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type** | Specifies the id of the resource pool to recover the Pure SAN Volume to. This field must be specified if recoverToNewSource is true. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


