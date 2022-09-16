# MongoDBSourceRegistrationParams

Specifies parameters to register MongoDB source.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hosts** | **[str]** | Specify the MongoS hosts for a sharded cluster and the MongoD hosts for a non-sharded cluster. You can specify a sub-set of the hosts. | 
**auth_type** | **str, none_type** | MongoDB authentication type. | 
**is_ssl_required** | **bool** | Set to true if connection to MongoDB has to be over SSL. | 
**use_secondary_for_backup** | **bool** | Set this to true if you want the system to peform backups from secondary nodes. | 
**username** | **str, none_type** | Specifies the username of the MongoDB cluster. Should be set if &#39;authType&#39; is &#39;LDAP&#39; or &#39;SCRAM&#39;. | [optional] 
**principal** | **str, none_type** | Specifies the principal name of the MongoDB cluster. Should be set if &#39;authType&#39; is &#39;KERBEROS&#39;. | [optional] 
**password** | **str, none_type** | Specifies the password for the MongoDB cluster. Should be set if &#39;authType&#39; is &#39;LDAP&#39; or &#39;SCRAM&#39;. | [optional] 
**authenticating_database** | **str, none_type** | Authenticating Database for this cluster. Should be set if &#39;authType&#39; is &#39;LDAP&#39; or &#39;SCRAM&#39;. | [optional] 
**secondary_node_tag** | **str** | MongoDB Secondary node tag. Required only if &#39;useSecondaryForBackup&#39; is true.The system will use this to identify the secondary nodes for reading backup data. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


