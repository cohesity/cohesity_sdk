# S3OwnerInfo

Specifies the owner info of an S3 bucket. For ABAC enabled bucket, owner is specified by distinguishedName of the user. In all other cases, it is defined by userId.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**distinguished_name** | **str, none_type** | Specifies the distinguished name of the bucket owner for an ABAC enabled S3 Bucket. | [optional] 
**user_id** | **str, none_type** | Specifies the user id of the owner. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


