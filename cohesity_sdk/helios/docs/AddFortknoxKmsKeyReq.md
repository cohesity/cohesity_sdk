# AddFortknoxKmsKeyReq

Request params for adding KMS key for Fortknox.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **str** | ID of the helios account. | 
**cloud_provider** | [**FortknoxCloudProvider**](FortknoxCloudProvider.md) |  | [optional] 
**kms_key_type** | **str** | Whether the KMS key is customer provided or by Cohesity. | 
**aws_params** | [**AddAwsKmsKeyReq**](AddAwsKmsKeyReq.md) |  | [optional] 

## Example

```python
from cohesity_sdk.helios.models.add_fortknox_kms_key_req import AddFortknoxKmsKeyReq

# TODO update the JSON string below
json = "{}"
# create an instance of AddFortknoxKmsKeyReq from a JSON string
add_fortknox_kms_key_req_instance = AddFortknoxKmsKeyReq.from_json(json)
# print the JSON string representation of the object
print(AddFortknoxKmsKeyReq.to_json())

# convert the object into a dict
add_fortknox_kms_key_req_dict = add_fortknox_kms_key_req_instance.to_dict()
# create an instance of AddFortknoxKmsKeyReq from a dict
add_fortknox_kms_key_req_from_dict = AddFortknoxKmsKeyReq.from_dict(add_fortknox_kms_key_req_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


