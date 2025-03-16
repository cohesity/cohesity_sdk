# RpaasRegionInfo

Specifies a Rpaas enabled region.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bucket_name** | **str** | Name of the S3 bucket. | [optional] 
**global_vault_id** | **str** | Global vault ID. | [optional] 
**kms_key_info** | [**KmsKeyBasicInfo**](KmsKeyBasicInfo.md) |  | [optional] 
**pairing_info** | [**List[RpaasPairingInfo]**](RpaasPairingInfo.md) | The configured cluster for the particular region. | [optional] 
**provision_status** | [**ProvisionStatus**](ProvisionStatus.md) |  | [optional] 
**region_id** | **str** | ID that identifies a region. | [optional] 
**region_name** | **str** | Name of the region. | [optional] 
**region_provision_type** | **str** | Indicates whether the tenant type is Cohesity KMS or Customer managed KMS. | [optional] 
**storage_class** | **str** | Specifies the AWS storage class. | [optional] 
**vault_name** | **str** | Name of the vault. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.rpaas_region_info import RpaasRegionInfo

# TODO update the JSON string below
json = "{}"
# create an instance of RpaasRegionInfo from a JSON string
rpaas_region_info_instance = RpaasRegionInfo.from_json(json)
# print the JSON string representation of the object
print(RpaasRegionInfo.to_json())

# convert the object into a dict
rpaas_region_info_dict = rpaas_region_info_instance.to_dict()
# create an instance of RpaasRegionInfo from a dict
rpaas_region_info_from_dict = RpaasRegionInfo.from_dict(rpaas_region_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


