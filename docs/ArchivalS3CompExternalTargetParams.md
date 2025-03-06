# ArchivalS3CompExternalTargetParams

Specifies the parameters which are specific to S3 Compatible related External Targets of archival purpose type.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_key_id** | **str** | Specifies the access key id of the external target. | 
**bucket_name** | **str** | Specifies the bucket name of the external target. | 
**end_point** | **str** | Specifies the endpoint of the external target. | 
**is_aws_snowball** | **bool** | Specifies whether the external target is AWS Snowball. | [optional] 
**region** | **str** | Specifies the region of the external target. | [optional] 
**secret_access_key** | **str** | Specifies the secret access key of the external target. | [optional] 
**secure_connection** | **bool** | Specifies the secure connection(https) is enabled or not. | [optional] 
**signature_version** | **int** | Specifies the aws signature version of the external target. | [optional] 
**bucket_owner_account_id** | **str** | Specifies the account Id of the S3 bucket owner. | [optional] 
**is_forever_incremental_archival_enabled** | **bool** | Specifies if Forever Incremental Archival setting is enabled or not. | [optional] 
**is_incremental_archival_enabled** | **bool** | Specifies if Incremental Archival setting is enabled or not. | [optional] 
**source_side_deduplication** | **bool** | Specifies the Source Side Deduplication setting for the S3 Compatible external target | [optional] 
**storage_class** | **str** | Specifies the S3Compatible External Target storage class. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.archival_s3_comp_external_target_params import ArchivalS3CompExternalTargetParams

# TODO update the JSON string below
json = "{}"
# create an instance of ArchivalS3CompExternalTargetParams from a JSON string
archival_s3_comp_external_target_params_instance = ArchivalS3CompExternalTargetParams.from_json(json)
# print the JSON string representation of the object
print(ArchivalS3CompExternalTargetParams.to_json())

# convert the object into a dict
archival_s3_comp_external_target_params_dict = archival_s3_comp_external_target_params_instance.to_dict()
# create an instance of ArchivalS3CompExternalTargetParams from a dict
archival_s3_comp_external_target_params_from_dict = ArchivalS3CompExternalTargetParams.from_dict(archival_s3_comp_external_target_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


